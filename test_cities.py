import unittest
from city_functions import get_name

class NameTestCase(unittest.TestCase):
    def test_city_country(self):
        name = get_name('santiago', 'chile')
        self.assertEqual(name, 'Santiago,Chile')
        
    def test_city_country_population(self):
        name = get_name('santiago', 'chile', 5000000)
        self.assertEqual(name, 'Santiago,Chile-Population 5000000')

unittest.main()
