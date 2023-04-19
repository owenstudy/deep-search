#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path

# @Time    : 4/4/2023 3:27 PM
# @Author  : Owen_study
# @Email   : owen_study@126.com
# @File    : aws_role_access_test.py
# @Software: PyCharm
# ===============================================
import boto3

# The calls to AWS STS AssumeRole must be signed with the access key ID
# and secret access key of an existing IAM user or by using existing temporary
# credentials such as those from another role. (You cannot call AssumeRole
# with the access key for the root account.) The credentials can be in
# environment variables or in a configuration file and will be discovered
# automatically by the boto3.client() function. For more information, see the
# Python SDK documentation:
# http://boto3.readthedocs.io/en/latest/reference/services/sts.html#client

# create an STS client object that represents a live connection to the
# STS service
sts_client = boto3.client('sts')

# Call the assume_role method of the STSConnection object and pass the role
# ARN and a role session name.
assumed_role_object = sts_client.assume_role(
    RoleArn="arn:aws:iam::282874896445:role/aws-hsbc-datamo-pfm-role",
    # RoleArn="arn:aws:iam::792248265079:role/s3test",
    # RoleArn="arn:aws:iam::account-of-role-to-assume:role/name-of-role",
    RoleSessionName="AssumeRoleSession1"
)

# From the response that contains the assumed role, get the temporary
# credentials that can be used to make subsequent API calls
credentials = assumed_role_object['Credentials']

# Use the temporary credentials that AssumeRole returns to make a
# connection to Amazon S3
s3_resource = boto3.resource(
    's3',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken'],
)

client = boto3.client('s3')
bucket_name = 'aws-hsbc-datamo-pfm-bucket'
object_name = os.path.basename('README.md')
client.upload_file('README.md',bucket_name,object_name)

# Use the Amazon S3 resource object that is now configured with the
# credentials to access your S3 buckets.
for bucket in s3_resource.buckets.all():
    print(bucket.name)

if __name__ == '__main__':
    pass