#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 3/25/2023 9:06 PM
# @Author  : Owen_study
# @Email   : owen_study@126.com
# @File    : chatgpt.py
# @Software: PyCharm
# ===============================================
# import poai
import openai
from config_center import chatgpt_key


# def chat_old(question):
#     key = chatgpt_key()['chatgpt_key']
#     try:
#         answer = poai.chatgpt.chat(key, question)
#     except Exception as e:
#         answer = f"ai response error: {str(e)}"
#     return answer


# 直接使用openai接口进行查询
def chat(propmpt):
    key = chatgpt_key()['chatgpt_key']
    try:
        answer = chat_openai(key, propmpt, model_engine='text-davinci-003')
    except Exception as e:
        answer = f"ai response error: {str(e)}"
    return answer


def chat_openai(api_key, prompt, model_engine="text-davinci-003"):
    # 设置 API Key
    openai.api_key = api_key  # your_api_key

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # 获取 ChatGPT 的回复
    message = completions.choices[0].text
    print(message)
    return message


if __name__ == '__main__':
    pass
