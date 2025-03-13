# Kalıtım, nesne yönelimli programlamada (OOP) bir sınıfın (parent/base class) özelliklerini ve metodlarını başka bir sınıfa (child/derived class) aktarmasını sağlayan mekanizmadır.

# Bu sayede:

# Kod tekrarını önler.
# Daha düzenli ve yönetilebilir bir yapı oluşturur.
# Ana sınıfı (base class) genişleterek (extend) yeni işlevler eklemeyi kolaylaştırır.

# Parent Class (Base Class)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Some generic animal sound")

# Child Class (Derived Class)
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says Meow!")

# Nesneler oluşturalım
dog = Dog("Rex")
cat = Cat("Mia")

dog.make_sound()  # Rex says Woof!
cat.make_sound()  # Mia says Meow!
