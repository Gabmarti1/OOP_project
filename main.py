from datetime import datetime
class Product:
    def __init__(self,name,category,stock,price,code):
        if stock < 0:
            raise ValueError("Stock cannot be negative.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.name=name
        self.category=category
        self.stock=stock
        self.price=price
        self.code=code

    def update_price(self,increasement):
        self.price=self.price * (1+(increasement/100))

    def update_stock(self,sold_stock):
        self.stock=self.stock-sold_stock

    def __str__(self):
        return f"{self.name}({self.category}): stock={self.stock}, price={self.price:.2f}, id={self.code}"
        
class PerishableProduct(Product):
    def __init__(self,name,category,stock,price,code,expiration_date):
        super().__init__(name, category, stock, price, code)
        self.expiration_date=datetime.strptime(expiration_date,"%Y-%m-%d")
    def is_expired(self):
        return datetime.now()>self.expiration_date
    def __str__(self):
        status = "Expired" if self.is_expired() else "Valid"
        return super().__str__() + f", Expiration Date: {self.expiration_date.date()} ({status})"

class ElectronicProduct(Product):
    def __init__(self,name,category,stock,price,code,ram,battery,cpu):
        super().__init__(name, category, stock, price, code)
        self.ram=ram
        self.battery=battery
        self.cpu=cpu
    def __str__(self):
        return super().__str__() + f", RAM:{self.ram}, Battery:{self.battery}, cpu:{self.cpu}"

class Inventory:
    def __init__(self):
        self.products={}

    def add_product(self,product):
        if product.code in self.products:
            raise ValueError("This product is already in the inventory.")
        self.products[product.code]=product

    def remove_product(self,product):
        if product.code not in self.products:
            raise ValueError("This product is not in the inventory")
        del self.products[product.code]
    def update_product_price(self,code,price_increase):
        self.products[code].update_price(price_increase)

    def update_product_stock(self,code,items_sold):
        self.products[code].update_stock(items_sold)

    def get_all_products(self):
        return list(self.products.values())

    def __str__(self):
        return f"Inventory. Total number of items:{len(self.products)} "

class Store:
    def __init__(self,name,location,code):
        self.name = name
        self.location = location
        self.code = code
        self.inventory=Inventory()
    
    def list_all_products(self):
        products=self.inventory.get_all_products()
        if not products:
            print(f"The store {self.name}has no inventory.")
        else:
            print(f"Products in the store {self.name}:")
            for product in products:
                print(product)
    def update_location(self,new_location):
        self.location=new_location

    def __str__(self):
        return f"{self.name} located in {self.location} with an id {self.code}"

class StoreOnline(Store):
    def __init__(self,name,location,code,url):
        super().__init__(name,location,code)
        self.url=url

    def __str__(self):
        return super().__str__() + f", Online URL:{self.url}"

class Customer:
    def __init__(self,name,address,electronic_email):
        self.name = name
        self.address = address
        self.electronic_email = electronic_email
    def __str__(self):
        return f"Name:{self.name}, Address:{self.address},email:{self.electronic_email}"

class Orders:
    def __init__(self,order_id,tienda,products_quantities_dicc,customer,distance):
        self.order_id = order_id
        self.tienda=tienda
        self.products_quantities_dicc=products_quantities_dicc
        self.customer = customer
        self.status="Pending"
        self.distance=distance
    def cost_per_transport(self):
        cost_base = 2
        price_per_km = 0.1
        cost = cost_base if self.distance <= 10 else cost_base + price_per_km * (self.distance - 10)    
        return cost
    
    def total_cost_calculation(self):
        total_cost=0
        for p,q in self.products_quantities_dicc.items():

            if q > p.stock:
                print(f"The maximum amount of products available is {p.stock}")
                q=p.stock
            total_cost += q*p.price
        total_cost += self.cost_per_transport()
        return total_cost 

    def set_status(self, new_status):
        self.status=new_status

    def process_order(self):
        products_to_send=0
        for p,q in self.products_quantities_dicc.items():
            if q > p.stock:
                products_to_send=p.stock
                self.tienda.inventory.update_product_stock(p.code,products_to_send)
            else:
                products_to_send=q
                self.tienda.inventory.update_product_stock(p.code,products_to_send)
        self.set_status('Processed')
        
    
    def __str__(self):
        return f"Costumer {self.customer}, Tienda {self.tienda.code}, Identificador {self.order_id},Total: {self.total_cost_calculation():.2f}, Status: {self.status}"

class OrdersHistory:
    def __init__(self):
        self.orders=[]
    def add_order(self,order):
        self.orders.append(order)
    def get_all_orders(self,order):
        return self.orders

    def __str__(self):
        return f"Order History: {len(self.orders)} orders"
    
class StoreManager:
    def __init__(self):
        self.stores={}
    def add_store(self,store):
        if store.name in self.stores:
            raise ValueError("This store is already in the storemaneger.")
        self.stores[store.code]=store
    def remove_store(self,store):
        if store.code not in self.stores:
            raise ValueError("This store is not in the storemaneger")
        del self.stores[store.code]
    
    def update_store_location(self,code,new_location):
        self.stores[code].update_location(new_location)

    def list_all_stores(self):
        for i in self.stores.values():
            print(i)

    def __str__(self):
        return f"Store Manager. Total number of stores:{len(self.stores)} "