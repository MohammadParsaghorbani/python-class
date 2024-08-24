#rock paper scissor
import random as rnd

print("welcom to rock,paper,scissor game!")
name = input("at first please register.enter your name:")
last_name = input("enter your last name: ")
phone_num = input("enter your phone number: ")
file = open("rps.txt" , "a")
file.write(f"\n----------------\nname = {name}\nlast_name = {last_name}\nphone_number = {phone_num}")
choice = ["r","p","s"]
again = "y"
again_num = 0
p_score = 0
pc_score = 0
while again == "y":
    print("you have 3 choice:\nrock = r\npaper = p\nscissors = s")
    player_choice = input("choose on: ")
    while player_choice not in choice:
        print(f"please choose from {choice}")
        player_choice = input("choose on: ")
    pc_choice = rnd.choice(choice)
    if pc_choice == player_choice:
        print("draw!!")
    elif player_choice == "r":
        if pc_choice == "p":
            pc_score +=1
            print("pc is the winer!!!")
        elif pc_choice == "s":
            p_score +=1
            print("player win!!")
    elif player_choice == "p":
        if pc_choice == "r":
            p_score +=1
            print("player win!!")
        elif pc_choice == "s":
            pc_score += 1
            print("pc is the winer!!!")
    elif player_choice == "s":
        if pc_choice == "p":
            p_score +=1
            print("player win!!")
        elif pc_choice == "r":
            pc_score += 1
            print("pc is the winer!!!")
    again_num+=1
    file.write(f"\nround = {again_num}\nplayer_choice = {player_choice}\npc_choice = {pc_choice}")
    print(f"player = {p_score} , pc = {pc_score}")
    again = input("do you want to play again?y/n ")

print(f"player = {p_score}\npc = {pc_score}")
file.write(f"\nplayer = {p_score}\npc = {pc_score}\nagain_num = {again_num}")
file.close()