import sqlite3
sqliteConnection=sqlite3.connect("Library.db")
cursor=sqliteConnection.cursor()
print("Created successfully!")
cursor.close()
sqliteConnection.close() 

import sqlite3
sqliteConnection=sqlite3.connect("Library.db")
cursor=sqliteConnection.cursor()
create_table_query='''CREATE TABLE Books(
                      Name TEXT NOT NULL,
                      Author TEXT NOT NULL,
                      EnNumber INTEGER PRIMARY KEY,
                      Shelf TEXT NOT NULL,
                      Row INTEGER NOT NULL,
                      Quantity INTEGER NOT NULL,
                      Available INTEGER NOT NULL);'''
cursor.execute(create_table_query)
sqliteConnection.commit()
cursor.close()
sqliteConnection.close() 

import sqlite3
sqliteConnection=sqlite3.connect("Library.db")
cursor=sqliteConnection.cursor()
sqlite_insert_query='''INSERT INTO Books
                       (Name, Author, EnNumber, Shelf, Row, Quantity, Available)
                       VALUES
                       ("Harry Potter","J.K Rowling",100,"A",5,8,8)'''
cursor.execute(sqlite_insert_query)
sqliteConnection.commit()
cursor.close()
sqliteConnection.close()

import sqlite3
sqliteConnection=sqlite3.connect("Library.db")
cursor=sqliteConnection.cursor()
sqlite_insert_query='''INSERT INTO Books
                       (Name, Author, EnNumber, Shelf, Row, Quantity, Available)
                       VALUES
                       ("Alice in Wonderland","Lewis Carroll",101,"A",6,3,3)'''
cursor.execute(sqlite_insert_query)
sqliteConnection.commit()
cursor.close()
sqliteConnection.close()
import sqlite3
sqliteConnection=sqlite3.connect("Library.db")
cursor=sqliteConnection.cursor()
sqlite_insert_query='''INSERT INTO Books
                       (Name, Author, EnNumber, Shelf, Row, Quantity, Available)
                       VALUES
                       ("The Famous Five","Enid Blyton",103,"B",2,4,4)'''
cursor.execute(sqlite_insert_query)
sqliteConnection.commit()
cursor.close()
sqliteConnection.close()

import sqlite3
sqliteConnection=sqlite3.connect("Library.db")
cursor=sqliteConnection.cursor()
sqlite_create_table_query='''CREATE TABLE Borrow(
                             Name TEXT NOT NULL,
                             EnNumber PRIMARY KEY,
                             DateBorrowed INTEGER NOT NULL);'''
cursor.execute(sqlite_create_table_query)
cursor.close()
sqliteConnection.close()

import sqlite3
sqliteConnection=sqlite3.connect("Library.db")
cursor=sqliteConnection.cursor()
create_table_query='''CREATE TABLE Borrow(
                             Name TEXT NOT NULL,
                             Book TEXT NOT NULL,
                             Author TEXT NOT NULL,
                             EnNumber INTEGER PRIMARY KEY,
                             Shelf TEXT NOT NULL,
                             Row INTEGER NOT NULL,
                             Quantity INTEGER NOT NULL,
                             Available INTEGER NOT NULL);'''
cursor.execute(create_table_query)
sqliteConnection.commit()
cursor.close()
sqliteConnection.close()

import sqlite3
sqliteConnection=sqlite3.connect("Library.db")
cursor=sqliteConnection.cursor()
create_table_query='''CREATE TABLE Return(
                      Name TEXT NOT NULL,
                      Book TEXT NOT NULL,
                      DateBorrowed INTEGER NOT NULL,
                      DateReturned INTEGER NOT NULL);'''
cursor.execute(create_table_query)
sqliteConnection.commit()
cursor.close()
sqliteConnection.close()
