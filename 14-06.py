import boto3
import pandas as pd

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

# Download the file from S3
temp_file_path = '/path/to/temp/file.csv'  # Specify a temporary file path on your local system
s3_client.download_file(bucket_name, file_key, temp_file_path)

# Read the CSV file into a DataFrame
df = pd.read_csv(temp_file_path)

# Now you can work with the DataFrame
print(df.head())

# Clean up the temporary file
import os
os.remove(temp_file_path)
