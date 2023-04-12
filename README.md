Український переклад документації Python
========================================
![build](https://github.com/python/python-docs-uk/workflows/.github/workflows/update-and-build.yml/badge.svg)

Якщо ви знайшли помилку або маєте пропозицію,
[додати issue](https://github.com/python/python-docs-uk/issues) у цьому проєкті або запропонуйте зміни:

* Зареєструйтесь на платформі [Transifex](https://www.transifex.com/) 
* Перейдіть на сторінку [документації Python](https://www.transifex.com/python-doc/python-newest/).
* Натисніть кнопку „Join Team”, оберіть українську (uk) мову та натисніть „Join”, щоб приєднатися до команди.
* Приєднавшись до команди, виберіть ресурс, що хочете виправити/оновити.
* Ваш прогрес буде відображатися у файлі [TEAM.md](TEAM.md).

Додаткову інформацію про використання Transifex дивіться [в документації](https://docs.transifex.com/getting-started-1/translators).

Українська мова з’явиться в меню вибору мови docs.python.org, [коли будуть повністю перекладені](https://www.python.org/dev/peps/pep-0545/#add-translation-to-the-language-switcher):
* `bugs`,
* всі ресурси в каталозі `tutorial`,
* `library/functions`.
Поточний прогрес у файлі [RESOURCE.md](RESOURCE.md)  

**Як переглянути останню збірку документації?**

Завантажте останню створену документацію зі списку артефактів в останній дії GitHub (вкладка Actions).
Переклади завантажуються з Transifex до цього репозиторію щодня.
Документація на python.org оновлюється приблизно раз на день.

**Канали зв'язку**

* [Telegram-чат перекладачів](https://t.me/+dXwqHZ0KPKYyNDc6)
* [Python translations working group](https://mail.python.org/mailman3/lists/translation.python.org/)
* [Python Documentation Special Interest Group](https://www.python.org/community/sigs/current/doc-sig/)

**Ліцензія**

Запрошуючи вас до спільного створення проєкту на платформі Transifex, ми пропонуємо договір на передачу ваших перекладів
Python Software Foundation [по ліцензії CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.uk).
Натомість ви побачите, що ви є перекладачем тієї частини, яку ви переклали.
Ви висловлюєте свою згоду з цією угодою, надаючи свою роботу для включення в документацію.

**Налаштування**
* `pip install transifex-python`
* Згенерувати [ключ API](https://app.transifex.com/user/settings/api/) та зберегти локально
* `export TX_TOKEN=token_from_previous_step`

**Оновлення статистики**
* `.github/scripts/manage_translation.py recreate_resource_stats`
* `.github/scripts/manage_translation.py recreate_team_stats`

**Оновлення локального перекладу**
* `.github/scripts/manage_translation.py recreate_config`
* `.github/scripts/manage_translation.py fetch_translations`

**Подяка**
* Maciej Olko - Polish team
* Julien Palard - French team
* Tomo Cocoa - Japanese team
