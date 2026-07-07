import pytest

# # 4 pytest1

# შექმენით ფუნქცია Celsius → Fahrenheit. დაწერეთ pytest ტესტები approx-ის გამოყენებით.

# ნიმუში: assert pytest.approx

def temperature(deg):
    F = deg * 1.8 + 32
    return F

def test_temperature_true():
    assert temperature(30) == pytest.approx(86)
    
def test_temperature_false():
    assert temperature(30) != pytest.approx(80)

def test_temperature_negative():
    assert temperature(-10) == pytest.approx(14)

def test_temperature_float():
    assert temperature(37) == pytest.approx(98.6)


# # 5 pytest2

# შექმენით ფუნქცია რომელიც ამოწმებს მომხმარებლის ლოგინს და პაროლს dictionary-დან
# pytest-ში გამოიყენეთ raises შეცდომის დასატესტად

# ნიმუში: raise ValueError

user = {
    "email" : "esmo@mail.com",
    "password" : "1234eeee."
}

def login(email, password):
    if email == user["email"] and password == user["password"]:
        print("Login successful")
    else:
        raise ValueError("Wrong credentials")
    return email, password

def test_login():
    assert login("esmo@mail.com", "1234eeee.") == (user["email"], user["password"])
    with pytest.raises(ValueError):
        login('', '')
    with pytest.raises(ValueError):
        login('esmo@mail.com', 'wrong')





# # 6 pytest3

# დაწერეთ ფუნქცია, რომელიც ამოწმებს არის თუ არა სტრიქონი სწორი email(ანუ შეიცავს @ და . სიმბოლოებს)
# pytest-ით გააკეთეთ ტესტები parametrization-ის გამოყენებით

# ნიმუში: @ pytest.mark.parametrize

def check_email(email):
    return "@" in email and "." in email

@pytest.mark.parametrize("email, expected", [
    ("esmo@mail.com", True),
    ("esmo.mail", False),
    ("esmo@mail", False)
])
def test_check_email(email, expected):
    assert check_email(email) == expected