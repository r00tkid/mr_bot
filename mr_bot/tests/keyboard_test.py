# -*- coding: utf-8 -*-
#!/usr/bin/python
import unittest
from keyboard import KeyboardBuilder
from mr_logger.logger import Logger


class KeyboardTest(unittest.TestCase):
    logger = Logger()
    keyboard_builder = KeyboardBuilder()

    def test_get_inline_keyboard(self):
        keyboard = [['1', '2<:alien:>', '3'], ['4']]
        callbacks = [['1_cb', 'alien_cb', '3_cb'], ['4_cb']]
        keyboard = self.keyboard_builder.get_inline_keyboard(keyboard=keyboard, callbacks=callbacks)
        self.assertIsNotNone(keyboard['inline_keyboard'])

    def test_get_keyboard(self):
        keyboard = [['1', '2<:alien:>', '3'], ['4']]
        keyboard = self.keyboard_builder.get_keyboard(keyboard=keyboard, is_one_time=True,
                                                            is_selective=True)
        self.assertIsNotNone(keyboard['keyboard'])
