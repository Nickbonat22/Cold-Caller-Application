#   4/14/19 14:00
#   Created by: Jerry Xie
#   Contributors: Jerry Xie
#   Purpose of this code is as a prototype for accessing and modifying the queue class

from singleton import Singleton
from student_queue import Student_queue
from student import Student
from logService import dailyRemove, dailyConcern
from IOService import IO

# By runing "python3 coldCallerService.py"
# You should see :
# Cold Caller Service started
# True

@Singleton
class ColdCallerService:
    def get_queue_length(self):
        f = IO.instance()
        curr_queue = f.get_curr_queue()
        return curr_queue.length()
    
    def perform_good(self):
        f = IO.instance()
        curr_queue = f.get_curr_queue()
        curr_queue.clear_last_rencent()

    def remove_stuent_at(self, position : int) -> bool:
        f = IO.instance()
        curr_queue = f.get_curr_queue()
        if(curr_queue.isEmpty() or position >= curr_queue.length()):
            return False
        the_student = curr_queue.popfrom(position)
        the_student.calledOnCount += 1
        curr_queue.pushRandom(the_student)
        dailyRemove(the_student)
        f.set_curr_queue(curr_queue)
        return True

    def concern_recent_student(self) -> bool:
        f = IO.instance()
        curr_queue = f.get_curr_queue()
        if(not curr_queue.has_recent_student_on_deck() or curr_queue.isEmpty()):
            return False
        the_student = curr_queue.lastRemove()
        the_student.concernCount += 1
        dailyConcern(the_student)
        return True
    
    def get_studnt_at(self, position : int) -> Student:
        f = IO.instance()
        curr_queue = f.get_curr_queue()
        if(curr_queue.isEmpty() or position >= curr_queue.length()):
            return None
        return curr_queue.get_student_at(position)

if __name__ == '__main__':
    # f = ColdCallerService() # Error, this isn't how you get the instance of a singleton
    # test = Student("Test","Test","95111111","daa@email.com","Test","sdsd")
    # print(test)
    f = ColdCallerService.instance() # Good. Being explicit is in line with the Python Zen
    g = ColdCallerService.instance() # Returns already created instance

    print(f is g) # True
    