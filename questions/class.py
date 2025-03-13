# SINIF NASIL OLUŞTURULUR VE NESNE NASIL TANIMLANIR
# Python'da bir sınıf (class) tanımlamak için class anahtar kelimesi kullanılır. Bir sınıf, içinde metotlar (fonksiyonlar) ve özellikler (değişkenler) bulundurabilir. Bu sınıftan bir nesne (object) oluşturmak için ise sınıfın adı, bir fonksiyon gibi çağrılır.

# Sınıf Oluşturma
class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka  # Nesne değişkeni (attribute)
        self.model = model
        self.yil = yil

    def bilgileri_goster(self):
        print(f"Araba: {self.marka} {self.model}, Yıl: {self.yil}")

# Nesne Oluşturma
araba1 = Araba("Toyota", "Corolla", 2022)

# Nesne Metodunu Çağırma
araba1.bilgileri_goster()
