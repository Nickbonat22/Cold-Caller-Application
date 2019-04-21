#   4/14/19 14:00
#   Created by: Jerry Xie
#   Contributors: Jerry Xie
#   Purpose of this code is as a prototype for accessing and modifying the queue class

from singleton import Singleton
from student_queue import Student_queue
from student import Student
from dailylog import dailyRemove, dailyConcern

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
    
    def perform_good_at(self, student_q : Student_queue, position : int) -> bool:
        if(student_q.isEmpty()):
            return False
        the_student = student_q.popfrom(position)
        the_student.correctQ += 1
        the_student.calledOnCount += 1
        student_q.pushRandom(the_student)
        dailyRemove(the_student)
        return True

    def perform_bad_at(self, student_q : Student_queue, position : int) -> bool:
        if(student_q.isEmpty()):
            return False
        the_student = student_q.popfrom(position)
        the_student.correctQ -= 1
        dailyConcern()
        return True
    
    def get_studnt_at(self, student_q : Student_queue, position : int) -> Student:
        if(student_q.isEmpty() or position >= student_q.length()):
            return None
        return student_q.get_student_at(position)

if __name__ == '__main__':
    # f = ColdCallerService() # Error, this isn't how you get the instance of a singleton
    # test = Student("Test","Test","95111111","daa@email.com","Test","sdsd")
    # print(test)
    f = ColdCallerService.instance() # Good. Being explicit is in line with the Python Zen
    g = ColdCallerService.instance() # Returns already created instance

    print(f is g) # True
    