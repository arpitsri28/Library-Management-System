import sqlite3
sqliteConnection=sqlite3.connect("Library.db")
sqliteConnection.row_factory = lambda cursor, row: row[0]
cursor=sqliteConnection.cursor()
name=cursor.execute("SELECT Name from Books").fetchall()
names=[]
for val in name:
    names.append(val)
author=cursor.execute("SELECT Author from Books").fetchall()
authors=[]
for val in author:
    authors.append(val)
avail=cursor.execute("SELECT Available from Books").fetchall()
avails=[]
for val in avail:
    avails.append(val)
num=cursor.execute("SELECT EnNumber from Books").fetchall()
nums=[]
for val in num:
    nums.append(val)
shelf=cursor.execute("SELECT Shelf from Books").fetchall()
shelfs=[]
for val in shelf:
    shelfs.append(val)
row=cursor.execute("SELECT Row from Books").fetchall()
rows=[]
for val in row:
    rows.append(val)
person=cursor.execute("SELECT Name from Borrow").fetchall()
people=[]
for val in person:
    people.append(val)

class library:
    def __init__(self, name):
        self.name=name
    def checkavail(self):
        print(names)
        print("Enter 0 for the first book, 1 for the second, 2 for the third and 3 for the fourth")
        n=int(input("Enter the book number:"))
        print("=======================")
        print("Name:",names[n])
        print("Author:",authors[n])
        print("Enrollment Number:",nums[n])
        if avails[n]>0:
            print("Book Available")
        else:
            print("Book Not Available")
    def borrow(self):
        print(names)
        print("Enter 0 for the first book, 1 for the second, 2 for the third and 3 for the fourth")
        x=int(input("Enter the book name:"))
        z=input("Enter your name:")
        if avails[x]>0:
           a=names[x]
           d=authors[x]
           b=nums[x]
           c=(input("Enter date borrowed:"))
           params=(z,a,d,b,c)
           import sqlite3
           sqliteConnection=sqlite3.connect("Library.db")
           cursor=sqliteConnection.cursor()
           cursor.execute("INSERT INTO Borrow(Name, Book, Author, EnNumber, DateBorrowed) VALUES(?, ?, ?, ?, ?)",params)
           sqliteConnection.commit()
           cursor.close()
           sqliteConnection.close
           print("Book borrowed!")
        u=nums[x]
        t=avails[x]-1
        import sqlite3
        sqliteConnection=sqlite3 .connect("Library.db")
        cursor=sqliteConnection.cursor()
        sql_update_query="""Update Books set Available = ? where EnNumber = ?"""
        data = (t,u)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        cursor.close()
        sqliteConnection.close()
        print(a,", availability:",t)
    def returns(self):
        z=input("What is your name?")
        if z in people:
           print(names)
           print("Enter 0 for the first book, 1 for the second, 2 for the third and 3 for the fourth")
           x=int(input("Enter the book name you wish to return:"))
           a=names[x]
           c=(input("Enter date borrowed:"))
           m=(input("Enter date returned:"))
           param=(z,a,c,m)
           import sqlite3
           sqliteConnection=sqlite3.connect("Library.db")
           cursor=sqliteConnection.cursor()
           cursor.execute("INSERT INTO Return(Name, Book, DateBorrowed, DateReturned) VALUES(?, ?, ?, ?)",param)
           sqliteConnection.commit()
           cursor.close()
           sqliteConnection.close
           print("Book Returned, Thank You!")
           u=nums[x]
           t=avails[x]+1
           import sqlite3
           sqliteConnection=sqlite3 .connect("Library.db")
           cursor=sqliteConnection.cursor()
           sql_update_query="""Update Books set Available = ? where EnNumber = ?"""
           data = (t,u)
           cursor.execute(sql_update_query, data)
           sqliteConnection.commit()
           cursor.close()
           sqliteConnection.close()
           print(a,", availability:",t)
        else:
             print("Invalid Input")
                   

