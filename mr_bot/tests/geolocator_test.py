# -*- coding: utf-8 -*-
#!/usr/bin/python

import unittest
from geolocator import locate, GeoValidator
from sender import Sender
from .sender_test import bot, TEST_CHAT_ID
import time


class GeoValidatorTest(unittest.TestCase):

    sender = Sender(bot=bot)
    validator = GeoValidator(sender=sender)

    def test_locate(self):
        self.assertIsNotNone(locate('Kaliningrad'))
        self.assertIsNone(locate('012Kaliningrad'))

    def test_geo_validator(self):
        self.validator.validate(incoming_city='San Hose"', lang='en',
                                chat_id=TEST_CHAT_ID)
        time.sleep(0.5)
        self.validator.validate(incoming_city='Gdansk"', lang='en',
                        chat_id=TEST_CHAT_ID)
        time.sleep(0.5)
        self.validator.validate(incoming_city='Киев"', lang='ru',
                        chat_id=TEST_CHAT_ID)