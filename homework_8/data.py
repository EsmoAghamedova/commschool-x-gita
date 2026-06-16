import json
import requests
# # 3 მოცემულია JSON მასივი:
# [
#     {"id": 1, "price": 50},
#     {"id": 2, "price": 200},
#     {"id": 3, "price": 150}
# ]
# ამოიღე მხოლოდ ის პროდუქტები, რომელთა ფასი 100-ზე მეტია.

with open("data.json", "r") as file:
    data = json.load(file)

products = data["task3"]

filtered_products = [
    product for product in products
    if product.get("price", 0) > 100
]

print("Filtered prdoducts: ")
for product in filtered_products:
    print(product)

# # 4 მოცემულია რთული JSON:
# {
#     "company": {
#         "departments": [
#             {"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
#             {"name": "HR", "employees": [{"name": "Nino"}]}
#         ]
#     }
# }
# ამოიღე ყველა თანამშრომლის სახელი

employees = data["task4"]["company"]["departments"]

employees_names = [
    employee["name"]
    for department in employees
    for employee in department["employees"]
]

print("Employees names: ")
print(employees_names)
# # 5 მოცემულია სტუდენტების სია:
# [
#     {"name": "Ana", "grades": [90, 80, 95]},
#     {"name": "Beka", "grades": [70, 85, 88]},
#     {"name": "Nino", "grades": [100, 95, 99]}
# ]

# იპოვე სტუდენტი, რომელსაც აქვს საშუალო ქულის მიხედვით საუკეთესო
# შედეგი.

students = data["task5"]

best_student = None
best_average = 0

for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    if avg > best_average:
        best_average = avg
        best_student = student["name"]

print("best student:", best_student, best_average)
# # 6 მოცემულია კომპანიების სია:
# {
#     "companies": [
#         {
#             "name": "TechCorp",
#             "employees": [
#                 {"name": "Ana", "salary": 3000},
#                 {"name": "Beka", "salary": 4500}
#             ]
#         },
#         {
#             "name": "SoftPlus",
#             "employees": [
#                 {"name": "Nino", "salary": 5000},
#                 {"name": "Giorgi", "salary": 2500}
#             ]
#         }
#     ]
# }
# იპოვე ყველა თანამშრომელი, რომლის ხელფასი მეტია 4000-ზე და დაბეჭდე
# მათი სახელები + კომპანიის სახელი.

companies = data["task6"]["companies"]

print("high salary employees: ")

for company in companies:
    for employee in company["employees"]:
        if employee["salary"] > 4000:
            print(f"{employee["name"]} - {company["name"]}")
# # 7 გააგზავნე GET მოთხოვნა https://jsonplaceholder.typicode.com/users და
# დაბეჭდე პირველი მომხმარებლის სახელი.

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

print("first user name: ", users[0]["name"])

# # 8 გააგზავნე POST მოთხოვნა https://jsonplaceholder.typicode.com/posts და
# შექმენი ახალი პოსტი შემდეგი მონაცემებით:
# {"title": "Test", "body": "Hello World", "userId": 5}

post_data = {
    "title": "Test",
    "body": "Hello World",
    "userId": 5
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=post_data
)

print("Post response: ", response.json())

# # 9 წამოიღე ყველა TODO task და დაბეჭდე მხოლოდ ის, სადაც "completed": False -
# https: // jsonplaceholder.typicode.com/todos
# ბოლოს დათვალე რამდენი შეუსრულებელი ტასკია(რაოდენობაში)

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todo = response.json()

count = 0

for i in todo:
    if i["completed"] == False:
        count += 1

print(f"uncompleted tasks: {count}")

# # 10 ამოიღე ყველა პოსტი https://jsonplaceholder.typicode.com/posts, შემდეგ
# იპოვე ავტორის სახელი(users API-დან) და დაბეჭდე:
# "Post Title – Author Name"
# გამოიტანე მხოლოდ პირველი 5

posts_response = requests.get("https://jsonplaceholder.typicode.com/posts")
users_response = requests.get("https://jsonplaceholder.typicode.com/users")

posts = posts_response.json()
users = users_response.json()

for post in posts[:5]:
    for user in users:
        if user["id"] == post["userId"]:
            print(f'{post["title"]} - {user["name"]}')
            break
