# Homework 2 — Solutions

This document summarizes the solutions for Homework 2. Each item includes the problem, a concise Python solution, and the expected output.

---

## 1. Store types instead of values

Problem: Save the variable types (not the values).

Solution (excerpt):

```python
var1 = "1 --> intenger"
var2 = "-1 --> intenger"
var3 = "True --> boolean"
print(var1, var2, var3)
```

Expected output:

```
1 --> intenger -1 --> intenger True --> boolean
```

---

## 2. Type casting

Problem: Convert values using type casting.

Solution:

```python
var4 = float(False)
var5 = float(3)
var6 = list({"key": "value", "key1": "value", "key3": "value"})
print(var4, var5, var6)
```

Expected output:

```
0.0 3.0 ['key', 'key1', 'key3']
```

---

## 3. Appropriate data types for group data

Problem: Represent group data in suitable types.

Solution:

```python
group = {
	"name": "Python2023",
	"count": 35,
	"male": 22,
	"female": 13,
	"students": ["student1", "student2", "student3", "student4", "student5"],
	"ages": [24, 33, 15, 45, 42]
}
print(group)
```

Expected output: a dictionary printed with the fields above.

---

## 4. Formatted sentence and age calculation

Problem: Calculate age from birthdate and format a sentence.

Solution (class-based):

```python
from datetime import date

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
```

Expected output: a formatted Georgian sentence with the calculated age.

---

## 5. Percentages of supporters and opponents

Problem: Compute percentages for Yes/No votes and round to two decimals.

Solution:

```python
yes = 119
no = 82
total_votes = yes + no
yes_percentage = (yes / total_votes) * 100
no_percentage = (no / total_votes) * 100
print(f"YES: {yes} = {yes_percentage:.2f}% \n NO: {no} = {no_percentage:.2f}%")
```

Expected output:

```
YES: 119 = 59.22%
 NO: 82 = 40.78%
```

---

## 6. Convert 3670 seconds to hours, minutes, seconds

Solution:

```python
seconds = 3670
hour = seconds // 3600
minute = (seconds % 3600) // 60
sec = seconds % 60
print(f"{hour} საათი, {minute} წუთი და {sec} წამი")
```

Expected output:

```
1 საათი, 1 წუთი და 10 წამი
```

---

## 7. First and last character of a string

Solution:

```python
text = "Python"
first = text[0]
last = text[-1]
print(first, last)
```

Expected output:

```
P n
```

---

## 8. Subject score percentage

Solution:

```python
math = 45
total = 60
percentage = int((math/total) * 100)
print(f"პროცენტი: {percentage}%")
```

Expected output:

```
პროცენტი: 75%
```

---

## 9. Age next year

Solution:

```python
from datetime import date
today = date.today()
def age_next_year(birth_year):
	return (today.year - birth_year) + 1
user_birth_year = age_next_year(2009)
print(f"მომავალ წელს შენ იქნები {user_birth_year} წლის")
```

Expected output (example):

```
მომავალ წელს შენ იქნები 18 წლის
```

---

## 10. Convert 350 minutes to hours and minutes

Solution:

```python
minutes = 350
hour_2 = minutes // 60
minutes_2 = minutes % 60
print(f"{hour_2} საათი და {minutes_2} წუთი")
```

Expected output:

```
5 საათი და 50 წუთი
```

---

If you want, I can also:

- run the script and include the exact runtime output,
- or commit these changes to a Git branch.
