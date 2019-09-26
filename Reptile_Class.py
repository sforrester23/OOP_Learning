from Animal_Class import *
#
class Reptile(Animal): # Inheritance
    # This adds parameters (characteristics) from the parent class and adds more needed for this sub-class
    def __init__(self, name, eyes, number_hearts, camouflage, num_eaten = 60): #define the same parametes and the new ones
        super().__init__(name, eyes, num_eaten) #super overrides it. define the same arguments as before to override them
        self.number_hearts = number_hearts #add new parameters
        self.camouflage = camouflage
        # This method above overrides the previous init method from the parent class.
        # The super call to the previous init method does have all of the previous characteristics
        # THEN: We add extra characteristics for the subclass of reptiles that the parent class doesn't have

    def eat(self, food = 'Fajitas'):
        return ('Wait foooooor iiiit.... waaaiiiiit...... AND POUNCE! ' + food)

    # Adding new methods (behaviours) to this class that the parent class doesn't have
    # Using POLYMORPHISM
    def seek_heat(self):
        return ('Hmmm bit chilly, where that sun at? Why did I sit at the back of the class...')





