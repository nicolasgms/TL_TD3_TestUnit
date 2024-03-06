import unittest
from unittest.mock import Mock
from pizza import Pizza
from cartePizzeria import CartePizzeria
from cartePizzeriaException import CartePizzeriaException


class TestCartePizzeria(unittest.TestCase):
    def test_is_empty(self):
        crt_pizzeria = CartePizzeria()
        self.assertTrue(crt_pizzeria.is_empty())

        pizza_mock = Mock()
        crt_pizzeria.add_pizza(pizza_mock)
        self.assertFalse(crt_pizzeria.is_empty())
        
    def test_add_pizza(self):
            crt_pizzeria = CartePizzeria()
            pizza_mock = Mock()

            crt_pizzeria.add_pizza(pizza_mock)
            self.assertEqual(crt_pizzeria.nb_pizzas(), 1)
            self.assertIn(pizza_mock, crt_pizzeria.pizzas) 
            
    def test_nb_pizzas(self):
        crt_pizzeria = CartePizzeria()
        self.assertEqual(crt_pizzeria.nb_pizzas(), 0)

        pizza_mock1 = Mock()
        pizza_mock2 = Mock()
        crt_pizzeria.add_pizza(pizza_mock1)
        crt_pizzeria.add_pizza(pizza_mock2)
        # verifie si le nb de pizza est bien egal à 2
        self.assertEqual(crt_pizzeria.nb_pizzas(), 2)
         
    def test_remove_pizza(self):
            crt_pizzeria = CartePizzeria()
            pizza1 = Pizza("Pizza1", ["tomate, fromage"], 5)

            crt_pizzeria.add_pizza(pizza1)

            # on retire une pizza qui existe
            crt_pizzeria.remove_pizza("Pizza1")
            self.assertEqual(crt_pizzeria.nb_pizzas(), 0)
            self.assertNotIn(pizza1, crt_pizzeria.pizzas)

            # on retire une pizza qui n'existe pas
            with self.assertRaises(CartePizzeriaException):
                crt_pizzeria.remove_pizza("Pizza2")
                
if __name__ == '__main__':
    unittest.main()
