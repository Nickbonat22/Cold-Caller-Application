'''
CIS 422 Project 1
Contributors: Jerry Xie, Vu Vo, Qi Han
'''
from collections import deque
import random
import math
import functools
REINSERTION_AFTER_FIRST_N_PERCENT = 30
class Student_queue:
    #studentQ = [] # [Studeng]
    def __init__(self):
        self.studentQ = []
        self.recent = None
    
    def __str__(self):
        rslt = ''
        for student in self.studentQ:
            rslt += student.getFName() + student.getLName()
            rslt += '->'
        return rslt
    
    def has_recent_student_on_deck(self):
        return not self.recent == None

    def isEmpty(self):
        return self.studentQ == []

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
    
    def clear_last_rencent(self):
        self.recent = None

    def popfrom(self,location):
        # this function will remove a student from a specified location
        # and call IOService to save the queue
        #self.studentQ.pop(location)
        self.recent = self.studentQ.pop(location)
        return self.recent

    def length(self):
        return len(self.studentQ)

    def lastRemove(self):
        return self.recent

    def pushRandom(self,student):
        # dont forget to use the reinsertion_after_first_n_percent info
        # we can set this up in the main.py as an environment variable
        #this function will randomly reinsert a student back into queue
        global REINSERTION_AFTER_FIRST_N_PERCENT
        lower_bound = math.floor(len(self.studentQ) * REINSERTION_AFTER_FIRST_N_PERCENT / 100)
        value = random.randint(lower_bound, len(self.studentQ))
        self.studentQ.insert(value,student)

    def get_student_at(self, position):
        return self.studentQ[position]