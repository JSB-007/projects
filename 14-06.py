import boto3

# AWS credentials (replace with your own)
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'

# Create an S3 client
s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

# Specify the details of your S3 bucket
bucket_name = 'your-bucket-name'

# Perform operations on the S3 bucket
# Example: List all objects in the bucket
response = s3.list_objects(Bucket=bucket_name)

# Print the object keys
for obj in response['Contents']:
    print(obj['Key'])
