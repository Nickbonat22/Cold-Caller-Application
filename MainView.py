#!/usr/bin/env python3
'''
Author: Jerry Xie

Created on: Apr 5, 2019

Last modified by: Jerry Xie @ Apr 8, 2019

Topic: GUI for Cold Caller

Effect: Demonstrating a GUI demo based on TKinter.

'''
from tkinter import *
from tkinter.ttk import *
from coldCallerTabView import ColdCallerTabView
from logTabView import LogTabView
class MainView(Frame):
    def __init__(self, master, name):
        Frame.__init__(self, master)
        self.master = master
        self.name = name

        self.nb = Notebook(master)
        self.nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky=(N,W,S,E))
        
        self.tab1 = ColdCallerTabView(self.nb)
        self.nb.add(self.tab1, text="Cold Caller")

        self.tab2 = LogTabView(self.nb)
        self.nb.add(self.tab2, text="Log")
    
    def get_cold_caller_tab_view(self):
        return self.tab1

    def get_log_tab_view(self):
        return self.tab2