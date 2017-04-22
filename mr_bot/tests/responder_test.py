# -*- coding: utf-8 -*-
#!/usr/bin/python

import unittest
from telegram import Bot
from sender import Sender, logger
from responder import Responder, Answer
from settings import TEST_BOT_TOKEN, TEST_CHAT_ID
bot = Bot(token=TEST_BOT_TOKEN)


class ResponderTest(unittest.TestCase):
    sender = Sender(bot=bot)
    responder = Responder(sender=sender)

    def test_respond(self):
        logger.log(self.responder)
        answer = Answer()
        answer.create_reply_keyboard(keyboard=[['hello']], is_one_time=True, is_selective=True)
        # self.responder.respond(answer)

