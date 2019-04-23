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

class MainViewController():
    def __init__(self):
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
        self.mainView.get_cold_caller_tab_view().set_Widgets_top_portrait(name_pos1='Bob', spelling_pos1='Bob')
        self.mainView.get_cold_caller_tab_view().set_Widgets_top_portrait(name_pos2='Eve', spelling_pos2='E')
        self.mainView.get_cold_caller_tab_view().set_Widgets_top_portrait(name_pos3='Mallory', spelling_pos3='Ma Lorry')
        

        # Bind button/keystrokes to Cold Caller Service APIs
        self.cold_caller_tab_view.createWidgets_bottom_Frame()
        self.cold_caller_tab_view.btn_good1.bind("<Button-1>", lambda e: self.test_func(e, 1))
        self.cold_caller_tab_view.btn_concern1.bind("<Button-1>", lambda e: self.test_func(e, -1))

        self.cold_caller_tab_view.btn_good2.bind("<Button-1>", lambda e: self.test_func(e, 2))
        self.cold_caller_tab_view.btn_concern2.bind("<Button-1>", lambda e: self.test_func(e, -2))

        self.cold_caller_tab_view.btn_good3.bind("<Button-1>", lambda e: self.test_func(e, 3))
        self.cold_caller_tab_view.btn_concern3.bind("<Button-1>", lambda e: self.test_func(e, -3))
        
        # Keystrokes mapping
        self.root.bind("<space>", self.test_func)
        self.root.bind("1", self.test_func)
        self.root.bind("2", self.test_func)
        self.root.bind("3", self.test_func)

        # Load the log file and set log tab's text
        self.mainView.get_log_tab_view().set_text("""HAMLET: To be, or not to be--that is the question:Whether 'tis nobler in the mind to sufferThe slings and arrows of outrageous fortuneOr to take arms against a sea of troublesAnd by opposing end them. To die, to sleep--No more--and by a sleep to say we endThe heartache, and the thousand natural shocksThat flesh is heir to. 'Tis a consummationDevoutly to be wished.""")
    
    def test_func(self, event, arg = None):
        if(self.mainView.nb.index("current") == 0):
            print("It worked in the tab", event.type)
            if(not arg == None):
                print("Arguments passed", arg)
    
    def show(self):
        self.root.mainloop()

