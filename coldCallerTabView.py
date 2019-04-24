from tkinter import *
# from tkinter.ttk import *

class ColdCallerTabView(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid(row=0, column=0, sticky=(N,S,E,W))
        self.top_frames = {}
        self.name_labels = {}
        self.portraits_labels = {}
        self.spellings_labels = {}
        self.portraits = {}

    def _make_portrait_with_name_label(self, parent, rownum, colnum, name, number, portrait_path, spelling):
        Grid.rowconfigure(parent, rownum, weight=1)
        Grid.columnconfigure(parent, colnum, weight=1)

        id = str(rownum) + str(colnum)
        self.top_frames[id] = Frame(parent)
        frame = self.top_frames[id]
        frame.grid(row=rownum, column=colnum, sticky=(N,S,E,W))

        Grid.rowconfigure(frame, 0, weight=1)
        Grid.columnconfigure(frame, 0, weight=1)
        try:
            self.portraits[colnum] = PhotoImage(file=portrait_path)
        except:
            self.portraits[colnum] = PhotoImage(file='Resources/default.png')
        self.portraits_labels[colnum] = Label(frame, image=self.portraits[colnum])
        self.portraits_labels[colnum].grid(row=0, column=0, sticky=(N, S, E, W), columnspan=2)

        Grid.rowconfigure(frame, 1, weight=1)
        Grid.columnconfigure(frame, 0, weight=1)
        numlabel = Label(frame, text=number)
        numlabel.grid(row=1, column=0, sticky=(N, S, E))
            
        Grid.rowconfigure(frame, 1, weight=1)
        Grid.columnconfigure(frame, 1, weight=1)
        self.name_labels[colnum] = Label(frame, text=name)
        self.name_labels[colnum].grid(row=1, column=1, sticky=(N, S, W))

        Grid.rowconfigure(frame, 2, weight=1)
        Grid.columnconfigure(frame, 0, weight=1)
        self.spellings_labels[colnum] = Label(frame, text=spelling)
        self.spellings_labels[colnum].grid(row=2, column=0, sticky=(N, E, S, W), columnspan=2)
    
    def _update_portrait_with_name_label(self, rownum, colnum, new_portrait_path = None, new_name = None, new_spelling = None):
        # Could throw, use with try...except
        if not new_portrait_path == None:
            target_portrait_label = self.portraits_labels[colnum]
            try:
                self.portraits[colnum] = PhotoImage(file=new_portrait_path)
            except:
                self.portraits[colnum] = PhotoImage(file='Resources/default.png')
            target_portrait_label.config(image=self.portraits[colnum])
        if not new_spelling == None:
            target_splling_label = self.spellings_labels[colnum]
            target_splling_label.config(text=new_spelling)
        if not new_name == None:
            target_name_label = self.name_labels[colnum]
            target_name_label.config(text=new_name)

    # def set_Widgets_top_portrait(self, image_pos1 = None, name_pos1 = None, spelling_pos1 = None, image_pos2 = None, name_pos2 = None, spelling_pos2 = None, image_pos3 = None, name_pos3 = None, spelling_pos3 = None):
    def set_Widgets_top_portrait(self, pos:int, portrait_path = None, name = None, spelling = None):
        # pos should be 1,2,3
        pos -= 1
        try:
            self._update_portrait_with_name_label(0, pos, portrait_path, name, spelling)
        except KeyError:
            self._make_portrait_with_name_label(self, 0, pos, name, str(pos) + ': ', portrait_path, spelling)

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