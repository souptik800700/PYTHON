letter = """Dear <|Name|>,
You are selected!
<|Date|>"""

a = input("name ")

b = input("date ")

print(letter.replace("<|Name|>","Harry").replace("<|Date|>", "24 september 2050"))