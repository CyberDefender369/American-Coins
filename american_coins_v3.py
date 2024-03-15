import random

#creating coin parent class
class Coin():
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): #adds kw arguments from child classes
            setattr(self, key, value)
            
    def __del__(self):
        print("Coin spent!")
        
    def __str__(self):
        if self.value >= 1:
            return "${} Coin".format(int(self.value))
        else:
            return "{} Cent Coin".format(int(self.value * 100))
 
#penny child class
class Penny(Coin):
    def __init__(self):
        specifications = {
            "value": 0.01,
            "color": "Bronze",
            "edge": "Plain",
            "composition": "Copper Plated Zinc",
            "diameter": 19.05, #mm
            "thickness": 1.52, #mm
            "num_of_reeds": "N/A",
            "weight": 2.500 #g
            }
        super().__init__(**specifications) #referring to parent class
        
#nickel child class
class Nickel(Coin):
    def __init__(self):
        specifications = {
            "value": 0.05,
            "color": "Silver",
            "edge": "Plain",
            "composition": "Cupro-Nickel",
            "diameter": 21.21, #mm
            "thickness": 1.95, #mm
            "num_of_reeds": "N/A",
            "weight": 5.000 #g
            }
        super().__init__(**specifications) #referring to parent class
        
#dime child class
class Dime(Coin):
    def __init__(self):
        specifications = {
            "value": 0.10,
            "color": "Silver",
            "edge": "Reeded",
            "composition": "Cupro-Nickel",
            "diameter": 17.91, #mm
            "thickness": 1.35, #mm
            "num_of_reeds": 118,
            "weight": 2.268 #g
            }
        super().__init__(**specifications) #referring to parent class
        
#quarter child class
class Quarter_Dollar(Coin):
    def __init__(self):
        specifications = {
            "value": 0.25,
            "color": "Silver",
            "edge": "Reeded",
            "composition": "Cupro-Nickel",
            "diameter": 24.26, #mm
            "thickness": 1.75, #mm
            "num_of_reeds": 119,
           "weight": 5.670 #g
            }
        super().__init__(**specifications) #referring to parent class
        
#half dollar child class
class Half_Dollar(Coin):
    def __init__(self):
        specifications = {
            "value": 0.50,
            "color": "Silver",
            "edge": "Reeded",
            "composition": "Cupro-Nickel",
            "diameter": 30.61, #mm
            "thickness": 2.15, #mm
            "num_of_reeds": 150,
            "weight": 11.340 #g
            }
        super().__init__(**specifications) #referring to parent class

#dollar child class
class Dollar(Coin):
    def __init__(self):
        specifications = {
            "value": 1.00,
            "color": "Gold",
            "edge": "Edge-Lettering",
            "composition": "Manganese-Brass",
            "diameter": 26.49, #mm
            "thickness": 2.00, #mm
            "num_of_reeds": "N/A",
            "weight": 8.100 #g
            }
        super().__init__(**specifications) #referring to parent class

#list of all coin child classes        
coins = [
    Penny(), Nickel(), Dime(),
    Quarter_Dollar(), Half_Dollar(), Dollar()
    ]

coin_row = []

#iterate through all coin child class keyword values
for coin in coins:
    arguments = [
        coin, coin.value, coin.color, coin.edge,
        coin.composition, coin.diameter, coin.thickness,
        coin.num_of_reeds, coin.weight
        ]

    string = ("{} | Value: {:.2f} | Color: {} | Edge: {} | Composition: {}\n" 
              "Diameter(mm): {} | Thickness(mm): {:.2f} | Number of Reeds: {} |"
              " Weight(g): {:.3f}".format(*arguments))
    
    coin_row.append(string)
    
options = {
    "penny": coin_row[0],
    "nickel": coin_row[1],
    "dime": coin_row[2],
    "quarter": coin_row[3],
    "half dollar": coin_row[4],
    "dollar": coin_row[-1],
    }

print("Welcome to the coin shop, we help you find the specifications of "
      "all American coins.")
print("------------------------------------------------------------------------"
      "------------\n")

user_input = input("Which American coin specification do you need?: ").lower()
print()

if user_input in options:
    print(options[user_input])
else:
    print("Sorry, that's not an option.")