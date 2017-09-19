'''
Code illustration: 7.12
    Phonebook Application
Tkinter GUI Application Development Blueprints
'''
from tkinter import *
from tkinter import ttk
import sqlite3


class PhoneBook:

    db_filename = 'foresthouse.db'
    #db_filename = 'C:\\PyProjects\\learnpy\\guest.db'
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
        #self.create_left_icon()
        self.create_label_frame()
        self.create_message_area()
        self.create_tree_view()
        self.create_bottom_buttons()
        self.view_records()

    def create_left_icon(self):
        #photo = PhotoImage(file='phonebook.gif')
        photo = PhotoImage(file='C:\\PyProjects\\learnpy\\we1.gif')
        label = Label(image=photo)
        label.image = photo
        label.grid(row=0, column=2,padx=100)
        self.root.title("The Foresthouse Guests")

    def create_label_frame(self):
        labelframe = LabelFrame(self.root, text='Create New Record')
        labelframe.grid(row=0, column=0, padx=2, pady=8, sticky='we')

        Label(labelframe, text='Name:',relief=RIDGE,width=15).grid(row=1, column=1, sticky=W, pady=2)
        self.namefield = Entry(labelframe,width=50)
        self.namefield.grid(row=1, column=2, sticky='we', padx=5, pady=2)

        Label(labelframe, text='Phone:',relief=RIDGE,width=15).grid(row=2, column=1, sticky=W, pady=2)
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
        self.tree.grid(row=4, column=0) #, columnspan=2)

        self.tree.heading('#0', text='Name', anchor=W)
        #self.tree.heading('#1', text='Phone Number', anchor=W)



        self.tree["columns"] = ("one", "two", "three")

        self.tree.column("one", width=150)
        self.tree.column("two", width=200)
        self.tree.column("three", width=100)

        self.tree.heading("one", text="Phone")
        self.tree.heading("two", text="Email")
        self.tree.heading("three", text="Comments")

        #self.tree.heading('#2', text='Phone Number', anchor=W)


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
        self.execute_db_query(query, (name,))
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
        name = self.tree.item(self.tree.selection())['text']
        old_phone_number = self.tree.item(self.tree.selection())['values'][0]
        self.transient = Toplevel()
        Label(self.transient, text='Name:').grid(row=0, column=1)
        Entry(self.transient, textvariable=StringVar(
            self.transient, value=name), state='readonly').grid(row=0, column=2)
        Label(self.transient, text='Old Phone Number:').grid(row=1, column=1)
        Entry(self.transient, textvariable=StringVar(
            self.transient, value=old_phone_number), state='readonly').grid(row=1, column=2)
        Label(self.transient, text='New Phone Number:').grid(row=2, column=1)
        new_phone_number_entry_widget = Entry(self.transient)
        new_phone_number_entry_widget.grid(row=2, column=2)
        Button(self.transient, text='Update Record', command=lambda:
        self.update_record(new_phone_number_entry_widget.get(),
                           old_phone_number,name)).grid(row=3, column=2, sticky=E)
        self.transient.mainloop()

    def update_record(self, newphone, old_phone_number, name):
        query = 'UPDATE guest SET phone=? WHERE phone=? AND name=?'
        parameters = (newphone, old_phone_number, name)
        self.execute_db_query(query, parameters)
        self.transient.destroy()
        self.message['text'] = 'Phone number of {} modified'.format(name)
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
            self.message['text'] = 'name and phone number cannot be blank'
        self.view_records()

    def create_bottom_buttons(self):
        ttk.Button(text='Delete Selected',
            command=self.on_delete_selected_button_clicked).grid(row=5, column=0, sticky=W)
        ttk.Button(text='Modify Selected',
            command=self.on_modify_selected_button_clicked).grid(row=5, column=0, sticky=E)

    def view_records(self):
        items = self.tree.get_children()

        for item in items:
            self.tree.delete(item)
        query = 'SELECT * FROM guest ORDER BY name desc'
        phone_book_entries = self.execute_db_query(query)
        for row in phone_book_entries:
            self.tree.insert('', 0, text=row[1], values=(row[2],row[3],row[4]))

    def new_records_validated(self):
        return len(self.namefield.get()) != 0 and len(self.phonefield.get()) != 0

    def create_message_area(self):
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, sticky=W)

if __name__ == '__main__':
    root = Tk()
    application = PhoneBook(root)
    root.mainloop()
