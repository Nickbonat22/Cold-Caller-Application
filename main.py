#!/usr/bin/env python3
'''
Author: Jerry Xie

Created on: Apr 5, 2019

Last modified by: Jerry Xie @ Apr 7, 2019

Topic: GUI for Cold Caller

Effect: Demonstrating a GUI demo based on TKinter.

'''
from tkinter import *
from tkinter.ttk import *
from mainViewController import MainViewController
import student_queue
from student_queue import Student_queue
student_queue.REINSERTION_AFTER_FIRST_N_PERCENT = 60
a = Student_queue()

app = MainViewController()
app.show()

