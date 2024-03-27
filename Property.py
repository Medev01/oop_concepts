class Human:
    def __init__(self, first, last):
        self.first = first 
        self.last = last 
        
    @property
    def email(self):
        return f"{self.first}_{self.last}.@email.com"
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        if name is None:
            raise ValueError('must enter right name !!')
        else :
            first, last = name.split(" ")
            self.first = first
            self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete full name !!')
        self.first = None
        self.last = None


Human1 = Human('mohamed','medo')
Human2 = Human('Douaa','Doua')

print(Human1.email)
print(Human1.first)
Human1.fullname = 'Aya hamdi'
print(Human1.email)
print(Human1.fullname)
print(Human1.last)
del Human2.fullname
    