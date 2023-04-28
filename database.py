import sqlite3 as sql

conn = sql.connect("database.db")
print("Connected to the datbase")

cmd = "CREATE TABLE employee (EMPID INTEGER, EMPname TEXT, EMPgender TEXTAREA, EMPphone TEXT, EMPBdate Text)"

conn.execute(cmd)

print("Table created")

conn.close()


