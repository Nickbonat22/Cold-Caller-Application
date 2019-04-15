'''
CIS 422 Project 1
Contributors: Jerry Xie, Vu Vo
'''
from collections import deque
class Queue:
    studentQ = []
    def __init__(self,studentQ):
        stqueue = deque(studentQ)
        pass

    def pop(self):
        return stqueue.popleft()

    def push(self,student):
        return stqueue.append(student)

    def popfrom(self,location):
        #this function will remove a student from a specified location

    def pushRandom(self,student):
        #this function will randomly reinsert a student back into queue 
