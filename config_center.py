#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 1/11/2023 12:07 PM
# @Author  : Owen_study
# @Email   : owen_study@126.com
# @File    : config_center.py
# @Software: PyCharm
# ===============================================
import requests
import json
from setting import CONFIG_CENTER_TOKEN, CONFIG_CENTER_URL, DEFAULT_CHATGTP_KEY


def get_config_from_config_center(profile='ebaoeco', tenant='ebaoeco', env='local', application='data-migration-engine',
                                  url='https://ptdev-gw.insuremo.com') -> dict:
    if not profile:
        print("No tenant is specified, will use local folder!")
        # pb.logger(tenant).info('There is not tenant S3 config found, use local folder!')

        return {}

    headers = {
        'Authorization': CONFIG_CENTER_TOKEN,
        'Content-Type': 'application/json'
    }
    # print(f'CONFIG_CENTER_TOKEN:{CONFIG_CENTER_TOKEN}')
    payload = {}
    config_url = f"{url}/eBao/1.0/api/configs?profile={profile}&application={application}"
    # if url == 'https://ptdev-gw.insuremo.com':
    #     config_url = f"{url}/eBao/1.0/api/configs?profile={profile}&application={application}"
    # else:
    #     config_url = f"{url}/api/configs?profile={profile}&application={application}"

    print(f'config_url:{config_url}')
    config_data_response = requests.request("GET", config_url, headers=headers, data=payload)
    # config_data_response = requests.get(config_url, timeout=2, headers=headers)
    if config_data_response.status_code == 200:
        config_data = json.loads(config_data_response.content)
        config_data = config_data.get("data")
        config_data = {k.split('/')[-1]: v for k, v in config_data.items() if tenant in k}

        return config_data
    else:
        print(f'error info:{config_data_response}')
        print(
            "Error connecting to config center %s, %s" % (
            config_data_response.status_code, config_data_response.content))
        return {}

# Chatgpt key，以租户级进行配置
def chatgpt_key(tenant_id='ebaoeco'):
    try:
        all_config_data = get_config_from_config_center(tenant=tenant_id, url=CONFIG_CENTER_URL)
        chatgpt_config_data = {}
        if 'chatgpt_key' in all_config_data.keys():
            chatgpt_config_data = all_config_data
        if len(chatgpt_config_data) == 0:
            # 默认没有租户配置的处理，使用本地文件夹
            chatgpt_config_data = DEFAULT_CHATGTP_KEY
            print('There is not run param config found in config center, use default!')
        # 如果找不到配置信息，则使用本地文件的方式
    except Exception as e:
        chatgpt_config_data = DEFAULT_CHATGTP_KEY

    return chatgpt_config_data


def test():
    DOMAIN = 'https://ptdev-gw.insuremo.com'
    SERVICE_NAME = 'data-migration-engine'
    config_data = get_config_from_config_center('ebaoeco', 'ebaoeco', url=DOMAIN, application=SERVICE_NAME)
    print(config_data)


if __name__ == '__main__':
    test()
    pass
