from random import randint

class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)
        
    def stealability(self, price=10, weight=20):
        price = self.price
        weight = self.weight
        ratio = price / weight
        if ratio < 0.5:
            return 'Not so stealable...'
        elif ratio >= 0.5 and ratio < 1:
            return 'Kinda stealable'
        else:
            return 'Very stealable!'
        
    def explode(self, flammability=0.5, weight=20):
        flammability = self.flammability
        weight = self.weight
        ratio = flammability * weight
        if ratio < 10:
            return '...fizzle.'
        elif ratio >= 10 and ratio < 50:
            return '...Boom!'
        else:
            return '...BABOOM!'
        
class BoxingGlove(Product):
    
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)
    
    def explode(self):
            return "...it's a glove."
    
    def punch(self, weight=10):
        weight = self.weight
        if weight < 5:
            return "That tickles."
        elif weight >= 5 and weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
    