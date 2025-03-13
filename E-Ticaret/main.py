from product import Product
from customer import Customer
from cart import Cart
from order import Order

def main():
    # Ürünleri oluştur
    products = {
        "Laptop": Product("Laptop", 15000, 5),
        "Telefon": Product("Telefon", 10000, 15),
        "Kulaklık": Product("Kulaklık", 500, 150)
    }

    # Müşteri oluştur
    customer = Customer("Ahmet Yılmaz", "ahmet@example.com")

    # Sepet oluştur ve ürün ekle
    cart = Cart()
    
    cart.add_product(products["Laptop"], 1)  # 1 adet Laptop
    cart.add_product(products["Telefon"], 2)  # 2 adet Telefon
    cart.add_product(products["Kulaklık"], 3)  # 3 adet Kulaklık

    # Sepeti görüntüle
    cart.display_cart()

    # Sipariş oluştur ve tamamla
    order = Order(customer, cart)
    order.total_amount = cart.get_amount()
    order.place_order()


main()
