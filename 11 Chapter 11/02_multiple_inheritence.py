class Employee:
    company = "ITC"
    name = "Default company"
    def show(self):
        name = "Default company"
        print(f"the name is {self.name} and the salary is {self.company}")


class Coder:
    language = "python"
    def printLanguage(self):
        print(f"out of all the language {self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.company} and he language {self.language}")
a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()