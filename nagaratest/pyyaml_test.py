#!/usr/bin/env python
import yaml
config = yaml.load(open('config.yml'))

Image = config['ImageId']

print (Image)

