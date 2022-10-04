class Phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phoneNumber):
        print(f"{self.brand} is calling {phoneNumber}")

    def __str__(self) -> str:
        return f"Brand={self.brand}\n Price = {self.price}"

    

iphone = Phone("Iphone 7+", 300)
Samsung = Phone("Samsung S20",1400)

print(iphone.brand)
print(iphone.price)
iphone.call("999")


print(Samsung.brand)
print(Samsung.price)
Samsung.call("083733872")




