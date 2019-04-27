#!/usr/bin/env python3
'''
Author: Jerry Xie

Created on: Apr 5, 2019

Last modified by: Jerry Xie @ Apr 9, 2019

Topic: Controller for Main View

Effect: Handle MainView intereaction, response logic

'''
from tkinter import *
# from tkinter.ttk import *
from MainView import *
from coldCallerTabView import ColdCallerTabView
from coldCallerService import ColdCallerService
from student import Student
from logService import getDailyLog

CONCERN_1A = 'c'
CONCERN_1B = 'v'
CONCERN_2 = 'b'
CONCERN_3 = 'n'
REMOVE_1A = '1'
REMOVE_1B = '<space>'
REMOVE_2 = '2'
REMOVE_3 = '3'

class MainViewController():
    def __init__(self):
        self.num_popup = 0
        self.aboutme_popup = None
        self.fontsize_popup = None

        self.root = Tk()
        self.root.title("Cold Caller")
        self.root.geometry("500x500")
        rows = 0
        while rows <= 50:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows += 1

        self.mainView = MainView(self.root)
        self.mainView.grid(row=0, column=0, columnspan=50, rowspan=50, sticky=(N,W,S,E))
        self.cold_caller_tab_view = self.mainView.get_cold_caller_tab_view()

        # Call Cold Caller Service to get the first 3 students
        self.update_stuents_portrait()
        # Bind button/keystrokes to Cold Caller Service APIs
        self.cold_caller_tab_view.createWidgets_bottom_Frame()
        self.cold_caller_tab_view.good_btns[1].bind("<Button-1>", lambda e: self.remove(e, 0))
        self.cold_caller_tab_view.concern_btns[1].bind("<Button-1>", lambda e: self.remove(e, 0, True))

        self.cold_caller_tab_view.good_btns[2].bind("<Button-1>", lambda e: self.remove(e, 1))
        self.cold_caller_tab_view.concern_btns[2].bind("<Button-1>", lambda e: self.remove(e, 1, True))

        self.cold_caller_tab_view.good_btns[3].bind("<Button-1>", lambda e: self.remove(e, 2))
        self.cold_caller_tab_view.concern_btns[3].bind("<Button-1>", lambda e: self.remove(e, 2, True))
        # Keystrokes mapping
        global CONCERN_1A, CONCERN_1B, CONCERN_2, CONCERN_3
        global REMOVE_1A, REMOVE_1B, REMOVE_2, REMOVE_3
        self.root.bind(CONCERN_1A, lambda e: self.remove(e, 0, True))
        self.root.bind(CONCERN_1B, lambda e: self.remove(e, 0, True))
        self.root.bind(CONCERN_2, lambda e: self.remove(e, 1, True))
        self.root.bind(CONCERN_3, lambda e: self.remove(e, 2, True))

        self.root.bind(REMOVE_1A, lambda e: self.remove(e, 0))
        self.root.bind(REMOVE_1B, lambda e: self.remove(e, 0))
        self.root.bind(REMOVE_2, lambda e: self.remove(e, 1))
        self.root.bind(REMOVE_3, lambda e: self.remove(e, 2))

        # Load the log file and set log tab's text
        self.mainView.get_log_tab_view().refresh_log.config(command=lambda: self.mainView.get_log_tab_view().set_text(getDailyLog()))

        self.createMenu()
    
    def update_stuents_portrait(self):
        f = ColdCallerService.instance()
        for i in range(3):
            new_student = f.get_studnt_at(i)
            if not new_student == None:
                self.mainView.get_cold_caller_tab_view().set_Widgets_top_portrait(i, name=new_student.getFName() + " " + new_student.getLName(), spelling=new_student.getPSpell())
     
    def remove(self, event, pos:int, concern = False):
        if(self.mainView.nb.index("current") == 0 and self.num_popup == 0):
            f = ColdCallerService.instance()
            if(not concern):
                if(f.remove_stuent_at(pos)):
                    self.update_stuents_portrait()
            else:
                f.concern_recent_student()

    def test_func(self, event, arg = None):
        if(self.mainView.nb.index("current") == 0 and self.num_popup == 0):
            print("It worked in the tab", event.type)
            if(not arg == None):
                print("Arguments passed", arg)
    
    def createMenu(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.submenu= Menu(self.menu)
        self.menu.add_cascade(label="Import/Export",menu=self.submenu)
        self.submenu.add_command(label="Import a roster", command=self.test_func)
        self.submenu.add_command(label="Export to a roster", command=self.test_func)
        self.submenu.add_separator()
        self.submenu.add_command(label="Exit", command=self.root.quit)

        self.submenu2 = Menu(self.menu)
        self.menu.add_cascade(label="Misc",menu=self.submenu2)
        self.submenu2.add_command(label="Font size", command=self.font_size_window)
        self.submenu2.add_command(label="About", command=self.aboutme_window)

    def destory_popup_window_after(self, popup, doing_this_before = None):
        if not doing_this_before == None:
            try:
                doing_this_before()
            except Exception as e:
                print(e)
        popup.destroy()
        self.num_popup -= 1
    
    def font_size_window(self):
        try:
            self.font_size_window.focus_set()
            return
        except Exception:
            pass
        self.num_popup += 1
        self.fontsize_popup = Toplevel(self.root)
        self.fontsize_popup.title("Set names' font size")
        self.fontsize_popup.resizable(0,0)

        onclosing = lambda: self.destory_popup_window_after(self.fontsize_popup)
        self.fontsize_popup.protocol('WM_DELETE_WINDOW', onclosing)
        Label(self.fontsize_popup,text="Select font size").grid(row=0, column=0)
        
        listbox = Listbox(self.fontsize_popup)
        for i in range(12, 25):listbox.insert(END, i)
        listbox.select_set(int(self.mainView.get_cold_caller_tab_view().label_font['size']) - 12)
        listbox.grid(row=0, column=1)
        
        onOk = lambda: self.destory_popup_window_after(self.fontsize_popup, 
            lambda: self.mainView.get_cold_caller_tab_view().label_font.config(size=listbox.get(ANCHOR)))
        Button(self.fontsize_popup,text='OK',command=onOk).grid(row=1, column=0)
        Button(self.fontsize_popup,text='Cancel',command=onclosing).grid(row=1, column=1)
        self.fontsize_popup.transient(self.root)
        self.mainView.wait_window(self.fontsize_popup)

    def aboutme_window(self):
        try:
            self.aboutme_popup.focus_set()
            return
        except Exception:
            pass
        self.num_popup += 1
        self.aboutme_popup = Toplevel(self.root)
        self.aboutme_popup.title("About")
        self.aboutme_popup.resizable(0,0)

        explanation = "This program is built to help in increasing students' participation in classes."

        onclosing = lambda: self.destory_popup_window_after(self.aboutme_popup)
        self.aboutme_popup.protocol('WM_DELETE_WINDOW', onclosing)
        Label(self.aboutme_popup,text=explanation).grid()
        Button(self.aboutme_popup,text='OK',command=onclosing).grid()

        self.aboutme_popup.transient(self.root)
        self.mainView.wait_window(self.aboutme_popup)
    
    def show(self):
        self.root.mainloop()

