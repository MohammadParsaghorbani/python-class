import mysql.connector

con = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    password = "",
    database = "homeProject"
)

cur = con.cursor()

# def table():
#     t_name = input("enter table name: ")
#     while True:
#         row_n = input("enter row name: ")
#         row_type = input("enter row type: ")

while True :
    try:
        option = int(input("options:\n\t1) enter data\n\t2) read data\n\t3) update\n\t4) delete data\n\t5) exit\n:"))

    except ValueError:
        print("wrong option!")
        # baraye database avaliye model figma rasm shavad
        # ba tedad tabel kam

    