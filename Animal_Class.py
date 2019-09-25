class Animal():

    # Characteristics
    def __init__(self, name, eyes, num_eaten = 60): # runs only once when intialize an object
        self.name = name
        self.number_eyes = eyes
        self.alive = True
        self.number_animals_eaten = num_eaten
        self.age = 0
        self.intelligence = 20



    # Defining Behaviours: functions that belong to a class
    # Methods - functions that can only be used on this class' instance
    def eat(self, food= 'Fajitas'): # optional argument
        return 'NOM NOM NOM ' + food

    def sleep(self):
        return 'ZZZZZeetZZZZ'

    def hunt(self):
        return 'AAAAATTTACCCCKKKK!'

    def potty(self):
        return 'O_O ... HNNN o_O --- HUUUHHH!! O_O SPLOSH! -.- :D'

    def rave(self):
        return 'Mmmst MMMST MMMST MMMMST MMMMST'
