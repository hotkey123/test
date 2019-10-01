#!/usr/bin/env python
import boto3
import subprocess
#output = subprocess.call(['/home/ansadmin/nagaratest/docker.sh'])
import time
ec2 = boto3.resource('ec2')
import yaml
config = yaml.load(open('config.yml'))

ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId = config['ImageId'],
    MinCount = config['MinCount'],
    MaxCount = config['MaxCount'],
    InstanceType = config['InstanceType'],
    KeyName = config['KeyName'],
    SubnetId = config['SubnetId'],
    UserData = '#!/bin/bash'+'\n'+'sudo su'+'\n'+'yum update -y'+'\n'+'yum install docker -y'+'\n'+'yum install git -y'+'\n'+'git clone https://github.com/asquarezone/DockerZone.git /home/ec2-user/tomcat_test'+'\n'+'sleep 15'+'\n'+'service docker start'+'\n'+'docker build -t tomcat_test /home/ec2-user/tomcat_test/ImageCreation/DockerFiles/tomcat_demo'+'\n'+'docker run -itd -p 8080:8080 tomcat_test')
print (instance[0].id)

instance = instance[0]
# Wait for the instance to enter the running state
instance.wait_until_running()

# Reload the instance attributes
instance.load()
print (instance.public_ip_address)
print ( "url is: " + instance.public_dns_name + ":8080" )
