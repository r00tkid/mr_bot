# -*- coding: utf-8 -*-
#!/usr/bin/python

import unittest
from ui import send_select_language_keyboard, send_manage_folders_keyboard
from .sender_test import bot, TEST_CHAT_ID


class UiTest(unittest.TestCase):

    def test_send_select_language_keyboard(self):
        #send_select_language_keyboard(bot=bot, user_id=TEST_CHAT_ID)
        pass

    def test_send_manage_folders_keyboard(self):
        send_manage_folders_keyboard(lang='ru', user_id=TEST_CHAT_ID, bot=bot)