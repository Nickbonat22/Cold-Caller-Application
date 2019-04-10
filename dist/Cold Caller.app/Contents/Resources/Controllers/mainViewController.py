#!/usr/bin/env python3
'''
Author: Jerry Xie

Created on: Apr 5, 2019

Last modified by: Jerry Xie @ Apr 8, 2019

Topic: GUI for Cold Caller

Effect: Demonstrating a GUI demo based on TKinter.

'''
import sys
sys.path.append("./Models")
sys.path.append("./Views")
sys.path.append("./Controllers")
from Views.MainView import *

class MainViewController():
    def __init__(self):
        self.mainView = MainView()
        self.mainView.createMenu()
        self.mainView.set_Widgets_top_portrait(name_pos1='Bob', spelling_pos1='Bob')
        self.mainView.set_Widgets_top_portrait(name_pos2='Eve', spelling_pos2='E')
        self.mainView.set_Widgets_top_portrait(name_pos3='Mallory', spelling_pos3='Ma Lorry')
        self.mainView.createWidgets_bottom_Frame()
        self.mainView.bind_btn_bad_to(self.test_func)
        self.mainView.bind_btn_good_to(self.test_func)
        self.mainView.show()
    
    def test_func(self, event):
        print("It worked")


