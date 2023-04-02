#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 3/30/2023 12:14 PM
# @Author  : Owen_study
# @Email   : owen_study@126.com
# @File    : deep_search_service.py
# @Software: PyCharm
# ===============================================
from flask_restful import Resource
from flask import request, Response

from resources.chatgpt import chat


# Chatgpt test
class ChatGPT(Resource):
    def post(self):
        try:
            answer = ''
            data = request.get_json()
            question = data['question']
            answer = chat(question)
            # print(answer)
            return {"status": 0, "message": 'success', 'answer': answer}
        except Exception as e:
            return {"status": 1, "message": f"failed reason: {str(e)}", 'answer': answer}


if __name__ == '__main__':
    pass
