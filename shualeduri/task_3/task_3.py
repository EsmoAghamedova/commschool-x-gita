import logging

logging.basicConfig(
    filename="atm_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

max_deposit = 1000
currency = "GEL"
balance = 2500


def check_balance():
    print(f"\n Your balance is: {balance:.2f} {currency}\n")
    logging.info(f"Balance check: {balance:.2f} {currency}")


def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= 0:
        print("Amount must be greater than 0.")
        logging.info("Failed withdrawal: Amount must be greater than 0.")
        return

    if amount > balance:
        print("\n Insufficient funds.\n")
        logging.info(
            f"Failed withdrawal: Requested {amount:.2f} {currency}, Balance {balance:.2f} {currency}")
        return

    balance -= amount
    print(
        f"\n Withdrawn {amount:.2f} {currency}. New balance: {balance:.2f} {currency}\n")
    logging.info(
        f"Withdrawal: {amount:.2f} {currency}, New balance {balance:.2f} {currency}")


def deposit():
    global balance
    amount = float(input("Enter the amount to deposit: "))

    if amount > max_deposit:
        print(
            f"\n You cannot deposit more than {max_deposit} {currency} at a time.\n")
        logging.info(
            f"Failed deposit: Requested {amount:.2f} {currency} > Limit {max_deposit}")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        logging.info("Failed Deposit: Amount must be greater than 0.")
        return

    balance += amount
    print(
        f"\n Deposited {amount:.2f} {currency}. New balance: {balance:.2f} {currency}\n")
    logging.info(
        f"Deposit: {amount:.2f} {currency}, New balance {balance:.2f} {currency}")


def main():
    print("=== Welcome to the ATM ===")
    while True:
        print("\n1. Check balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("0. Exit")

        choice = input("\nSelect an option: ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            deposit()
        elif choice == "0":
            print("Thank you, goodbye!")
            logging.info("ATM closed.")
            break
        else:
            print("\nInvalid choice.\n")


main()
