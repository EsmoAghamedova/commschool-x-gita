import random

# # 1 შექმენი თამაში
# შექმენით Character კლასი(სახელი, სიცოცხლე, ძალა)
# გააკეთეთ მემკვიდრეები: Warrior, Mage, Archer
# გამოიყენეთ super() რომ მშობლის კონსტრუქტორი გამოიძახოთ
# თამაში: ორი გმირი ებრძვის ერთმანეთს(attack() მეთოდი).
# Warrior სჯობს Mage-ს, Mage სჯობს Archer-ს, Archer სჯობს Warrior-ს
# ტესტირების დროს სცადე სამივე ვარიანტი, ანუ როცა ერთმანეთზე გააკეთებინებ შეტევას 1 უნდა
# დამარცხდეს და 1მა გაიმარჯვოს, ეს უნდა გამოიტანო ტერმინალში. ზედმეტი ვალიდაციები და
# პირობის შეცვლა არაა საჭირო. რაც პირობაში წერია ამ მონახაზით გააკეთეთ თავისუფლად.


class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        if (
            isinstance(self, Warrior) and isinstance(enemy, Mage)
            or isinstance(self, Mage) and isinstance(enemy, Archer)
            or isinstance(self, Archer) and isinstance(enemy, Warrior)
        ):
            print(f"{self.name} Won!")
            print(f"{enemy.name} Lost!")

        else:
            print(f"{enemy.name} Won!")
            print(f"{self.name} Lost!")


class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)


class Mage(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)


class Archer(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)


warrior = Warrior("Thor", 100, 50)
mage = Mage("Merlin", 100, 40)
archer = Archer("Robin", 100, 45)

# warrior.attack(mage)
# mage.attack(archer)
# archer.attack(warrior)

# # 2 პატარა პროგრამა მონსტრებზე
# თქვენი ვალია შექმნათ მონსტრების ქარხანა სადაც:
# შექმენით Monster კლასი.
# დაამატეთ classmethod create_from_level(level), რომელიც ქმნის მონსტრს სიძლიერის
# მიხედვით.
# სხვადასხვა level -> სხვადასხვა ტიპის მონსტრი.
# შექმენი მინიმუმ 10 მონსტრი რომლებსაც ექნებათ სახელები, სახელები არ უნდა იყოს ბოროტული: )
#     (ეს მონსტრები ეხმარებიან ადამიანებს) “აქაც იგივე” არაა საჭირო ზედმეტი ვალიდაციები და პირობის
#     ცვლილება. ამ მონახაზში იმუშავეთ თავისუფლად.


class Monster:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level

    @classmethod
    def create_from_level(cls, level):
        if level == 1:
            name = "Max"
            power = random.randint(5, 10)
        elif level == 2:
            name = "Luna"
            power = random.randint(10, 20)
        elif level == 3:
            name = "Jackson"
            power = random.randint(20, 30)
        else:
            name = "helper"
            power = 1

        return cls(name, power, level)


monsters = []

for i in range(10):
    level = random.randint(1, 3)
    monster = Monster.create_from_level(level)
    monsters.append(monster)

for m in monsters:
    print(f"{m.name}, level: {m.level}, power: {m.power}")

# 3 მარტივი კაზინო თამაში
# შექმენით SlotMachine კლასი.
# გამოიყენეთ staticmethod შემთხვევითი სიმბოლოების დასაგენერირებლად.
# გამოიყენეთ classmethod from_difficulty(level) -> უფრო რთული დონის სლოტები
# მოთამაშე მოიგებს თუ სამივე სიმბოლო დაემთხვევა.
# აუცილებლად გატესტეთ, სცადეთ რამოდენიმე ვარიანტის გაშვება.


class SlotMachine:
    symbols = ["🍒", "🍋", "⭐", "🔔"]

    def __init__(self, symbols):
        self.symbols = symbols

    @staticmethod
    def get_random_symbol(symbols):
        return random.choice(symbols)

    def spin(self):
        result = []
        for _ in range(3):
            result.append(self.get_random_symbol(self.symbols))

        print(" | ".join(result))

        if result[0] == result[1] == result[2]:
            print("Win!!!")
        else:
            print("Lose!!!")

        return result

    @classmethod
    def from_difficulty(cls, level):

        if level == 1:
            symbols = ["🍒", "🍒", "🍋", "⭐", "⭐", "🔔"]  # easier win chance
        elif level == 2:
            symbols = ["🍒", "🍋", "⭐", "🔔"]
        else:
            symbols = ["🍋", "⭐", "🔔"]  # harder

        return cls(symbols)


game = SlotMachine.from_difficulty(2)

game.spin()
game.spin()
game.spin()

# 4 გმირის ქულების სისტემა
# შექმენით Hero კლასი.
# private health, private score.
# staticmethod random_event() -> შემთხვევითი მოვლენა(ქულა ემატება ან ჯანმრთელობა
# აკლდება).
# classmethod from_name(cls, name) -> ქმნის გმირს სახელით.
# მემკვიდრე SuperHero -> დამატებითი ძალა.
# super() გამოიძახეთ მშობლის კონსტრუქტორისთვის.
# თამაში გრძელდება სანამ გმირის health > 0.


class Hero:
    def __init__(self, name):
        self.name = name
        self.__health = 100
        self.__score = 0

    @staticmethod
    def random_event():
        events = [
            ("heal", 20, 0),
            ("damage", -30, 0),
            ("score", 0, 50)
        ]
        return random.choice(events)

    @classmethod
    def from_name(cls, name):
        return cls(name)

    def play_turn(self):
        event, hp_change, score_change = self.random_event()

        self.__health += hp_change
        self.__score += score_change

        print(self.name, event, self.__health, self.__score)

    def is_alive(self):
        return self.__health > 0


class SuperHero(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power = 10

    def play_turn(self):
        event, hp_change, score_change = self.random_event()

        self._Hero__health += hp_change + 10  
        self._Hero__score += score_change

        print(self.name, "(super)", event,
              self._Hero__health, self._Hero__score)


hero = SuperHero.from_name("Esmira")

turn = 0

while hero.is_alive() and turn < 10:
    hero.play_turn()
    turn += 1

print("Game over 🎮")

# 5 პროგრამა კარტზე
# Card კლასი(rank, suit).
# Deck კლასი -> private cards list.
# classmethod create_standard_deck() აბრუნებს სტანდარტულ 52 კარტიან დასტას.
# staticmethod shuffle(cards) აურევს კარტებს.
# მოთამაშე იღებს 5 კარტს და ამოწმებს, აქვს თუ არა “მარტივი კომბინაცია”(მაგ: ორი ერთნაირი)
# აუცილებლად გატესტეთ კოდი, შეასრულეთ მხოლოდ პირობაში მოცემული ვარიანტი, არაა საჭირო
# დამატება.


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self, cards):
        self.__cards = cards

    @classmethod
    def create_standard_deck(cls):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "J", "Q", "K", "A"]

        cards = []

        for s in suits:
            for r in ranks:
                cards.append(Card(r, s))

        return cls(cards)

    @staticmethod
    def shuffle(cards):
        random.shuffle(cards)

    def draw_5(self):
        hand = self.__cards[:5]
        self.__cards = self.__cards[5:]
        return hand


deck = Deck.create_standard_deck()

Deck.shuffle(deck._Deck__cards)

hand = deck.draw_5()

print("Your hand:")
for c in hand:
    print(c)


ranks = [c.rank for c in hand]

if len(set(ranks)) < 5:
    print("You got a pair")
else:
    print("No pair")
