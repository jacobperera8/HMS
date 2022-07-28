# This is the database file used to make the tables
# I have used SQLITE3 as the database for saving the data from the webpage to the database


import sqlite3

conn = sqlite3.connect("database.db")

print("opened database successfully")

conn.execute("CREATE TABLE Doctors (Firstname TEXT, Secondname TEXT, Lastname TEXT)")

conn.execute("CREATE TABLE Appointments (Firstname TEXT, Lastname TEXT, Datetime NULL, Kind TEXT)")

print("table created successfully")

conn.close()