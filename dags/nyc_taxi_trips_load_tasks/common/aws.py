import boto3


def upload_file_to_s3(file_path, destiny_path, credentials, content_type="image/png", acl="public-read"):
    img_data = open(file_path, "rb")
    s3 = boto3.resource('s3', aws_access_key_id=credentials.access_key, aws_secret_access_key=credentials.secret_key, region_name='us-east-2')
    bucket = s3.Bucket('social-wiki-datalake')
    bucket.put_object(
        Key=destiny_path,
        Body=img_data,
        ContentType=content_type,
        ACL=acl
    )
