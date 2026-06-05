f = open("file.txt")

print(f.read())

f.close()

# the same can be write

with open("file.txt") as f:
    print(f.read())

# U do not have to explicitly close the file