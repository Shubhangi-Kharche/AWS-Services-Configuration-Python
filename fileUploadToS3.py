# python code for uploading a file to an s3 bucket
import boto.s3

ACCESS_KEY="<enter access key>" #enter your aws account access key
SECRET_KEY="<enter secret key>" #enter your aws account access key

conn = boto.connect_s3(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY) #set connection to s3 service using
# your aws account access key and secret access key
#boto.connect_s3() is a function wherein the keys are passed

def percent_cb(complete, total):
    print('.')

#upload file to the s3 bucket at the specified path
def upload_to_s3_bucket_path(bucketname, path, filename):
    mybucket = conn.get_bucket(bucketname)
    fullkeyname = os.path.join(path, filename)
    key = mybucket.new_key(fullkeyname)
    key.set_contents_from_filename(filename, cb=percent_cb, num_cb=10)

#upload file to the s3 bucket root
def upload_to_s3_bucket_root(bucketname, filename):
    mybucket = conn.get_bucket(bucketname)
    key = mybucket.new_key(filename)
    key.set_contents_from_filename(filename, cb=percent_cb, num_cb=10)

upload_to_s3_bucket_path('mybucketsk2023', 'data','file.txt') #provide your bucket name, path and filename
