class Person:
    cnt_users = 0

    @classmethod
    def count_users(cls):
        print(f"there are {cls.cnt_users} users")

    def __init__(self, name, age, hobie, gender):
        self._name = name  # protected property also (private)
        self.__age = age   # Strongly private
        self.hobie = hobie
        self.gender = gender
        Person.cnt_users += 1

    def show_info(self):
        return f"name : {self._name} \nhobie : {self.hobie} \nGender: {self.gender}"

    def __str__(self):
        return f" your information =>[name :{self._name}]"

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    @property
    def calcule_age_anymode(self):
        mode = input("which mode do you want calculate your age: ").lower()

        if mode == "days" or mode == "day":
            return f"{self.__age * 365} days "

        elif mode == "hours" or mode == "hour":
            return f"{self.__age * 365 * 60} Hours"

        elif mode == "seconds" or mode == "second":
            return f"{self.__age * 365 * 3600} Seconds"
        else:
            return self.__age


# name = input(" what's your name : ")
# age = int(input("Enter your age: "))
# hobie = input("What is your favourite Hobie: ")
# gender = input("enter your Gender :")

class Employee(Person):

    def __init__(self, name, age, hobie, gender, job, salary):
        super().__init__(name, age, hobie, gender)
        self.job = job
        self.salary = salary

    def Calcul_yearly_salary(self):
        return self.salary * 12


medo  = Person("ali", 21, "reading", "male")
medo1 = Person("ali", 21, "reading", "male")
medo2 = Person("ali", 21, "reading", "male")
emp1  = Employee("mohamed", 21, "swimming", "male", "Developer", 8000)

print(emp1.show_info())
print(medo.show_info())
print(medo.get_age())

# print(medo.calcule_age_anymode)

medo.set_age(19)
print(medo.get_age())
print(medo.__str__())
Person.count_users()
medo._Person__age = 33
print(medo.get_age())

