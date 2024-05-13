class Customer(Person):#this class works as the bluepritnt for making new types of objects, the "person" defines the class' inhertience 
  def __init__(self, name):
    self.name = name # the def innit initializes the object attribute 

class Person(Customer):
    def __init__(self):
        self.name = ""
        self.money = 0


def main():
    richter = Person()
    richter.name = "Richter"
    richter.money = 777

    print(richter.name, "has", richter.money, "dollars.")

class Customer:
    def __init__(self, name, purchasing):
        self.name = name
        self.favorite_purchase = "cheese"

    def greet(self):
        print(f"Good day, {self.name}! How can I help you?")

customer1 = Customer("Squidward Tentacles", "Clarinet")
customer1.age = 30
customer1.greet()

main()
