class Order:
    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = cart
        self.total_amount = cart.get_amount()  # Düzeltildi ✅

    def place_order(self):
        if self.total_amount > 0:
            print("\nSiparişiniz başarıyla oluşturuldu!")
            print(self.customer)
            self.cart.display_cart()
            print(f"\nToplam Tutar: {self.total_amount} TL")
        else:
            print("\nSepet boş, sipariş oluşturulamadı.")
