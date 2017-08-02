# -*- coding: utf-8 -*-
#!/usr/bin/python
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup
import emoji
import re
from mr_logger.logger import Logger


class KeyboardBuilder:
    """ keyboard incoming data:
        [
             ['1<emo_code>'], ['2'], ['3'],
             ['4', '5'], ['6'],
             ['7'], ['8', '9']
        ]
    """

    def __init__(self):
        self.logger = Logger()

    @staticmethod
    def get_emo(code):
        """ get emotion unicode """
        emo = emoji.emojize(code, use_aliases=True)
        return emo

    def _basic_prepare(self, keyboard):
        """ change <code> to emoji in buttons  """
        result_keyboard = []
        for line in keyboard:
            btn_line = []
            for button in line:
                emo = re.search(r'<.*?>', button)
                if emo:
                    marker = emo.group(0)
                    emo_code = marker.replace('<', '').replace('>', '')
                    button = button.replace(marker, self.get_emo(emo_code))
                btn_line.append(button)
            result_keyboard.append(btn_line)
        return result_keyboard

    def _inline_prepare(self, keyboard, callbacks, urls=None):
        """ create inline keyboard from list of list """
        inline_keyboard = []
        for ind_line, line in enumerate(keyboard):
            btn_line = []
            for ind_btn, button in enumerate(line):
                if not urls:
                    button = InlineKeyboardButton(text=button,
                                                  callback_data=callbacks[ind_line][ind_btn])
                else:
                    button = InlineKeyboardButton(text=button,
                                                  callback_data=callbacks[ind_line][ind_btn],
                                                  url=urls[ind_line][ind_btn])
                btn_line.append(button)
            inline_keyboard.append(btn_line)
        return inline_keyboard

    def get_keyboard(self, keyboard, is_one_time, is_selective):
        """ basic method for get reply keyboard """
        keyboard = self._basic_prepare(keyboard=keyboard)
        return ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=is_one_time,
                    selective=is_selective, resize_keyboard=True)

    def get_inline_keyboard(self, keyboard, callbacks):
        """ method for get inline keyboard """
        keyboard = self._basic_prepare(keyboard)
        inline_keyboard = self._inline_prepare(keyboard=keyboard, callbacks=callbacks)
        return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
