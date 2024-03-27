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

    @classmethod
    def fromstring(cls, str_):
        first, last, salary = str_.split('-')
        return cls(first, last, salary)
    
     
class Developer(Employee):
    def __init__(self,first,last,salary,prog_lang):
        super().__init__(first,last,salary)
        self.prog_lang = prog_lang

    

class Manager(Employee):
    def __init__(self, first, last, salary, employees = None):
        super().__init__(first,last,salary)
        if self.employees is None:
           self.employees = []
        else :
            self.employees = employees 

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.personnal_info())


dev_1 = Developer('Mohmaed', 'Ouahlou', 105000, 'Python')
print(dev_1.generate_email())

emp_str = 'mohamed-ouahlou-230000'
Emp_1 = Employee('Mohamed', 'Ouahlou', 105000)
Emp_2 = Employee('Alex', 'Martinz', 12500)
new_emp = Employee.fromstring(emp_str)




mgr_1 = Manager('Susi','alina',9000, [Emp_1])
mgr_1.print_emps()
# print(new_emp.generate_email())
# print(Employee.raise_amount)
# print(Emp_1.generate_email())
# print(Emp_2.generate_email())
# print(help(Developer))

  
