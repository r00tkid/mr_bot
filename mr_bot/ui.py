# -*- coding: utf-8 -*-
#!/usr/bin/python
from mr_bot.sender import Sender
from mr_bot.keyboard import KeyboardBuilder

DEFAULT_LANGUAGE = 'EN'
kb = KeyboardBuilder()


def send_select_language_keyboard(bot, user_id):
    sender = Sender(bot=bot)
    message_text = "Please select your language:"
    keyboard = [['<:earth_asia:>Russian', '<:earth_americas:>English']]
    keyboard = kb.get_keyboard(keyboard=keyboard, is_one_time=True, is_selective=True)
    sender.send_message(chat_id=user_id, text=message_text, reply_markup=keyboard)


def send_reponse_on_language_select_action(lang, user_id, bot, keyboard):
    sender = Sender(bot=bot)
    if lang == 'ru':
        text = 'Я сохранил ваши языковые настройки.'
    elif lang == 'en':
        text = 'I have saved your language settings.'
    sender.send_message(chat_id=user_id, text=text, reply_markup=keyboard)