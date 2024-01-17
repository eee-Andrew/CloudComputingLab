import boto3

# Replace 'YOUR_ACCESS_KEY' and 'YOUR_SECRET_KEY' with your AWS access and secret keys
aws_access_key = 'YOUR_ACCESS_KEY'
aws_secret_key = 'YOUR_SECRET_KEY'
bucket_name = 'your-s3-bucket-name'
file_to_upload = 'path/to/your/file.txt'
uploaded_file_key = 'uploaded_file.txt'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Upload a file to S3
def upload_file():
    try:
        s3.upload_file(file_to_upload, bucket_name, uploaded_file_key)
        print(f'{file_to_upload} uploaded to {bucket_name}/{uploaded_file_key}')
    except Exception as e:
        print(f'Error uploading file: {e}')

# Download a file from S3
def download_file():
    try:
        s3.download_file(bucket_name, uploaded_file_key, f'downloaded_{uploaded_file_key}')
        print(f'{uploaded_file_key} downloaded to current directory')
    except Exception as e:
        print(f'Error downloading file: {e}')

if __name__ == "__main__":
    upload_file()
    download_file()
