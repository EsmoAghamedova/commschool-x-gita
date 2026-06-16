from dataclasses import dataclass

# # 1 ამოცანა 1
# შექმენი კლასი BankAccount, რომელსაც ექნება:
# დახურული ატრიბუტები: __balance, __owner.
# მეთოდი deposit(amount) – თანხის დამატება.
# მეთოდი withdraw(amount) – თანხის გამოტანა(არ უნდა გადავიდეს მინუსში).
# მეთოდი get_balance() – მხოლოდ წაკითხვისთვის.
# დაწერე კოდი ისე, რომ მომხმარებელს პირდაპირ __balance-ზე წვდომა არ ჰქონდეს.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.__balance -= amount
        else:
            print("Amount must be positive.")

    def get_balance(self):
        return self.__balance


account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())

# # 2 ამოცანა 2
# შექმენი კლასი ShoppingCart, რომელსაც ექნება:
# ატრიბუტი items(სიაში პროდუქტების რაოდენობა).
# __len__() დააბრუნებს პროდუქტების რაოდენობას.
# __eq__() ორი კალათის შედარება – აბრუნებს True, თუ რაოდენობა ტოლია.
# გააკეთე 2 კალათა და შეადარე.
# გააკეთე 3 კალათა და შეადარე.
# გააკეთე 4 კალათა და შეადარე.


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        if isinstance(other, ShoppingCart):
            return len(self) == len(other)
        return NotImplemented


cart1 = ShoppingCart()
cart1.add_item("apple")
cart1.add_item("banana")
cart1.add_item("orange")

cart2 = ShoppingCart()
cart2.add_item("banana")

cart3 = ShoppingCart()
cart3.add_item("orange")
cart3.add_item("grape")

cart4 = ShoppingCart()
cart4.add_item("grape")
print(cart1 == cart2)
print(cart1 == cart3)
print(cart1 == cart4)
print(cart2 == cart3)
print(cart2 == cart4)
print(cart3 == cart4)

# # 3 ამოცანა 3
# გამოიყენე @ dataclass მოდული კლასის Book შესაქმნელად:
# ველები: title, author, year.
# დაამატე მეთოდი is_classic() → აბრუნებს True, თუ წელი < 1970.
# შექმენი რამდენიმე წიგნი და შეამოწმე ფუნქცია.


@dataclass
class Book:
    title: str
    author: str
    year: int

    def is_classic(self):
        return self.year < 1970


book1 = Book("The Right Hand of the Grand Master",
             "Konstantine Gamsahurdia", 1939)
book2 = Book("Harry Potter", "J.K. Rowling", 1997)
book3 = Book("xevisberi gocha", "aleqsandre yazbegi", 1884)

print(book1.is_classic())
print(book2.is_classic())
print(book3.is_classic())

# # 4 ამოცანა 4
# შექმენი კლასი Person, რომელსაც ექნება __del__() მეთოდი, რომელიც ბეჭდავს "Person removed" როცა ობიექტი წაიშლება.
# შექმენი ობიექტი, შემდეგ წაშალე del -ით და ნახე როგორ რეაგირებს garbage collector.


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Person removed")


p = Person("John")
del p

# # 5 ამოცანა 5
# შექმენი კლასი Temperature, რომელსაც ექნება:
# დახურული ატრიბუტი __celsius.
# get და set property °C-სთვის.
# fahrenheit property(read-only), რომელიც აბრუნებს °F.
# შექმენი ობიექტი, შეცვალე °C და შეამოწმე °F ავტომატურად იცვლება თუ არა.


class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        self.__celsius = value

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32


temp = Temperature(25)
print(temp.celsius)
print(temp.fahrenheit)

# # 6 ამოცანა 6
# შექმენი კლასი CustomList, რომელიც:
# ინახავს ელემენტებს.
# __getitem__() – აბრუნებს ელემენტს ინდექსით.
# __setitem__() – ცვლის ელემენტს.
# __iter__() – Iterable უნდა იყოს.
# გამოიყენე for ციკლში შენი CustomList.


class CustomList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __iter__(self):
        return iter(self.items)

my_list = CustomList()

my_list.add_item("apple")
my_list.add_item("banana")
my_list.add_item("orange")

print(my_list[0]) 

my_list[1] = "grape"

for item in my_list:
    print(item)


# # 7 ამოცანა 7
# შექმენი კლასი Refrigerator, რომელსაც ექნება:
# ატრიბუტი items(სია).
# __contains__() – აბრუნებს True, თუ პროდუქტი მაცივარშია("milk" in fridge).
# __str__() – "Fridge with N items".
# __del__() – "Fridge unplugged!".
# დაამატე პროდუქტები, შეამოწმე "milk" in fridge, დაბეჭდე ობიექტი და ბოლოს წაშალე.

class Refrigerator:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        return f"Fridge with {len(self.items)} items"

    def __del__(self):
        print("Fridge unplugged!")
        
fridge = Refrigerator()
fridge.add_item("milk")

print("milk" in fridge)
print(fridge) 
del fridge  

# # 8 ამოცანა 8
# შექმენი კლასი FunnyCalculator, რომელსაც ექნება:
# __add__() – აბრუნებს "Why are you adding numbers? Just buy a calculator".
# __mul__() – აბრუნებს "Multiplication is too mainstream...".
# __truediv__() – თუ გაყოფ 0-ზე, ბეჭდავს "ZeroDivisionError? Nah, let’s just say infinity"
# __str__() – "I’m the funniest calculator in Python!".
# ცადე calc + 5, calc * 2, 10 / calc და ნახე რა მოხდება.

class FunnyCalculator:
    def __add__(self, other):
        return "Why are you adding numbers? Just buy a calculator"

    def __mul__(self, other):
        return "Multiplication is too mainstream..."

    def __truediv__(self, other):
        if other == 0:
            return "ZeroDivisionError? Nah, let’s just say infinity"
        return "Division is not my thing either."
    
    def __rtruediv__(self, other):
        if self == 0:
            return "ZeroDivisionError? Nah, let’s just say infinity"
        return "Division is not my thing either."

    def __str__(self):
        return "I’m the funniest calculator in Python!"
    
calc = FunnyCalculator()
print(calc + 5)
print(calc * 2)
print(10 / calc)