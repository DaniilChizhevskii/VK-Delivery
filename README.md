# VK Delivery
[![Python 3.5](https://img.shields.io/badge/Python-3.5-blue.svg)](https://python.org)
[![VK API 5.80](https://img.shields.io/badge/VK%20API-5.80-blue.svg)](https://vk.com/dev/manuals)
[![GNU GPL](https://img.shields.io/github/license/daniilchizhevskii/vk-delivery.svg)](/)

`VK Delivery` - скрипт для автоматической рассылки пользователям сообществ ВКонтакте.
Скрипт написан на `Python 3` с использованием `VK API`.

# Зависимости

[![vk >= 2.0](https://img.shields.io/badge/vk->=2.0-green.svg)](https://vk.com/antiparasite_package)

# Использование

* Установите зависимости.
* Перейдите в директорию `data` и измените настройки в файле `settings.py`.
* Запустите скрипт `delivery.py`.

Дополнительно:

* Только для рассылки поместите ID пользователей в файл `data/dialogs.json` и выполните команду `delivery.py send`.
* Только для сбора базы пользоватлей выполните команду `delivery.py get`. База будет находиться в файле `data/dialogs.json`.

# Контакты

[![Создатель](https://img.shields.io/badge/Author-%40nochnoj__hichnik-orange.svg)](https://vk.com/nochnoj_hichnik)
