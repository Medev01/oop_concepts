class Students:
    not_allowed_names = ["maj", "sai", "fat"]
    cnt = 0

    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        Students.cnt += 1

    def info(self):
        return f"Hello {self.fname} {self.lname} \n Your age is {self.age}"

    def check_name(self):
        if self.fname not in Students.not_allowed_names:
            return f" Hello {self.fname}"
        else:
            raise ValueError("not allowed")


print(Students.cnt)
student_1 = Students("maj", "Mohamed", 21, "male")
student_2 = Students("khafifi", "Aya", 17, "female")
print(Students.cnt)
print(student_1.info())
print(student_2.info())
print(student_1.check_name())
print(student_2.check_name())
