from tkinter import *
import bookstore_backend

window = Tk()
window.title("Bookstore")
window.maxsize(width = 420 , height = 250)
window.minsize(width = 420 , height = 250)

def get_selected_row(event):
    if txt_box.curselection() != ():
        global selected
        index = txt_box.curselection()[0]
        selected = txt_box.get(index)
        title_entry.delete(0,END)
        title_entry.insert(END , selected[1])
        author_entry.delete(0,END)
        author_entry.insert(END , selected[2])
        year_entry.delete(0,END)
        year_entry.insert(END , selected[3])
        isbn_entry.delete(0,END)
        isbn_entry.insert(END , selected[4])
   

def view_all_btn():
    txt_box.delete(0,END)
    for row in bookstore_backend.view_all():
        txt_box.insert(END , row)
        

def search_entry_btn():
    txt_box.delete(0,END)
    for row in bookstore_backend.search_entry(title_value.get() , author_value.get() , year_value.get() , isbn_value.get()):
        txt_box.insert(END , row)

def add_entry_btn():
    bookstore_backend.add_entry(title_value.get() , author_value.get() , year_value.get() , isbn_value.get())

def update_selected_btn():
    bookstore_backend.update_selected(selected[0] , title_value.get() , author_value.get() , year_value.get() , isbn_value.get())

def delete_selected_btn():
    bookstore_backend.delete_selected(selected[0])

txt_box = Listbox(window , width= 40)
txt_box.grid(row = 3 , column = 0 , rowspan = 6 , columnspan = 2)

scroll_bar = Scrollbar(window)
scroll_bar.grid(row = 2 , column = 2 , rowspan = 6)

txt_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command= txt_box.yview)

txt_box.bind('<<ListboxSelect>>' , get_selected_row)

title_label = Label(window , text = "Title")
title_label.grid(row = 0 , column = 0)

title_value = StringVar()
title_entry = Entry(window , textvariable= title_value)
title_entry.grid(row = 0 , column = 1)

author_label = Label(window , text = "Author")
author_label.grid(row = 0 , column = 2)

author_value = StringVar()
author_entry = Entry(window , textvariable= author_value)
author_entry.grid(row = 0 , column = 3)

year_label = Label(window , text = "Year")
year_label.grid(row = 1 , column = 0)

year_value = StringVar()
year_entry = Entry(window , textvariable= year_value)
year_entry.grid(row = 1 , column = 1)

isbn_label = Label(window , text = "ISBN")
isbn_label.grid(row = 1 , column = 2)

isbn_value = StringVar()
isbn_entry = Entry(window , textvariable= isbn_value)
isbn_entry.grid(row = 1 , column = 3)

view_btn = Button(window , text = 'View All'  , width = 12, command = view_all_btn)
view_btn.grid(row = 2 , column = 3)

search_btn = Button(window , text = 'Search Entry', width = 12 , command = search_entry_btn)
search_btn.grid(row = 3 , column = 3)

add_btn = Button(window , text = 'Add Entry' , width = 12, command = lambda:[add_entry_btn() , view_all_btn()])
add_btn.grid(row = 4 , column = 3)

update_btn = Button(window , text = 'Update Entry' , width = 12, command = lambda:[update_selected_btn() , view_all_btn()])
update_btn.grid(row = 5 , column = 3)

delete_btn = Button(window , text = 'Delete Entry' , width = 12, command = lambda:[delete_selected_btn() , view_all_btn()])
delete_btn.grid(row = 6 , column = 3)

close_btn = Button(window , text = 'Close' , width = 12, command = window.destroy)
close_btn.grid(row = 7 , column = 3)

window.mainloop()