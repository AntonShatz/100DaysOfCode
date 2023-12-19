import random
#
# random_num = random.randint(0,1)
# if random_num ==1:
#     print("heads")
# else:
#     print("tails")

# names = input("Enter 3 names : ")
# names = names.split(",")
# print(names[random.randint(0,len(names)-1)])

# row1 = ["","",""]
# row2 = ["","",""]
# row3 = ["","",""]
# map= [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the tressure ? \n")
# row = int(position[0])
# column = int(position[1])
# selected_row = map[row-1]
# selected_row[column-1]= "X"
# print(f"{row1}\n{row2}\n{row3}")

# Rock paper Scissors
# user_choice = int(input("What do you choose ? 1 - rock 2- paper 3 - scissors\n"))
# if user_choice>3 or user_choice<1:
#     print("Wrong number choose again")
# else:
#     pc_choice = random.randint(1,3)
#     list = ['rock','paper','scissors']
#     print(f"You chose {list[user_choice-1]}\n"+"Pc chose " + list[pc_choice-1])
#
#     if user_choice==1 and pc_choice==3:
#         print("You win ")
#     elif pc_choice > user_choice:
#         print("You lost")
#     elif pc_choice==user_choice:
#         print("Its a draw")
#     elif pc_choice==1 and user_choice==3:
#         print("you lost ")
#     elif pc_choice < user_choice:
#         print("you won")

print(len(input("whats your name ")))
