# -*- coding: utf-8 -*-
#!/usr/bin/python

import unittest
from telegram import Bot
from ui import send_select_language_keyboard

TEST_BOT_TOKEN = ''
TEST_CHAT_ID = 161933860
bot = Bot(token=TEST_BOT_TOKEN)


class UiTest(unittest.TestCase):

    def test_send_select_language_keyboard(self):
        send_select_language_keyboard(bot=bot, user_id=TEST_CHAT_ID)
