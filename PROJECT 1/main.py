import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your Choice: ")

youDict = {"s": 1,"w": -1,"g": 0 }
reverseDict = {1: "snake",
-1: "water",
0: "gun" }
you = youDict[youstr]

#By now we have 2 numbers(variable), you and computer

print(f"you choose {reverseDict[you]}\n com choose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")
else:
    if(computer == -1 and you == 1):
        print("you win")

    elif(computer == -1 and you == 0):
        print("You Lose")
    elif(computer == 1 and you == -1):
        print("You Lose")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Lose!")
    else:
        print("something went wrong")

