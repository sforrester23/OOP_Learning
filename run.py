from Animal_Class import *
from Reptile_Class import *

# Let's create an object of class animal
    # Initializing an object

# my_animal = Animal('Guadelupe') # This is where we created an instance of class Animal
#
# print(my_animal)
# print(type(my_animal))
#
# print(my_animal.eat('Lasagne'))
# print(my_animal.sleep())
# print(my_animal.potty())
#
# print(my_animal.name)
#
# my_animal_2 = Animal('Geraldine')
# print(my_animal_2.eat('Lasagne'))
# print(my_animal_2.sleep())
# print(my_animal_2.potty())
#
# print(my_animal_2.name)
#
# my_animal_2 = Animal('Frank', 3)
# print(my_animal_2)

my_animal_3 = Animal('Ignacio', 1, 45)
# print(my_animal_3.name)
# print(my_animal_3.number_eyes)
# print(my_animal_3.number_animals_eaten)
# print(my_animal_3.eat('Swaghetti Yolonese'))
# print(my_animal_3.sleep())
# print(my_animal_3.potty())

my_reptile = Reptile('Sergio', 1 , 45, 3, True)
print('My Reptile:')
print(my_reptile)

print('Reptile name')
print(my_reptile.name)

print('what is the type of my_animal_3?')
print(type(my_animal_3))
print('what is the type of my_reptile? ')
print(type(my_reptile))

print('How does my animal eat & sleep?')
print(my_animal_3.eat())
print(my_animal_3.sleep())

print('How does my reptile eat & sleep?')
print(my_reptile.eat('crickets'))
print(my_reptile.sleep())

print('What does my reptile do differently from humans')
print(my_reptile.seek_heat())
print('Can my human seek heat? (NO)')
# print(my_animal_3.seek_heat())  ## this breaks the run code

print('Does {} have camouflage?: '.format(my_reptile.name))
print(my_reptile.camouflage)
print('How many hearts does {} have?: '.format(my_reptile.name))
print(my_reptile.number_hearts)

