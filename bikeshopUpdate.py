class BikeShop(object):
    """name, inventory of 6 bikes, sell bikes at 20% profit,
    can view profit made from sales"""
    
    def __init__(self, shopname):
        self.shopname = shopname
        self.profit = []
        self.inventory = {}
        

    def add_inventory(self, bike, count):
        if bike in self.inventory:
            old_count = self.inventory[bike]    #Retrieves bikes current count in inventory
            self.inventory[bike] = old_count + count    #adds count of bikes to the inventory if bikes already there
        elif bike not in self.inventory:
            self.inventory[bike] = count #Adds to inventory if bikes not there already
                  
    def bike_price(self, bike):
        if bike in self.inventory:
            adjusted_price =  bike.raw_cost() * 1.2
            return adjusted_price
        raise Exception ("Not in stock")

           
    def affordable_bikes(self, customer):
       potential_bikes = []
       for bike in self.inventory:
            bike_option = self.inventory[bike]
            if bike_option <= customer.customer_budget():
                potential_bikes.append(bike)
       print potential_bikes

       
    def bike_sold(self, bike):
        self.inventory[bike] -= 1
        raw_cost = bike.raw_cost()
        sale_profit = (raw_cost*1.2) - raw_cost
        self.profit.append(sale_profit)
        #print "We just made %s dollars on that deal!"%self.profit.pop()
        
    #def earnings_report(self):
        
        

          
           
class Bike(object):
    """Each bike has name, weight, raw cost"""
    
    def __init__(self, bikename, weight, rawcost):
        self.bikename = bikename
        self.weight = weight
        self.rawcost = rawcost
        
    def raw_cost(self):
        return self.rawcost

        
    def bike_weight(self):
        return self.weight
     
    def__str__(self):
        self.bikename
        
          

class Customer(object):
    """Have name, budget to buy bike, can buy new bike"""
    
    def __init__(self,customer, budget):
        self.budget = budget
        self.customer = customer
        
    def customer_budget(self):
        return self.budget
        
    def buy_bike(self, bike, bikeshop):
        purchased_bikes = []
        if bikeshop.bike_price(bike) <= self.budget:
            print "Great. You just got yourself a %s" %bike
            bikeshop.bike_sold(bike)
        else:
            print "You can't afford that bike!"
          
        
#First create 6 different bikes

via = BikeShop("Via")

binachi = Bike("binachi", 20, 500)
trekk = Bike("trekk", 30, 400)
GT = Bike("GT", 14, 700)
SE = Bike("SE", 23, 100)
haro = Bike("haro", 20, 300)
dyno = Bike("dyno", 10, 500)

via.add_inventory(trekk, 5)
via.add_inventory(GT,5)
via.add_inventory(SE,5)
via.add_inventory(haro,5)
via.add_inventory(dyno, 5)
via.add_inventory(binachi,5)

via.bike_price(binachi)

billy = Customer("billy", 500)
sean = Customer("sean", 200)
john = Customer("john", 1000)


via.affordable_bikes(billy)

billy.buy_bike(SE, via)
sean.buy_bike(SE, via)

via.earnings_report()
