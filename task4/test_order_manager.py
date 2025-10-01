import unittest
from order_manager import OrderManager

class TestOrderManager(unittest.TestCase):

    def setUp(self):
        self.manager = OrderManager()

    def test_add_valid_order(self):
        self.manager.add_order("A1", 100)
        self.assertEqual(self.manager.total_order_value(), 100)

    def test_add_order_invalid_id_type(self):
        with self.assertRaises(ValueError):
            self.manager.add_order(123, 50)   # keine str

    def test_add_order_empty_id(self):
        with self.assertRaises(ValueError):
            self.manager.add_order("   ", 50)  # nur Leerzeichen

    def test_add_order_invalid_value_type(self):
        with self.assertRaises(ValueError):
            self.manager.add_order("B1", "fifty")  # kein int/float

    def test_add_order_negative_value(self):
        with self.assertRaises(ValueError):
            self.manager.add_order("C1", -10)

    def test_add_order_duplicate_id(self):
        self.manager.add_order("D1", 20)
        with self.assertRaises(KeyError):
            self.manager.add_order("D1", 30)   # gleiche ID nochmal

    def test_total_order_value_multiple_orders(self):
        self.manager.add_order("E1", 10)
        self.manager.add_order("E2", 20)
        self.assertEqual(self.manager.total_order_value(), 30)

if __name__ == "__main__":
    unittest.main()