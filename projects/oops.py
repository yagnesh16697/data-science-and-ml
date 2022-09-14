class Item:
    def __init__(self):
        print("created")

    def calculate_total(self, x, y):
        return x * y


item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total(item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 200
item2.quantity = 3
print(item2.calculate_total(item2.price, item2.quantity))
