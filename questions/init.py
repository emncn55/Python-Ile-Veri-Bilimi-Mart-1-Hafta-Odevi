# __init__ metodu, bir sınıfın yapıcı (constructor) metodudur. Bir sınıfın yeni bir örneği (instance) oluşturulduğunda otomatik olarak çağrılır ve nesnenin başlangıç durumunu ayarlamak için kullanılır.

class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgileri_goster(self):
        return f"{self.yil} {self.marka} {self.model}"

# Nesne oluşturma
araba1 = Araba("Toyota", "Corolla", 2022)

print(araba1.bilgileri_goster())  # Çıktı: 2022 Toyota Corolla
