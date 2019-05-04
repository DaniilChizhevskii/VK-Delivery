VK Delivery
===========

|Python 3.5| |VK API 5.80| |GNU GPL|

``VK Delivery`` is a script for automatically sending to users of
VKontakte communities. The script is written in ``Python 3`` using
``VK API``.

Dependencies
============

|vk> = 2.0|

Usage
=====

Install this package from pip using ``pip3 install vkdelivery`` command.

Arguments
========

Required:

-  ``tokens``: list of the VK community access tokens (*85-digit
   strings*);
-  ``group_id``: your community ID (*integer*).

``vkdelivery.send()`` method:

-  ``message``: your message for the delivery (*string up to 4096
   sybmols*);
-  ``dialogs``: list of the required users’ IDs (*integers*).

Additional:

-  ``ui``: whether to display current progress (*boolean*).

Methods
=======

-  ``vkdelivery.get()``

   -  Arguments:

      -  ``tokens`` (reqiured);
      -  ``group_id`` (reqiured);
      -  ``ui``.

   -  Output format: list of the current community’s dialogs
      (``[user_1, user_2, ..., user_n]``).

-  ``vkdelivery.send()``

   -  Arguments:

      -  ``tokens`` (reqiured);
      -  ``group_id`` (reqiured);
      -  ``message`` (reqiured);
      -  ``dialogs`` (reqiured);
      -  ``ui``.

   -  Output format: ``True`` expression.

-  ``vkdelivery.getandsend()``

   -  Arguments:

      -  ``tokens`` (reqiured);
      -  ``group_id`` (reqiured);
      -  ``message`` (reqiured);
      -  ``ui``.

   -  Output format: ``True`` expression.

Errors
======

-  ``vk.exceptions.VkAPIError``: standard VKontakte error;
-  ``KeyError``: one of arguments is missing or invalid.
-  ``SystemError``: one of arguments is invalid.

Contacts
========

|Daniil Chizhevskij|

.. |Python 3.5| image:: https://img.shields.io/badge/Python-3.5-blue.svg
   :target: https://python.org
.. |VK API 5.80| image:: https://img.shields.io/badge/VK%20API-5.80-blue.svg
   :target: https://vk.com/dev/manuals
.. |GNU GPL| image:: https://img.shields.io/github/license/daniilchizhevskii/vk-delivery.svg
   :target: /
.. |vk> = 2.0| image:: https://img.shields.io/badge/vk-%3E=2.0-green.svg
   :target: https://vk.com/antiparasite_package
.. |Daniil Chizhevskij| image:: https://img.shields.io/badge/Mail-Daniil%20Chizhevskij-orange.svg
   :target: mailto:daniilchizhevskij@gmail.com