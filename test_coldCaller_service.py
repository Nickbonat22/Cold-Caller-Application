from student_queue import Student_queue
from student import Student
from coldCallerService import ColdCallerService
from tkinter import *
from test_coldCaller_scope_helper import testing_scope
g = testing_scope()
def remove(name_labels, pos:int):
    global g
    f = ColdCallerService.instance()
    assert(f.curr_queue.studentQ == g.f.curr_queue.studentQ)  
    if(f.perform_good_at(pos)):
        for i in range(len(name_labels)):
            new_student = f.get_studnt_at(i)
            if not new_student == None:
                name_labels[i].config(text=new_student.getFName() + " " + new_student.getLName())

if __name__ == '__main__':
    f = ColdCallerService.instance()

    window = Tk()
    window.title("Cold Call")
    window.geometry('350x200')

    Student1 = f.get_studnt_at(0)
    name1 = Label(window, text=Student1.getFName() +" "+ Student1.getLName())
    name1.grid(column=0, row=0)

    Student2 = f.get_studnt_at(1)
    name2 = Label(window, text=Student2.getFName() +" "+ Student2.getLName())
    name2.grid(column=1, row=0)

    Student3 = f.get_studnt_at(2)
    name3 = Label(window, text=Student3.getFName() +" "+ Student3.getLName())
    name3.grid(column=2, row=0)

    removeB1 = Button(window, text="Remove",command=lambda: remove([name1, name2, name3], 0))
    removeB1.grid(column=0,row=1)
    removeB2 = Button(window, text="Remove",command=lambda: remove([name1, name2, name3], 1))
    removeB2.grid(column=1,row=1)
    removeB3 = Button(window, text="Remove",command=lambda: remove([name1, name2, name3], 2))
    removeB3.grid(column=2,row=1)

    window.mainloop()