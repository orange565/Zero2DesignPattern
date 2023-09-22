import animals.cats as ct
import animals.dogs as dg


my_dog = dg.Dog("Karabas",2)
print(f"{my_dog.name} is {my_dog.age} years old")
my_dog.bark()

my_cat = ct.Cat("Duman",3)
print(f"{my_cat.name} is {my_cat.age} years old")
my_cat.meow()
