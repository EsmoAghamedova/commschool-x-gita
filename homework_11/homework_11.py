# # 1 ლაბირინთი
# გვაქვს მოცემული მსგავსი ლაბირინთი:
# maze = [
#     ["S", ".", "#", ".", "."],
#     ["#", ".", "#", ".", "#"],
#     [".", ".", ".", ".", "."],
#     ["#", "#", "#", ".", "#"],
#     [".", ".", ".", ".", "E"]
# ]
# S -> არის საწყისი წერტილი
# E -> არის საბოლოო წერტილი
# # -> არის კედელი
# . -> არის გზა, რომელიც უნდა გაიაროს მომხმარებელმა
# თქვენი მიზანია დაწეროთ ლოგიკა სადაც მომხმარებელს შეეკითხებით რომელ მხარეს უნდა წასვლა:
# მაღლა, დაბლა, მარცხნივ, მარჯვნივ. თუ სწორად აირჩევს უნდა უთხრა რომ სწორად მიდის და კიდევ
# ჰკითხო ახლა რომელ მხარეს უნდა წასვლა, არასწორი გზის არჩევის შემთხვევაში უნდა დააწყებინო
# თავიდან თამაში და ისევ ჰკითხო სად წავა, თუ გავა ბოლოში უნდა დაუწერო რომ “შენ გაიარე
# ლაბირინთი” ვალიდაცია არაა საჭირო მომხმარებელს სწორად შეჰყავს სიტყვები.

# maze = [
#     ["S", ".", "#", ".", "."],
#     ["#", ".", "#", ".", "#"],
#     [".", ".", ".", ".", "."],
#     ["#", "#", "#", ".", "#"],
#     [".", ".", ".", ".", "E"]
# ]

# start_position = (0, 0)

# rows = len(maze)
# cols = len(maze[0])

# row, col = start_position
# while True:
#     direction = input(
#         "რომელ მხარეს უნდა წასვლა? (up, down, left, right): ").strip().lower()

#     new_row = row
#     new_col = col

#     if direction == "up":
#         new_row -= 1
#     elif direction == "down":
#         new_row += 1
#     elif direction == "left":
#         new_col -= 1
#     elif direction == "right":
#         new_col += 1

#     if 0 <= new_row < rows and 0 <= new_col < cols:
#         if maze[new_row][new_col] == "#":
#             print("კედელი! თავიდან დაიწყე.")
#             row, col = start_position
#         else:
#             row, col = new_row, new_col
#             if maze[row][col] == "E":
#                 print("შენ გაიარე ლაბირინთი!")
#                 break
#             else:
#                 print("სწორად მიდიხარ!")
#     else:
#         print("გარე ზღვარი! თავიდან დაიწყე.")
#         row, col = start_position

# # 2 თამაში 1 VS 1
# თქვენი მიზანია შექმნათ თამაში სადაც ორი ადამიანი ეჯიბრება ერთმანეთს, მომხმარებელს უნდა
# ჰქონდეს 5-დან 1 მებრძოლის არჩევა: “გიგანტი”, “სწრაფი”, “მოქნილი”, “აქილევსი” & “პითონისტი”,
# თითოეულს გაუკეთეთ 3 შესაძლებლობა იგივე skill მაგალითად: ცეცხლის სროლა, ყონულის და ა.შ.
# სიცოცხლეები განსხვავებული უნდა ჰქონდეთ და ასევე დარტყმის ძალებიც.
# ჯერ პირველი მოთამაშეს ვარჩევინებთ გმირს, შემდეგ მეორეს(ერთნაირის არჩევა შეუძლიათ), მერე
# იწყებს პირველი მოთამაშე და ირჩევს ამ გმირზე რა სკილებიცაა იქიდან ერთს და ესვრის მეორეს,
# ასევე აკეთებს მეორე მოთამაშეც, ყოველ სროლაზე უნდა გამოუტანო დარჩენილი სიცოცხლე
# მოთამაშეს.


from abc import ABC, abstractmethod


class Fighter:
    def __init__(self, name, health, skills):
        self.name = name
        self.health = health
        self.skills = skills

    def clone(self, player_num):
        return Fighter(f"{self.name} (P{player_num})", self.health, self.skills.copy())


templates = {
    "გიგანტი": Fighter("გიგანტი", 120, {"გიგანტური მუშტი": 20, "ქვის სროლა": 25, "მიწის რყევა": 30}),
    "სწრაფი": Fighter("სწრაფი", 80, {"სწრაფი დარტყმა": 15, "ელვის სისწრაფე": 20, "ქარის შეტევა": 25}),
    "მოქნილი": Fighter("მოქნილი", 90, {"აკრობატული ილეთი": 15, "მოულოდნელი შეტევა": 20, "ორმაგი დარტყმა": 25}),
    "აქილევსი": Fighter("აქილევსი", 100, {"შუბის შეტევა": 20, "ფარის დარტყმა": 25, "ლეგენდარული იერიში": 30}),
    "პითონისტი": Fighter("პითონისტი", 95, {"Syntax Error": 15, "Infinite Loop": 20, "Import Power": 25})
}


