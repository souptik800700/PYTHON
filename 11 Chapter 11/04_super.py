class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1
class Pro(Employee):
    def __init__(self):
        print("Constructor of pro")
    b = 2
class man(Pro):
    def __init__(self):
        super().__init__()
        print("Constructor of man")
    c =3

o = man()

print(o.a)