# # 1 დაწერეთ პაროლის გენერატორი.
# დავალების შესრულებაში დაგეხმარებათ: random მოდული, while ან for ციკლი, list,
# სტრიქონის ფორმატირება.
# input ის მეშვეობით უნდა შეგვეძლოს მითითება რა სიგრძის პაროლი გვინდა და რა
# სიმბოლეობიდან გენერირდება იგი: პაროლის სიგრძეს ირჩევს მომხმარებელი, უნდა თუ
# არა სიმბოლოები, რიცხვები, დიდი/პატარა ასოები(ლათინურად) თუ ქართულს შემოიტანს
# უნდა დაუწერო რომ “შეიყვანე მხოლოდ ლათინური ასოები”
import random

RED = "\033[31m"
RESET = "\033[0m"


def get_choice(message):
    while True:
        choice = input(message).lower()

        if not choice.isascii(): #isascii() არის მეთოდი რომელიც მარტო კითხულობს ლათინურ ასოებსა და ციფრებს და თუ მოცემული სტრინგი ამასის გარდა რაიმე შეიცავ გამოაქვს ბულეანად false
            print(f"{RED}შეიყვანე მხოლოდ ლათინური ასოები{RESET}")
            continue

        if choice in ["yes", "no"]:
            return choice == "yes"

        print(f"{RED}შეიყვანე მხოლოდ yes ან no{RESET}")


def password_generator(length, use_symbols, use_numbers, use_uppercase, use_lowercase):
    characters = ""

    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"

    if use_numbers:
        characters += "0123456789"

    if use_uppercase:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if use_lowercase:
        characters += "abcdefghijklmnopqrstuvwxyz"

    if characters == "":
        print(f"{RED}აირჩიეთ მინიმუმ ერთი ტიპი!{RESET}")
        return ""

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


length = int(input("Enter password length: "))

use_symbols = get_choice("Use symbols? (yes/no): ")
use_numbers = get_choice("Use numbers? (yes/no): ")
use_uppercase = get_choice("Use uppercase letters? (yes/no): ")
use_lowercase = get_choice("Use lowercase letters? (yes/no): ")

password = password_generator(
    length,
    use_symbols,
    use_numbers,
    use_uppercase,
    use_lowercase
)

if password:
    print(f"Generated password: {RED}{password}{RESET}")

# # 2 პაროლის შეფასება
# ამოცანა: მომხმარებლის შეყვანილი პაროლი შეაფასე 0–10 შკალით: სიგრძე, ციფრები, სიმბოლოები,
# დიდი/პატარა ასოები, განმეორებადი სიმბოლოების არსებობა.
# მოთხოვნები: გამოიტანე “weak/medium/strong”.

password = input("Enter password: ")

score = 0

if len(password) >= 8:
    score += 2

if any(char.isdigit() for char in password):
    score += 2
    
if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/~`" for char in password):
    score += 2

if any(char.isupper() for char in password):
    score += 2
    
if any(char.islower() for char in password):
    score += 2
    
if len(set(password)) < len(password):
    score -= 2
    
if score <= 3:
    print("Weak")
elif score <= 6:
    print("Medium")
else:
    print("Strong")

# # 3 დაწერე ფუნქცია (ფიბონაჩის რიგი) - *რა არის ფიბონაჩი - ბოლო ორი ელემენტის ჯამით ვამატებთ
# ახალ რიცხვს*, სანამ სიგრძე არ გახდება მომხმარებლის მიერ შემოყვანილი რიცხვი, აუცილებლად
# უნდა შემოიტანოს რიცხვი, სხვა რამის შემოტანის დროს უნდა შემოწმდეს რა შემოიტანა
# მომხმარებელმა და უნდა დაუსახელო აღნიშნული და უთხრა რომ მხოლოდ რიცხვი შემოიტანოს. მაგ:
# შემოიტანა სიმბოლო, უნდა უთხრა შენ შემოიტანე სიმბოლო არასწორია, მხოლოდ რიცხვი!

def fibonacci(length):
    if length == 1:
        return [0]

    sequence = [0, 1]

    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


while True:
    user_input = input("შეიყვანე რიცხვი: ")

    if user_input.isdigit():
        number = int(user_input)

        if number <= 0:
            print("შეიყვანე 0-ზე დიდი რიცხვი!")
            continue

        print(fibonacci(number))
        break

    elif user_input.isalpha():
        print("შენ შემოიტანე ასო, არასწორია! მხოლოდ რიცხვი შეიყვანე.")

    else:
        print("შენ შემოიტანე სიმბოლო, არასწორია! მხოლოდ რიცხვი შეიყვანე.")
    
    