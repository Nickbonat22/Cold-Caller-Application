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
        self.has_popup = False
        self.aboutme_popup = None
        self.root = Tk()
        self.root.geometry("500x500")
        rows = 0
        while rows <= 50:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows += 1

        self.mainView = MainView(self.root, "Main Canvas")
        self.cold_caller_tab_view = self.mainView.get_cold_caller_tab_view()

        # Call Cold Caller Service to get the first 3 students
        self.mainView.get_cold_caller_tab_view().set_Widgets_top_portrait(1, name='Bob', spelling='Bob')
        self.mainView.get_cold_caller_tab_view().set_Widgets_top_portrait(2, name='Eve', spelling='E')
        self.mainView.get_cold_caller_tab_view().set_Widgets_top_portrait(3, name='Mallory', spelling='Ma Lorry')
        self.mainView.get_cold_caller_tab_view().set_Widgets_top_portrait(1, name='Alice', spelling='A ly se')

        # Bind button/keystrokes to Cold Caller Service APIs
        self.cold_caller_tab_view.createWidgets_bottom_Frame()
        self.cold_caller_tab_view.btn_good1.bind("<Button-1>", lambda e: self.test_func(e, 1))
        self.cold_caller_tab_view.btn_concern1.bind("<Button-1>", lambda e: self.test_func(e, -1))

        self.cold_caller_tab_view.btn_good2.bind("<Button-1>", lambda e: self.test_func(e, 2))
        self.cold_caller_tab_view.btn_concern2.bind("<Button-1>", lambda e: self.test_func(e, -2))

        self.cold_caller_tab_view.btn_good3.bind("<Button-1>", lambda e: self.test_func(e, 3))
        self.cold_caller_tab_view.btn_concern3.bind("<Button-1>", lambda e: self.test_func(e, -3))
        
        # Keystrokes mapping
        global CONCERN_1A, CONCERN_1B, CONCERN_2, CONCERN_3
        global REMOVE_1A, REMOVE_1B, REMOVE_2, REMOVE_3
        self.root.bind(CONCERN_1A, lambda e: self.test_func(e, -1))
        self.root.bind(CONCERN_1B, lambda e: self.test_func(e, -1))
        self.root.bind(CONCERN_2, lambda e: self.test_func(e, -2))
        self.root.bind(CONCERN_3, lambda e: self.test_func(e, -3))

        self.root.bind(REMOVE_1A, lambda e: self.test_func(e, 1))
        self.root.bind(REMOVE_1B, lambda e: self.test_func(e, 1))
        self.root.bind(REMOVE_2, lambda e: self.test_func(e, 2))
        self.root.bind(REMOVE_3, lambda e: self.test_func(e, 3))

        # Load the log file and set log tab's text
        self.mainView.get_log_tab_view().set_text("""HAMLET: To be, or not to be--that is the question:Whether 'tis nobler in the mind to sufferThe slings and arrows of outrageous fortuneOr to take arms against a sea of troublesAnd by opposing end them. To die, to sleep--No more--and by a sleep to say we endThe heartache, and the thousand natural shocksThat flesh is heir to. 'Tis a consummationDevoutly to be wished.""")

        self.createMenu()

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
        self.menu.add_cascade(label="About",menu=self.submenu2)
        self.submenu2.add_command(label="About", command=self.aboutme_windows)

    def destory_popup_window(self, popup):
        popup.destroy()
        self.has_popup = False

    def aboutme_windows(self):
        try:
            self.aboutme_popup.focus_set()
            return
        except Exception:
            pass
        self.has_popup = True
        self.aboutme_popup = Toplevel(self.root)
        self.aboutme_popup.title("About")
        self.aboutme_popup.resizable(0,0)

        explanation = "This program is built to help in increasing students' participation in classes."

        Label(self.aboutme_popup,text=explanation).grid()
        Button(self.aboutme_popup,text='OK',command=lambda: self.destory_popup_window(self.aboutme_popup)).grid()

        self.aboutme_popup.transient(self.root)
        self.mainView.wait_window(self.aboutme_popup)
    
    def update_stuents_portrait(self):
        f = ColdCallerService.instance()
        for i in range(3):
            new_student = f.get_studnt_at(i)
            if not new_student == None:
                name_labels[i].config(text=new_student.getFName() + " " + new_student.getLName())

    def remove(self, pos:int, concern = False):
        f = ColdCallerService.instance()
        if(not concern):
            if(f.perform_good_at(pos)):
                self.update_stuents_portrait()
        else:
            if(f.perform_bad_at(pos)):
                self.update_stuents_portrait()

    def test_func(self, event, arg = None):
        if(self.mainView.nb.index("current") == 0 and not self.has_popup):
            print("It worked in the tab", event.type)
            if(not arg == None):
                print("Arguments passed", arg)
    
    def show(self):
        self.root.mainloop()

