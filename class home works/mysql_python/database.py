import mysql.connector

con = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    password = "",
    database = "parsa"
)

cur = con.cursor()
# cur.execute("create database parsa")

cur.execute("create table if not exists users (id int AUTO_INCREMENT PRIMARY KEY,name VARCHAR(500),age varchar(10))")

# cur.execute("INSERT INTO users(name, age) VALUES ('parsa' , '15')")
a = cur.execute("SELECT * from users")
res = cur.fetchall()
for i in res:
    print(i)
con.commit()