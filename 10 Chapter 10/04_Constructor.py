class Employee:
    # name = "Harry"
    language = "python"
    salary = 1200000

    def __init__(self, name, salary, language): #it is automatically call
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. the salary is {self.salary}")


    @staticmethod
    def greet():
        print("Good Morning")


harry = Employee("Harry", 1300000, "JavaScript")
# harry.name = "Harry"
harry.language= "javscript"
print(harry.name, harry.salary)

 