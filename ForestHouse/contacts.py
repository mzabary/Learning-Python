'''
Code illustration: 7.12
    Phonebook Application
Tkinter GUI Application Development Blueprints
'''
from tkinter import *
from tkinter import ttk
import sqlite3


class PhoneBook:
    db_filename = 'C:\\PyProjects\\learnpy\\foresthouse.db'

    def __init__(self, root):
        self.root = root
        self.create_gui()

    def execute_db_query(self, query, parameters=()):
        with sqlite3.connect(self.db_filename) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result


    def create_gui(self):
        self.create_left_icon()
        self.create_label_frame()
        self.create_message_area()
        self.create_tree_view()
        self.create_bottom_buttons()
        self.view_records()

        #self.select_item()

    def create_left_icon(self):
        #photo = PhotoImage(file='phonebook.gif')
        photo = PhotoImage(file='C:\\PyProjects\\learnpy\\we1.png')
        label = Label(image=photo)
        label.image = photo
        label.grid(row=0, column=0, sticky='w',padx=50)
        self.root.title("The Foresthouse Guests")

    def create_label_frame(self):
        labelframe = LabelFrame(self.root, text='Create New Record')
        labelframe.grid(row=0, column=0, padx=8, pady=8, sticky='e')

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

        ttk.Button(labelframe, text='Add Record', command=self.on_add_record_button_clicked).grid(
            row=5, column=2, sticky=E, padx=5, pady=2)


    def on_add_record_button_clicked(self):
        self.add_new_record()

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
        ###print ('The test_str = ', type(test_str_library), test_str_library, '\n')
        item = self.tree.selection()[0] # which row did you click on
        ###print ('item clicked ', item) # variable that represents the row you clicked on
        ###print (self.tree.item(item)['values'][0]) # prints the first value of the values (the id value)
        record_id=self.tree.item(item)['text']
        ###print("Record ID:", record_id)

    def on_delete_selected_button_clicked(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'No item selected to delete'
            return
        self.delete_record()

    def delete_record(self):
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM guest WHERE name = ?'
        self.execute_db_query(query, name)
        self.message['text'] = 'Phone record for {} deleted'.format(name)
        self.view_records()

    def on_modify_selected_button_clicked(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'No item selected to modify'
            return
        self.open_modify_window()

    def open_modify_window(self):


        item = self.tree.selection()[0]
        idfield = self.tree.item(item)['text']
        #idfield = self.tree.item(self.tree.selection())['values']
        namefield = self.tree.item(self.tree.selection())['values'][0]
        phonefield = self.tree.item(self.tree.selection())['values'][1]
        emailfield = self.tree.item(self.tree.selection())['values'][2]
        commentfield = self.tree.item(self.tree.selection())['values'][3]

        oldidfield=idfield
        oldnamefield=namefield
        oldphonefield=phonefield
        oldemailfield=emailfield
        oldcommentfield=commentfield

        self.transient = Toplevel()

        Label(self.transient, text='Name:').grid(row=0, column=1)
        Entry(self.transient, textvariable=StringVar(self.transient, value=namefield),width=50)\
            .grid(row=0, column=2, padx=5, pady=5)

        Label(self.transient, text='Phone:').grid(row=1, column=1)
        Entry(self.transient, textvariable=StringVar(self.transient, value=phonefield),width=50)\
            .grid(row=1, column=2, padx=15, pady=5)

        Label(self.transient, text='Email:').grid(row=2, column=1)
        Entry(self.transient, textvariable=StringVar(self.transient, value=emailfield),width=50)\
            .grid(row=2, column=2, padx=5, pady=5)

        Label(self.transient, text='Comment:').grid(row=3, column=1)
        Entry(self.transient, textvariable=StringVar(self.transient, value=commentfield),width=50)\
            .grid(row=3, column=2, padx=5, pady=5)


        new_phone_number_entry_widget = Entry(self.transient)


        new_phone_number_entry_widget.grid(row=3, column=2, padx=5, pady=5)


        Button(self.transient, text='Update Record', command=lambda:
        self.update_record2(new_phone_number_entry_widget.get(), namefield))\
            .grid(row=5, column=2, sticky=E)
            # new_phone_number_entry_widget.get(), old_phone_number, name)).grid(row=3, column=2, sticky=E)

        newoldcommentfield=commentfield

        print('newoldcommentfield=', newoldcommentfield, 'commentfield=', commentfield)

        self.transient.mainloop()

    #def update_record2(self,oldcommentfield, commentfield, namefield):      #    , commentfield, idfield):
    def update_record2(self, commentfield, namefield):
        #print('oldcommentfield=',oldcommentfield, 'commentfield=',commentfield)
        ###print('namefield=',namefield)
        #def update_record2(self, newphone, old_phone_number, name):
        #query = 'UPDATE contacts SET contactnumber=? WHERE contactnumber=? AND name=?'
        query =  'UPDATE guest SET comment=?       WHERE  name=?'
        #query = 'UPDATE guest SET comment=?       WHERE comment=? AND name=?'
        #parameters = (newphone, old_phone_number, name)
        #parameters = (oldcommentfield, commentfield, namefield)
        parameters = (commentfield, namefield)

        self.execute_db_query(query, parameters)
        self.transient.destroy()
        self.message['text'] = 'The Comment for {} was modified'.format(namefield)
        self.view_records()

    def execute_db_query2(self, query, parameters=()):
        with sqlite3.connect(self.db_filename) as conn:
            #print('The patameters are:', parameters[0:])
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result
        ####

    def update_record(self):
        ###print('**', self.namefield, self.phonefield, self.emailfield, self.commentfield)
        query = 'UPDATE guest SET name=? phone=? email=? comment=? WHERE id=record_id'
        #parameters = (self.namefield, self.phonefield, self.emailfield, self.commentfield)
        self.execute_db_query2(query, self.namefield, self.phonefield, self.emailfield, self.commentfield)

        self.message['text'] = 'record of {} modified'.format(self.namefield)
        self.transient.destroy()
        self.view_records()
    def add_update_record(self):
        if self.new_records_validated():
            query = 'INSERT INTO guest VALUES(NULL,?, ?, ?, ?)'
            parameters = (self.namefield.get(), self.phonefield.get(),
                          self.emailfield.get(), self.commentfield.get())
            #print(parameters)
            self.execute_db_query(query, parameters)
            self.message['text'] = 'Phone record of {} {} {} {} added'.format(
                self.namefield.get(), self.phonefield.get(),self.emailfield.get(), self.commentfield.get())
            self.namefield.delete(0, END)
            self.phonefield.delete(0, END)
            self.emailfield.delete(0, END)
            self.commentfield.delete(0, END)
        else:
            self.message['text'] = 'Name cannot be blank'
        self.view_records()

    def add_new_record(self):
        if self.new_records_validated():
            query = 'INSERT INTO guest VALUES(NULL,?, ?, ?, ?)'
            parameters = (self.namefield.get(), self.phonefield.get(),
                          self.emailfield.get(), self.commentfield.get())
            #print(parameters)
            self.execute_db_query(query, parameters)
            self.message['text'] = 'Phone record of {} {} {} {} added'.format(
                self.namefield.get(), self.phonefield.get(),
                self.emailfield.get(), self.commentfield.get())
            self.namefield.delete(0, END)
            self.phonefield.delete(0, END)
            self.emailfield.delete(0, END)
            self.commentfield.delete(0, END)
        else:
            self.message['text'] = 'Name cannot be blank'
        self.view_records()

    def create_bottom_buttons(self):
        ttk.Button(text='Delete Selected',
            command=self.on_delete_selected_button_clicked).grid(row=5, column=0, sticky=W)
        ttk.Button(text='Modify Selected',
            command=self.open_modify_window).grid(row=5, column=0, sticky=E)
            #command=self.on_modify_selected_button_clicked).grid(row=5, column=0, sticky=E)

    def view_records(self):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        query = 'SELECT * FROM guest ORDER BY ID asc'
        phone_book_entries = self.execute_db_query(query)
        for row in phone_book_entries:
            #self.tree.insert('', 0, text=row[1], values=(row[2],row[3],row[4]))
            ###print(row)
            self.tree.insert('','end',text=row[0], values=(row[1],row[2], row[3], row[4]))
        self.tree.bind('<ButtonRelease-1>', self.select_item)
    def new_records_validated(self):
        return (self.namefield.get() != 0) # and len(self.phonefield.get()) != 0

    def create_message_area(self):
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, sticky=W)

if __name__ == '__main__':
    root = Tk()
    application = PhoneBook(root)
    root.mainloop()
