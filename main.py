import sqlite3

dbConnect = sqlite3.connect("sqlite.db")

dbCursor = dbConnect.cursor()

queryString = "SELECT bitcoin, month FROM SQLite"

data = dbCursor.execute(queryString).fetchall()

print(data)