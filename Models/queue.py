'''
CIS 422 Project 1
Contributors: Jerry Xie, Vu Vo, Qi Han
'''
from collections import deque
import random
import functools
REINSERTION_AFTER_FIRST_N_PERCENT = 30
class Queue:
    #studentQ = [] # [Studeng]
    def __init__(self):
        # call IOService to load a saved queue
        # if it doesnt find a save queue
        # init a new queue
        self.studentQ = []
		self.recent = None
    
	def push(self,item):
		self.studentQ.append(item)

	def pop(self):
		popItem = self.studentQ.pop(0)
		self.recent = popItem
		return popItem

	def isEmpty(self):
		return self.studentQ = []

	def get_item(self):
		return self.studentQ

    def get_first_three(self):# -> Student
        t = 3
        rslt = []
        for student in self.studentQ:
            if(t == 0):
                break
            rslt.append(student)
            t -= 1
        return rslt

	def length(self):
		return len(self.studentQ)

    def popfrom(self,location):
        # this function will remove a student from a specified location
        # and call IOService to save the queue
        #self.studentQ.pop(location)
        popItem = self.studentQ.pop(location)
		self.recent = popItem
		return popItem

    def length(self):
        return len(self.studentQ)

    def lastRemove(self):
		return self.recent

    def pushRandom(self,student):
        # dont forget to use the reinsertion_after_first_n_percent info
        # we can set this up in the main.py as an environment variable
        #this function will randomly reinsert a student back into queue
        value = random.randint(0, self.length()-1)
        self.studentQ.insert(value,student)
