import calendar
from datetime import datetime, timedelta
import calendar
from itertools import permutations, combinations
import time
import random

# \#1 მოცემულია სიტყვა "ABCD". დაბეჭდე ყველა შესაძლო ვარიანტი და **დაითვალე** რამდენია სულ რაოდენობრივად (უნდა დააბრუნო რიცხვი)
# word = "ABCD"


# word = "ABCD"
# count = 0

# for p in permutations(word):
#     print("".join(p))
#     count += 1

# print(f"სულ: {count}")

# \#2 იპოვე მომდევნო კვირის პირველი სამშაბათი, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)


# today = datetime.today()

# weekday = today.weekday()
# tuesday_day = 1

# day = (tuesday_day - weekday) % 7

# if day == 0:
#     day = 7

# next_tuesday = today + timedelta(days=day)

# print(next_tuesday)


# \#3 დაადგინე, არის თუ არა შეყვანილი წელი ნაკიანი, მომხმარებელს შემოჰყავს მხოლოდ წელი და ვეუბნებით არის თუ არა ნაკიანი

# myinput = ...

# myinput = input("შეიყვანეთ წელი: ")

# if calendar.isleap(int(myinput)) == True:
#     print(f"{myinput} არის ნაკიანი წელი")
# else:
#     print(f"{myinput} არ არის ნაკიანი წელი")


# \#4 დაითვალე რამდენი კვირაა დარჩენილი ახალ წლამდე, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)

# today = datetime.today()
# next_year = datetime(today.year + 1, 1, 1)
# days_until_new_year = (next_year - today).days
# weeks_until_new_year = days_until_new_year // 7

# print(f"ახალ წლამდე დარჩენილი კვირების რაოდენობა: {weeks_until_new_year}")


# \#5 შექმენი ყველა 3-ელემენტიანი კომბინაცია სიიდან \[1,2,3,4,5] (itertools-ის გამოყენებით)

# mylist = [1, 2, 3, 4, 5]
# combinations_list = list(combinations(mylist, 3))

# print(combinations_list)


# \#6 მიიღე ყველა კომბინაცია "XYZ"-ის სიმბოლოებით სიგრძე 1-დან 3-მდე
# მაგალითი: X, Y, Z, XY, XZ, YZ, XYZ უნდა მივიღოთ მსგავსი შედეგი.


# symbols = ['X', 'Y', "Z"]

# for i in range(1,4):
#     for combo in combinations(symbols, i):
#         print("".join(combo))

# \#7 თამაში უკუსვლაზე
# კომპიუტერი ირჩევს შემთხვევითობის პრინციპით რიცხვს 1-20 მდე, მოთამაშეს აქვს მხოლოდ 5 წამი რიცხვის გამოსაცნობად, თუ 5 წამში სწორ რიცხვს ვერ შეიყვანს, თამაში სრულდება და გამოდის ტექსტი "დრო ამოიწურა, თქვენ დამარცხდით".
# from datetime import datetime, timedelta
# import time, random

# num = random.randint(1, 20)
# print("გამოიცანი რიცხვი 1-დან 20-მდე 5 წამში.")

# end_time = datetime.now() + timedelta(seconds=5)

# while datetime.now() < end_time:
#     try:
#         user_ans = int(input("number: "))

#         if user_ans == num:
#             print("it's correct")
#             break

#         else:
#             print("it's not correct")

#     except ValueError:
#         print("only number")

# else:
#     print("time out")


# \#8 ორი მოთამაშე იწყებს "გარბენს". უნდა შეამოწმო რომელი დაასრულებს ნაკლებ დროში
# player1 = start + timedelta(seconds=random.randint(5,20))
# player2 = start + timedelta(seconds=random.randint(5,20))

start = datetime.now()

player1 = start + timedelta(seconds=random.randint(5, 20))
player2 = start + timedelta(seconds=random.randint(5, 20))

if player1 > player2:
    print("winner player 2")
elif player1 < player2:
    print("winner player 1")
else:
    print("draw")

# \#9 იღბლიანი დაბადების დღე
# მოთამაშემ უნდა შეიყვანოს დაბადების თარიღი და თამაში დაითვლის რამდენი დღეა დარჩენილი შემდეგ დაბადების დღემდე

from datetime import date

while True:
    birthday_input = input("შეიყვანე დაბადების თარიღი (YYYY-MM-DD): ").strip()

    try:
        birthday = date.fromisoformat(birthday_input)
        break
    except ValueError:
        print("არასწორი ფორმატია. გამოიყენე YYYY-MM-DD.")

today = date.today()
next_birthday = date(today.year, birthday.month, birthday.day)

if next_birthday == today:
    print("გილოცავ დაბადების დღეს!")
elif next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)
    days_left = (next_birthday - today).days
    print(f"შემდეგ დაბადების დღემდე დარჩენილია {days_left} დღე.")
else:
    days_left = (next_birthday - today).days
    print(f"შემდეგ დაბადების დღემდე დარჩენილია {days_left} დღე.")



# \#10 საცავი - ჯუნიორ ჰაკერი :)
# თამაში არის შემდეგი - გვაქვს სეიფი რომელსაც აქვს ციფრები 1-6 მდე პაროლი არ ვიცით, ყოველ დღე კომპიუტერი აგენერირებს ახალ პაროლს
# შემთხვევითობის პრინციპით. პაროლი არის 4 ციფრიანი. ჩვენი მიზანია დავწეროთ ისეთი კოდი რომელიც შეამოწმებს ვარიანტებს და როცა მოხდება
# კომპიუტერის მიერ დაგენერირებული პაროლის დამთხვევა უნდა გამოვიტანოთ შეტყობინება "პაროლი სწორია, საცავი გახსნილია", აუცილებელი პირობაა
# გამოვიტანოთ ყველა ჩვენს მიერ ნაცადი პაროლი სანამ მივალთ სწორ ვარიანტამდე.

from itertools import product

target_password = "".join(random.choice("123456") for _ in range(4))

for attempt in product("123456", repeat=4):
    attempt_password = "".join(attempt)
    print(attempt_password)

    if attempt_password == target_password:
        print("პაროლი სწორია, საცავი გახსნილია")
        break
