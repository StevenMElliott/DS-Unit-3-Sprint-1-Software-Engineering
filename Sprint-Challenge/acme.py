from random import randint

class Product:

    #default values for the product
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)
    
    #How stealable is the product?
    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return 'Not so stealable...'
        elif ratio >= 0.5 and ratio < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'
        
    #How will this product explode    
    def explode(self):
        ratio = self.flammability * self.weight
        if ratio < 10:
            return '...fizzle.'
        elif ratio >= 10 and ratio < 50:
            return '...Boom!'
        else:
            return '...BABOOM!'
        
class BoxingGlove(Product):
    
    #default values for boxingglove
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)
    
    #always a glove
    def explode(self):
            return "...it's a glove."
    
    #punch strength
    #quit hitting yourself
    def punch(self):
        weight = self.weight
        if weight < 5:
            return "That tickles."
        elif weight >= 5 and weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'    