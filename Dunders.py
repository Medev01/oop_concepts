class Employee:
    num_emp = 0
    raise_amount = 0.97
    def __init__(self, first,last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        Employee.num_emp += 1

    def generate_email(self)  : 
        email = self.first.lower()+'.'+self.last.lower()+'@company.com'
        return email
        
    def personnal_info(self):
        return "Fullname: {}, Salary : {}.".format(self.first+' '+self.last, self.salary)
    
    def raise_salary(self):
        self.salary = int(self.salary * self.raise_amount)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first+''+self.last,self.generate_email(),self.salary)
    

    def __str__(self):
        return f"{self.first} {self.last}"
    
     
Emp_1 = Employee('aya','hamdi',23800)
Emp_2 = Employee('Katrin','Alisha',90000)
print(Emp_1.__repr__())
print(Emp_2.__str__())