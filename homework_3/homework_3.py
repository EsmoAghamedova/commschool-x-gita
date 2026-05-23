# # 1 გაქვთ ონლაინ მაღაზია, როდესაც მომხმარებელი შემოდის პროგრამის გაშვებისას უნდა
# გამოუჩნდეს მენიუ მაგალითად: “გამარჯობა” თქვენ იმყოფებით მაღაზია SpaceX-ში, პროდუქტები:
# რაკეტა - 15000$, ხომალდი - 25000$, ჩაფხუტი - 5000$ და ა.შ. მომხმარებელს უნდა ჰკითხოთ
# რომელი ნივთები უნდა და დაუთვალოთ რა დაუჯდება ჯამურად, თუ დაგეთანხმებათ უნდა მიჰყიდოთ
# ნივთები თუ უარს იტყვის შეთავაზებაზე უნდა დაასრულოთ მუშაობა.

print("“გამარჯობა” თქვენ იმყოფებით მაღაზია SpaceX-ში,\n  პროდუქტები: \nრაკეტა - 15000$, \nხომალდი - 25000$, \nჩაფხუტი - 5000$")

products = {"რაკეტა": 15000,
            "ხომალდი": 25000,
            "ჩაფხუტი": 5000}

cart = []
total = 0

while True:
    user_input = input(
        "აირჩიეთ პროდუქტი.\nთუ გინდათ შენაძენის გაუქმბა/შეწყვეტა დაწერეთ exit.\nთუ დასრულება და ყიდვა გინდათ დაწერეთ purchase\n")

    if user_input == "exit":
        print("პროცესი შეწყდა")
        break

    if user_input == "purchase" and cart != {}:
        print(f'თქვენი შენაძენი: {str(cart)}, სულ დაგიჯდათ: {total}')
        break

    if user_input not in products:
        print("ასეთი პროდუქტი არ მოიძებნება")
        continue

    if user_input in products:
        cart.append(user_input)

        total += products[user_input]
        print(
            f'კალათაში დაემატა: {user_input}\nკალათაშია: {str(cart)}, ჯამში გიჯდებათ: {total}')

# # 2 While loop და FOR LOOP-ის გამოყენებით დაწერეთ ციკლი, რომელიც დაბეჭდავისას, გვერდით
# დაუწერს რიცხვს ლუწია თუ კენტი 20-მდე. (დაწერეთ ორივე ვარიანტი)

i = 1

while i < 21:
    if i % 2 == 0:
        print(f'{i}: even')
    else:
        print(f'{i}: odd')

    i += 1

for i in range(1, 21):
    if i % 2 == 0:
        print(f'{i}: even')
    else:
        print(f'{i}: odd')

# # 3 გამოითვალეთ თითოეული სტუდენტის საშუალო არითმეტიკული ქულა და დააბრუნეთ მისთვის
# შესაფერისი ნიშანი:

# Students = {
#     “Ana”: [89, 66, 12, 75, 11],
#     “Giorgi”: [67, 72, 90, 91, 55],
#     “Levant”: [49, 36, 88, 98, 34],
#     “Veronika”: [99, 88, 32, 65, 99],
#     “Nika”: [77, 81, 41, 73, 99]
# }
# Print(students)

students = {
    "Ana": [89, 66, 12, 75, 11],
    "Giorgi": [67, 72, 90, 91, 55],
    "Levant": [49, 36, 88, 98, 34],
    "Veronika": [99, 88, 32, 65, 99],
    "Nika": [77, 81, 41, 73, 99]
}

for i in students:
    sashualo = sum(students[i]) / len(students[i])
    print(i,":" ,sashualo)


# # 4 დაწერეთ ციკლი, რომელიც მოითხოვს მომხმარებლისგან ასაკის შეყვანას, თუ შეყვანილი
# მონაცემი არ იქნება რიცხვური ტიპის, მაშინ ციკლი დატრიალდეს და თავიდან კითხოს, სხვაგვარად
# დაუანგარიშოს დაბადების თარიღი.

while True:
    age = input("შეიყვანეთ თქვენი ასაკი: ")

    if age.isdigit():
        birth_year = 2026 - int(age)
        print(f"შენ დაიბადე {birth_year}")
        break
    else: print("არასწორი მონაცემი, რიცხვი ჩაწერეთ")
    continue

# # 5 While ციკლის მეშვეობით დაითვალეთ მოცემული მასივის:
# mylist = range(100)
# *მეორე ხარისხი
# *მესამე ხარისხი

