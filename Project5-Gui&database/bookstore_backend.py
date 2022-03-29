import sqlite3

con = sqlite3.connect('bookstore.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY , title TEXT, author TEXT, year INTEGER, isbn INTEGER)")

def view_all():
    con = sqlite3.connect('bookstore.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    view_value = cur.fetchall()
    con.close()
    return view_value

def search_entry(title_value="" , author_value="" , year_value="" , isbn_value=""):
    con = sqlite3.connect('bookstore.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?" , (title_value , author_value , year_value , isbn_value))
    search_value = cur.fetchall()
    con.close()
    return search_value

def add_entry(title_value , author_value , year_value , isbn_value):
    con = sqlite3.connect('bookstore.db')
    cur = con.cursor()
    cur.execute("INSERT INTO books VALUES (NULL , ? , ? , ? ,?)" , (title_value , author_value , year_value , isbn_value))
    con.commit()
    con.close() 

def update_selected(id_value , title_value , author_value , year_value , isbn_value):
    con = sqlite3.connect('bookstore.db')
    cur = con.cursor()
    cur.execute("UPDATE books SET title = ? , author = ? , year = ? , isbn = ? WHERE id = ?" , (title_value , author_value , year_value , isbn_value , id_value))
    con.commit()
    con.close()

def delete_selected(id_value):
    con = sqlite3.connect('bookstore.db')
    cur = con.cursor()
    cur.execute("DELETE FROM books WHERE id = ?" , (id_value,))
    con.commit()
    con.close()

con.commit()
con.close()