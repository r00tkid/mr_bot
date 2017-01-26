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


def send_validate_city_keyboard(lang, user_id, bot, validated):
    """ validated is None or Location (pygeo) """
    sender = Sender(bot=bot)
    if lang == 'ru':
        text = 'К сожалению город не найден, попробуйте еще раз.'
        btn_caption_yes = 'Да'
        btn_caption_no = 'Нет'
    else:
        text = 'Sorry, i can not find this city. Please try again.'
        btn_caption_yes = 'Yes'
        btn_caption_no = 'No'
    if validated:
        buttons = [[btn_caption_yes, btn_caption_no]]
        callbacks = [['city_ok|%s' % user_id, 'city_false|%s' % user_id]]
        keyboard = kb.get_inline_keyboard(keyboard=buttons, callbacks=callbacks)
        sender.send_message(chat_id=user_id, text=str(validated), reply_markup=keyboard)
        return True
    else:
        sender.send_message(chat_id=user_id, text=text)
        return False


def send_manage_folders_keyboard(lang, user_id, bot):
    sender = Sender(bot=bot)
    if lang == 'ru':
        message_text = "Перешел в раздел управления папками"
        keyboard = [['<:file_folder:> Добавить папку', '<:pouch:> Список папок'],
        ['<:back:> Назад']]
    else:
        message_text = "We are in the folders manage section"
        keyboard = [['<:file_folder:> Add folder', '<:pouch:> Folders list'], ['<:back:>']]

    keyboard = kb.get_keyboard(keyboard=keyboard, is_one_time=False, is_selective=True)
    sender.send_message(chat_id=user_id, text=message_text, reply_markup=keyboard)
