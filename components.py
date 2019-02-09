# CLASSES AND METHODS
class Store():
    
    
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name= name
        self.products= []
        
        

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        for i in self.products:
            print(i)


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return "Product Name: %s \nProduct Description: %s \nPrice: %s SAR " %(self.name, self.description,self.price)


    
class Cart():
        
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        self.cart= []

    def add_to_cart(self, product): #product object
        """
        Adds a product to this cart.
        """
        self.cart.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        price = 0
        for i in self.cart:
            price += i.price
        return price

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        print("Thank you for shopping with us. \nThis is the final step before checking out.\n\nOrder summary:")
        for i in self.products:
            print(i)
        print("The total is: %s") %(self.get_total_price())
        
    def checkout(self):
        """
        Does the checkout.
        """
        while True:
            confirm= input("Would you like to confirm your order? Yes or No? ")
            if confirm.lower() == "yes":
                print("Your order has been confirmed")
                break
            elif confirm.lower() == "no":
                print("Your order has been canceled")
                break

