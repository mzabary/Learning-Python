#
import tkinter  # assuming Python 3 for simplicity's sake
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *

#root = tkinter.Tk()

from tkinter import *
import sqlite3
import datetime
from tkinter import ttk

from urllib import request
import simplejson as json
locu_api='9fb8cd70cb34cab8e83690473133f51943b5c93f'
root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
#top_frame = Frame(root).grid(row=0, column=0)
#btm_frame = Frame(root).grid(row=0, column=0)

# self.create_bottom_buttons()

class Lookup:
    #searchfor=''
    #location=''
    #query2=''
    def __init__(self, root):
        self.root = root

        self.main_screen()

    def main_screen(self):
        searchfor = ''
        location = ''
        query2 = ''
        Lookup.searchfor = ''
        Lookup.location = ''
        Lookup.query2 = ''

        self.creat_menu_bar()

        #self.create_bottom_buttons()


    def mainframe(self):
        RTitle = root.title("Life is good")
        RWidth = root.winfo_screenwidth()
        RHeight = root.winfo_screenheight()
        root.geometry(("%dx%d") % (RWidth, RHeight))
        #top_frame = Frame(root).grid(row=0, column=0)
        #self.btm_frame = Frame(root).grid(row=0, column=0)

    def donothing(self):

        searchfor = ''
        location = ''
        query2 = ''
        self.searchfor = ''
        self.location = ''
        self.query2 = ''
        Lookup.searchfor = ''
        Lookup.location = ''
        Lookup.query2 = ''
        for widget in root.winfo_children():
            widget.destroy()
        self.main_screen()

    def on_restaurant_clicked(self):
        self.searchfor = 'restaurant'
        #Lookup.searchfor='restaurant'
        self.create_bottom_buttons()

    def on_gym_clicked(self):
        self.searchfor = 'gym'
        self.create_bottom_buttons()

    def on_laundry_clicked(self):
        self.searchfor = 'laundry'
        self.create_bottom_buttons()

    def on_hair_care_clicked(self):
        self.searchfor = 'hair_care'
        self.create_bottom_buttons()

    def on_beauty_salon_clicked(self):
        self.searchfor = 'beauty_salon'
        self.create_bottom_buttons()

    def on_other_search_clicked(self):
        self.searchfor = ''
        self.create_bottom_buttons()


    def on_New_york_clicked(self):
        self.location = 'New York'
        #Lookup.location='New York'
        self.create_bottom_buttons()

    def on_Great_Neck_clicked(self):
        self.location = 'Great Neck'
        self.create_bottom_buttons()

    def on_Bayside_clicked(self):
        self.location = 'Bayside'
        self.create_bottom_buttons()

    def on_Stroudsburg_clicked(self):
        self.location = 'Stroudsburg'
        self.create_bottom_buttons()

    def on_Tannersville_clicked(self):
        self.location = 'Tannersville_clicked'
        self.create_bottom_buttons()

    def on_Pocono_clicked(self):
        self.location = 'Pocono'
        self.create_bottom_buttons()

    def on_Scranton_clicked(self):
        self.location = 'Scranton'
        self.create_bottom_buttons()

    def on_Other_location_clicked(self):
        self.location = ''
        self.create_bottom_buttons()


    def dosomething(self):

        #searchfor1.delete(0, END)
        #location1.delete(0, END)

        #Button(text='Quit', command=lambda: self.destroy()).grid(row=2, column=1, sticky=W, pady=2)
        locu_api = '9fb8cd70cb34cab8e83690473133f51943b5c93f'

        Lookup.location=self.location
        Lookup.searchfor=self.searchfor

        query2=Lookup.location
        self.locu_search(query2)


        #self.create_bottom_buttons()
        #self.create_activities_xls_tree_view()



    def locu_search(self,query2):

        api_key = locu_api
        bus = Lookup.searchfor
        query = Lookup.location
        url = 'http://api.locu.com/v1_0/venue/search/?api_key=9fb8cd70cb34cab8e83690473133f51943b5c93f'
        locality = query.replace(' ', '%20')
        final_url = url + '&locality=' + locality + '&category=' + bus
        json_obj = request.urlopen(final_url)
        data = json.load(json_obj)
        final_url = url + '&locality=' + locality + '&category=' + bus
        json_obj = request.urlopen(final_url)
        data = json.load(json_obj)
        def selectItem(a):
            curItem = tree.focus()
            #print(tree.item(curItem))
        # tree = ttk.Treeview(root, columns=("size", "modified"))
        tree = ttk.Treeview(height=20, columns=0)

        tree.delete(*tree.get_children())

        tree.delete(*tree.get_children())
        for i in tree.get_children():
            tree.delete(i)
        for widget in root.winfo_children():
            widget.destroy()

        def selectItem(a):
            curItem = tree.focus()
            #print(tree.item(curItem))
        # tree = ttk.Treeview(root, columns=("size", "modified"))
        tree = ttk.Treeview(height=20, columns=0)
        #tree = ttk.Treeview(root, columns=0)
        tree.heading('#0')
        # self.xlstree.column("#0", width=0)
        tree.column("#0", width=0, stretch=NO)

        tree["columns"] = ("", "1", "2", "3", "4", "5", "6")

        tree.column("", width=175, stretch=NO)
        tree.column("1", width=100, stretch=YES)
        tree.column("2", width=150, stretch=YES)
        tree.column("3", width=80, stretch=YES)

        tree.column("4", width=25, stretch=YES)
        tree.column("5", width=40, stretch=YES)

        tree.column("6", width=250, stretch=YES)

        # self.xlstree.heading("", text="Guest/Vendor", anchor=W)
        tree.heading("", text="Name", anchor=W)
        tree.heading("1", text="Phone", anchor=W)
        tree.heading("2", text="Address", anchor=W)
        tree.heading("3", text="City/Region", anchor=W)
        tree.heading("4", text="ST", anchor=W)
        tree.heading("5", text="Zip", anchor=W)
        tree.heading("6", text="Website", anchor=W)

        tree.bind('<ButtonRelease-1>', selectItem)
        # tree.insert('',"end",values = ("Name1","Date1","Time2","Loc3"))
        for item in data['objects']:
            tree.insert('', "end", values=(item['name'], item['phone'], item['street_address'], item['locality'],
                                       item['region'], item['postal_code'], item['website_url']))

        tree.grid()
        b3 = Button(root, text='Scroll / Done', command=lambda: self.donothing())
        b3.grid(row=4, column=0, sticky=W, padx=1, pady=10)
        bus = ''
        Lookup.searchfor=''
        query = ''
        Lookup.location=''

    def create_bottom_buttons(self):

        label1=Label(root,text="Looking For:")
        label1.grid(row=0,column=0, sticky=W, pady=5, padx=1)
        searchfor1 = Entry(root,width=30 )
        searchfor1.grid(row=0, column=0, sticky=W, padx=80)
        #searchfor1.delete(0, 'end')
        searchfor1.insert(30, self.searchfor)
        self.searchfor=searchfor1.get()

        Label(root,text="City/Region:").grid(row=1,column=0, sticky=W, pady=5, padx=1)
        location1 = Entry(root,width=30)
        location1.grid(row=1, column=0,sticky=W, padx = 80)
        #location1.delete(0, 'end')
        location1.insert(30, self.location)
        self.location = location1.get()
        #searchfor1.delete(0, END)
        #location1.delete(0, END)
        #print('I am on line 274')
        b1=Button(root,text='Show', command=self.dosomething)
        b1.grid(row=2, column=0, sticky=W, padx=80)
        b2=Button(root,text='Clear', command=lambda: (searchfor1.delete(0, END),location1.delete(0, END)))
        b2.grid(row=2, column=0, sticky=W, padx=190, pady=10)
        #b3=Button(text='Quit', command=lambda: self.destroy())
        #b3.grid(row=2, column=0, sticky=W, padx=190, pady=10)

        #searchfor1.delete(0, END)
        #location1.delete(0, END)

    def creat_menu_bar(self):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="restaurant", command=self.on_restaurant_clicked)
        filemenu.add_command(label="gym", command=self.on_gym_clicked)
        filemenu.add_command(label="laundry", command=self.on_laundry_clicked)
        filemenu.add_command(label="beauty salon", command=self.on_beauty_salon_clicked)
        filemenu.add_command(label="hair care", command=self.on_hair_care_clicked)
        filemenu.add_separator()
        # filemenu.add_command(label="Exit", command=root.quit)
        filemenu.add_command(label="Other", command=self.on_other_search_clicked)

        menubar.add_cascade(label="Search", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)

        editmenu.add_command(label="New York", command=self.on_New_york_clicked)

        #editmenu.add_separator()

        editmenu.add_command(label="Great Neck", command=self.on_Great_Neck_clicked)

        editmenu.add_command(label="Bayside", command= self.on_Bayside_clicked)

        editmenu.add_command(label="Stroudsburg", command=self.on_Stroudsburg_clicked)

        editmenu.add_command(label="Tannersville", command=self.on_Tannersville_clicked)

        editmenu.add_command(label="Pocono", command=self.on_Pocono_clicked)

        editmenu.add_command(label="Scranton", command=self.on_Scranton_clicked)

        #editmenu.add_command(label="Scranton", command=self.on_Scranton_clicked)


        editmenu.add_separator()
        editmenu.add_command(label="Others", command=self.on_Other_location_clicked())

        menubar.add_cascade(label="Location", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)

        menubar.add_cascade(label="Help", menu=helpmenu)

        root.config(menu=menubar)



if __name__ == '__main__':
    # root = Tk()


    # def resize(event):
    #    print("New size is: {}x{}".format(event.width, event.height))
    # root.bind("<Configure>", resize)

    # w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    # root.geometry("%dx%d+0+0" % (w,h))

    # root.geometry("%dx%d+0+0" % (743, 529))
    #root.geometry("%dx%d+50+50" % (743, 529))
    '''
    RTitle = root.title("Forest House System")
    RWidth = root.winfo_screenwidth()
    RHeight = root.winfo_screenheight()
    root.geometry(("%dx%d") % (RWidth, RHeight))
    '''
    application = Lookup(root)

    root.mainloop()
