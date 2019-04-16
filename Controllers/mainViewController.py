#!/usr/bin/env python3
'''
Author: Jerry Xie

Created on: Apr 5, 2019

Last modified by: Jerry Xie @ Apr 9, 2019

Topic: Controller for Main View

Effect: Handle MainView intereaction, response logic

'''
import os, sys
sys.path.append(os.path.dirname(os.getcwd()) + '/Views')
sys.path.append('./Views')
from MainView import *

class MainViewController():
    def __init__(self):
        self.mainView = MainView()
        self.mainView.createMenu()

        # Call Cold Caller Service to get the first 3 students
        self.mainView.set_Widgets_top_portrait(name_pos1='Bob', spelling_pos1='Bob')
        self.mainView.set_Widgets_top_portrait(name_pos2='Eve', spelling_pos2='E')
        self.mainView.set_Widgets_top_portrait(name_pos3='Mallory', spelling_pos3='Ma Lorry')
        

        self.mainView.createWidgets_bottom_Frame()
        self.mainView.btn_good.bind("<Button-1>", self.test_func)
        self.mainView.btn_concern.bind("<Button-1>", self.test_func)
        
        self.mainView.show()
    
    def test_func(self, event):
        print("It worked", event.type)


