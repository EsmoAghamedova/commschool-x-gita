import random
import logging

logging.basicConfig(
    filename="lottery_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

jackpot_amount = 500000


def generate_winning_nums():
    return random.sample(range(1, 50), 6)


def player_nums():
    print("Enter your 6 numbers (1-49) separated by spaces, e.g., 3 12 24 30 41 49")
    numbers = input("Your numbers: ").split()
    return [int(n) for n in numbers]


def count_matches(player_nums, winning_nums):
    return len(set(player_nums) & set(winning_nums))


def calculate_prize(matches):
    if matches == 6:
        return jackpot_amount, "JACKPOT!!!"
    elif matches == 5:
        prize = jackpot_amount * (1-0.4)
        return prize, "5/6 Matches"
    elif matches == 4:
        prize = jackpot_amount * (1-0.6)
        return prize, "4/6 Matches"
    elif matches == 3:
        prize = jackpot_amount * (1-0.8)
        return prize, "3/6 Matches"
    else:
        return 0, f"{matches}/6 Matches - No prize"


def play():
    winning_numbers = generate_winning_nums()
    player_numbers = player_nums()

    matches = count_matches(player_numbers, winning_numbers)
    prize, message = calculate_prize(matches)

    print(f"\nWinning numbers: {sorted(winning_numbers)}")
    print(f"Your numbers: {sorted(player_numbers)}")
    print(f"{message}")

    if prize > 0:
        print(f"Your prize is: {prize:,.2f} GEL\n")
    else:
        print(f"you lost")

    logging.info(
        f"Lottery Draw - Winning: {sorted(winning_numbers)}, "
        f"Player: {sorted(player_numbers)}, Matches: {matches}, "
        f"Result: {message}, Prize: {prize:.2f} GEL"
    )
    
def main():
    print("=== Lottery ===\n")
    while True:
        play()
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye")
            break

main()