def choose_fighter(player_num):
    while True:
        choice = input(
            f"მოთამაშე {player_num}, აირჩიე მებრძოლი ({', '.join(templates.keys())}): ")
        if choice in templates:
            return templates[choice].clone(player_num)
        print("არასწორი არჩევანი! გთხოვთ სცადოთ თავიდან.")


fighter1 = choose_fighter(1)
fighter2 = choose_fighter(2)


def play_turn(attacker, defender):
    print(
        f"\nსტატუსი: {fighter1.name}: {max(0, fighter1.health)} HP | {fighter2.name}: {max(0, fighter2.health)} HP")

    skill = input(
        f"{attacker.name}, აირჩიე სკილი ({', '.join(attacker.skills.keys())}): ")
    if skill in attacker.skills:
        damage = attacker.skills[skill]
        defender.health -= damage
        print(f"-> {attacker.name}-მა გამოიყენა {skill} და მიაყენა {damage} ზიანი!")
    else:
        print("-> არასწორი სკილი! სვლა გადადის მეორე მოთამაშეზე.")


while fighter1.health > 0 and fighter2.health > 0:
    play_turn(fighter1, fighter2)
    if fighter2.health <= 0:
        print(f"\n{fighter2.name} დამარცხდა! {fighter1.name}-მა გაიმარჯვა!")
        break

    play_turn(fighter2, fighter1)
    if fighter1.health <= 0:
        print(f"\n{fighter1.name} დამარცხდა! {fighter2.name}-მა გაიმარჯვა!")
        break

final_status = f"\nფინალური სტატუსი: {fighter1.name}: {max(0, fighter1.health)} HP | {fighter2.name}: {max(0, fighter2.health)} HP"
print(final_status)


# # 3
# შექმენით Earth კლასი, რომელიც იქნება მშობელი მინიმუმ 3 შვილის, თქვენი სურვილით უნდა
# დაწეროთ ისეთი ლოგიკა ამ კლასში რომ გამოყენებული გქონდეთ ობიექტზე ორიენტირებული
# პროგრამირების 4 პრინციპი, აბსტრაქცია, პოლიმორფიზმი, მრავალჯერადი მემკვიდრეობა &
# ენკაფსულაცია, შიდა ლოგიკა უნდა იყოს თანმიმდევრული, ანუ მაგალითად: class Animal-ში არ უნდა
# შეინახოთ შვილობილი class Engine. თავისუფალი ხართ შიგნით რას ჩაწერთ.


# აბსტრაქცია

