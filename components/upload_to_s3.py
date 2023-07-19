import boto3

AWS_SHARED_CREDENTIALS_FILE = '~/.aws/credentials'
AWS_CONFIG_FILE = '~/.aws/config'

def upload_to_s3(input_file_path, bucket_name, s3_output_key):
    session = boto3.Session()
    s3 = session.resource('s3')

    # Filename - File to upload
    # Bucket - Bucket to upload to (the top level directory under AWS S3)
    # Key - S3 object name (can contain subdirectories). If not specified then file_name is used
    s3.meta.client.upload_file(Filename=input_file_path,
                            Bucket=bucket_name, Key=s3_output_key)




