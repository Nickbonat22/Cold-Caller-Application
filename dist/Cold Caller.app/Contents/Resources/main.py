#!/usr/bin/env python3
'''
Author: Jerry Xie

Created on: Apr 5, 2019

Last modified by: Jerry Xie @ Apr 7, 2019

Topic: GUI for Cold Caller

Effect: Demonstrating a GUI demo based on TKinter.

'''
import sys
sys.path.append("./Models")
sys.path.append("./Views")
sys.path.append("./Controllers")
from Controllers.mainViewController import MainViewController

app = MainViewController()