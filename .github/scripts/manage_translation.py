#!/usr/bin/env python
#
# This python file contains utility scripts to manage Python docs Ukrainian translation.
# It has to be run inside the python-docs-uk git root directory.

import os
import re
from argparse import ArgumentParser
from pathlib import Path

from transifex.api import transifex_api


transifex_api.setup(auth=os.getenv('TX_TOKEN'))

RESOURCE_NAME_MAP = {'glossary_': 'glossary'}

ORGANISATION_ID = 'o:python-doc'
PROJECT_ID = 'o:python-doc:p:python-newest'
LANGUAGE_ID = 'l:uk'
ORGANISATION = transifex_api.Organization.get(id=ORGANISATION_ID)
PROJECT = transifex_api.Project.get(id=PROJECT_ID)
LANGUAGE = transifex_api.Language.get(id=LANGUAGE_ID)


def _slug_to_file_path(slug: str) -> Path:
    """Set of rules how to transform slug to translation file path"""
    file_path = RESOURCE_NAME_MAP.get(slug, slug)  # Legacy slug to file mapping
    file_path = file_path.replace('--', '/')
    if re.match(r'\d+_\d+', file_path):
        file_path = file_path.replace('_', '.')
    file_path = file_path + '.po'
    return Path(file_path)


def recreate_config() -> None:
    """Regenerate Transifex client config for all resources."""
    resources = transifex_api.Resource.filter(project=PROJECT).all()
    with open('.tx/config', 'w') as fo:
        fo.writelines(('[main]\n', 'host = https://api.transifex.com\n',))
        for resource in resources:
            path = _slug_to_file_path(resource.slug)
            fo.writelines((
                '\n',
                f'[{resource.id}]\n',
                f'file_filter = {path}\n',
                'type = PO\n',
                'source_lang = en\n',
            ))


def recreate_resource_stats() -> None:
    """Create resource stats."""
    stats = transifex_api.ResourceLanguageStats.filter(project=PROJECT, language=LANGUAGE).all()
    with open('RESOURCE.md', 'w') as fo:
        fo.writelines(('| Файл | Перекладено | Переглянуто | Вичитано |\n', '|:-----|:-----|:-----|:-----|\n'))
        for stat in stats:
            file_name = _slug_to_file_path(stat.id.split(':')[5])
            translated_pct = round(100 * stat.attributes['translated_words'] / stat.attributes['total_words'], 1)
            reviewed_pct = round(100 * stat.attributes['reviewed_words'] / stat.attributes['total_words'], 1)
            proofread_pct = round(100 * stat.attributes['proofread_words'] / stat.attributes['total_words'], 1)
            fo.writelines(f'| {file_name} | {translated_pct} % | {reviewed_pct} % | {proofread_pct} % |\n')


def recreate_team_stats() -> None:
    """Create contributor stats"""
    members = transifex_api.TeamMembership.filter(organization=ORGANISATION, language=LANGUAGE).all()

    users = {member.user.id: member.attributes['role'] for member in members}
    translators = dict.fromkeys(users.keys(), 0)
    reviewers = dict.fromkeys(users.keys(), 0)
    proofreaders = dict.fromkeys(users.keys(), 0)

    resources = transifex_api.Resource.filter(project=PROJECT).all()
    for resource in resources:
        translations = transifex_api.ResourceTranslation.filter(resource=resource, language=LANGUAGE).all()
        for translation in translations:
            if translation.relationships['translator']:
                translators[translation.relationships['translator']['data']['id']] += 1
            if translation.relationships['reviewer']:
                reviewers[translation.relationships['reviewer']['data']['id']] += 1
            if translation.relationships['proofreader']:
                proofreaders[translation.relationships['proofreader']['data']['id']] += 1

    with open('TEAM.md', 'w') as fo:
        fo.writelines(('| | Роль | Переклав | Переглянув | Вичитав |\n', '|:---|:---|:---|:---|:---|\n',))
        for user, role in users.items():
            fo.writelines(f"| {user} | {role} | {translators[user]} | {reviewers[user]} | {proofreaders[user]} |\n")


def fetch_translations():
    """Fetch translations from Transifex, remove source lines."""
    pull_return_code = os.system(f'tx pull -l uk --force --skip')
    if pull_return_code != 0:
        exit(pull_return_code)


if __name__ == "__main__":
    RUNNABLE_SCRIPTS = ('recreate_config', 'recreate_resource_stats', 'recreate_team_stats',  'fetch_translations')

    parser = ArgumentParser()
    parser.add_argument('cmd', nargs=1, choices=RUNNABLE_SCRIPTS)
    options = parser.parse_args()

    eval(options.cmd[0])()
