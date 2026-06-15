a = int(input("Enter a number"))
b = int(input("Enter second number"))

if(b==0):
    raise ZeroDivisionError("np")
else:
    print(a/b)

print(a/b)