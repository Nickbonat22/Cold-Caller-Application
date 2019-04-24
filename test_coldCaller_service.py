from student_queue import Student_queue
from student import Student
from coldCallerService import ColdCallerService
from tkinter import *
from test_coldCaller_scope_helper import testing_scope
g = testing_scope()

def update(name_labels):
    f = ColdCallerService.instance()
    for i in range(len(name_labels)):
        new_student = f.get_studnt_at(i)
        if not new_student == None:
            name_labels[i].config(text=new_student.getFName() + " " + new_student.getLName())
def remove(name_labels, pos:int, concern = False):
    global g
    f = ColdCallerService.instance()
    assert(f.curr_queue.studentQ == g.f.curr_queue.studentQ)
    if(not concern):
        if(f.perform_good_at(pos)):
            update(name_labels)
    else:
        if(f.perform_bad_at(pos)):
            update(name_labels)
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

    btn_group_1 = Frame(window)
    btn_group_1.grid(column=0,row=1,sticky=(N,W,S,E))
    removeB1 = Button(btn_group_1, text="Remove",command=lambda: remove([name1, name2, name3], 0))
    concernB1 = Button(btn_group_1, text="Concern",command=lambda: remove([name1, name2, name3], 0, True))
    removeB1.grid(column=0, row=0)
    concernB1.grid(column=1, row=0)

    btn_group_2 = Frame(window)
    btn_group_2.grid(column=1,row=1,sticky=(N,W,S,E))
    removeB2 = Button(btn_group_2, text="Remove",command=lambda: remove([name1, name2, name3], 1))
    concernB2 = Button(btn_group_2, text="Concern",command=lambda: remove([name1, name2, name3], 1, True))
    removeB2.grid(column=0, row=0)
    concernB2.grid(column=1, row=0)

    btn_group_3 = Frame(window)
    btn_group_3.grid(column=2,row=1,sticky=(N,W,S,E))
    removeB3 = Button(btn_group_3, text="Remove",command=lambda: remove([name1, name2, name3], 2))
    concernB3 = Button(btn_group_3, text="Concern",command=lambda: remove([name1, name2, name3], 2, True))
    removeB3.grid(column=0, row=0)
    concernB3.grid(column=1, row=0)


    window.mainloop()