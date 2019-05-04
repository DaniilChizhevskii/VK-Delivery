# VK Delivery
[![Python 3.5](https://img.shields.io/badge/Python-3.5-blue.svg)](https://python.org)
[![VK API 5.80](https://img.shields.io/badge/VK%20API-5.80-blue.svg)](https://vk.com/dev/manuals)
[![GNU GPL](https://img.shields.io/github/license/daniilchizhevskii/vk-delivery.svg)](/)

`VK Delivery` is a script for automatically sending to users of VKontakte communities.
The script is written in `Python 3` using `VK API`.

# Dependencies

[![vk> = 2.0](https://img.shields.io/badge/vk->=2.0-green.svg)](https://vk.com/antiparasite_package)

# Usage

Install this package from pip using `pip3 install vkdelivery` command.

# Arguments

Required:

* `tokens`: list of the VK community access tokens (*85-digit strings*);
* `group_id`: your community ID (*integer*).

`vkdelivery.send()` method:

* `message`: your message for the delivery (*string up to 4096 sybmols*);
* `dialogs`: list of the required users' IDs (*integers*).

Additional:

* `ui`: whether to display current progress (*boolean*).

# Methods

* `vkdelivery.get()`
  * Arguments:
    * `tokens` (reqiured);
    * `group_id` (reqiured);
    * `ui`.
  * Output format: list of the current community's dialogs (`[user_1, user_2, ..., user_n]`).

* `vkdelivery.send()`
  * Arguments:
    * `tokens` (reqiured);
    * `group_id` (reqiured);
    * `message` (reqiured);
    * `dialogs` (reqiured);
    * `ui`.
  * Output format: `True` expression.

* `vkdelivery.getandsend()`
  * Arguments:
    * `tokens` (reqiured);
    * `group_id` (reqiured);
    * `message` (reqiured);
    * `ui`.
  * Output format: `True` expression.

# Errors

* `vk.exceptions.VkAPIError`: standard VKontakte error;
* `KeyError`: one of arguments is missing or invalid.
* `SystemError`: one of arguments is invalid.

# Contacts

[![Mail | Daniil Chizhevskij](https://img.shields.io/badge/Mail-Daniil%20Chizhevskij-orange.svg)](mailto:daniilchizhevskij@gmail.com)