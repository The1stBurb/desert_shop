from desert import (candy,iceCream,cookie,sunday)
# In Part 2, implement the ability to create an order consisting of items available at the Dessert Shop to what you already did in Part 1. These items include Candy, Cookies, Ice Cream and Sundaes. You will also implement a main function with a simple console user interface to interactively test the order entry system.
# Order Class
# The order class is a list-like container for DessertItem objects.
# The Order class has the following attribute and methods:
# order: list of DessertItem objects
# A constructor that creates an empty Order yugasdkjighdfga
# add() method that takes a single DessertItem argument and adds it to the order list sdfhdfgjggfj
# __len__() magic method that returns the number of items in the order gfjsfjgfj
# main() fgsjfjgfjg
# main should do the following:
# Create a new instance of the order class fsgjfgjgf s
# Add the following items to the order: fgsjfgsjsj

# Candy("Candy Corn", 1.5, .25)
# Candy("Gummy Bears", .25, .35)
# Cookie("Chocolate Chip", 6, 3.99)
# IceCream("Pistachio", 2, .79)
# Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
# Cookie("Oatmeal Raisin", 2, 3.45)
# Print out just the name of each DessertItem in the order rfksyk
# Print out the total number of items in the order ghfkdgkg
# The Order class is implemented as above. htdkd
# Program output looks exactly like the example run.
# You submit 3 code files in your Codio workspace: dessert.py, test_dessert.py dessertshop.py. test_dessert.py is carried forward from Part 1, but not modified.
items=[
    # candy("Candy Corn",0,0),
    # iceCream("Gummy Bears",0,0),
    # candy("Chocolate Chips",0,0),
    # sunday("Pistachio",0,0,"pistachios"),
    # iceCream("Vanilla",0,0),
    # cookie("Oatmeal Raisin",0,0),
    candy("Candy Corn", 1.5, .25),
    iceCream("Gummy Bears", .25, .35),
    candy("Chocolate Chips", 6, 3.99),
    sunday("Pistachio", 2, .79, "Hot Fudge", 1.29),
    iceCream("Vanilla", 3, .69),
    cookie("Oatmeal Raisin", 2, 3.45),
]
class order:
    def __init__(self):
        self.ord=[]
    def add(self,itm):
        # quan=input(f"How many {itm.nm}s would you like? ")
        # itm.quan=quan
        self.ord.append(itm)
    def __str__(self):
        return "\n".join([f"{i.nm}" for i in self.ord])+f"\nTotal number of items in the order: {len(self.ord)}"#{i.quan}x 
    def __len___(self):
        return len(self.ord)
ord=order()
# print(ord)
for i in items:
    ord.add(i)
# ord.add(items[3])
print(ord)