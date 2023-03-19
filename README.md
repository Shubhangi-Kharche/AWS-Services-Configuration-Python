# AWS-Services-Configuration-Python
#1 File Upload To S3
This is the python code to upload file to Amazon S3 Cloud Storage.
S3 is first established by calling boto.connect_s3 function.
The AWS access key and AWS secret access key are passed to this function
Two functions are used upload_to_s3_bucket_path and upload_to_s3_bucket_root
upload_to_s3_bucket_path uploads file to s3 bucket at the specified path
upload_to_s3_bucket_root uploads file to s3 bucket root

#2 Launching an EC2 Instance
A connection to EC2 service is first established by calling boto.ec2.connect_to_region.
The EC2 region, AWS access key and AWS secret key are passed to this function.
After connecting to EC2, a new instance is launched using the conn.run_instances function.
The AMI-ID, instance type, EC2 key handle and security group are passed to this function.
This function returns areservation.
The instances associated with the reservation are obtained using reservation.instances.
Finally the status of an instance associated with the reservation is obtained using the instance.update function.
The program waits till the status of the newly launched instance becomes running and then prints the instance details such as public DNS, instance IP, and launch time.
