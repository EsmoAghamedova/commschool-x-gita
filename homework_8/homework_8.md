#1 SQL დავალება
გამოიტანე ProductName, CategoryID, Unit, Price ცხრილი- “პროდუქტები
”
სადაც ფასი მოთავსებული 18-სა და 25-ს შორის
დაალაგე კლებადობით ფასის მიხედვით

```sql
SELECT ProductName, CategoryID, Unit, Price 
FROM Products
WHERE Price BETWEEN 18 AND 25
ORDER BY Price DESC;
```

#2 SQL დავალება2
გამოიტანე ყველა ველი, სადაც რაოდენობა ტოლია 15-ის ან 12-ის
დაალაგე ზრდადობით
ცხრილი - “OrderDetails”

```sql
SELECT *
FROM OrderDetails
WHERE Quantity IN (12, 15)
ORDER BY Quantity ASC;
```

#3 მოცემულია JSON მასივი:
[
{"id": 1, "price": 50},
{"id": 2, "price": 200},
{"id": 3, "price": 150}
]
ამოიღე მხოლოდ ის პროდუქტები, რომელთა ფასი 100-ზე მეტია.

#4 მოცემულია რთული JSON:
{
"company": {
"departments": [
{"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
{"name": "HR", "employees": [{"name": "Nino"}]}
]
}
}
ამოიღე ყველა თანამშრომლის სახელი

#5 მოცემულია სტუდენტების სია:
[
{"name": "Ana", "grades": [90, 80, 95]},
{"name": "Beka", "grades": [70, 85, 88]},
{"name": "Nino", "grades": [100, 95, 99]}
]

იპოვე სტუდენტი, რომელსაც აქვს საშუალო ქულის მიხედვით საუკეთესო
შედეგი.

#6 მოცემულია კომპანიების სია:
{
"companies": [
{
"name": "TechCorp",
"employees": [
{"name": "Ana", "salary": 3000},
{"name": "Beka", "salary": 4500}
]
},
{
"name": "SoftPlus",
"employees": [
{"name": "Nino", "salary": 5000},
{"name": "Giorgi", "salary": 2500}
]
}
]
}
იპოვე ყველა თანამშრომელი, რომლის ხელფასი მეტია 4000-ზე და დაბეჭდე
მათი სახელები + კომპანიის სახელი.

#7 გააგზავნე GET მოთხოვნა https://jsonplaceholder.typicode.com/users და
დაბეჭდე პირველი მომხმარებლის სახელი.

#8 გააგზავნე POST მოთხოვნა https://jsonplaceholder.typicode.com/posts და
შექმენი ახალი პოსტი შემდეგი მონაცემებით:
{"title": "Test", "body": "Hello World", "userId": 5}

#9 წამოიღე ყველა TODO task და დაბეჭდე მხოლოდ ის, სადაც "completed": False -
https://jsonplaceholder.typicode.com/todos
ბოლოს დათვალე რამდენი შეუსრულებელი ტასკია (რაოდენობაში)

#10 ამოიღე ყველა პოსტი https://jsonplaceholder.typicode.com/posts, შემდეგ
იპოვე ავტორის სახელი (users API-დან) და დაბეჭდე:
"Post Title – Author Name"
გამოიტანე მხოლოდ პირველი 5