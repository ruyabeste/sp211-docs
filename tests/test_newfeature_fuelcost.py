import unittest
from sp211.new_feature import calculate_fuel_cost

class TestCalculateFuelCost(unittest.TestCase):
    def test_default_fuel_cost(self):
        # Default consumption: 6.5L/100km, Price: 44.90TL/L, Distance: 100km
        expected = (100 / 100) * 6.5 * 44.90
        cost = calculate_fuel_cost(100)
        self.assertAlmostEqual(cost, expected, places=2)

    def test_custom_fuel_cost(self):
        expected = (250 / 100) * 5.0 * 40.0
        cost = calculate_fuel_cost(250, consumption_l_per_100km=5.0, fuel_price_per_liter=40.0)
        self.assertAlmostEqual(cost, expected, places=2)

if __name__ == '__main__':
    unittest.main()