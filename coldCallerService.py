#   4/14/19 14:00
#   Created by: Jerry Xie
#   Contributors: Jerry Xie
#   Purpose of this code is as a prototype for accessing and modifying the queue class

from singleton import Singleton
from student_queue import Student_queue
from student import Student
from logService import dailyRemove, dailyConcern
from IOPrototype import readFile

# By runing "python3 coldCallerService.py"
# You should see :
# Cold Caller Service started
# True

@Singleton
class ColdCallerService:
    _instance = None
    curr_queue = None
    def __init__(self):
        print("Cold Caller Service started")
        print("Loading queue from IO service")
        # call IOService to load a saved queue
        # if it doesnt find a save queue
        # init a new queue
        self.curr_queue = Student_queue()
        self.curr_queue.studentQ = readFile(self.curr_queue.studentQ)
    
    def perform_good_at(self, position : int) -> bool:
        if(self.curr_queue.isEmpty() or position >= self.curr_queue.length()):
            return False
        the_student = self.curr_queue.popfrom(position)
        the_student.correctQ += 1
        the_student.calledOnCount += 1
        self.curr_queue.pushRandom(the_student)
        dailyRemove(the_student)
        return True

    def perform_bad_at(self, position : int) -> bool:
        if(self.curr_queue.isEmpty() or position >= self.curr_queue.length()):
            return False
        the_student = self.curr_queue.lastRemove()
        the_student.correctQ -= 1
        dailyConcern(the_student)
        return True
    
    def get_studnt_at(self, position : int) -> Student:
        if(self.curr_queue.isEmpty() or position >= self.curr_queue.length()):
            return None
        return self.curr_queue.get_student_at(position)

if __name__ == '__main__':
    # f = ColdCallerService() # Error, this isn't how you get the instance of a singleton
    # test = Student("Test","Test","95111111","daa@email.com","Test","sdsd")
    # print(test)
    f = ColdCallerService.instance() # Good. Being explicit is in line with the Python Zen
    g = ColdCallerService.instance() # Returns already created instance

    print(f is g) # True
    