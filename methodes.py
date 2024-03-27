class FactoryCake:
    num_cake = 0

    @classmethod
    def show_num_of_cakes(cls):
        print(f'Number of Cakes: {cls.num_cake}')

    def __init__(self, Cake: str, size: str, ingredients: list, price : float):
        self.cake = Cake
        self.size = size 
        self.ingredients = ingredients
        self.price = price 
        FactoryCake.num_cake += 1

    
    def change_price(self):
        if 'chocolate' in self.ingredients:
            self.price += 4
        elif 'vanilla' in self.ingredients:
            self.price += 2
        else:
            self.price += 0
        
    def print_cake(self):
        print(f'''
                  Cake : {self.cake}
                  size : {self.size}
                  Ingredients : {self.ingredients}
                  Price : {self.price}
            ''')
        


cake1 = FactoryCake('FreshCake', 'medium', ['Banana', 'Oil','Sugar','4 Eggs','chocolate'],19.65)
cake2 = FactoryCake('QueenCake', 'large', ['vanilla', 'Oil','Sugar','4 Eggs','chocolate'],20.99)

cake1.print_cake()
cake1.change_price()
print(cake1.price)
FactoryCake.show_num_of_cakes()



