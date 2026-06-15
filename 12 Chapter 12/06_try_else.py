try:
    a = int(input("Hey"))
    print(a)

except ValueError as v:
    print("Heyy")
    print(v)
except Exception as e:
    print(e)

else:
    print("else")