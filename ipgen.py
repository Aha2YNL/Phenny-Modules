#!/usr/bin/env python
import random

"""
Random IP Generator module.
Copyright 2011, Aha2Y. 

"""

#Function which generates random ip address.
def generateip(phenny, input):
    for x in range(0,1):
       A = random.randrange(255) + 1
       B = random.randrange(255) + 1
       C = random.randrange(255) + 1
       D = random.randrange(255) + 1
       ip = "%d.%d.%d.%d" % (A,B,C,D)
       phenny.say(ip)
generateip.commands = ['genip']
generateip.priority = 'medium'


