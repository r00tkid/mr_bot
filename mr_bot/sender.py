# -*- coding: utf-8 -*-
#!/usr/bin/python

import traceback
from mr_logger.logger import Logger
from telegram.error import BadRequest, Unauthorized

logger = Logger()


class Sender:
    """ this class will send bot messages (photo, voice, video, audio, docs) """
    """ bot is instance if Telegram bot """
    """ return True on success and false on error """

    bot = None

    def __init__(self, bot):
        self.bot = bot

    def edit_message_text(self, message_id, chat_id, text, reply_markup, parse_mode='HTML'):
        try:
            self.bot.editMessageText(message_id=message_id, chat_id=chat_id,
                                                            text=text, reply_markup=reply_markup,
                                                            parse_mode=parse_mode)
            return True
        except BadRequest as bad_request_exception:
            logger.warn(traceback.format_exception_only(type(bad_request_exception),
            bad_request_exception))
        except Unauthorized:
            logger.warn('[Unauthorized]: cant edit message text.\nID=%s' % str(message_id))
        except Exception as e:
            logger.err(e)
        return False


    def edit_inline_message_text(self, inline_message_id, text, reply_markup):
        try:
            self.bot.editMessageText(inline_message_id=inline_message_id,
                                                            text=text, reply_markup=reply_markup)
            return True
        except BadRequest as bad_request_exception:
            logger.warn(traceback.format_exception_only(type(bad_request_exception),
            bad_request_exception))
        except Unauthorized:
            logger.warn('[Unauthorized]: cant edit message text.\nID=%s' % str(inline_message_id))
        except Exception as e:
            logger.err(e)
        return False


    # todo venue
    def send_message(self, chat_id, parse_mode=None, text=None, photo=None, video=None, document=None,
                     voice=None, audio=None, sticker=None, location=None, contact=None,
                     reply_markup=None, reply_to_message_id=None):
        try:
            if text:
                if not parse_mode:
                    self.bot.sendMessage(chat_id=chat_id,
                                    text=text, reply_markup=reply_markup,
                                    reply_to_message_id=reply_to_message_id)
                else:
                    self.bot.sendMessage(chat_id=chat_id,
                                    text=text, reply_markup=reply_markup,
                                    reply_to_message_id=reply_to_message_id, parse_mode=parse_mode)
            elif photo:
                self.bot.sendPhoto(chat_id=chat_id, photo=photo, reply_markup=reply_markup,
                                   reply_to_message_id=reply_to_message_id)
            elif video:
                self.bot.sendVideo(chat_id=chat_id, video=video, reply_markup=reply_markup,
                                   reply_to_message_id=reply_to_message_id)
            elif document:
                self.bot.sendDocument(chat_id=chat_id, document=document, reply_markup=reply_markup,
                                   reply_to_message_id=reply_to_message_id)
            elif voice:
                self.bot.sendVoice(chat_id=chat_id, voice=voice, reply_markup=reply_markup,
                                   reply_to_message_id=reply_to_message_id)
            elif audio:
                self.bot.sendAudio(chat_id=chat_id, audio=audio, reply_markup=reply_markup,
                                   reply_to_message_id=reply_to_message_id)
            elif sticker:
                self.bot.sendSticker(chat_id=chat_id, sticker=sticker, reply_markup=reply_markup,
                    reply_to_message_id=reply_to_message_id)
            elif location:
                self.bot.sendLocation(chat_id=chat_id, latitude=location.latitude,
                                      longitude=location.longitude, reply_markup=reply_markup,
                                      reply_to_message_id=reply_to_message_id)
            elif contact:
                self.bot.sendContact(chat_id=chat_id, phone_number=contact.phone_number,
                                     first_name=contact.first_name, reply_markup=reply_markup,
                                     reply_to_message_id=reply_to_message_id)
            return True
        except BadRequest as bad_request_exception:
            logger.warn(traceback.format_exception_only(type(bad_request_exception),
            bad_request_exception))
        except Unauthorized:
            logger.warn('cant send message to chat_id %s ( the bot was blocked by the user )'
            % str(chat_id))
        except Exception as e:
            logger.err(e)
        return False
