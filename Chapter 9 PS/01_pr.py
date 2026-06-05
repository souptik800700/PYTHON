
f = open("poems.txt")
c = f.read()

if("twinkle" in c):
    print("yes")
else:
    print("no")

f.close()
