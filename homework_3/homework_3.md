# Homework 3 — Solutions

This document summarizes the solutions for Homework 3. Each item includes the problem, a concise Python solution (excerpt), and the expected output. Code excerpts are taken from `homework_3.py`.

---

## 1. Shop simulation (CLI)

Problem: Show products, let the user pick items, accumulate a cart and total; support `exit` to cancel and `purchase` to finish.

Solution (excerpt):

```python
print("გამარჯობა თქვენ იმყოფებით მაღაზია SpaceX-ში,\n  პროდუქტები: \nრაკეტა - 15000$, \nხომალდი - 25000$, \nჩაფხუტი - 5000$")

products = {"რაკეტა": 15000, "ხომალდი": 25000, "ჩაფხუტი": 5000}
cart = []
total = 0

while True:
	user_input = input("აირჩიეთ პროდუქტი (exit, purchase): \n")
	if user_input == "exit":
		print("პროცესი შეწყდა")
		break
	if user_input == "purchase" and len(cart) > 0:
		print(f'თქვენი შენაძენი: {cart}, სულ დაგიჯდათ: {total}')
		break
	if user_input not in products:
		print("ასეთი პროდუქტი არ მოიძებნება")
		continue
	cart.append(user_input)
	total += products[user_input]
	print(f'კალათაში დაემატა: {user_input}\nკალათაშია: {cart}, ჯამში გიჯდებთ: {total}')
```

Expected behavior: interactive additions to `cart`, total updates; `exit` cancels, `purchase` prints the cart and total.

---

## 2. Even / Odd up to 20

Problem: Print numbers 1..20 with a tag whether each is even or odd using `while` and `for`.

Solution:

```python
# while
i = 1
while i <= 20:
	print(f"{i}: {'even' if i % 2 == 0 else 'odd'}")
	i += 1

# for
for i in range(1, 21):
	print(f"{i}: {'even' if i % 2 == 0 else 'odd'}")
```

Expected output (excerpt):

```
1: odd
2: even
...
20: even
```

---

## 3. Students' average scores

Problem: Compute each student's arithmetic mean and print it.

Solution:

```python
students = {
	"Ana": [89, 66, 12, 75, 11],
	"Giorgi": [67, 72, 90, 91, 55],
	"Levant": [49, 36, 88, 98, 34],
	"Veronika": [99, 88, 32, 65, 99],
	"Nika": [77, 81, 41, 73, 99]
}

for name, scores in students.items():
	avg = sum(scores) / len(scores)
	print(name + ':', avg)
```

Expected output (example):

```
Ana: 50.6
Giorgi: 75.0
...
```

---

## 4. Age input validation and birth year

Problem: Ask user for age until a numeric value is entered, then compute birth year.

Solution:

```python
while True:
	age = input("შეიყვანეთ თქვენი ასაკი: ")
	if age.isdigit():
		birth_year = 2026 - int(age)   # consider using datetime for current year
		print(f"შენ დაიბადე {birth_year}")
		break
	else:
		print("არასწორი მონაცემი, რიცხვი ჩაწერეთ")
```

Expected interaction: repeats until numeric input, then prints birth year.

---

## 5. Squares and cubes (while loop)

Problem: For numbers in `range(1, 100)` print square and cube using a `while` loop.

Solution:

```python
i = 1
mylist = range(100)
while i <= len(mylist):
	square = i ** 2
	cube = i ** 3
	print(f"{i} squared is {square} and cubed is {cube}")
	i += 1
```

Expected output (excerpt):

```
1 squared is 1 and cubed is 1
2 squared is 4 and cubed is 8
...
```

---

## 6. Multiplication table (10x10)

Problem: Print a 10x10 multiplication table.

Solution:

```python
for i in range(1, 11):
	for j in range(1, 11):
		print(i * j, end=" ")
	print()
```

Expected output (first 4 rows shown):

```
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
4 8 12 16 20 24 28 32 36 40
```

---

## 7. Fix summing bug

Problem: Original code attempted to sum strings; fix it so `total` sums numeric values.

Solution (fixed):

```python
numbers = [1, 2, 3, 4]
total = 0
for n in numbers:
	total += n
print("Total:", total)
```

Expected output:

```
Total: 10
```

---

## 8. Sum mixed data types from a list

Problem: Iterate `data` and add numeric values: convert digit-only strings to int, add ints, skip others.

Solution:

```python
data = ["5", 0, "3", True, "", 2, "x", False]
total = 0
for item in data:
	if isinstance(item, bool):
		# Only True counts as 1
		total += int(item)
	elif isinstance(item, int):
		total += item
	elif isinstance(item, str) and item.isdigit():
		total += int(item)
print(total)
```

Expected output:

```
11
```

---

## 9. Transactions aggregation

Problem: Iterate `transactions` values. Add integers, convert numeric strings, count `True` as 1, skip others.

Solution:

```python
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
	if isinstance(value, bool):
		total += int(value)
	elif isinstance(value, int):
		total += value
	elif isinstance(value, str) and value.isdigit():
		total += int(value)
print(total)
```

Expected output:

```
221
```

---

## 10. Number guessing game

Problem: User guesses a random number in the given range, type `exit` to quit. Track attempts and report when guessed.

Solution (excerpt):

```python
import random
num = random.randint(1, 51)
attempts = 0
while True:
	user_ans = input("guess number: ")
	if user_ans == "exit":
		print("game over")
		break
	try:
		guess = int(user_ans)
	except ValueError:
		print("Enter a valid integer or 'exit'")
		continue
	if guess < 1 or guess > 51:
		print("this number is out of zone")
		attempts += 1
		continue
	attempts += 1
	if guess != num:
		print("try again")
	else:
		print(f"congratulations you guessed {num} number, attempts: {attempts}")
		break
```

Expected interaction: multiple guesses until correct; prints attempts on success.

---

If you want, I can run the script and capture sample runs, or update `homework_3.py` to add the small input-validation improvements noted above.
