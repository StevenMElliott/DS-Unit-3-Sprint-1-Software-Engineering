from random import randint, sample, uniform
from acme import Product

#Name Generator
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        #Name(adj 'space' noun), price, weight, flammability,
        products.append(Product(sample(ADJECTIVES, 1)[0]+ ' ' + sample(NOUNS, 1)[0],
                               randint(5,100),
                               randint(5,100),
                               uniform(0,2.5)))
    return products


def inventory_report(products):
    #specs
    name = [prod.name for prod in products]
    price = [prod.price for prod in products]
    weight = [prod.weight for prod in products]
    flame = [prod.flammability for prod in products]
    
    #calculate
    unique = len(set(name))
    avg_price = sum(price)/len(price)
    avg_weight = sum(weight)/len(weight)
    avg_flame = sum(flame)/len(flame)
    
    #generate report
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique Product Lines: {}'.format(unique))
    print("Average Price: {}".format(avg_price))
    print("Average Weight: {}".format(avg_weight))
    print("Average Flammability: {}".format(avg_flame))
    
    pass  


if __name__ == '__main__':
    inventory_report(generate_products())