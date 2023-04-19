import boto3,os

# Use the assume_role method to create an AWS service client
sts_client = boto3.client('sts')
RoleArn = "arn:aws:iam::282874896445:role/aws-hsbc-datamo-pfm-role",

# Assume the role defined in your environment variables
response = sts_client.assume_role(
    RoleArn=RoleArn,
    RoleSessionName='session1'
)

# Create an S3 service client
s3_client = boto3.client(
    's3',
    aws_access_key_id=response['Credentials']['AccessKeyId'],
    aws_secret_access_key=response['Credentials']['SecretAccessKey'],
    aws_session_token=response['Credentials']['SessionToken'],
)

# Use the S3 client to perform S3 operations
response = s3_client.list_buckets()

# Refresh the credentials after they expire
if 'Expiration' in response['Credentials']:
    new_response = sts_client.assume_role(
        RoleArn=os.environ['AWS_ROLE_ARN'],
        RoleSessionName='session1',
        DurationSeconds=3600
    )

    # Update the S3 client with the new credentials
    s3_client = boto3.client(
        's3',
        aws_access_key_id=new_response['Credentials']['AccessKeyId'],
        aws_secret_access_key=new_response['Credentials']['SecretAccessKey'],
        aws_session_token=new_response['Credentials']['SessionToken'],
    )

# Use the cloudpath package to access S3
import cloudpath

s3_path = cloudpath.Path("s3://mybucket/mykey.txt")

# Download a file from S3
s3_path.download("/tmp/mykey.txt")

# Upload a file to S3
s3_path.upload("/tmp/mykey.txt")