class Earth(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def exist(self):
        pass


class Migratory:
    def migrate(self):
        return f"{self.name} იცვლის ადგილმდებარეობას სეზონურად."

# ინკაფსულაცია


class Human(Earth):
    def __init__(self, name, age):
        super().__init__(name)
        self.__age = age  # Private ცვლადი

    # Getter
    def get_age(self):
        return self.__age

    # Setter
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("ასაკი არ შეიძლება იყოს უარყოფითი.")

    # პოლიმორფიზმი
    def exist(self):
        return f"ადამიანი სახელით {self.name} (ასაკი: {self.__age}) ცხოვრობს დედამიწაზე, აშენებს ქალაქებს."

# მრავალჯერადი მემკვიდრეობა


class Bird(Earth, Migratory):
    def exist(self):
        return f"ფრინველი {self.name} დაფრინავს დედამიწის ცაზე."


class Tree(Earth):
    def exist(self):
        return f"ხე {self.name} იზრდება დედამიწის ნიადაგზე და გამოყოფს ჟანგბადს."


entities = [
    Human("გიორგი", 25),
    Bird("მერცხალი"),
    Tree("მუხა")
]

for entity in entities:
    print(entity.exist())
    if isinstance(entity, Migratory):
        print(entity.migrate())


# # 4 ჯადოქარი
# მომხმარებელს აქვს 5 ინგრედიენტი: “ღამურა”, “ბუმბული”, “ვაშლი”, “ყვავილი”, “წყალი”. შეუძლია
# მხოლოდ 2-ის არჩევა და “მოხარშვა” ამ ორიდან უნდა გამოვიდეს რაღაც მაგალითად: “ვაშლი” +
# “წყალი” = “ვაშლის წვენი” და ასე შემდეგ.ყველა კომბინაცია უნდა იყოს განსხვავებული.

# ingredients = ["ღამურა", "ბუმბული", "ვაშლი", "ყვავილი", "წყალი"]

# recipes = {
#     frozenset(["ვაშლი", "წყალი"]): "ვაშლის წვენი",
#     frozenset(["ღამურა", "წყალი"]): "უხილავობის ელექსირი",
#     frozenset(["ბუმბული", "ყვავილი"]): "სიყვარულის ნექტარი",
#     frozenset(["ღამურა", "ბუმბული"]): "ფრენის წამალი",
#     frozenset(["ვაშლი", "ყვავილი"]): "ჯადოსნური ნამცხვარი",
#     frozenset(["ბუმბული", "წყალი"]): "სიმსუბუქის სასმელი",
#     frozenset(["ღამურა", "ყვავილი"]): "შხამიანი ნაყენი",
#     frozenset(["ვაშლი", "ბუმბული"]): "ტკბილი მუსი",
#     frozenset(["ყვავილი", "წყალი"]): "არომატული ჩაი",
#     frozenset(["ღამურა", "ვაშლი"]): "აკრძალული ხილი"
# }


ingredients = {
    "ვაშლი": ["sweet", "fruit"],
    "წყალი": ["liquid", "pure"],
    "ბუმბული": ["light", "air"],
    "ღამურა": ["dark", "fly"],
    "ყვავილი": ["nature", "scent"]
}


def craft(ing1, ing2):
    t1, t2 = ingredients[ing1], ingredients[ing2]
    all_traits = t1 + t2

    if "sweet" in all_traits and "liquid" in all_traits:
        return "🍎 ვაშლის წვენი"

    if ("dark" in all_traits or "fly" in all_traits) and "liquid" in all_traits:
        return "🧛 უხილავობის ელექსირი"

    if ("dark" in all_traits or "fly" in all_traits) and ("light" in all_traits or "air" in all_traits):
        return "🦅 ფრენის წამალი"

    if "scent" in all_traits and "liquid" in all_traits:
        return "🌸 სურნელოვანი პარფიუმი"

    if "light" in all_traits and "nature" in all_traits:
        return "☁️ ჰაერის მსუბუქობა"

    if "sweet" in all_traits and "nature" in all_traits:
        return "🥧 ჯადოსნური ვაშლის ნამცხვარი"

    return "✨ უცნაური მაგიური ნაზავი"


print("ინგრედიენტები:")
print(", ".join(ingredients.keys()))

ing1 = input("პირველი ინგრედიენტი: ")
ing2 = input("მეორე ინგრედიენტი: ")

if ing1 == ing2:
    print("ერთნაირი ინგრედიენტები არ შეიძლება!")
elif ing1 not in ingredients or ing2 not in ingredients:
    print("არასწორი ინგრედიენტი!")
else:
    result = craft(ing1, ing2)
    print("⚗️ შედეგი:", result)

# # 5 ტრანსპორტირების სისტემა
# უნდა ავაწყოთ სისტემა, სადაც სხვადასხვა ტრანსპორტი(Car, Bus, Bike) იმართება ერთიანი
# კლასით Transport
# - ყველა ტრანსპორტს აქვს fuel, speed, capacity.
# - არის აბსტრაქტული მეთოდი move().
# - ყოველი transport სხვადასხვა წესით ხარჯავს საწვავს(პოლიმორფიზმი).
# - fuel ინახება private(ენკაფსულაცია).
# - ყველა transport იღებს ძირითად ფუნქციონალს Transport-იდან.(მემკვიდრეობა)


class Transport(ABC):
    def __init__(self, fuel, speed, capacity):
        self.__fuel = fuel
        self.speed = speed
        self.capacity = capacity

    def get_fuel(self):
        return self.__fuel

    def _reduce_fuel(self, amount):
        if amount > self.__fuel:
            print("Not enough fuel!")
            self.__fuel = 0
        else:
            self.__fuel -= amount

    @abstractmethod
    def move(self, distance):
        pass


class Car(Transport):
    def move(self, distance):
        fuel_needed = distance * 0.1
        self._reduce_fuel(fuel_needed)
        print(f"Car moved {distance} units. Remaining fuel: {self.get_fuel()}")


class Bus(Transport):
    def move(self, distance):
        fuel_needed = distance * 0.2
        self._reduce_fuel(fuel_needed)
        print(f"Bus moved {distance} units. Remaining fuel: {self.get_fuel()}")


class Bike(Transport):
    def move(self, distance):
        fuel_needed = distance * 0.05
        self._reduce_fuel(fuel_needed)
        print(
            f"Bike moved {distance} units. Remaining fuel: {self.get_fuel()}")


fleet = [
    Car(fuel=50, speed=120, capacity=5),
    Bus(fuel=100, speed=80, capacity=50),
    Bike(fuel=20, speed=25, capacity=1)
]

print("\nTransport Simulation")
for vehicle in fleet:
    vehicle.move(100)