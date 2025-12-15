
import sqlite3

con = sqlite3.connect("hospital.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS patients (id TEXT, name TEXT, age INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS appointments (pid TEXT, date TEXT, doctor TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS billing (pid TEXT, amount INTEGER)")

con.commit()
con.close()
print("Database initialized")
