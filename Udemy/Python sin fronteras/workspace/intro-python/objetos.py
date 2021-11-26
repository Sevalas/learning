class User:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def greeting(self):
        print('hi, my name is '+self.name,self.lastName)

class Admin(User):
    def superGreeting(self):
        print('hi, my name is '+self.name,self.lastName+', i\'m a admin')

# user1 = User('Carl','Jhonson')
# user2 = User('Mario','Bros')

# user1.greeting()

# user2.name = 'Luigi'

# user2.greeting()

# admin = Admin('Mike','Tyson')

# admin.superGreeting()

class Pet:
    def __init__(self, name, onomatopeia):
        self.name = name
        self.onomatopeia = onomatopeia

    def greeting(self):
        print('hi, i\'m a '+self.race+' named '+self.name+' and a say '+self.onomatopeia)

class Cat(Pet):
    race = 'cat'
    def __init__(self, name, onomatopeia):
        Pet.__init__(self, name, onomatopeia)
        print('i\'m a extended cat')

class Dog(Pet):
    race = 'dog'
    def __init__(self, name, onomatopeia):
        super().__init__(name, onomatopeia)
        print('i\'m a extended dog')

class Chicken(Pet):
    race = 'pio'

cat = Cat('Lola','miau')
dog = Dog('Kruk','wouf')
chicken = Chicken('Elma','pio')

cat.greeting()
dog.greeting()
chicken.greeting()