from tkinter import *
# from tkinter.ttk import *
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

class ColdCallerTabView(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid(row=0, column=0, sticky=(N,S,E,W))
        self.btns_good = {}
        self.btns_concern = {}
    def set_Widgets_top_portrait(self, image_pos1 = None, name_pos1 = None, spelling_pos1 = None, image_pos2 = None, name_pos2 = None, spelling_pos2 = None, image_pos3 = None, name_pos3 = None, spelling_pos3 = None):
        if not name_pos1 == None:
            if not image_pos1 == None:
                self.portrait1 = PhotoImage(file=image_pos1)
            else:
                self.portrait1 = PhotoImage(file='Resources/default.png')
            make_portrait_with_name_label(self, 0, 0, self.portrait1, name_pos1, spelling_pos1,  '1:')
        if not name_pos2 == None:
            if not image_pos2 == None:
                self.portrait2 = PhotoImage(file=image_pos2)
            else:
                self.portrait2 = PhotoImage(file='Resources/default.png')
            make_portrait_with_name_label(self, 0, 1, self.portrait2, name_pos2, spelling_pos2, '2:')
        if not name_pos3 == None:
            if not image_pos3 == None:
                self.portrait3 = PhotoImage(file=image_pos3)
            else:
                self.portrait3 = PhotoImage(file='Resources/default.png')
            make_portrait_with_name_label(self, 0, 2, self.portrait3, name_pos3, spelling_pos3, '3:')

    def createWidgets_bottom_Frame(self):
        Grid.rowconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 2, weight=1)

        # First student
        self.btns_1 = Frame(self)
        self.btns_1.grid(row=1, column=0, sticky=(N,S,E,W))
        self.btn_good1 = Button(self.btns_1, text="Good")
        self.btn_concern1 = Button(self.btns_1, text="Concern")
        
        self.btn_good1.grid(row=0, column=0, sticky=(N,S,E,W))
        self.btn_concern1.grid(row=0, column=1, sticky=(N,S,E,W))
        Grid.rowconfigure(self.btns_1, 0, weight=1)
        Grid.columnconfigure(self.btns_1, 0, weight=1)
        Grid.columnconfigure(self.btns_1, 1, weight=1)

        # Second student
        self.btns_2 = Frame(self)
        self.btns_2.grid(row=1, column=1, sticky=(N,S,E,W))
        self.btn_good2 = Button(self.btns_2, text="Good")
        self.btn_concern2 = Button(self.btns_2, text="Concern")
        
        self.btn_good2.grid(row=0, column=0, sticky=(N,S,E,W))
        self.btn_concern2.grid(row=0, column=1, sticky=(N,S,E,W))
        Grid.rowconfigure(self.btns_2, 0, weight=1)
        Grid.columnconfigure(self.btns_2, 0, weight=1)
        Grid.columnconfigure(self.btns_2, 1, weight=1)

        # Third student
        self.btns_3 = Frame(self)
        self.btns_3.grid(row=1, column=2, sticky=(N,S,E,W))
        self.btn_good3 = Button(self.btns_3, text="Good")
        self.btn_concern3 = Button(self.btns_3, text="Concern")
        
        self.btn_good3.grid(row=0, column=0, sticky=(N,S,E,W))
        self.btn_concern3.grid(row=0, column=1, sticky=(N,S,E,W))
        Grid.rowconfigure(self.btns_3, 0, weight=1)
        Grid.columnconfigure(self.btns_3, 0, weight=1)
        Grid.columnconfigure(self.btns_3, 1, weight=1)