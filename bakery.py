#bakery

bakery = {
    "barbary" : 1500,
    "lavash" : 3500,
    "taftoon" : 2500,
    "buget" : 7000,
    "sangak" : 3000
}

print(f"welcom to our bakery! \nthis are the bread types which we have: \n{bakery}")
print("b : barbary\nl : lavash\nt : taptoon\nbu : buget\ns : sangak")
user_name = input("at first you should register!\nso please enter your name: ")
user_lastname = input("now enter your last name: ")
user_phone = input("enter your phone number: ")
file = open("data.txt" , "a")
content = file.write(f"\n----------------\nname = {user_name}\nlastname = {user_lastname}\nphonenumber = {user_phone}")
again = "y"
total = 0
buy_times = 0
item_num = 0
choice = ""
while again == "y":
    user_choice = input("which one? ")
    product = ["b","l","t","bu","s"]
    while user_choice not in product:
        user_choice = input(f"please choice from the items:\n{product}\nwhich one? ")
    item_num = int(input("how many? "))
    if user_choice == "b":
        choice="barbary"
        total+=bakery["barbary"]*item_num
    elif user_choice == "l":
        choice="lavash"
        total+=bakery["lavash"]*item_num
    elif user_choice == "t":
        choice ="taftoon"
        total+=bakery["taftoon"]*item_num
    elif user_choice == "bu":
        choice ="buget"
        total+=bakery["buget"]*item_num
    elif user_choice == "s":
        choice = "sangak"
        total+=bakery["sangak"]*item_num
    buy_times +=1
    file.write(f"\nitem = {choice}-item_number = {item_num}")
    again = input("do you want to buy anything else?y/n ")
print(f"you should pay {total}T")
file.write(f"\nbuy_times = {buy_times}\ntotal = {total}T")
file.close()