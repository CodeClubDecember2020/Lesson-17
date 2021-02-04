# Exception handling

# Reading:
"""
https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions
https://pymbook.readthedocs.io/en/latest/exceptions.html#exceptions
"""


# what's the problem here?
print('crocodile')

# what is the problem here?
result = 2 + 2


# Exceptions can happen at any place in our code, not just where we expect them.
# Sometimes, they are expected, sometimes, they 

# iterate over the list and print the half of every item
# if the item cannot be divided (due to TypeError), print "Not a number"
list_of_things = [2, 2, 'banana', 'superman', 30.0, 416]

for item in list_of_things:
    if type(item) == str:
        print('Not a number!')
    else:
        print(item / 2)

for item in list_of_things:
    try:
        print(item / 2)
    except:
        print('Not a number!')

for item in list_of_things:
    try:
        print(item / 2)
    except TypeError:
        print('Not a number!')

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
    def __init__(self, name, powers, strength, legal_name=None):
        self.name = name
        self.powers = powers
        self.legal_name = legal_name
        self.strength = strength
        self.life = 20
        self.max_life = 20

        self.description = self.name + ' has the following powers: ' + ', '.join(self.powers)
        if self.legal_name is not None:
            self.description += ' and their legal name is ' + self.legal_name

    # this is an "instance method"
    def get_description(self):
        return self.description

    def speak(self):
        pass

    def fight(self, other):

        def check_if_sick(self, other):
            result = False
            if self.life <= self.max_life//5:
                print(f'They will not fight - {self.name} is sick')
                result = True
            elif other.life <= other.max_life//5:
                print(f'They will not fight - {other.name} is sick')
                result = True
            if result is True:
                print('They will have to go to the hospital 🏥 🚑 👩‍⚕️')

            return result
            
        is_anyone_sick = check_if_sick(self, other)

        if is_anyone_sick:
            return

        print(f'Friendly fight: {self.name} VS {other.name}')
        print('-------------')

        if other.strength > self.strength:
            self.life //= 2
            print(f'Result: {self.name} was beaten by {other.name} 💥')

        elif other.strength < self.strength:
            print(f'{self.name} has beaten {other.name} 💥')
            other.life //= 2

        print(f'{self.name} has {self.life} health points left')
        print(f"{self.life * '💚'}")
        print()
        print(f'{other.name} has {other.life} health points left')
        print(f"{other.life * '💚'}")


# another approach is to create a Fight class:
class Fight:
    def __init__(self, player_one, player_two):
        self.p1 = player_one
        self.p2 = player_two

    def start(self):
        self.p1.fight(self.p2)


# a class can inherit from another class:
# in this case, the DCSuperHero class inherits from the SuperHero class
class DCSuperHero(SuperHero):
    def get_description(self):
        return self.description + ' and they are part of the DC universe'

superman = DCSuperHero('Superman', strength=93, powers=['x-ray vision', 'flying', 'super strength'])
batman = DCSuperHero('Batman', strength=85, powers=['lots of money'])
catwoman = DCSuperHero('Catwoman', strength=88, powers=['speed', 'agility'])
robin = DCSuperHero('Robin', strength=75, powers=['agility'])


# https://realpython.com/python3-object-oriented-programming/
