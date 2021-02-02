# Exception handling

# Reading:
"""
https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions
https://pymbook.readthedocs.io/en/latest/exceptions.html#exceptions
"""


# what's the problem here?
print(crocodile)

# what is the problem here?
result = 2 + '2'

# iterate over the list and print the half of every item
# if the item cannot be divided (due to TypeError), print "Not a number"
list_of_things = [2, 2, 'banana', 'superman', 30.0, 416]



# Object oriented programming basics

# let's say we want to work with superheroes.
# We can store their names in a list:
superheroes = [
    'Superman', 'Catwoman', 'Batman', 'Spiderman', 'Wonder Woman',
]

# What if we want to store more information about them?
# We could store it in a dictionary:
superheroes = {
    'Superman': {
        'legal name': 'Clark Kent',
        'powers': ['x-ray vision', 'flying', 'super strength'],
    },
    'Catwoman': {
        'legal name': 'Selina Kyle',
        'powers': ['speed', 'agility']
    },
    'Wonder Woman': {
        'legal name': 'Diana Prince',
        'powers': ['strength', 'speed', 'agility']
    }, 
    'Spiderman': {
        'legal name': 'Peter Parker',
        'powers': ['spider senses', 'spider webs'],
    },
    'Batman': {
        'legal name': 'Bruce Wayne',
        'powers': ['lots of money']
    }

}

# This is good but a bit clumsy.
# We can use classes and objects!


# this is a class
class SuperHero:
    # this is the "constructor" method - the __init__ method
    def __init__(self, name, powers, legal_name=None):
        self.name = name
        self.powers = powers
        self.legal_name = legal_name


    # this is an "instance method"
    def description(self):
        description = self.name + ' has the following powers: ' + ', '.join(self.powers)
        if self.legal_name is not None:
            description += ' and their legal name is ' + self.legal_name
            
        return description


superman = SuperHero('Superman', ['x-ray vision', 'flying', 'super strength'])



# https://realpython.com/python3-object-oriented-programming/