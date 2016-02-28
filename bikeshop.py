"""
Build a system that models bycicle industry.

    bikes with fixed cost to produce
    shops that sell bikes with added margin on top
    customers with varied budgets to buy bikes
    """
""" So you add the variables formed in the class to the other classes() and create attributes within those classes
        based on the variables"""
""" You need the shop instances to record the purchases and sales of each 
    customer and log them"""

class Bicycle():
    
    def __init__(self, model):
        self.model = model
        self.weight = 0
        self.cost = 0
        
    def bikeWeight(self):
        """shows the weight of the bycicles"""
        rawWeight = {
            "GT" : 25,
            "schwin": 10,
            "dyno": 13,
            "trekk": 60,
            "SE": 35,
            "binachi": 18,
        }
        
        self.weight =  rawWeight[self.model]
        print "A %s weighs %s" %(self.model, self.weight)
        
    def productionCost(self):
        rawCost = {
            "GT" : 100,
            "schwin": 200,
            "dyno": 350,
            "trekk": 550,
            "SE": 750,
            "binachi": 1000,
        }
        self.cost = rawCost[self.model]
        print "A %s costs %s to produce" %(self.model, self.cost)
        
        
class Customers():
    
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def customerBudget(self):
        print "Your budget is %s"%self.budget
        
    def customerName(self):
        print "Your name is %s" %self.name
        
    def remainingBudget(self, price):
        remaining = self.budget - price
        print remaining
        
    

class Shop():
    
    def __init__(self, name, rawCost, stock):
        self.name = name
        self.profit = 0
        self.stock = stock
        self.markup = .2
        self.retail = {}
        self.rawCost = rawCost
        
    def shopID(self):
        print "Your shop's named %s" %self.name

        
    def backroom(self):
        print "Here is our backroom"
        for k, v in self.stock.items():
            print k + " : " + str(v)

            
    def menu(self, budget):
        print "Your budget is %s.\nLets see what we have in that price range"%budget
        for k,v in self.rawCost.items():
            self.retail.setdefault(k, self.rawCost[k] + (self.rawCost[k]*.2))
        for k, v in self.retail.items():
            if self.retail[k] <= budget:
                print k +"\t"+str(int(v))

                
    def purchased(self, model):
        print "You bought a %s"%model
        self.profit += self.retail[model] - self.rawCost[model]
        self.stock[model] -=1
        return self.retail[model]
        

    def status(self):
        print "Total profits:\t%s" %self.profit
        for k, v in self.stock.items():
            print k+" : "+ str(v)
        
