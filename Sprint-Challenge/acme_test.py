import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    #check that price is 10 and an int
    def test_default_product_price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertIsInstance(prod.price, int)
        
   #check that weight is 20 and an int
    def test_default_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
        self.assertIsInstance(prod.weight, int)
        
    #check that flammability is 0.5 and a float    
    def test_default_flammability(self):
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)
        self.assertIsInstance(prod.flammability, float)

    #Check stealability function at default, lower, boundary, and upper
    def test_steability(self):
        steal1 = Product('steal1', 10, 20)
        steal2 = Product('steal2', 5, 20)
        steal3 = Product('steal3', 20, 20)
        steal4 = Product('steal4', 21, 20)
        
        self.assertEqual(steal1.stealability(), "Kinda stealable.")
        self.assertEqual(steal2.stealability(), "Not so stealable...")
        self.assertEqual(steal3.stealability(), "Very stealable!")
        self.assertEqual(steal4.stealability(), "Very stealable!")
        
    #Check explode function at lower, default, middle, and boundary
    def test_explode(self):
        explode1 = Product('explode1', 0, 10, 0.5)
        explode2 = Product('explode2', 0, 20, 0.5)
        explode3 = Product('explode3', 0, 49, 1)
        explode4 = Product('explode4', 0, 50, 1)
        
        self.assertEqual(explode1.explode(), "...fizzle.")
        self.assertEqual(explode2.explode(), "...Boom!")
        self.assertEqual(explode3.explode(), "...Boom!")
        self.assertEqual(explode4.explode(), "...BABOOM!")


class AcmeReportTests(unittest.TestCase):
    
    #check that we generate 30 products
    def test_default_num_products(self):
        prod_list = generate_products()
        self.assertEqual(len(prod_list), 30)
    
    #check that we got 1 noun and 1 adjective for each name
    def test_legal_names(self):
        prod_list = generate_products()
        names = [prod.name for prod in prod_list]
        
        for name in names:
            self.assertEqual(name.count(' '), 1)
            self.assertEqual(len(name.split()), 2)
            self.assertIn(name.split()[0], ADJECTIVES)
            self.assertIn(name.split()[1], NOUNS)


if __name__ == '__main__':
    unittest.main()