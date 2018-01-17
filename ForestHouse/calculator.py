#import string
#import pygame
#from pygame import event
from tkinter import *
from tkinter import ttk

class calculator:
    def __init__(self):

        self.error=False
        window = Tk()
        window.title('Calculator')
        window.configure(background='white')
        window.resizable(width=False, height=False)
        self.string = StringVar()
        # create the calculator display
        entry = Entry(window, textvariable = self.string, font="Helvetica 17")
        entry.grid(row = 0, column = 0, columnspan = 6)

        # to control wrong keys from keyboard
        entry.bind('<KeyPress>', self.keypress)
        # now put the cursor in the disply box
        entry.focus_set()

        # create a list of all the values on the keypads
        values = ['7','8','9','/','Clear','<-',
                  '4','5','6','*','(',')','1','2','3','-','=','0','.','%','+']

        # create buttons
        i=0
        row=1
        col=0
        for txt in values:
            padx=12
            pady=12
            # i represent the rows
            if(i==6):
                row=2
                col=0
            if (i == 12):
                row = 3
                col = 0
            if (i == 17):
                row = 4
                col = 0

            if (txt=='='):
                #create button
                btn = Button(window, height = 2, width = 4, padx = 25, pady = 25, text = txt,
                             command = lambda:self.equals())
                # place the buttons in the window
                btn.grid(row = row, column = col, columnspan = 2, rowspan = 2, padx = 1, pady = 1,)
            elif(txt=='Clear'):
                btn = Button(window, height=1, width=2, padx=padx, pady=pady, text=txt,
                             command=lambda: self.clearTxt())
                btn.grid(row=row, column=col, padx=1, pady=1)
            elif (txt == '<-'):
                btn = Button(window, height=1, width=2, padx=padx, pady=pady, text=txt,
                             command = lambda: self.delete())
                btn.grid(row=row, column=col, padx=1, pady=1)
            # just any other entry
            else:
                btn = Button(window, height=1, width=2, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.addchar(txt))
                btn.grid(row=row, column=col, padx=1, pady=1)

            i=i+1
            col=col+1

        window.mainloop()

    # conrol keys pressed from keyboard
    def keypress(self, event):

        allowedvalues = ['KP 0','KP 01','KP 2','KP 3','KP 4','KP 5','KP 6','KP 7','KP 8','KP 9',
                     '0','1','2','3','4','5','6','7','8','9', 'KP Devide', 'slash', 'KB Multiply',
                     'parenleft','parenright','KB Subtract','minus','equal','period','percent','KB add',
                     'plus','BackSpace','asterisk','Right','Left','KP Decimal']
        if(not self.error):
            if event.keysym in("Return", "KP Enter"):
                self.string.set().equals()
            elif event.keysym not in allowedvalues:
                return 'break'
        else:
            return 'break'
    # now we create function for the actions
    def clearTxt(self):
        self.string.set('')
        self.error=False
    def equals(self):
        result=''
        try:
            result=eval(self.string.get())
        except:
            self.error=True
            result='Error'

        self.string.set(result)
    def addchar(self, char):
        # this function will add character/number to the display string witout erasing what in there
        if(not self.error):
            self.string.set(self.string.get() + (str(char)))
    def delete(self):
        # -1 to delete the last character
        if (not self.error):
            self.string.set(self.string.get()[0:-1])

calculator()