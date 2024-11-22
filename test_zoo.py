import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
    
    def test_negative_age(self):
        """Test case for C1b1: age < 0"""
        with self.assertRaises(ValueError):
            self.zoo.get_ticket_price(-1)
    
    def test_child_ticket(self):
        """Test case for C1b2: 0 <= age <= 12"""
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
    
    def test_teen_ticket(self):
        """Test case for C1b3: 13 <= age <= 20"""
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
    
    def test_adult_ticket(self):
        """Test case for C1b4: 21 <= age <= 60"""
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    
    def test_elder_ticket(self):
        """Test case for C1b5: age > 60"""
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
    
    def test_zero_age(self):
        """Test boundary case: age = 0"""
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    
    def test_twenty_age(self):
        """Test boundary case: age = 20"""
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    
    def test_sixty_age(self):
        """Test boundary case: age = 60"""
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

if __name__ == '__main__':
    unittest.main()