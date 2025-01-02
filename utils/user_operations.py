class Order:
    def __init__(self, order_id, customer, store, products, quantities):
        """
        Inicializa un pedido con un cliente, una tienda, productos y cantidades.
        
        :param order_id: ID único del pedido.
        :param customer: Cliente que realiza el pedido.
        :param store: Tienda desde donde se realiza el pedido.
        :param products: Lista de productos pedidos.
        :param quantities: Lista de cantidades correspondientes a los productos.
        """
        self.order_id = order_id
        self.customer = customer
        self.store = store
        self.products = products  # Lista de productos
        self.quantities = quantities  # Lista de cantidades correspondientes a los productos
        self.status = "Pending"  # Estado inicial del pedido

    def calculate_total_cost(self):
        """
        Calcula el costo total del pedido sumando el precio de cada producto por su cantidad.
        
        :return: Costo total del pedido.
        """
        total_cost = 0
        for product, quantity in zip(self.products, self.quantities):
            total_cost += product.price * quantity
        return total_cost

    def set_status(self, new_status):
        """
        Actualiza el estado del pedido.
        
        :param new_status: El nuevo estado del pedido (pendiente, enviado, entregado).
        """
        if new_status not in ["Pending", "Shipped", "Delivered"]:
            raise ValueError("Invalid status.")
        self.status = new_status

    def process_order(self):
        """
        Procesa el pedido, actualizando el stock de la tienda y cambiando el estado del pedido.
        """
        # Verifica si hay suficiente stock para todos los productos
        for product, quantity in zip(self.products, self.quantities):
            if product.stock < quantity:
                raise ValueError(f"Not enough stock for product: {product.name}")
        
        # Actualiza el stock de la tienda
        for product, quantity in zip(self.products, self.quantities):
            self.store.inventory.update_product_stock(product.code, quantity)
        
        # Cambia el estado del pedido a "Shipped"
        self.set_status("Shipped")

    def __str__(self):
        """
        Devuelve una representación del pedido con su estado.
        
        :return: String con los detalles del pedido.
        """
        return f"Order {self.order_id} for {self.customer.name}, Status: {self.status}, Total: {self.calculate_total_cost():.2f}"

# Ejemplo de uso
class Customer:
    def __init__(self, name):
        self.name = name

# Crear productos
product1 = Product("Laptop", "Electronics", 10, 1000, "P001")
product2 = Product("Phone", "Electronics", 20, 500, "P002")

# Crear tienda
store = Store("Tech Store", "New York", "S001")
store.inventory.add_product(product1)
store.inventory.add_product(product2)

# Crear cliente
customer = Customer("John Doe")

# Crear pedido
order = Order(order_id="O001", customer=customer, store=store, products=[product1, product2], quantities=[2, 3])

# Procesar pedido
print(order)
order.process_order()
print(order)

# Verificar el stock de los productos después del pedido
store.list_all_products()
