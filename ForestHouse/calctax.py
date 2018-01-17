import os

from tkinter import *
from tkinter.messagebox import *
import sys
n1=0
n2=0
def show_answer():
    n0 = int(tax_rate.get())
    n1 = int(gross_income.get())   
    Ans = round((n1 / ((n0 / 100) + 1)), 2)
    Ans = round((n1-Ans),2)
    total_tax.insert(0,Ans)

main = Tk()

RTitle=main.title("Calculate Hotel Tax")
RWidth=main.winfo_screenwidth()
RHeight=main.winfo_screenheight()
main.geometry(("%dx%d")%(RWidth/4,RHeight/4))

#Label(main, text = "Gross Incom:").grid(row=1, sticky=E, pady=10, padx=20)
#Label(main, text = "Tax Rate:").grid(row=2, sticky=E, pady=10, padx=20)
#Label(main, text = "The Tax is:").grid(row=3, sticky=E, pady=10, padx=20)

Label(main, text = "Tax Rate:").grid(row=1, sticky=E, pady=10, padx=20)
Label(main, text = "Gross Income:").grid(row=2, sticky=E, pady=10, padx=20)
Label(main, text = "The Tax is:").grid(row=3, sticky=E, pady=10, padx=20)

#num1 = Entry(main)
#num2 = Entry(main)
#blank = Entry(main)

tax_rate = Entry(main)
gross_income = Entry(main)
total_tax = Entry(main)

tax_rate.grid(row=1, column=2)
gross_income.grid(row=2, column=2)
total_tax.grid(row=3, column=2)

Button(main, text='Show Tax', command=show_answer).grid(row=5, sticky=W, padx=30)
Button(main, text='Clear', command= lambda: (total_tax.delete(0, END),
                                             gross_income.delete(0, END))).grid(row=5, column=2, sticky=W, pady=2)
# clear tax rate too add to above --->   tax_rate.delete(0, END),
Button(main, text='Quit', command=main.destroy).grid(row=5, column=2, sticky=E, pady=2)

main.mainloop()
