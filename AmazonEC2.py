# python code for Launching an EC2 Instance
import boto.ec2
from time import sleep

ACCESS_KEY="<enter access key>" #enter your aws account access key
SECRET_KEY="<enter secret key>" #enter your aws account access key

REGION="us-east-1"
AMI_ID = "ami-d0f89fb9"
EC2_KEY_HANDLE = "<enter key handle>"
INSTANCE_TYPE="t1.micro"
SECGROUP_HANDLE="default"

print "Connecting to EC2"

conn = boto.ec2.connect_to_region(REGION, aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY) #set connection to EC2 service using
# your aws account access key and secret access key

print "Launching instance with AMI-ID %s, with keypair %s, instance type %s, security group %s"%(AMI_ID,EC2_KEY_HANDLE,INSTANCE_TYPE,SECGROUP_HANDLE)

reservation = conn.run_instances(image_id=AMI_ID,key_name=EC2_KEY_HANDLE,instance_type=INSTANCE_TYPE,security_groups=[SECGROUP_HANDLE,])

instance = reservation.instances[0]

print "Waiting for instance to be up and running"

status = instance.update()
while status == 'pending':
 sleep(10)
 status = instance.update()

if status == 'running':
    print "\n instance is now running, instance details are:"
    print "instance size: " + str(instance.instance_type)
    print "instance state: " + str(instance.state)
    print "instance Launch Time: " + str(instance.launch_time)
    print "instance public DNS: " + str(instance.public_dns_name)
    print "instance private DNS: " + str(instance.private_dns_name)
    print "instance IP: " +str(instance.ip_address)
    print "instance private IP : " + str(instance.private_ip_address)

