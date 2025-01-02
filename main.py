class Product:
    def __init__(self,name,category,stock,price,id):
        self.name=name
        self.category=category
        self.stock=stock
        self.price=price
        self.id=id

    def update_price(self,new_price):
        self.price=new_price

    def update_stock(self,new_stock):
        self.stock=new_stock

    def __str__(self):
        return f"{self.name}({self.category}): stock={self.stock}, price={self.price}, id={self.id}"

class Inventory:
    def __init__(self):
        self.products={}

    def add_product(self,product)
        if product.id in self.products:
            raise ValueError("This product is already in the inventory.")
        self.products[product.id]=product

    def remove_product(self,code):
        if code not in self.products:
            raise ValueError("This product is not in the inventory")
            del self.products[code]
    def update_product_price(self,code,new_price):
        self.products[code].update_price(new_price)

    def update_product_stock(self,code,new_stock):
        self.products[code].update_stock(new_stock)

    def list_all_products(self):
        return self.products.values()

    def __str__(self):
        return f"Inventory. Total number of items:{len(self.products)} "

    