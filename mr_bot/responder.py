# -*- coding: utf-8 -*-
from keyboard import KeyboardBuilder


# todo generate answer - choose answer by
class Answer:

    def __init__(self):
        self.kb = KeyboardBuilder()

    def _create_reply_keyboard(self, keyboard, is_one_time, is_selective):
        return self.kb.get_reply_keyboard(keyboard=keyboard,
                    is_one_time=is_one_time, is_selective=is_selective)

    def generate_answer():
        pass


class Responder:

    def __init__(self, sender):
        self.sender = sender

    def respond(self):
        print(self.kb)
