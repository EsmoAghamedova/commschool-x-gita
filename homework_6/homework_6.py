import calendar
from datetime import datetime, timedelta
import calendar
from itertools import permutations, combinations

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

mylist = [1, 2, 3, 4, 5]
combinations_list = list(combinations(mylist, 3))

print(combinations_list)