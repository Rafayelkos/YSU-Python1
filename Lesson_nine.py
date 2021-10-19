"""class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def  getDesc(self):
        print(f"A {self.color} with radius {self.radius}")    



my_obj = Circle(4, "red")

my_obj.getDesc()

class Car:
    def __init__(self,model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed

    def compareCar(self,car2):
        if self.max_speed > car2.max_speed:
            return "car2 is better than car1"
        return   "car1 is better than car2"



new_obj = Car("Mercedess", "Red", 220)

new_obj2 = Car("Audio", "White", 20)
print(new_obj2.compareCar(new_obj))
"""

class Person:
    def __init__(self, name, last_name, age, gender, student:bool, password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password

    def Greeting(self, second_person):
        return f"Welcome dear {second_person.name}"  

    def Goodbye(self):
        return f"Bye Everyone"   

    def Favorite_num(self, num1):
        return f'my favorite number is {num1}' 

    def Read_file(self, filename):
        with open (filename, 'r') as f:
            return f
        

my_person_one = Person("Rafayel","Kosyan", 33, "male", True, 7788)
my_second_person = Person("Armen","Hakobyan", 53, "Male", False, 8877)

print(my_person_one.Greeting(my_second_person))







