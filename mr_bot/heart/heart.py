# -*- coding: utf-8 -*-
import json

from telegram import Update

DEFAULT = [
    [
        {}
    ]
]

class RequestParser:

    def __init__(self, request, bot):
        self.request_body = request.body.decode('utf8')
        update = json.loads(self.request_body)
        self.update = Update.de_json(update, bot=bot)

    def _parse_update(self):
        data = {}
        try:
            entity = self.update.message
            user_id = entity.from_user.id
            text = entity.text
        except KeyError:
            entity = self.update.callback_query
            user_id = entity.from_user.id


        data['']
        return data
    def _get_user_id(self):


    def _get_reply_markup(self):
        pass

    def do_response(self):
        user_id = self._get_user_id()
        reply_markup = self._get_reply_markup()
        template_name = self._get_template_name()


