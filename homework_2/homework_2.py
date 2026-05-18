from datetime import date

# 1. შეინახეთ ცვლადებში ცვლადების ტიპები მათი მნიშვნელობების ნაცვლად
# var1 = 1
# var2 = -1
# var3 = True
# print(var1, var2, var3)

var1 = "1 --> intenger"
var2 = "-1 --> intenger"
var3 = "True --> boolean"

print(var1, var2, var3)
print(f"\n")


# 2. შეცვალეთ ცვლადების ტიპები(type casting-ის მეშვეობით)
# var4 = False  # გადაიყვანეთ Float -ში
# var5 = 3  # გადაიყვანეთ Float -ში
# var6 = {"key": "value", "key1": "value",
#         "key3": "value"}  # გადაიყვანეთ list -ში
# print(var4, var5, var6)

var4 = float(False)
var5 = float(3)
var6 = list({"key": "value", "key1": "value", "key3": "value"})
print(var4, var5, var6)
print(f"\n")



# 3. შექმენით შესაფერისი ტიპის ცვლადები მონაცემებისთვის.
# group:
# name: Python2023
# count: 35
# male: 22
# female: 13
# students: Student1, Student2, Student3, Student4, Student5
# ages: 24, 33, 15, 45, 42

group = {
    "name":"Python2023",
    "count": 35,
    "male": 22,
    "female": 13,
    "students": ["student1", "student2", "student3", "student4", "student5"],
    "ages": [24, 33, 15, 45, 42] }

print(group)
print(f"\n")



# 4. დააფორმატეთ სტრიქონი და გამოითვალეთ თქვენი ასაკი
# birth_year = 1970  # ჩაწერეთ წელი
# name = ‘სახელი’  # ჩაწერეთ სახელი
# surname = ‘გვარი’  # ჩაწერე გვარი
# current_year = ‘2025’
# # უნდა მიიღოთ შემდეგი წინადადება - მე ‘სახელი’ ‘გვარი’ დავიბადე ‘ამ წელს’ შესაბამისად ვარ
# ‘ამდენი წლის’


today = date.today()

class Person:
    def __init__(self, birth_year, birth_month, birth_day, name, surname):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day

        self.age = today.year - birth_year
        
        if (today.month, today.day) < (birth_month, birth_day):
            self.age -= 1

    def __str__(self):
        return f"მე, {self.name} {self.surname}, დავიბადე {self.birth_year} წელს, შესაბამისად ვარ {self.age} წლის"


me = Person(2009, 8, 6, "ესმირა", "აღამედოვა")
print(me)
print(f"\n")

# 5. გამოითვალეთ მომხრეთა და მოწინააღმდეგეთა პროცენტი და აჩვენეთ ორივე.
# (შეეცადეთ დაამრგვალოთ პროცენტები მეასედებამდე)
# მაგალითი:
# YES: 1234 = 34.80%
# NO: 2312 = 65.20%
# Yes = 119
# No = 82

yes = 119
no = 82
total_votes = yes + no

yes_percentage = (yes / total_votes) * 100
no_percentage = (no / total_votes) * 100

print(f"YES: {yes} = {yes_percentage:.2f}% \n NO: {no} = {no_percentage:.2f}%")
print(f"\n")

# 6. გადაიყვანეთ 3670 წამი საათებად და წუთებად
# seconds = 3670
# დაბეჭდეთ: "X საათი Y წუთი Z წამი"

seconds = 3670

hour = seconds // 3600
minute = (seconds % 3600) // 60
sec = seconds % 60

print(f"{hour} საათი, {minute} წუთი და {sec} წამი")
print(f"\n")



# 7. გამოიტანეთ სტრიქონის პირველი და ბოლო ასო
# text = "Python"

text = "Python"
first = text[0]
last = text[-1]

print(first, last)
print(f"\n")

# 8. გამოითვალეთ სასწავლო საგნის შეფასების პროცენტული წილი
# math = 45
# total = 60
# დაბეჭდეთ: "პროცენტი: XX%"

math = 45
total = 60

percentage = int((math/total) * 100)

print(f"პროცენტი: {percentage}%")
print(f"\n")

# 9. გამოითვალეთ ასაკი მომავალ წელს
# birth_year = 2000
# current_year = 2025
# დაბეჭდეთ ფორმატში:
# “მომავალ წელს შენ იქნები XX წლის”

def age_next_year(birth_year):
    return (today.year - birth_year) + 1

user_birth_year = age_next_year(2009)

print(f"მომავალ წელს შენ იქნები {user_birth_year} წლის")
print(f"\n")
# 10. 350 წუთი რამდენი საათია და რამდენი წუთი დარჩება გამოიტანეთ
# minutes = 350
# მაგალითი: “X საათი და XX წუთი”

#1 საათში არსებული წუთების რაოდენობას ზეოთ მოცემულ თასქში არსებულ ცვლადით გამოვსახავ

minutes = 350 

hour_2 = minutes // 60
minutes_2 = minutes % 60

print(f"{hour_2} საათი და {minutes_2} წუთი")

