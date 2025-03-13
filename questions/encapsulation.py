#Encapsulation (kapsülleme), nesne yönelimli programlamada (OOP) bir nesnenin verilerini (değişkenlerini) ve bu verilere erişimi sağlayan metodları bir sınıf içinde gizleyerek dış dünyadan koruma işlemidir. Bu, veri bütünlüğünü sağlar ve kodun daha güvenli, esnek ve yönetilebilir olmasını sağlar.

#Python'da kapsülleme, private (özel) ve protected (korumalı) erişim belirteçleri ile sağlanır:

# _protected: Tek alt çizgi (_) ile belirtilir. Bu değişkenlere dışarıdan erişilebilir, ancak bunlar yalnızca sınıf içinde veya alt sınıflarda kullanılmak üzere tasarlanmıştır.

# __private: Çift alt çizgi (__) ile belirtilir. Bu değişkenlere doğrudan dışarıdan erişilemez, sadece sınıf içinden erişilebilir.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public değişken
        self._bank_name = "ABC Bank"  # Protected değişken
        self.__balance = balance  # Private değişken

    def deposit(self, amount):
        """Hesaba para yatırma işlemi"""
        if amount > 0:
            self.__balance += amount
            print(f"{amount} TL yatırıldı. Yeni bakiye: {self.__balance} TL")
        else:
            print("Geçersiz miktar!")

    def withdraw(self, amount):
        """Hesaptan para çekme işlemi"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} TL çekildi. Kalan bakiye: {self.__balance} TL")
        else:
            print("Yetersiz bakiye veya geçersiz miktar!")

    def get_balance(self):
        """Bakiye bilgisini güvenli bir şekilde almak için bir metod"""
        return self.__balance

# Kullanım
account = BankAccount("Ahmet Yılmaz", 5000)

# Public değişkenlere erişim
print(account.account_holder)  # Ahmet Yılmaz

# Protected değişkene erişim (dışarıdan erişilebilir, ama önerilmez)
print(account._bank_name)  # ABC Bank

# Private değişken dışarıdan erişilemez
# print(account.__balance)  # HATA! AttributeError: 'BankAccount' object has no attribute '__balance'

# Bakiye sorgulama
print("Gizli Bakiye:", account.get_balance())  # Gizli Bakiye: 5000

# Para yatırma
account.deposit(1000)  # 1000 TL yatırıldı. Yeni bakiye: 6000 TL

# Para çekme
account.withdraw(2000)  # 2000 TL çekildi. Kalan bakiye: 4000 TL

# Doğrudan private değişkene erişim engellenmiş olsa da
# Python'un ismini değiştirdiği için `_BankAccount__balance` ile erişilebilir (ancak önerilmez).
print(account._BankAccount__balance)  # 4000
