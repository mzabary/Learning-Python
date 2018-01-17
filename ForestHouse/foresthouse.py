
from tkinter import *
from tkinter import ttk
import sqlite3

class PhoneBook:

    #db_filename = 'C:\\PyProjects\\learnpy\\foresthouse.db'
    db_filename = 'foresthouse.db'

    def __init__(self, root):
        self.root = root
        self.create_gui()

    def execute_db_query(self, query, parameters=()):
        with sqlite3.connect(self.db_filename) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result

    def execute_db_query2(self, query, idfield):
        idfield=str(idfield)
        with sqlite3.connect(self.db_filename) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, str(idfield))
            conn.commit()
        return query_result

    def create_gui(self):
        self.create_left_icon()
        #self.create_label_frame()
        self.create_message_area()
        self.create_tree_view()
        self.create_bottom_buttons()
        self.view_records()

        self.create_label_frame2()
        #self.select_item()

    def create_left_icon(self):
        #photo = PhotoImage(file='phonebook.gif')
        #photo = PhotoImage(file='C:\\PyProjects\\learnpy\\we1.png')
        photo = PhotoImage(file='we1.png')
        label = Label(image=photo)
        label.image = photo
        label.grid(row=0, column=0, sticky='w',padx=140)
        self.root.title("The Foresthouse Guests")

    def create_label_frame(self):
        labelframe = LabelFrame(self.root, text='Create New Record')
        labelframe.grid(row=0, column=0, padx=38, pady=8, sticky='w')

        Label(labelframe, text='Name:',relief=RIDGE,width=15).grid(row=1, column=1, sticky=W, pady=2)
        self.namefield = Entry(labelframe,width=50)
        self.namefield.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        Label(labelframe, text='Phone:',relief=RIDGE, width=15).grid(row=2, column=1, sticky=W, pady=2)
        self.phonefield = Entry(labelframe,width=50)
        self.phonefield.grid(row=2, column=2, sticky=W, padx=5, pady=2)

        Label(labelframe, text='Email:',relief=RIDGE,width=15).grid(row=3, column=1, sticky=W, pady=2)
        self.emailfield = Entry(labelframe,width=50)
        self.emailfield.grid(row=3, column=2, sticky=W, padx=5, pady=2)

        Label(labelframe, text='Comment:',relief=RIDGE,width=15).grid(row=4, column=1, sticky=W, pady=2)
        self.commentfield = Entry(labelframe,width=50)
        self.commentfield.grid(row=4, column=2, sticky=W, padx=5, pady=2)

        ttk.Button(labelframe, text=' Save ', command=self.on_add_record_button_clicked).grid(
            row=5, column=2, sticky=W, padx=5, pady=2)

        ttk.Button(labelframe, text='Exit', command=lambda: labelframe.grid_remove()).grid(
            row=5, column=2, sticky=E, padx=5, pady=2)

        self.create_left_icon

    def create_label_frame2(self):
        labelframe2 = LabelFrame(self.root, text='Foresthouse Menu')
        labelframe2.grid(row=0, column=0, padx=40, pady=0, sticky='e')

        ttk.Button(labelframe2, text='CalcTax', width=40, command=self.on_calctax_button_clicked).grid(
            row=1, column=1, sticky=W, padx=2, pady=2)

        ttk.Button(labelframe2, text='Activities', width=40, command=self.on_calctax_button_clicked).grid(
            row=2, column=1, sticky=W, padx=2, pady=1)
        ttk.Button(labelframe2, text='Calculator', width=40, command=self.on_calculator_button_clicked).grid(
            row=3, column=1, sticky=W, padx=2, pady=1)
        ttk.Button(labelframe2, text='Accounting', width=40, command=self.on_calctax_button_clicked).grid(
            row=4, column=1, sticky=W, padx=2, pady=1)
        ttk.Button(labelframe2, text='Pictures', width=40, command=self.on_calctax_button_clicked).grid(
            row=5, column=1, sticky=W, padx=2, pady=1)

    def on_add_record_button_clicked(self):
        self.add_new_record()

        self.create_left_icon

    def on_calctax_button_clicked(self):
        import subprocess
        subprocess.call(["python", "calctax.py"])
        #subprocess.call(["python", "myscript2.py"])

    def on_calculator_button_clicked(self):
        import subprocess
        subprocess.call(["python", "calculator.py"])
        # subprocess.call(["python", "myscript2.py"])

    def create_tree_view(self):
        self.tree = ttk.Treeview()

        self.tree = ttk.Treeview(height=10, columns=1)
        self.tree.grid(row=4, column=0)

        self.tree.heading('#0', text='ID', anchor=W)
        self.tree.column("#0", width=40)
        style = ttk.Style()
        #style.configure(".", font=('Helvetica', 8), foreground="white")
        #style.configure("Treeview", foreground='red')

        style.configure("Treeview.Heading", background='blue', foreground='blue')

        self.tree["columns"] = ("one", "two", "three", "four")

        self.tree.column("one", width=150)
        self.tree.column("two", width=100)
        self.tree.column("three", width=200)
        self.tree.column("four", width=250)

        self.tree.heading("one", text="name", anchor=W)
        self.tree.heading("two", text="Phone",anchor=W)
        self.tree.heading("three", text="Email",anchor=W)
        self.tree.heading("four", text="Comments",anchor=W)

    def select_item(self, a): # added self and a (event)
        # gets all the values of the selected row
        test_str_library = self.tree.item(self.tree.selection())
        # prints a dictionay of the selected row
        #print ('The test_str = ', type(test_str_library), test_str_library, '\n')
        item = self.tree.selection()[0] # which row did you click on
        #print ('item clicked ', item) # variable that represents the row you clicked on
        #print (self.tree.item(item)['values'][0]) # prints the first value of the values (the id value)
        record_id=self.tree.item(item)['text']
        #print("Record ID:", record_id)

    def on_delete_selected_button_clicked(self):
        self.message['text'] = ''
        try:
            #self.tree.item(self.tree.selection())[0]
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'No item selected to delete     '
            return
        self.delete_record()

    def delete_record(self):
        item = self.tree.selection()  # [0]
        idfield = self.tree.item(item)['text']
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        conn.text_factory = str
        data3 = str(idfield)
        query = "DELETE FROM guest WHERE id = '%s';" % data3
        mydata = c.execute(query)
        conn.commit()
        self.view_records()
        
    def on_modify_selected_button_clicked(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'No item selected to modify     '
            return
        self.open_modify_window()
        #self.show_entry_fields2()
        #self.show_entry_fields1()


    def open_modify_window(self):
        win = Tk()
        Label(win, text="Name").grid(row=0)
        Label(win, text="phone").grid(row=1)
        Label(win, text="Email").grid(row=2)
        Label(win, text="Comment").grid(row=3)

        item = self.tree.selection()  # [0]
        idfield = self.tree.item(item)['text']

        namefield = self.tree.item(self.tree.selection())['values'][0]
        phonefield = self.tree.item(self.tree.selection())['values'][1]
        emailfield = self.tree.item(self.tree.selection())['values'][2]
        commentfield = self.tree.item(self.tree.selection())['values'][3]

        e1 = Entry(win, width=30)
        e2 = Entry(win, width=30)
        e3 = Entry(win, width=30)
        e4 = Entry(win, width=30)

        e1.insert(20, namefield)
        e2.insert(20, phonefield)
        e3.insert(20, emailfield)
        e4.insert(20, commentfield)

        e1.grid(row=0, column=1, padx=10, pady=5)
        e2.grid(row=1, column=1, padx=10, pady=5)
        e3.grid(row=2, column=1, padx=10, pady=5)
        e4.grid(row=3, column=1, padx=10, pady=5)

        Button(win, text='Quit', command=win.destroy, fg='green').grid(row=4, column=1, sticky=W, pady=4, padx=10)
        Button(win, text='Update', fg='red', command=lambda:
           self.modify_record(e1.get(),e2.get(),e3.get(),e4.get())).grid(row=4, column=1, sticky=E, pady=4, padx=10)
        #win.destroy()
        #mainloop()

        #self.windestroy(win)

    def modify_record(self, namefield, phonefield, emailfield, commentfield):
        item = self.tree.selection()  # [0]
        idfield = self.tree.item(item)['text']

        query = 'UPDATE guest SET name=?, phone=?, email=?, comment=? WHERE  id=?'
        parameters = (namefield, phonefield, emailfield, commentfield, idfield)

        with sqlite3.connect(self.db_filename) as conn:
            cursor = conn.cursor()
            #print('parameters=', parameters)
            query_result = cursor.execute(query, parameters)
            #print('query_result=', query_result)
            conn.commit()
        self.message['text'] = 'The record of  {}  was modified     '.format(namefield)
        #self.transient.destroy()
        # self.windestroy(win)
        self.view_records()

        return
    #def windestroy(win):
    #    win.destrroy
    #    #win.quit
    #    return

    def add_update_record(self):
        if self.new_records_validated():
            query = 'INSERT INTO guest VALUES(NULL,?, ?, ?, ?)'
            parameters = (self.namefield.get(), self.phonefield.get(),
                          self.emailfield.get(), self.commentfield.get())
            #print(parameters)
            self.execute_db_query(query, parameters)
            self.message['text'] = 'Phone record of {} {} {} {} added     '.format(
                self.namefield.get(), self.phonefield.get(),self.emailfield.get(), self.commentfield.get())
            self.namefield.delete(0, END)
            self.phonefield.delete(0, END)
            self.emailfield.delete(0, END)
            self.commentfield.delete(0, END)
        else:
            self.message['text'] = 'Name cannot be blank     '
        self.view_records()

    def add_new_record(self):
        if self.new_records_validated():
            query = 'INSERT INTO guest VALUES(NULL,?, ?, ?, ?)'
            parameters = (self.namefield.get(), self.phonefield.get(),
                          self.emailfield.get(), self.commentfield.get())
            #print(parameters)
            self.execute_db_query(query, parameters)
            self.message['text'] = 'Phone record of {} {} {} {} added     '.format(
                self.namefield.get(), self.phonefield.get(),
                self.emailfield.get(), self.commentfield.get())
            self.namefield.delete(0, END)
            self.phonefield.delete(0, END)
            self.emailfield.delete(0, END)
            self.commentfield.delete(0, END)
        else:
            self.message['text'] = 'Name cannot be blank      '
        self.view_records()

    def create_bottom_buttons(self):
        ttk.Button(text='Delete Selected',
            command=self.on_delete_selected_button_clicked).grid(row=5, column=0, sticky=W)
        ttk.Button(text='Modify Selected',
                   command=self.on_modify_selected_button_clicked).grid(row=5, column=0, sticky=E)
            #command=self.open_modify_window).grid(row=5, column=0, sticky=E)
        ttk.Button(text='Add Record',
               command=self.create_label_frame).grid(row=5, column=0, sticky=W,padx=350)

    def view_records(self):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        query = 'SELECT * FROM guest ORDER BY ID asc'
        phone_book_entries = self.execute_db_query(query)
        for row in phone_book_entries:
            #self.tree.insert('', 0, text=row[1], values=(row[2],row[3],row[4]))
            self.tree.insert('','end',text=row[0], values=(row[1],row[2], row[3], row[4]))
        self.tree.bind('<ButtonRelease-1>', self.select_item)

    def new_records_validated(self):
        return (self.namefield.get() != 0) # and len(self.phonefield.get()) != 0

    def create_message_area(self):
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, sticky=E)

if __name__ == '__main__':
    root = Tk()
    application = PhoneBook(root)
    root.mainloop()
