import bikeshop

rawCost = {
            "GT" : 100,
            "schwin": 200,
            "dyno": 350,
            "trekk": 550,
            "SE": 750,
            "binachi": 1000,
        }

stock = {
            "GT" : 9,
            "schwin": 21,
            "dyno": 7,
            "trekk": 10,
            "SE": 8,
            "binachi": 5,
        }

name = "John"
budget = 500
customer1 = bikeshop.Customers(name, budget)
customer1.customerName()
customer1.customerBudget()

shopname = "Via"

shop1 = bikeshop.Shop(shopname, rawCost, stock )
shop1.backroom()
shop1.menu(budget)
selected = "dyno"

remaining budget = 
shop1.purchased(selected)
shop1.status()


name = "Bobby"
budget = 500
customer2 = bikeshop.Customers(name, budget)
customer2.customerName()
customer2.customerBudget()