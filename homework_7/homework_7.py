import random

# # 1 შექმენი გენერატორი, რომელიც ტექსტის თითოეულ სიმბოლოს აბრუნებს.
# Word = “CODE”

word = "CODE"
def word_generator(word):
    for letter in word:
        yield letter
for letter in word_generator(word):
    print(letter)

# # 2 დაწერე პროგრამა რომელშიც მომხმარებელი შემოიყვანს მხოლოდ ციფრებს, ლოგიკა
# უნდა იყოს შემდეგი: გვაქვს კონკრეტული ლისტი და მომხმარებელი უნდა მიწვდეს
# შემოყვანილი ციფრით რომელიმე ელემენტს, თუ ვერ მიწვდება პროგრამა შეცდომაზე არ
# უნდა გავიდეს.
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
try:
    user_input = int(input("შეიყვანეთ რიცხვი: "))
    print(arr[user_input])
except ValueError:
    print("გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი.")
except IndexError:
    print("ასეთი ინდექსი ლისტში არ არსებობს.")
finally:
    print("End")


# # 3 შექმენი დეკორატორი, რომელიც ითვლის რამდენჯერ გამოიძახეს ფუნქცია.
# მაგალითი:
# @counter
# def say():


# print("Hi")
# say()
# say()
# გამოძახება: 1
# Hi
# გამოძახება: 2
# Hi

def counter(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print(f"called: {count}")
        func()
    return wrapper

@counter
def say():
    print("Hi")

say()
say()
say()


# # 4 მომხმარებელს უნდა დავუსვათ 5 მათემატიკური შეკითხვა, თითოეულზე სწორი
# პასუხი არის 10 ქულა ხოლო არასწორი 0 ქულა, მიღებული პასუხებიდან უნდა
# განვსაზღვროთ რამდენი ქულა აიღო მომხმარებელმა, შევქმნათ ლოფ ფაილი
# game.log და შევინახოთ ყველა ქულა. ბოლოს გამოვუტანოთ მიღებული შედეგი

questions = {
    "2 + 2": 4,
    "5 * 3": 15,
    "10 - 7": 3,
    "8 / 2": 4,
    "6 + 6": 12
}

point = 0

for i in questions:
    print(i)
    user_ans = int(input("answer: "))
    if user_ans == questions[i]:
        point += 10
    else:
        print("wrong")
        continue

with open("game.log", "a") as file:
    file.write(f"score: {point}\n")

# # 5 შექმენით ფაილი quiz.log, შექმენით გენერატორი რომელშიც შენახული იქნება
# 5 შეკითხვა და სათითაოდ დააბრუნებს, მომხმარებელმა უნდა უპასუხოს ყველა
# შეკითხვას და პასუხები შეინახეთ ლოგ ფაილში.

questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the chemical symbol for water?": "H2O",
    "what is the tallest mountain in the world?": "Mount Everest",
    "What is the currency of Japan?": "Yen"
}

def question_generator(questions):
    for question in questions:
        yield question

with open("quiz.log", "a") as file:
    for question in question_generator(questions):
        print(question)
        user_ans = input("answer: ")
        file.write(f"question: {question} answer: {user_ans}\n")

# # 6 შექმენი პროგრამა სადაც მომხმარებელი ეჯიბრება კომპიუტერს: ქვა/ბადე/
# მაკრატელის თამაშში, თამაში არის სამამდე, კომპიუტერი შემთხვევითობის
# პრინციპით ირჩევს ამ სამიდან 1-ს, ასევე ტერმინალში მომხმარებელი წერს ერთ-
# ერთს, ერთნაირის შემთხვევაში ფრეა და გრძელდება თამაში 3-მდე, ვინც პირველი
# მიაღწევს 3-ს გამოიტანე შეტყობინება .....-მ გაიმარჯვა, ყველა ნათამაშები ხელი
# უნდა შეინახოო ლოგირების ფაილში.

choices = ["rock", "paper", "scissors"]
computer_score = 0
user_score = 0

while computer_score < 3 and user_score < 3:
    computer_choice = random.choice(choices)
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    if computer_choice == user_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Computer chose: {computer_choice}")
    print(f"Score: You {user_score} - {computer_score} Computer")

    with open("game_1.log", "a") as file:
        if user_score == 3:
            file.write("Winner: User\n")
        else:
            file.write("Winner: Computer\n")

# # 7 პროგრამა კამათელზე - გვყავს ორი მომხმარებელი Gamer 1 & Gamer 2,
# თითოეულს უნდა გავაგორებინოთ კამათელი თითო თითოჯერ, თუ ფრეა ვიმეორებთ,
# სხვა შემთხვევაში მოგებულ მოთამაშეს უნდა ვკითხოთ კიდევ 1 შანსს მისცემს თუ
# არა წაგებულს და კიდევ გააგორებს თუ არა, თუ უარია ვამთავრებთ, თუ თანახმაა
# იგივე ლოგიკა უნდა გაგრძელდეს სანამ უარს არ იტყვის ერთ-ერთი.


while True:
    gamer1 = random.randint(1, 6)
    gamer2 = random.randint(1, 6)

    print(f"Gamer 1: {gamer1}")
    print(f"Gamer 2: {gamer2}")

    if gamer1 == gamer2:
        print("ფრე! თავიდან ვაგორებთ.\n")
        continue

    if gamer1 > gamer2:
        winner = "Gamer 1"
    else:
        winner = "Gamer 2"

    print(f"{winner} გაიმარჯვა!")

    choice = input(
        f"{winner}, კიდევ შანსს აძლევ მოწინააღმდეგეს? (yes/no): "
    ).lower()

    if choice == "no":
        print("თამაში დასრულდა.")
        break

# # 8 შექმენი პროგრამა სადაც გექნება გადაცემული 10 სიტყვა ლისტში და ლოგიკა
# არის შემდეგი, ამ სიტყვებიდან 2 ცალს ირჩევ შემთხვევითობის პრინციპით და
# თითოეული სიტყვიდან უნდა ამოაკლო 2 ასო და მომხმარებელს აჩვენო მსგავსი
# ფორმით და უთხრა რომ გამოიცნოს სიტყვა და ჩაწეროს სრულად, თუ გამოიცნო
# “გამარჯვება” თუ ვერ გამოიცნო ვერცერთი სიტყვა “დამარცხდი”, ერთის
# გამოცნობის შემთხვევაში “50 % ”


words = [
    "python", "computer", "keyboard", "monitor", "internet",
    "programming", "school", "student", "teacher", "javascript"
]

selected_words = random.sample(words, 2)

hidden_words = []

for word in selected_words:
    indexes = random.sample(range(len(word)), 2)

    new_word = ""
    for i in range(len(word)):
        if i not in indexes:
            new_word += word[i]

    hidden_words.append(new_word)

print("გამოიცანი სიტყვები:")
print("1.", hidden_words[0])
print("2.", hidden_words[1])

score = 0

answer1 = input("პირველი სიტყვა: ")
if answer1.lower() == selected_words[0].lower():
    score += 1

answer2 = input("მეორე სიტყვა: ")
if answer2.lower() == selected_words[1].lower():
    score += 1

if score == 2:
    print("გამარჯვება!")
elif score == 1:
    print("50%")
else:
    print("დამარცხდი!")
