import unittest
import src.shopcart as sc

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("* setUp()")
        self.scart = sc.ShoppingCart()
        self.scart.add_product("Mąka",4,2)


    def test_add_product(self):
        print("** add_product()")
        result = self.scart.add_product("Mleko",2,5)
        self.assertEqual(result, True)
        pass

    def test_remove_product(self):
        print("** remove_product()")
        result = self.scart.remove_product("Mleko")
        self.assertEqual(result, True)
        pass

    def test_update_quantity(self):
        print("** update_quantity()")
        result = self.scart.update_quantity("Mąka",1)
        self.assertEqual(result, True)
        pass

    def test_get_products(self):
        print("** get_products()")
        with self.assertRaises(ValueError):
            self.scart.get_products()
        pass

    def test_count_products(self):
        print("** count_products()")
        result = self.scart.count_products()
        self.assertEqual(result, 2)
        pass

    def test_get_total_price(self):
        print("** get_total_price()")
        result = self.scart.get_total_price()
        self.assertEqual(result, 8)
        pass

    def test_apply_discount_code(self):
        print("** apply_discount_code()")
        result = self.scart.apply_discount_code("SAVE10")
        self.assertEqual(result, True)
        pass

    def test_checkout(self):
        print("** checkout()")
        result = self.scart.checkout()
        self.assertEqual(result, True)
        pass

if __name__ == '__main__':
    unittest.main()
