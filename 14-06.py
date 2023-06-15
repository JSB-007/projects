import boto3
import pandas as pd
from smart_open import open

# Set up AWS credentials
access_key = 'YOUR_ACCESS_KEY'
secret_key = 'YOUR_SECRET_KEY'
bucket_name = 'YOUR_BUCKET_NAME'
file_key = 'YOUR_FILE_KEY'  # The key or path of the file within the bucket

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

# Create an S3 client
s3_client = session.client('s3')

# Read the file from S3 into a DataFrame
s3_uri = f's3://{bucket_name}/{file_key}'
with open(s3_uri, 'rb') as file:
    df = pd.read_csv(file)

# Now you can work with the DataFrame
print(df.head())

#