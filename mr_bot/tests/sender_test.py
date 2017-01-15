# -*- coding: utf-8 -*-
#!/usr/bin/python

import unittest
from telegram import Bot
from sender import Sender, logger

TEST_BOT_TOKEN = ''
TEST_CHAT_ID = 161933860
bot = Bot(token=TEST_BOT_TOKEN)


class SenderTest(unittest.TestCase):
    sender = Sender(bot=bot)

    def test_send_simple_message(self):
        result = self.sender.send_message(chat_id=TEST_CHAT_ID,
                 text='AgADAgADWa0xGyTqpglMQ6fYM8gylh7OgQ0ABOD5lpITdqoF5EQEAAEC')
        if result:
            logger.ok('test message was send')
        else:
            logger.err('message was not send')
        self.assertTrue(result)



