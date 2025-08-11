import sqlite3

conn = sqlite3.connect("real_estate.db")
cursor = conn.cursor()

while True:
    try:
        option = int(input("optin:\n\t1) person\n\t2) sell\n\t3) rent\n\t4) factor\n\t5) exit\n: "))
        if option == 1:
            try:
                pr_op= int(input("option:\n\t1) owners\n\t2) buyers\n: "))
                qu = input("do you want to filter the results?(y/n) ")
                if pr_op == 1:
                    if qu == "y":
                        fl = int(input("which one?\n\t1) name\n\t2) phone_number\n: "))
                        if fl == 1:
                            ow_nm = input("enter name of owner to see the phone number: ")
                            cursor.execute("""
                                            select * from owners
                                            where owner_name = '{}' 
                                            """.format(ow_nm))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif fl == 2:
                            ow_ph = input("enter owner phone number to see the name: ")
                            cursor.execute("""
                                            select * from owners
                                            where phone_num = '{}' 
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                    else:
                        cursor.execute("""
                                        select * from owners
                                        """)
                        res = cursor.fetchall()
                        for i in res:
                            print(i)
                elif pr_op == 2:
                    if qu == "y":
                        fl = int(input("which one?\n\t1) name\n\t2) phone_number\n: "))
                        if fl == 1:
                            bu_nm = input("enter name of buyer to see the phone number: ")
                            cursor.execute("""
                                            select * from buyer
                                            where buyer_name = '{}' 
                                            """.format(bu_nm))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif fl == 2:
                            bu_ph = input("enter buyer phone number to see the name: ")
                            cursor.execute("""
                                            select * from buyer
                                            where phone_num = '{}' 
                                            """.format(bu_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                    else:
                        cursor.execute("""
                                        select * from buyer
                                        """)
                        res = cursor.fetchall()
                        for i in res:
                            print(i)
            except ValueError:
                print("wrong option!")
        elif option == 2:
            try:
                s_op = int(input("option:\n\t1) apartment\n\t2) villa\n\t3) land\n: "))
                qu = input("do you want to filter the results?(y/n) ")
                if s_op == 1:
                    if qu == "y":
                        fl = int(input("which one?\n\t1) apartment_id\n\t2) owner_name\n\t3) phone_number\n: "))
                        if fl == 1:
                            a_id = input("enter apartment id: ")
                            cursor.execute("""
                                            select * from apartment_buy
                                            where id = {}
                                            """.format(a_id))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif fl == 2:
                            name = input("enter owner name: ")
                            cursor.execute("""
                                            select * from apartment_buy
                                            where owner_name = '{}'
                                            """.format(name))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif fl == 3:
                            ph_nm = input("enter phone_number: ")
                            cursor.execute("""
                                            select * from apartment_buy
                                            where owner_phone = {}
                                            """.format(ph_nm))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                    else:
                        cursor.execute("""
                                        select * from villa_buy
                                        """)
                        res = cursor.fetchall()
                        for i in res:
                            print(i)
                if s_op == 2:
                    if qu == "y":
                        fl = int(input("which one?\n\t1) villa_id\n\t2) owner_name\n\t3) phone_number\n: "))
                        if fl == 1:
                            a_id = input("enter villa id: ")
                            cursor.execute("""
                                            select * from villa_buy
                                            where id = {}
                                            """.format(a_id))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif fl == 2:
                            name = input("enter owner name: ")
                            cursor.execute("""
                                            select * from villa_buy
                                            where owner_name = '{}'
                                            """.format(name))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif fl == 3:
                            ph_nm = input("enter phone_number: ")
                            cursor.execute("""
                                            select * from villa_buy
                                            where owner_phone = {}
                                            """.format(ph_nm))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                    else:
                        cursor.execute("""
                                        select * from villa_buy
                                        """)
                        res = cursor.fetchall()
                        for i in res:
                            print(i)
                if s_op == 3:
                    if qu == "y":
                        fl = int(input("which one?\n\t1) land_id\n\t2) owner_name\n\t3) phone_number\n: "))
                        if fl == 1:
                            a_id = input("enter land id: ")
                            cursor.execute("""
                                            select * from land
                                            where id = {}
                                            """.format(a_id))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif fl == 2:
                            name = input("enter owner name: ")
                            cursor.execute("""
                                            select * from land
                                            where owner_name = '{}'
                                            """.format(name))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif fl == 3:
                            ph_nm = input("enter phone_number: ")
                            cursor.execute("""
                                            select * from land
                                            where owner_phone = {}
                                            """.format(ph_nm))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                    else:
                        cursor.execute("""
                                        select * from villa_buy
                                        """)
                        res = cursor.fetchall()
                        for i in res:
                            print(i)
            except ValueError:
                print("wrong option!")
        elif option == 3:
            try:
                s_op = int(input("option:\n\t1) apartment\n\t2) villa\n: "))
                qu = input("do you want to filter the results?(y/n) ")
                if s_op == 1:
                    if qu == "y":
                        fl = int(input("which one?\n\t1) apartment_id\n\t2) owner_name\n\t3) phone_number\n: "))
                        if fl == 1:
                            a_id = input("enter apartment id: ")
                            cursor.execute("""
                                            select * from apartment_rent
                                            where id = {}
                                            """.format(a_id))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif fl == 2:
                            name = input("enter owner name: ")
                            cursor.execute("""
                                            select * from apartment_rent
                                            where owner_name = '{}'
                                            """.format(name))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif fl == 3:
                            ph_nm = input("enter phone_number: ")
                            cursor.execute("""
                                            select * from apartment_rent
                                            where owner_phone = {}
                                            """.format(ph_nm))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                    else:
                        cursor.execute("""
                                        select * from villa_buy
                                        """)
                        res = cursor.fetchall()
                        for i in res:
                            print(i)            
                if s_op == 2:
                    if qu == "y":
                        fl = int(input("which one?\n\t1) villa_id\n\t2) owner_name\n\t3) phone_number\n: "))
                        if fl == 1:
                            a_id = input("enter villa id: ")
                            cursor.execute("""
                                            select * from villa_rent
                                            where id = {}
                                            """.format(a_id))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif fl == 2:
                            name = input("enter owner name: ")
                            cursor.execute("""
                                            select * from villa_rent
                                            where owner_name = '{}'
                                            """.format(name))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif fl == 3:
                            ph_nm = input("enter phone_number: ")
                            cursor.execute("""
                                            select * from villa_rent
                                            where owner_phone = {}
                                            """.format(ph_nm))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                    else:
                        cursor.execute("""
                                        select * from villa_buy
                                        """)
                        res = cursor.fetchall()
                        for i in res:
                            print(i)
            except ValueError:
                print("wrong option!")
        elif option == 4:
            try:
                prc_op = int(input("option:\n\t1) apartment_buy\n\t2) apartment_rent\n\t3) villa_buy\n\t4) villa_rent\n\t5) land\n: "))
                if prc_op == 1:
                    try:
                        ab_op = int(input("option:\n\t1) apartment_id\n\t2) owner_phone\n\t3) buyer_phone\n: "))
                        if ab_op == 1:
                            ow_ph = input("enter apartment id: ")
                            cursor.execute("""
                                            select * from apartmentbuy_price_list
                                            where id = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif ab_op == 2:
                            ow_ph = input("enter owner phone: ")
                            cursor.execute("""
                                            select * from apartmentbuy_price_list
                                            where owner_phone = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif ab_op == 3:
                            ow_ph = input("enter buyer phone: ")
                            cursor.execute("""
                                            select * from apartmentbuy_price_list
                                            where buyer_phone = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                    except ValueError:
                        print("wrong option!")
                if prc_op == 2:
                    try:
                        ab_op = int(input("option:\n\t1) apartment_id\n\t2) owner_phone\n\t3) buyer_phone\n: "))
                        if ab_op == 1:
                            ow_ph = input("enter apartment id: ")
                            cursor.execute("""
                                            select * from apartmentrent_price_list
                                            where id = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif ab_op == 2:
                            ow_ph = input("enter owner phone: ")
                            cursor.execute("""
                                            select * from apartmentrent_price_list
                                            where owner_phone = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif ab_op == 3:
                            ow_ph = input("enter buyer phone: ")
                            cursor.execute("""
                                            select * from apartmentrent_price_list
                                            where buyer_phone = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                    except ValueError:
                        print("wrong option!")
                if prc_op == 3:
                    try:
                        ab_op = int(input("option:\n\t1) villa_id\n\t2) owner_phone\n\t3) buyer_phone\n: "))
                        if ab_op == 1:
                            ow_ph = input("enter villa id: ")
                            cursor.execute("""
                                            select * from villabuy_price_list
                                            where id = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif ab_op == 2:
                            ow_ph = input("enter owner phone: ")
                            cursor.execute("""
                                            select * from villabuy_price_list
                                            where owner_phone = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif ab_op == 3:
                            ow_ph = input("enter buyer phone: ")
                            cursor.execute("""
                                            select * from villabuy_price_list
                                            where buyer_phone = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                    except ValueError:
                        print("wrong option!")
                if prc_op == 4:
                    try:
                        ab_op = int(input("option:\n\t1) villa_id\n\t2) owner_phone\n\t3) buyer_phone\n: "))
                        if ab_op == 1:
                            ow_ph = input("enter villa id: ")
                            cursor.execute("""
                                            select * from villarent_price_list
                                            where id = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif ab_op == 2:
                            ow_ph = input("enter owner phone: ")
                            cursor.execute("""
                                            select * from villarent_price_list
                                            where owner_phone = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif ab_op == 3:
                            ow_ph = input("enter buyer phone: ")
                            cursor.execute("""
                                            select * from villarent_price_list
                                            where buyer_phone = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                    except ValueError:
                        print("wrong option!")
                if prc_op == 1:
                    try:
                        ab_op = int(input("option:\n\t1) land_id\n\t2) owner_phone\n\t3) buyer_phone\n: "))
                        if ab_op == 1:
                            ow_ph = input("enter apartment id: ")
                            cursor.execute("""
                                            select * from land_price_list
                                            where id = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif ab_op == 2:
                            ow_ph = input("enter owner phone: ")
                            cursor.execute("""
                                            select * from land_price_list
                                            where owner_phone = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                        elif ab_op == 3:
                            ow_ph = input("enter buyer phone: ")
                            cursor.execute("""
                                            select * from land_price_list
                                            where buyer_phone = {}
                                            """.format(ow_ph))
                            res = cursor.fetchall()
                            for i in res:
                                print(i)
                    except ValueError:
                        print("wrong option!")
            except ValueError:
                print("wrong option!")
        elif option == 5:
            print("goodbye!")
            break
        else:
            print("wrong option!")
    except ValueError:
        print("wrong option!")

conn.close()