# Name
# Gender
# Breed
# Age

class Dog:

    def __init__(self, name, gender, breed, age):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.age = age
        self.is_dead = False
    
    def roll_over(self):
        print(f"{self.name} rolls over!")

    def lay_down(self):
        print(f"{self.name} lays down.")

    def catch_ball(self, ball):
        print(f"{self.name} catches a {ball}")

    def eat(self, food):
        print(f"{self.name} eats {food}")
    
    def drink(self, liquid):
        print(f"{self.name} drinks {liquid}")

    def maul(self, object):
        print(f"{self.name} mauls {object}")
    
    def die(self, reason):
        print(f"{self.name} died due to {reason}")
        self.is_dead = True
    
    def __str__(self):
        if self.gender == "F":
            return f"{self.name} is a female {self.breed} that is {self.age} years old."
        else:
            return f"{self.name} is a male {self.breed} that is {self.age} years old."

my_dog = Dog("Coconut", "F", "Shiba-Inu", 696969696969696969)
print(my_dog)
my_dog.catch_ball("tennis ball")
my_dog.roll_over()
my_dog.die("COVID-20")

daniel = Dog("Daniel", "F", "Bulldog", 0)
daniel.die("bombing")

