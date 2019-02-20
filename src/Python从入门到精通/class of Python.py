##python3 面向对象

#编写一个小狗类
class Dog():
    def __init__ (self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+" now is sitting")

    def roll_over(self):
        print(self.name.title()+" now rolled over")




my_dog = Dog("sa",2)

my_dog.roll_over()
my_dog.sit()


# 定义一个父类car
class Car():
    def __init__(self):
        self.age = 0

    def print_message(self):
        print("I am a car")

#定义了一个ElectricCar 继承Car
class ElectricCar(Car):
    def __init__(self):
        #调用父类的构造函数
        super().__init__()

    def print_message(self):
        print("I am an ElectricCar")


my_Car = ElectricCar()
my_Car.print_message()


