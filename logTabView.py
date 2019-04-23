from tkinter import *
# from tkinter.ttk import *

class LogTabView(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.text = Text(self)
        self.scrollb = Scrollbar(self)
        self.export_summary = Button(self, text="Export Summary Log Button")

        self.scrollb.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollb.set)
        
        
        self.text.grid(row=0, column=0, sticky=(N,S,W,E))
        self.scrollb.grid(row=0, column=1, sticky=(N,S,W,E))
        self.export_summary.grid(row = 1, column=0, columnspan=2, sticky=(N,S,W,E))

        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)
        self.text.config(state=DISABLED)
    
    def set_text(self, new_text):
        self.text.config(state=NORMAL)
        self.text.delete(1.0, END)
        self.text.edit_reset()
        self.text.insert(END, new_text)
        self.text.config(state=DISABLED)