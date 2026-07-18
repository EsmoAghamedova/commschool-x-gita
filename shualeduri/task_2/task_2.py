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

        if value in ("J", "Q", "K"):
            total += 10
        elif value == "A":
            total += 11
        else:
            total += value

    return total


def start_game():
    while True:

        deck = create_deck()

        user = [draw_card(deck), draw_card(deck)]
        computer = [draw_card(deck), draw_card(deck)]

        user_sum = calculate_score(user)

        print("\n========== NEW GAME ==========")
        print(f"Your cards: {user[0]}, {user[1]}")
        print(f"Your score: {user_sum}")
        print(f"Computer: {computer[0]}, ?")

        user_busted = False

        while True:
            choice = input("add or stop: ").lower()

            if choice == "add":
                user.append(draw_card(deck))

                user_sum = calculate_score(user)

                print(f"Your cards: {user}")
                print(f"Your score: {user_sum}")

                if user_sum > 21:
                    print("You lose!")
                    user_busted = True
                    break

            elif choice == "stop":
                break

            else:
                print("Wrong choice.")

        if user_busted:
            break

        computer_sum = calculate_score(computer)

        while computer_sum < 17:
            computer.append(draw_card(deck))
            computer_sum = calculate_score(computer)

        print(f"\nComputer cards: {computer}")
        print(f"Computer score: {computer_sum}")

        if computer_sum > 21:
            print("Computer busts! You win!")
            break

        if user_sum > computer_sum:
            print("You win!")
            break

        elif user_sum < computer_sum:
            print("You lose!")
            break

        else:
            print("\nIt's a tie! Dealing again...\n")


start_game()
