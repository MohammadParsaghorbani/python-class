#fisher man
import random as rnd

fisher_pound = rnd.randint(100,2000)
fisher_kilo = fisher_pound * 0.4536
print(f"fisher get {fisher_kilo}kg or {fisher_pound}pound of fishs")
fish = {
    "Trout" : 200000,
    "Tuna" : 85500,
    "Bass" : 155000,
    "Carp" : 220000
}
print(f"welcom to our fishing shop!\nwe have this fish and price for a kilo:\n{fish}")
name = input("at first,you should register on system.\nplease enter yous name: ")
last_name = input("enter your last name: ")
phone_num = input("and enter your phone number: ")
file = open("fisherman.txt" , "a")
file.write(f"\n----------------\nname = {name}\nlast_name = {last_name}\nphone_number = {phone_num}")
again = "y"
again_num = 0
prodoct = ""
total = 0
while again == "y":
    coustomer_choice = input("enter fish: ")
    while coustomer_choice not in fish:
        coustomer_choice = input(f"you enter wrong item,please select from {list(fish)}: ")
    if coustomer_choice in fish:
        prodoct = fish[coustomer_choice]
    kilo = int(input("How many kilograms? "))
    again_num +=1
    price = prodoct*kilo
    total +=int(price)
    again = input("do you want to buy anything else?y/n ")
    file.write(f"\n{coustomer_choice} = {kilo}kg-{kilo/0.4536}\nprice = {price}")
print(f"you should pay {total}T")
file.write(f"\ntotal_price = {total}")
file.close()