class Employee:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")


class Programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"the name is {self.name} and slary is {self.salary}")
    def showlangauage(self):
            print(f"the name is {self.name} and he language {self.language}")



class programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.name} and he language {self.language}")
a = Employee()
b = Programmer()

print(a.company, b.company)