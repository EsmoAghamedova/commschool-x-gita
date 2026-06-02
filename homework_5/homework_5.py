# # 1 დაწერეთ პაროლის გენერატორი.
# დავალების შესრულებაში დაგეხმარებათ: random მოდული, while ან for ციკლი, list,
# სტრიქონის ფორმატირება.
# input ის მეშვეობით უნდა შეგვეძლოს მითითება რა სიგრძის პაროლი გვინდა და რა
# სიმბოლეობიდან გენერირდება იგი: პაროლის სიგრძეს ირჩევს მომხმარებელი, უნდა თუ
# არა სიმბოლოები, რიცხვები, დიდი/პატარა ასოები(ლათინურად) თუ ქართულს შემოიტანს
# უნდა დაუწერო რომ “შეიყვანე მხოლოდ ლათინური ასოები”
# import random

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
    

# # 4 პალინდრომი
# ამოცანა: შეამოწმე, არის თუ არა შეყვანილი ტექსტი პალინდრომი(მხოლოდ ასოები/ციფრები). თუ
# არაა, შესთავაზე ყველაზე ახლო პალინდრომი ერთი სიმბოლოს ჩასმით/წაშლით.
# 
def is_palindrome(text):
    cleaned = ""

    for char in text.lower():
        if char.isalnum():
            cleaned += char

    return cleaned == cleaned[::-1]


def closest_palindrome(text):
    cleaned = ""

    for char in text.lower():
        if char.isalnum():
            cleaned += char

    if cleaned == cleaned[::-1]:
        return "ეს უკვე პალინდრომია."

    # ერთი სიმბოლოს წაშლით ვამოწმებთ
    for i in range(len(cleaned)):
        candidate = cleaned[:i] + cleaned[i + 1:]

        if candidate == candidate[::-1]:
            return f"ყველაზე ახლო პალინდრომი: {candidate}"

    return "ერთი სიმბოლოს წაშლით პალინდრომი ვერ მივიღეთ."


text = input("შეიყვანე ტექსტი: ")

if is_palindrome(text):
    print("ტექსტი პალინდრომია.")
else:
    print("ტექსტი პალინდრომი არ არის.")
    print(closest_palindrome(text))

# # 5 ზედმეტსახელების გენერატორი
# მომხმარებელს შემოაქვს მხოლოდ ერთი სიტყვა(სხვა შემთხვევები დაბლოკე) და შენ სთავაზობ 5
# ზედმეტსახელს ამ სიტყვასთან კავშირში.

import random
def generate_nicknames(word):
    return [
        word + "Pro",
        word + "Master",
        "Dark" + word,
        word + "X",
        "The" + word
    ]


while True:
    user_word = input("შეიყვანე მხოლოდ ერთი სიტყვა: ").strip()

    if not user_word:
        print("ცარიელი მნიშვნელობა არ შეიძლება!")
        continue

    if " " in user_word:
        print("მხოლოდ ერთი სიტყვა უნდა შეიყვანო!")
        continue

    if not user_word.isalnum():
        print("გამოიყენე მხოლოდ ასოები და ციფრები!")
        continue

    break

nicknames = generate_nicknames(user_word)

print("\nშეთავაზებული ზედმეტსახელები:")
for i, nickname in enumerate(nicknames, start=1):
    print(f"{i}. {nickname}")

# # 6 სორტირება
# მომხმარებელს შემოჰყავს რიცხვები თითო გამოტოვებით, (ულიმიტოდ რამდენიც უნდა) პროგრამა
# სთავაზობს როგორ უნდა რომ დაუსორტირდეს აღნიშნული: კლებადობით, ზრდადობით, random-ად,
# მხოლოდ უნიკალური მონაცემები დატოვოს. რომელსაც აირჩევს უნდა გამოვიდეს ზუსტად ისე
# დალაგებული სია.


while True:
    user_input = input("შეიყვანე რიცხვები გამოტოვებით: ").strip()
    parts = user_input.split()
    if len(parts) == 0:
        print("მინიმუმ ერთი რიცხვი შეიყვანე!")
        continue
    valid = True
    for num in parts:
        if not (num.isdigit() or (num[0] == "-" and num[1:].isdigit())):
            valid = False
            break
    if valid:
        numbers = [int(num) for num in parts]
        break
    print("შეიყვანე მხოლოდ რიცხვები!")

print("""
1 - ზრდადობით
2 - კლებადობით
3 - Random-ად
4 - მხოლოდ უნიკალური მონაცემები
""")

choice = input("აირჩიე: ")

if choice == "1":
    print(sorted(numbers))
elif choice == "2":
    print(sorted(numbers, reverse=True))
elif choice == "3":
    random.shuffle(numbers)
    print(numbers)
elif choice == "4":
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    print(unique_numbers)
else:
    print("არასწორი არჩევანი!")
