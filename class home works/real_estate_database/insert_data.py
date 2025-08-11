import sqlite3
import datetime

conn = sqlite3.connect('real_estate.db')
cursor = conn.cursor()

today = datetime.datetime.now()
year = today.year
month = today.month
day = today.day

t = f"{year}/{month}/{day}"

while True:
    try:
        option = int(input("optin:\n\t1) person\n\t2) sell\n\t3) rent\n\t4) factor\n\t5) exit\n: "))
        if option == 1:
            try:
                person_option = int(input("option:\n\t1) owners\n\t2) buyers\n: "))
                if person_option == 1:
                    try:
                        ow_ph = int(input("enter owner phone number: "))
                        ow_name = input("enter owner name: ")
                        cursor.execute("""
                                        insert into owners values({},'{}','{}')
                                        """.format(ow_ph,ow_name,t))
                    except ValueError:
                        print("wrong option!")
                elif person_option == 2:
                    try:
                        bu_ph = int(input("enter buyer phone number: "))
                        bu_name = input("enter buyer name: ")
                        cursor.execute("""
                                        insert into buyer values({},'{}','{}')
                                        """.format(bu_ph,bu_name,t))
                    except ValueError:
                        print("wrong option!")
            except ValueError:
                print("wrong option!")
            conn.commit()
        elif option == 2:
            try:
                sell_option = int(input("option:\n\t1) apartment\n\t2) villa\n\t3) land\n:"))
                if sell_option == 1:
                    try:
                        id = input("enter apartment id: ")
                        ow_name = input("enter owner name: ")
                        ow_ph = input("entre owner phone: ")
                        meter = input("enter meter: ")
                        bar = input("enter bar of it: ")
                        loc = input("enter location of it: ")
                        p_m = input("price per meter : ")
                        total_price = input("enter total price: ")
                        document = input("enter document: ")
                        elev = input("it has elevator(yes/no): ")
                        storage = input("it has storage(yes/no): ")
                        park = input("it has parking(yes/no): ")
                        description = input("enter description: ")
                        cursor.execute("""
                                        insert into apartment_buy values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
                                        """.format(id,ow_name,ow_ph,meter,bar,loc,p_m,total_price,document,elev,storage,park,description,t))
                    except ValueError:
                        print("wrong option!")
                    conn.commit()
                elif sell_option == 2:
                    try:
                        id = input("enter villa id: ")
                        ow_name = input("enter owner name: ")
                        ow_ph = input("entre owner phone: ")
                        meter = input("enter meter: ")
                        bar = input("enter bar of it: ")
                        loc = input("enter location of it: ")
                        p_m = input("price per meter : ")
                        total_price = input("enter total price: ")
                        document = input("enter document: ")
                        elev = input("it has elevator(yes/no): ")
                        storage = input("it has storage(yes/no): ")
                        park = input("it has parking(yes/no): ")
                        description = input("enter description: ")
                        cursor.execute("""
                                        insert into villa_buy values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
                                        """.format(id,ow_name,ow_ph,meter,bar,loc,p_m,total_price,document,elev,storage,park,description,t))
                    except ValueError:
                        print("wrong option!")
                    conn.commit()
                elif sell_option == 3:
                    try:
                        id = input("enter land id: ")
                        ow_name = input("enter owner name: ")
                        ow_ph = input("entre owner phone: ")
                        meter = input("enter meter: ")
                        bar = input("enter bar of it: ")
                        loc = input("enter location of it: ")
                        p_m = input("price per meter : ")
                        total_price = input("enter total price: ")
                        document = input("enter document: ")
                        elev = input("it has elevator(yes/no): ")
                        storage = input("it has storage(yes/no): ")
                        park = input("it has parking(yes/no): ")
                        description = input("enter description: ")
                        cursor.execute("""
                                        insert into land values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
                                        """.format(id,ow_name,ow_ph,meter,bar,loc,p_m,total_price,document,elev,storage,park,description,t))
                    except ValueError:
                        print("wrong option!")
                    conn.commit()
            except ValueError:
                print("wrong option!")
            conn.commit()
        elif option == 3:
            try:
                rent_op = int(input("option:\n\t1) apartment\n\t2) villa"))
                if rent_op == 1:
                    try:
                        id = input("enter apartment id: ")
                        ow_name = input("enter owner name: ")
                        ow_ph = input("entre owner phone: ")
                        meter = input("enter meter: ")
                        bar = input("enter bar of it: ")
                        loc = input("enter location of it: ")
                        p_m = input("first_price : ")
                        total_price = input("enter price per month: ")
                        document = input("enter document: ")
                        elev = input("it has elevator(yes/no): ")
                        storage = input("it has storage(yes/no): ")
                        park = input("it has parking(yes/no): ")
                        description = input("enter description: ")
                        cursor.execute("""
                                        insert into apartment_rent values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{})
                                        """.format(id,ow_name,ow_ph,meter,bar,loc,p_m,total_price,document,elev,storage,park,description,t))
                    except ValueError:
                        print("wrong option!")
                    conn.commit()
                elif rent_op == 2:
                    try:
                        id = input("enter villa id: ")
                        ow_name = input("enter owner name: ")
                        ow_ph = input("entre owner phone: ")
                        meter = input("enter meter: ")
                        bar = input("enter bar of it: ")
                        loc = input("enter location of it: ")
                        p_m = input("first_price : ")
                        total_price = input("enter price per month: ")
                        document = input("enter document: ")
                        elev = input("it has elevator(yes/no): ")
                        storage = input("it has storage(yes/no): ")
                        park = input("it has parking(yes/no): ")
                        description = input("enter description: ")
                        cursor.execute("""
                                        insert into villa_rent values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
                                        """.format(id,ow_name,ow_ph,meter,bar,loc,p_m,total_price,document,elev,storage,park,description,t))
                    except ValueError:
                        print("wrong option!")
                    conn.commit()
            except ValueError:
                print("wrong option!")
            conn.commit()
        elif option == 4:
            try:
                price_op = int(input("option:\n\t1) apartment_buy\n\t2) apartment_rent\n\t3) villa_buy\n\t4) villa_rent\n\t5) land\n:"))
                if price_op == 1:
                    try:
                        ow_ph = input("enter owner phon: ")
                        id = input("enter apartment id: ")
                        bu_ph = input("enter buyer phone: ")
                        total_price = input("enter total price: ")
                        cursor.execute("""
                                        insert into apartmentbuy_price_list values('{}','{}','{}','{}')
                                        """.format(ow_ph,id,bu_ph,total_price,t))
                    except ValueError:
                        print("wrong")
                    conn.commit()
                elif price_op == 2:
                    try:
                        ow_ph = input("enter owner phon: ")
                        id = input("enter apartment id: ")
                        bu_ph = input("enter buyer phone: ")
                        total_price = input("enter total price: ")
                        cursor.execute("""
                                        insert into apartmentrent_price_list values('{}','{}','{}','{}')
                                        """.format(ow_ph,id,bu_ph,total_price,t))
                    except ValueError:
                        print("wrong")
                    conn.commit()
                elif price_op == 3:
                    try:
                        ow_ph = input("enter owner phon: ")
                        id = input("enter villa id: ")
                        bu_ph = input("enter buyer phone: ")
                        total_price = input("enter total price: ")
                        cursor.execute("""
                                        insert into villabuy_price_list values('{}','{}','{}','{}')
                                        """.format(ow_ph,id,bu_ph,total_price,t))
                    except ValueError:
                        print("wrong")
                    conn.commit()
                elif price_op == 4:
                    try:
                        ow_ph = input("enter owner phon: ")
                        id = input("enter villa id: ")
                        bu_ph = input("enter buyer phone: ")
                        total_price = input("enter total price: ")
                        cursor.execute("""
                                        insert into villarent_price_list values('{}','{}','{}','{}')
                                        """.format(ow_ph,id,bu_ph,total_price,t))
                    except ValueError:
                        print("wrong")
                    conn.commit()
                elif price_op == 5:
                    try:
                        ow_ph = input("enter owner phon: ")
                        id = input("enter land id: ")
                        bu_ph = input("enter buyer phone: ")
                        total_price = input("enter total price: ")
                        cursor.execute("""
                                        insert into land_price_list values('{}','{}','{}','{}')
                                        """.format(ow_ph,id,bu_ph,total_price,t))
                    except ValueError:
                        print("wrong")
                    conn.commit()
            except ValueError:
                print("wrong option!")
            conn.commit()
        elif option == 5:
            print("goodbye!")
            break
        else:
            print("wrong option!")
    except ValueError:
        print("wrong option!")
conn.close()