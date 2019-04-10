#!/usr/bin/env python3
'''
Author: Jerry Xie

Created on: Apr 5, 2019

Last modified by: Jerry Xie @ Apr 8, 2019

Topic: GUI for Cold Caller

Effect: Demonstrating a GUI demo based on TKinter.

'''
import sys

from tkinter import *
import tkinter.messagebox as messagebox
def make_image_label(parent, img, rownum, colnum):
    label = Label(parent, image=img)
    label.grid(row=rownum, column=colnum, sticky=(N, S, E, W), columnspan=2)
def make_portrait_with_name_label(parent, rownum, colnum, portrait, name, spelling, number):
    Grid.rowconfigure(parent, rownum, weight=1)
    Grid.columnconfigure(parent, colnum, weight=1)
    frame = Frame(parent)
    frame.grid(row=rownum, column=colnum, sticky=(N,S,E,W))

    Grid.rowconfigure(frame, 0, weight=1)
    Grid.columnconfigure(frame, 0, weight=1)
    make_image_label(frame, portrait, 0, 0)

    Grid.rowconfigure(frame, 1, weight=1)
    Grid.columnconfigure(frame, 0, weight=1)
    numlabel = Label(frame, text=number)
    numlabel.grid(row=1, column=0, sticky=(N, S, E))
        
    Grid.rowconfigure(frame, 1, weight=1)
    Grid.columnconfigure(frame, 1, weight=1)
    namelabel = Label(frame, text=name)
    namelabel.grid(row=1, column=1, sticky=(N, S, W))

    Grid.rowconfigure(frame, 2, weight=1)
    Grid.columnconfigure(frame, 0, weight=1)
    spellingLabel = Label(frame, text=spelling)
    spellingLabel.grid(row=2, column=0, sticky=(N, E, S, W), columnspan=2)

class FullScreenApp(object):
    # https://stackoverflow.com/questions/7966119/display-fullscreen-mode-on-tkinter
    # default full screen
    # press <escape> to set its size to 720P
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='1280x720+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        # print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

class MainView():
    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        Grid.rowconfigure(self.root, 0, weight=1)
        Grid.columnconfigure(self.root, 0, weight=1)
        self.frame.grid(row=0, column=0, sticky=(N,S,E,W))
    
    def createMenu(self):
        def test_function():
            print("It worked!!!!!")
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.submenu1 = Menu(self.menu)
        self.menu.add_cascade(label="This is a Menu",menu=self.submenu1)
        self.submenu1.add_command(label="This is a Command", command=test_function)
        self.submenu1.add_separator()
        self.submenu1.add_command(label="Exit", command=self.root.quit)

        self.submenu2 = Menu(self.menu)
        self.menu.add_cascade(label="This is another Menu",menu=self.submenu2)
        self.submenu2.add_command(label="This is a Command", command=test_function)

    def set_Widgets_top_portrait(self, image_pos1 = None, name_pos1 = None, spelling_pos1 = None, image_pos2 = None, name_pos2 = None, spelling_pos2 = None, image_pos3 = None, name_pos3 = None, spelling_pos3 = None):
        if not name_pos1 == None:
            if not image_pos1 == None:
                self.portrait1 = PhotoImage(file=image_pos1)
            else:
                self.portrait1 = PhotoImage(file='Resources/default.png')
            make_portrait_with_name_label(self.frame, 0, 0, self.portrait1, name_pos1, spelling_pos1,  '1:')
        if not name_pos2 == None:
            if not image_pos2 == None:
                self.portrait2 = PhotoImage(file=image_pos2)
            else:
                self.portrait2 = PhotoImage(file='Resources/default.png')
            make_portrait_with_name_label(self.frame, 0, 1, self.portrait2, name_pos2, spelling_pos2, '2:')
        if not name_pos3 == None:
            if not image_pos3 == None:
                self.portrait3 = PhotoImage(file=image_pos3)
            else:
                self.portrait3 = PhotoImage(file='Resources/default.png')
            make_portrait_with_name_label(self.frame, 0, 2, self.portrait3, name_pos3, spelling_pos3, '3:')

    def createWidgets_bottom_Frame(self):
        Grid.rowconfigure(self.frame, 1, weight=1)
        Grid.columnconfigure(self.frame, 0, weight=1)
        Grid.columnconfigure(self.frame, 2, weight=1)

        self.btn_good = Button(self.frame, text="Good")
        self.btn_concern = Button(self.frame, text="Concern")
        
        self.btn_good.grid(row=1, column=0, sticky=(N,S,E,W))
        self.btn_concern.grid(row=1, column=2, sticky=(N,S,E,W))

    def bind_btn_good_to(self, func):
        self.btn_good.bind("<Button-1>", func)
    
    def bind_btn_bad_to(self, func):
        self.btn_bad_func = func
        self.btn_concern.bind("<Button-1>", func)

    def show(self):
        self.root.title("Cold Caller")
        FullScreenApp(self.root)
        self.root.mainloop()


