# a = int(input("Enter your number"))

# b = 45

# c= 45

# average = (a+b+c)

# print(average)

#function Def
def avg():
    a = int(input("Enter your number"))
    b = int(input("Enter your number"))
    c = int(input("Enter your number"))

    average = (a+b+c)/3
    print(average)
    return average

#Function Call
a = avg()