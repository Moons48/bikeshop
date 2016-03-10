  


        
  
class Bicycle():

    def __init__(self, name, weight, rawcost):
        self.name = name
        self.weight = weight
        self.rawcost = rawcost
        self.shop = Bike_Shop()
        

    def add_to_shop(self,  name, quantity, production_cost):
        self.shop.add_inventory(name, quantity, production_cost)
            
     
  
    
class Customers():
    def __init__(name, budget):
        self.name = name
        self.budget = budget
        
    
    
    def purchase_bike(self):
        

class Bike_Shop(object):

    def __init__(self, name = "Via"):
        self.name = name
        self.inventory = {}
        self.price = {}
        self.profit = profit
        
    def add_inventory(self, bikeName, count,  rawcost):
        
        if name in self.inventory:
            self.inventory[name] += count
        elif name not in self.inventory:
            self.inventory.setdefault(name, count)
        if name not in self.price:
            self.price[name] = rawcost+(rawcost*.2)
            
    def affordable_bikes(self, ):
    
shop = Bike_Shop()
newbike1 = shop.add_inventory("binachi",10, 200)


