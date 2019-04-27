#!/usr/bin/env python3
'''
Author: Jerry Xie

Created on: Apr 25, 2019

Last modified by: Jerry Xie @ Apr 27, 2019

Effect: To test singleton services' scope

'''
from IOService import IO

class testing_scope:
    def __init__(self):
        self.f = IO.instance()