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


# another approach is to create a Fight class:
class Fight:
    def __init__(self, player_one, player_two):
        self.p1 = player_one
        self.p2 = player_two
        self.has_ended = False
        self.result = None

    def start(self):
        if self.has_ended:
            print('This fight is over. If you want to fight again, start a new fight!')
            return

        def check_if_sick():
            result = False
            if self.p1.life <= self.p1.max_life//5:
                print(f'They will not fight - {self.p1.name} is sick')
                result = True
            elif self.p2.life <= self.p2.max_life//5:
                print(f'They will not fight - {self.p2.name} is sick')
                result = True
            if result is True:
                print('They will have to go to the hospital 🏥 🚑 👩‍⚕️')

            return result
            
        is_anyone_sick = check_if_sick()

        if is_anyone_sick:
            return

        print(f'Friendly fight: {self.p1.name} VS {self.p2.name}')
        print('-------------')

        if self.p1.strength > self.p2.strength:
            self.p2.life //= 2
            self.result = f"{self.p1.name} has beaten {self.p2.name} 💥"

        elif self.p1.strength < self.p2.strength:
            self.p1.life //= 2
            self.result = f"{self.p2.name} has beaten {self.p1.name} 💥"
        self.has_ended = True

        print(self.result)
        self.print_health_points()

    def print_health_points(self):
        print(f'{self.p1.name} has {self.p1.life} health points left')
        print(f"{self.p1.life * '💚'} {(self.p1.max_life - self.p1.life) * '💔'}")
        print()
        print(f'{self.p2.name} has {self.p2.life} health points left')
        print(f"{self.p2.life * '💚'} {(self.p2.max_life - self.p2.life) * '💔'}")



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
