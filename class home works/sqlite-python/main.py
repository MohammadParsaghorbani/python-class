import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

# cur.execute("drop table students")

cur.execute("""
create table if not exists students(
    id int primary key,
    name varchar(50),
    nomre int
)
""")

cur.execute("insert into students (name,nomre) values ('parsa',20)")

conn.commit()
conn.close()