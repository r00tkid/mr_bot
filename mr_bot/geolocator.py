# -*- coding: utf-8 -*-
#!/usr/bin/python

from geopy.geocoders import Nominatim
from mr_logger.logger import Logger
from keyboard import KeyboardBuilder
geolocator = Nominatim()
logger = Logger()


def locate(location):
    result = None
    try:
        result = geolocator.geocode(str(location))
    except Exception as e:
        logger.warn('Can not get location %s in maxmind db;\n%s' % (location, e))
    return result


class GeoValidator:
    """ class for validate city throw pygeo and sending response """
    sender = None

    def __init__(self, sender):
        self.sender = sender

    #def ehlo(self):

    def validate(self, incoming_city, lang, chat_id):
        """ this method will validate address with pygeo """
        validated = locate(incoming_city)
        if lang is 'ru':
            text = 'К сожалению город не найден, попробуйте еще раз.'
            btn_caption_yes = 'Да'
            btn_caption_no = 'Нет'
        else:
            text = 'Sorry, i can not find this city. Please try again.'
            btn_caption_yes = 'Yes'
            btn_caption_no = 'No'
        if validated:
            buttons = [[btn_caption_yes, btn_caption_no]]
            callbacks = [['city_ok|%s' % chat_id, 'city_false|%s' % chat_id]]
            kb = KeyboardBuilder()
            keyboard = kb.get_inline_keyboard(keyboard=buttons, callbacks=callbacks)
            self.sender.send_message(chat_id=chat_id, text=str(validated), reply_markup=keyboard)
            return True
        else:
            self.sender.send_message(chat_id=chat_id, text=text)
            return False