import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

data = open('puppies.jpg', 'rb')
s3.buckets('vision20211').put_object(Key='puppies.jpg', Body=data)
