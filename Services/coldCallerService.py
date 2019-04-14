#   4/14/19 14:00
#   Created by: Jerry Xie
#   Contributors: Jerry Xie
#   Purpose of this code is as a prototype for accessing and modifying the queue class

from singleton import Singleton
import sys
sys.path.append("../Models/")
sys.path.append("..")
from Models.queue import Queue
from Models.student import Student

# By runing "python3 coldCallerService.py"
# You should see :
# Cold Caller Service started
# True

@Singleton
class ColdCallerService:
    _instance = None
    def __init__(self):
        print("Cold Caller Service started")
        print("Loading queue from IO service")
    
    def perform_good_at(self, position : int) -> bool:
        pass

    def perform_bad_at(self, position : int) -> bool:
        pass

    def perform_absent_at(self, position : int) -> bool:
        pass
    
    def get_studnt_at(self, position : int) -> Student:
        pass

if __name__ == '__main__':
    # f = ColdCallerService() # Error, this isn't how you get the instance of a singleton
    # test = Student("Test","Test","95111111","daa@email.com","Test","sdsd")
    # print(test)
    f = ColdCallerService.instance() # Good. Being explicit is in line with the Python Zen
    g = ColdCallerService.instance() # Returns already created instance

    print(f is g) # True