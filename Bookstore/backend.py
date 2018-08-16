import sqlite3

class Database:

    def __init__(self): #constructor
        self.connect = sqlite3.connect("bookstore.db")
        self.cur = self.connect.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT,title text, author text, year integer, isbn integer)")
        self.connect.commit()

    def insert(self, title, text, year, isbn): #insert to database
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ? )", (title, text, year, isbn))
        self.connect.commit()

    def view(self): # view records
        self.cur.execute("SELECT * FROM book")
        result = self.cur.fetchall()
        return result

    def search(self, title = "", author = "", year = "", isbn = ""): #records retrieve
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        result = self.cur.fetchall()
        return result

    def delete(self, id): # delete the records
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.connect.commit()

    def deleteAll(self): # delete every record
        self.cur.execute("DELETE FROM book")
        self.connect.commit()

    def update(self, id, title, author, year, isbn): #update the select record
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.connect.commit()

    def __del__(self): #close the database connection
        self.connect.close()
