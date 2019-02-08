# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "ShopBlop"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    for i in stores:
        print(i)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for i in stores:
        if store_name.capitalize() == i.name:
            return i.name
    else:
        return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    store_input = input('Pick a store by typing its name. Or type "checkout" to pay your bills and say your goodbyes.')
    if store_input.lower() == "checkout":
        x = Cart()
        print(x.checkout())
            
    elif get_store(store_input):
        return get_store(store_input)
            
    else: 
        print("No store with that name. Please try again.") 
        print(pick_store())

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    picked_store.print_products()
    product_input = input("What items would you like to add to your cart?. Type \"back\" to head back to the main menu")
    
    while product_input.lower() != "back":
        for i in picked_store.products:
            if product_input == i.name:
                cart.add_to_cart(product)
        print(product_input )    

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    i =pick_store()
    pick_products(cart, i)
    cart.checkout()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)

