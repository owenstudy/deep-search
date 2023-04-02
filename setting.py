#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 12/7/2022 9:07 PM
# @Author  : Owen_study
# @Email   : owen_study@126.com
# @File    : setting.py
# @Software: PyCharm
# ===============================================
# 需要从配置中心读取指定的配置信息

# 支持的s3类型，目前共有两种，一种是公司内部的s3,一种是公有云s3
import os


class S3Type(object):
    S3_MINIO = 'minio'
    S3_AWS = 'aws'


CLOUD_CONFIG = {
    'use_cloud_s3': False,
    's3_type': S3Type.S3_AWS
    # 's3_type': S3Type.S3_MINIO
}

# 公司内部的s3配置
MINIO_S3_CONFIG = {
    's3_aws_id': '',
    's3_aws_secret': '',
    's3_bucket_name': '',
    's3_endpoint': 'https://s3-minio-dev.insuremo.com'
}

# 公有云的配置
AWS_S3_CONFIG = {
    's3_aws_id': '',
    's3_aws_secret': '',
    's3_bucket_name': '',
    's3_region': 'ap-southeast-1'
}

# Config center token, sample for ptdev,默认从环境变更获取
CONFIG_CENTER_TOKEN = f"Bearer {os.getenv('ebao_config_center_token', 'eBaoCCBpLnlpoA0JljQNOJDLprHfsZCA')}"
CONFIG_CENTER_URL = os.getenv("ebao_config_center_url", 'https://ptdev-gw.insuremo.com')


# default chatgpt api key
DEFAULT_CHATGTP_KEY = {
    "chatgpt_key": "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"
}

if __name__ == '__main__':
    pass
