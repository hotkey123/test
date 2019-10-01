#!/usr/bin/env python
import boto3
import time
ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId = 'ami-00eb20669e0990cb4',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'hotkey',
    UserData = 'file://home/ansadmin/nagaratest/docker.sh',
    SubnetId = 'subnet-03d2957232f55007d')
print (instance[0].id)
print (instance[0].public_dns_name)
print (instance[0].state)

instance = instance[0]

# Wait for the instance to enter the running state
instance.wait_until_running()

# Reload the instance attributes
instance.load()
print(instance.public_dns_name)
