# # 1 დაწერეთ პირობა, რომელიც გაარკვევს შემოტანილი ასო არის თანხმოვანი თუ ხმოვანი
# import random
# მაგალითი:
# შემოიტანე სიმბოლო: ბ "ბ" თანხმოვანია
# == == == == == == == == == == =
# შემოიტანე სიმბოლო: ი "ი" ხმოვანია
# == == == == == == == == == == =

vowels = "აეიოუ"
consonants = "ბგდვზთკლმნპრსტფხცჩშჟ"
letter = input("შეიყვანეთ ასო (ქართული): ")

if letter in vowels:
    print(f"{letter}: ხმოვანი")
elif letter in consonants:
    print(f"{letter}: თანხმოვანი")
else:
    print(f"{letter}: არასწორი სიმბოლო")


# # 2 დაწერე პირობა რომელიც for ციკლის გამოყენებით გამოიტანს რიცხვებს 10-დან 0-მდე

ans = []
for i in range(1, 11):
    ans.append(i)
reversed_list = ans[::-1]
print(reversed_list)

# # 3 დაწერეთ ციკლი რომელიც დაბეჭდავს ლისტში მყოფ უდიდეს 3 რიცხვს და მათ ინდექსებს
# # ქმნის და ინახავს random მონაცემებს [1,4,2,3,6,5]
# lst = [random.randint(1, 20) for _ in range(10)]
# print(lst)
# მაგალითი:
# [3, 14, 4, 1, 2, 11, 12, 18, 7, 18]
# მონაცემი 1: 18
# მონაცემი 2: 18
# მონაცემი 3: 14

import random

list = [random.randint(1, 20) for _ in range(10)]
print(list)

indexed = []

for index, num in enumerate(list):
    indexed.append((num, index))

sorted_list = sorted(list, reverse=True)

for i in range(3):
    number = indexed[i][0]
    index = indexed[i][1]

    print(f"მონაცემი {i + 1}: {number} | ინდექსი: {index}")

# # 4 დაწერეთ ციკლი რომელიც დაბეჭდავს ოთხუთხედს “#” (ასეთს) მოცემული სიმაღლისა და სიგანის
# მიხედვით
# მაგალითი:
# width = 5
# height = 2
# # # # # #
# # # # # #
# -------------
# width = 2
# height = 5
# # #
# # #
# # #
# # #
# # #

height = input("Enter height: ")
width = input("width: ")

for i in range(int(height)):
    for j in range(int(width)):
        print("#", end=" ")
    print()

# # 5 მომხმარებელს შემოყავს ორი რიცხვი x & y შექმენით ფუნქცია, რომელიც მიიღებს ამ ორ
# პარამეტრს და დაბეჭდავს ყველა არითმეტიკულ ოპერაციას
# მაგალითი:
# 5 + 2 = 7
# 5 - 2 = 3
# 5 * 2 = 10
# 5 / 2 = 2.5
# 5 // 2 = 2
# 5 % 2 = 1

def arithmetic_operations(x, y):
    print(f"{x} + {y} = {int(x + y)}")
    print(f"{x} - {y} = {int(x - y)}")
    print(f"{x} * {y} = {int(x * y)}")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} // {y} = {int(x // y)}")
    print(f"{x} % {y} = {int(x % y)}")

while True:
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

arithmetic_operations(x, y)


# # 6 გადააქციეთ დავალება #4 ფუნქციად,
# რომელსაც ექნება 2 პარამეტრი სიმაღლე, სიგანე

def rectangle(height, width):
    for _ in range(height):
        for _ in range(width):
            print("#", end=" ")
        print()

print("Enter height and width of rectangle:")

while True:
    height = input("Height: ")
    width = input("Width: ")
    if height.isdigit() and width.isdigit():
        height = int(height)
        width = int(width)
        break
    else:
        print("Invalid input. Please enter valid integers.")

rectangle(height, width)