i = 1
mylist = range(100)

while i < len(mylist) + 1:
    square = i ** 2
    cube = i ** 3

    print(f"{i} კვადრატშია არის {square} და კუბშია {cube}" )
    i += 1

# # 6 FOR ციკლის/ციკლების გამოყენებით შექმენი გამრავლების ტაბულა და ტერმინალში გამოიტანე
# მსგავსი ფორმატით:
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# 4 8 12 16 20 24 28 32 36 40
# 5 10 15 20 25 30 35 40 45 50
# 6 12 18 24 30 36 42 48 54 60
# 7 14 21 28 35 42 49 56 63 70
# 8 16 24 32 40 48 56 64 72 80
# 9 18 27 36 45 54 63 72 81 90
# 10 20 30 40 50 60 70 80 90 100

for i in range(1,11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()

# # 7 გააანალიზე კოდის ფრაგმენტი და შემდეგ გაასწორე შეცდომები, ასევე დაწერე ახსნა:
# numbers = ["1", "2", "3", "4"]
# total = 0

# for n in numbers:
# total += n
# print("Total:", total)

numbers = [1, 2, 3, 4]
total = 0

for n in numbers:
    total += n
    
print("Total:", total)


# # 8 გამოიყენე FOR ციკლი რომელიც მიწვდება data ყველა ელემენტს და დაწერე შემდეგი ლოგიკა, თუ
# ელემენტი არის სტრინგი და შეიცავს მხოლოდ რიცხვს გადააქციე რიცხვად და შეინახე total-ში, თუ
# რიცხვია პირდაპირ შეინახე total-ში, თუ სხვა ტიპის მონაცემთა ტიპია გამოტოვე. ბოლოს დაბეჭდე
# სრული ჯამი.

# data = [“5”, 0, "3", True, "", 2, "x", False]
# total = 0

data = ["5", 0, "3", True, "", 2, "x", False]
total = 0

for i in data:
    if type(i) == int:
        total += int(i)
    elif type(i) == str and i.isdigit():
        total += int(i)
    else: continue
print(total)
        

# # 9 დაწერეთ FOR LOOP სადაც მიწვდებით მონაცემებს, თუ მნიშვნელობა არის სტრინგი და შეიცავს
# მხოლოდ რიცხვს გამოიყენე კასტინგი და შეინახე, თუ ინთეჯერია შეინახე პირდაპირ, თუ ბულიენია
# გადააქციე და შეინახე(მხოლოდ True) სხვა ყველა ტიპის მონაცემი გამოტოვე.

# transactions = {
#     “გიო”: "100",
#     “ნიკა”: 50,
#     “აკაკი”: "30a",
#     “ლევანი”: 0,
#     “ანა”: "70",
#     “მარი”: True
# }
# total = 0

transactions = {
    "გიო": "100",
    "ნიკა": 50,
    "აკაკი": "30a",
    "ლევანი": 0,
    "ანა": "70",
    "მარი": True
}

total = 0

for value in transactions.values():

    if type(value) == bool:
        if value == True:
            total += 1
        continue

    elif type(value) == int:
        total += value

    elif type(value) == str:
        if value.isdigit():
            total += int(value)

print(total)

# # 10 შექმენი პროგრამა (თამაში) სადაც მომხმარებელი შეძლებს გამოიცნოს შენი ჩაწერილი რიცხვი,
# მომხმარებელი წერს ციფრებს და ცდილობს გამოიცნოს შენი რიცხვი, დიაპაზონი 0-დან 51-მდე, თუ
# მომხმარებელმა ჩაწერა ამ დიაპაზონს გარეთ უნდა გამოუტანო შეტყობინება რომ “რიცხვი სცდება
# არეალს”, თუ ჩაწერა “exit” გამორთე თამაში, უნდა დაუთვალო მცდელობების რაოდენობა და
# გამოიტანო შეტყობინება: “გილოცავ გამოიცანი XX რიცხვი, მცდელობა: XX”

import random

num = random.randint(1, 51)
attempts = 0

while True:
    user_ans = input("guess number: ")

    if user_ans == "exit":
        print("game over")
        break

    if int(user_ans) < 1 or int(user_ans) > 51 :
        print("this number is out off zone")
        attempts += 1
        continue
    elif int(user_ans) != num:
        print("try again")
        attempts += 1
    else:
        print(f"congratulations you guessed {num} number, attempts: {attempts}")
        break
