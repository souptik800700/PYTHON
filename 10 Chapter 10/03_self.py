class Employee:
    # name = "Harry"
    language = "python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. the salary is {self.salary}")


    @staticmethod
    def greet():
        print("Good Morning")


harry = Employee()
harry.name = "Harry"
harry.language= "javscript"
print(harry.language, harry.salary)
harry.getInfo()
harry.greet()
# rohan = Employee()
# rohan.name = "Rohan ro ro"
# print(rohan.salary, rohan.language)
