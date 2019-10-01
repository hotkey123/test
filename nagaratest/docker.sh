#!/bin/bash
sudo su
yum update -y
yum install docker -y
docker --version
yum install git -y
git clone https://github.com/asquarezone/DockerZone.git
docker build -t tomcat_test /DockerZone/ImageCreation/DockerFiles/tomcat_demo/Dockerfile
docker run -itd --port 92:92 tomcat_test
