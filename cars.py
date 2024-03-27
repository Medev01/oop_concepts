# Remind this : "Everything in Python is Object "
class Cars:
    cars_nums = 0

    @classmethod
    def show_cars_count(cls):
        print(f"we have {cls.cars_nums} cars in our stock")

    @staticmethod
    def sayHi():
        print("Hello guys")

    def __init__(self, name, model, color, speed):
        self.name = name
        self.model = model
        self.color = color
        self.speed = speed
        Cars.cars_nums += 1

    def show_info(self):
        return f"{self.name} {self.model} {self.color} {self.speed}"

    def car_speed(self):
        return self.speed * 12


# Create objects

car1 = Cars("clio", "2020", "red", 280)
car2 = Cars("Dacia", "2022", "gray", 300)
car3 = Cars("ford", "2019", "black", 460)
car4 = Cars("Mercedes", "2017", "white", 480)

# print(car1.show_info())
# print(Cars.show_info(car1))

print('-' * 50)
print(car1.show_info())
print(car4.show_info())
print(car1.car_speed())
print(car4.car_speed())
Cars.show_cars_count()
Cars.sayHi()
print(Cars.cars_nums)