# # 7 დაწერეთ ფუნქცია, რომელიც მიიღებს 2 პარამეტრს:
# სტრიქონს და სიმბოლოს ფუნქციამ უნდა დაითვალოს თუ რამდენჯერ გვხვდება სიმბოლო სტიქონში.
# მაგალითი:
# in_str("John and Jane Doe", "J")
# >> > Character "J" in given string: 2 times

def count_character(in_str, char):
    count = in_str.count(char)
    print(f'Character "{char}" in given string: {count} times')


count_character("John and Jane Doe", "J")

# # 8 დაწერეთ ფუნქცია რომელიც დაითვლის სიტყვების რაოდენობას წინადადებაში.
# მაგალითი:
# wc("რამდენიმე სიტყვა რომლის დათვლასაც ვაპირებთ")
# >> > სიტყვების რაოდენობა წინადადებაში შეადგენს 5-ს.

def word_count(sentence):
    words = sentence.split()
    count = len(words)
    print(f"სიტყვების რაოდენობა წინადადებაში შეადგენს {count}-ს.")

word_count("რამდენიმე სიტყვა რომლის დათვლასაც ვაპირებთ")

# # 9 შექმენი თამაში hangman სიტყვის გამოცნობა...
# კომპიუტერი ირჩევს “შემთხვევით” სიტყვას და მომხმარებელს აქვს 10 ცდა სიტყვის გამოსაცნობად,
# მომხმარებელს აქვს ასოების ჩაწერის უფლება და ასევე სიტყვის ჩაწერის უფლება სრულად, თუ
# სიტყვას 10 ცდაში გამოიცნობს გამოიტანოს “გილოცავ” თუ ვერ გამოიტანოს “თქვენ დამარცხდით”
# თამაშის გამორთვა “exit”

import requests

url = "https://random-words-api.kushcreates.com/api?language=en&words=1"
response = requests.get(url)
data = response.json()
word = data[0]["word"].lower()

attempts = 10
guessed_letters = []

print("         HANGMAN         ")
print("type 'exit' to stop game")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print(f"\nWord: {display}")

    if "_" not in display:
        print("You Guessed Word!!!")
        break

    opinion = input("Guess a letter or the whole word: ").lower()

    if opinion == word:
        print("You Guessed Word!!!")
        break
    elif len(opinion) == 1:
        if opinion in word:
            if opinion not in guessed_letters:
                guessed_letters.append(opinion)
                print("Correst letter!")
                attempts -= 1
                print(f"Attempts left: {attempts}")
            else:
                print("Already guessed!")
                attempts -= 1
                print(f"Attempts left: {attempts}")
        else:
            attempts -= 1
            print("Wrong letter!")
            print(f"Attempts left: {attempts}")
    else:
        attempts -= 1
        print("Wrong word!")
        print(f"Attemots left: {attempts}")

else:
    print(f"\n You lost the game! The word was: {word}")

# # 10 შექმენი პატარა თამაში სადაც მომხმარებელს აქვს ორი არჩევანი “მარჯვენა” ან “მარცხენა”
# პროგრამამ შემთხვევითობის პრინციპით უნდა გაანაწილოს რომელია სწორი “მარჯვენა” თუ
# “მარცხენა”, თუ მომხმარებელი 5 ცდიდან ყველა სწორ მიმართულებას აირჩევს გამოიტანე
# “გამარჯვება” სხვა შემთხვევაში “შენ დამარცხდი”, თამაშის გამორთვა “exit”

import random

attempts = 5
correct_guesses = 0

while attempts > 0:

    user_input = input(
        "Choose 'right' or 'left' (type 'exit' to quit): "
    ).lower()

    if user_input == "exit":
        print("Game ended.")
        break

    if user_input != "right" and user_input != "left":
        print("Invalid choice!")
        continue

    correct_direction = random.choice(["right", "left"])
    print(f"Correct direction was: {correct_direction}")

    if user_input == correct_direction:
        print("Correct choice!")
        correct_guesses += 1
    else:
        print("Wrong choice!")
    attempts -= 1
    print(f"Attempts left: {attempts}")
    
if correct_guesses == 5:
    print("Victory!")
elif attempts == 0:
    print("You lost!")
