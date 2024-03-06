from cartePizzeriaException import CartePizzeriaException
import pizza

class CartePizzeria:
    def __init__(self):
        self.pizzas = []

    def is_empty(self):
        return len(self.pizzas) == 0

    def nb_pizzas(self):
        return len(self.pizzas)

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException(f"La pizza {name} n'existe pas dans la carte.")
    
    
# Création de quelques pizzas
pizza_margarita = pizza("Margarita", ["tomato sauce", "mozzarella", "basil"], 10.99)
pizza_pepperoni = pizza("Pepperoni", ["tomato sauce", "mozzarella", "pepperoni"], 12.99)

# Création de la carte de la pizzeria
carte_pizzeria = CartePizzeria()

# Ajout de pizzas à la carte
carte_pizzeria.add_pizza(pizza_margarita)
carte_pizzeria.add_pizza(pizza_pepperoni)

# Affichage du nombre de pizzas dans la carte
print("Nombre de pizzas dans la carte:", carte_pizzeria.nb_pizzas())

# Suppression d'une pizza de la carte
carte_pizzeria.remove_pizza("Margarita")

# Affichage mis à jour du nombre de pizzas dans la carte
print("Nombre de pizzas dans la carte après suppression:", carte_pizzeria.nb_pizzas())

# Tentative de suppression d'une pizza inexistante (va lever une exception)
try:
    carte_pizzeria.remove_pizza("Quattro Formaggi")
except CartePizzeriaException as e:
    print(f"Erreur: {e}")
