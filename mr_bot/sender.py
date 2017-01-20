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

    def send_message(self, chat_id, text=None, photo=None, video=None, document=None,
                     voice=None, audio=None, reply_markup=None, reply_to_message_id=None):
        try:
            if text:
                self.bot.sendMessage(chat_id=chat_id,
                                text=text, reply_markup=reply_markup,
                                reply_to_message_id=reply_to_message_id)
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

    def send_bunch_of_messages(self, users, text, photo=None):
        """ will send message for each user in users list """
        logger.log(text)
        for user in users:
            logger.log(user.id)
            self.send_message(chat_id=user.id, text=text, photo=photo)
