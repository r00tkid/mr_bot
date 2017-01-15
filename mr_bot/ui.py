# -*- coding: utf-8 -*-
#!/usr/bin/python
from mr_bot.sender import Sender
from mr_bot.keyboard import KeyboardBuilder

DEFAULT_LANGUAGE = 'EN'


def send_select_language_keyboard(bot, user_id):
    sender = Sender(bot=bot)
    kb = KeyboardBuilder()
    message_text = "Please select your language:"
    keyboard = [['<:earth_asia:>Russian', '<:earth_americas:>English']]
    keyboard = kb.get_keyboard(keyboard=keyboard, is_one_time=True, is_selective=True)
    sender.send_message(chat_id=user_id, text=message_text, reply_markup=keyboard)