'''
CIS 422 Project 1
Contributors: Jerry Xie, Vu Vo
'''
from collections import deque
REINSERTION_AFTER_FIRST_N_PERCENT = 30
class Queue:
    studentQ = [] # [Studeng]
    def __init__(self):
        # call IOService to load a saved queue
        # if it doesnt find a save queue
        # init a new queue
        pass
    
    def get_first_three(self):# -> Student
        t = 3
        rslt = []
        for student in self.studentQ:
            if(t == 0):
                break
            rslt.append(student)
            t -= 1
        return rslt

    def popfrom(self,location):
        # this function will remove a student from a specified location
        # and call IOService to save the queue
        self.studentQ.pop(location)
        pass

    def pushRandom(self,student):
        # dont forget to use the reinsertion_after_first_n_percent info
        # we can set this up in the main.py as an environment variable
        #this function will randomly reinsert a student back into queue
        global REINSERTION_AFTER_FIRST_N_PERCENT
        print(REINSERTION_AFTER_FIRST_N_PERCENT)
        pass