# Polymorphism (Çok Biçimlilik), nesne yönelimli programlamada (OOP) farklı sınıfların aynı arayüzü paylaşmasını sağlayan bir tekniktir. Bu sayede, farklı nesneler aynı metodları farklı şekillerde uygulayabilir.

# Python'da çok biçimlilik, genellikle inheritance (kalıtım) ve method overriding (metod geçersiz kılma) ile sağlanır. Aynı isimdeki metodlar, farklı sınıflarda farklı şekillerde uygulanabilir.

class Hayvan:
    def ses_cikar(self):
        raise NotImplementedError("Bu metod alt sınıflar tarafından uygulanmalıdır.")

class Kedi(Hayvan):
    def ses_cikar(self):
        return "Miyav"

class Kopek(Hayvan):
    def ses_cikar(self):
        return "Hav hav"

# Polymorphism kullanımı
hayvanlar = [Kedi(), Kopek()]

for hayvan in hayvanlar:
    print(hayvan.ses_cikar())  # Farklı sınıflar aynı metodu farklı şekillerde uyguluyor
