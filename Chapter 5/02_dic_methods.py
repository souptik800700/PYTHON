marks = {
    "Harry" : 100,
    "Subham": 50,
    "Roham": 40

}

# print(marks.items())

marks.update({"Harry": 99, "Renuka": 100})
print(marks)

print(marks.get("Harry"))
print(marks["Harry"])
# print(marks["Harry"])