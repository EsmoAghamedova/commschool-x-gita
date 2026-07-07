import unittest

# # 1 unittest1

# შექმენით Calculator კლასი add, subtract, multiply, divide მეთოდებით. დაწერეთ unittest რომელიც ამოწმებს ყველა მეთოდს.
# გაითვალისწინეთ 0-ზე გაყოფაც.
# გამოიყენეთ unittest მოდული
# გამოიყენეთ setup მეთოდი.


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = self.calc.subtract(3, 2)
        self.assertEqual(result, 1)

    def test_multiply(self):
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = self.calc.divide(6, 3)
        self.assertEqual(result, 2)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(4, 0)

# # 2 unittest2

# შექმენით BankAccount კლასი deposit და withdraw მეთოდებით. დაწერეთ unittest რომელიც ამოწმებს:

# - სწორი ბალანსი

# - უარყოფითი თანხის შეტანისას შეცდომა

# - თანხის გამოტანა ბალანსზე მეტისას შეცდომა


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self.balance:
            raise ValueError("Not enough balance")
        self.balance -= amount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.acc = BankAccount(100)

    def test_deposit(self):
        self.acc.deposit(50)
        self.assertEqual(self.acc.balance, 150)

    def test_withdraw(self):
        self.acc.withdraw(30)
        self.assertEqual(self.acc.balance, 70)

    def test_withdraw_error(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(1000)

    def test_deposit_error(self):
        with self.assertRaises(ValueError):
            self.acc.deposit(-10)

# # 3 unittest3

# შექმენით ფუნქცია რომელიც იღებს JSON(dict) response-ს და აბრუნებს "status"-ის მნიშვნელობას. თუ status არ არსებობს → შეცდომა.
# დაწერეთ ტესტები


responses = [
    {
        "status": "success",
        "data": {
            "user": "alex",
            "id": 1
        }
    },

    {
        "status": "error",
        "message": "Something went wrong"
    },

    {
        "data": {
            "user": "alex"
        }
    }
]

def get_status(response):
    if "status" not in response:
        raise KeyError("Status key not found in response")
    return response["status"]

class TestGetStatus(unittest.TestCase):    
    def test_get_status_success(self):
        response = responses[0]
        self.assertEqual(get_status(response), "success")
        
    def test_get_status_error(self):
        response = responses[1]
        self.assertEqual(get_status(response), "error")
        
    def test_get_no_status(self):
        response = responses[2]
        with self.assertRaises(KeyError):
            get_status(response)