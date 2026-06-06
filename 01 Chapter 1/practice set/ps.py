import os

path = "."   # Current directory

contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)