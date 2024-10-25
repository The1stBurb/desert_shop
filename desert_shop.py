# In Part 2, implement the ability to create an order consisting of items available at the Dessert Shop to what you already did in Part 1. These items include Candy, Cookies, Ice Cream and Sundaes. You will also implement a main function with a simple console user interface to interactively test the order entry system.
# Order Class
# The order class is a list-like container for DessertItem objects.
# The Order class has the following attribute and methods:
# order: list of DessertItem objects
# A constructor that creates an empty Order
# add() method that takes a single DessertItem argument and adds it to the order list
# __len__() magic method that returns the number of items in the order
# main()
# main should do the following:
# Create a new instance of the order class
# Add the following items to the order:

# Candy("Candy Corn", 1.5, .25)
# Candy("Gummy Bears", .25, .35)
# Cookie("Chocolate Chip", 6, 3.99)
# IceCream("Pistachio", 2, .79)
# Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
# Cookie("Oatmeal Raisin", 2, 3.45)
# Print out just the name of each DessertItem in the order
# Print out the total number of items in the order
# The Order class is implemented as above.
# Program output looks exactly like the example run.
# You submit 3 code files in your Codio workspace: dessert.py, test_dessert.py dessertshop.py. test_dessert.py is carried forward from Part 1, but not modified.