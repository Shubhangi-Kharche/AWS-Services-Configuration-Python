# AWS-Services-Configuration-Python
File Upload To S3
This is the python code to upload file to Amazon S3 Cloud Storage.
S3 is first established by calling boto.connect_s3 function.
The AWS access key and AWS secret access key are passed to this function
Two functions are used upload_to_s3_bucket_path and upload_to_s3_bucket_root
upload_to_s3_bucket_path uploads file to s3 bucket at the specified path
upload_to_s3_bucket_root uploads file to s3 bucket root
