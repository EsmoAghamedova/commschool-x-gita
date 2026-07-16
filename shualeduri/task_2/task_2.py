import random

ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "K", "Q")
suits = ("❤️", "♠️", "♦️", "♣️")


def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))
    return deck


def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card


def calculate_score(cards):
    total = 0

    for card in cards:
        value = card[1]

        if value in ("J", "K", "Q"):
            total += 10
        elif value == "A":
            total += 11
        else:
            total += value
    return total


def start_game():
    deck = create_deck()

    user = [draw_card(deck), draw_card(deck)]
    computer = [draw_card(deck), draw_card(deck)]
    user_sum = calculate_score(user)

    print(f"user: {user[0]}, {user[1]}")
    print(f"sum: {user_sum}")
    print(f"computer: {computer[0]}, ?")

    user_busted = False

    while True:
        choice = input("add or stop: ")
        if choice == "add":
            user.append(draw_card(deck))
            print(f"user: {user}")
            print(f"sum: {calculate_score(user)}")

            if calculate_score(user) > 21:
                print("you lose")
                user_busted = True
                break

        elif choice == "stop":
            break

        else:
            print("wrong choice")

    if not user_busted:
        computer_sum = calculate_score(computer)
        while computer_sum < 17:
            computer.append(draw_card(deck))
            computer_sum = calculate_score(computer)

        user_sum = calculate_score(user)
        print(f"computer: {computer}")
        print(f"computer sum: {computer_sum}")

        if computer_sum > 21:
            print("computer busts, you win")
        elif user_sum > computer_sum:
            print("you win")
        elif user_sum < computer_sum:
            print("you lose")
        else:
            print("tie")

start_game()