import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("hotel_log.txt", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

POINTS_PER_GEL_SPENT = 0.1


class Room:
    def __init__(self, room_number, room_type, price_per_night, max_guests, is_available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.is_available = is_available

    def book_room(self):
        self.is_available = False

    def release_room(self):
        self.is_available = True

    def calculate_price(self, nights: int, season: str = "regular") -> float:
        base_total = self.price_per_night * nights
        if season.lower() == "high":
            base_total *= 1.3
        elif season.lower() == "low":
            base_total *= 0.8
        return round(base_total, 2)

    def __str__(self):
        status = "თავისუფალია" if self.is_available else "დაჯავშნილია"
        return (
            f"ოთახი #{self.room_number} | {self.room_type} | "
            f"{self.price_per_night} GEL/ღამე | მაქს. {self.max_guests} სტუმარი | {status}"
        )


class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.booked_rooms = []
        self.reward_points = 0

    def add_room(self, room: Room):
        self.booked_rooms.append(room)

    def remove_room(self, room: Room):
        if room in self.booked_rooms:
            self.booked_rooms.remove(room)

    def pay_for_booking(self, total_price: float) -> bool:
        if total_price > self.budget:
            return False
        self.budget -= total_price
        self.budget = round(self.budget, 2)
        self.reward_points += int(total_price * POINTS_PER_GEL_SPENT)
        return True

    def show_booking_summary(self) -> str:
        if not self.booked_rooms:
            return f"{self.name}-ს ჯერ არცერთი ოთახი არ აქვს დაჯავშნილი."

        lines = [f"{self.name}-ის დაჯავშნები:"]
        for room in self.booked_rooms:
            lines.append(
                f"  - ოთახი #{room.room_number} ({room.room_type}) - {room.price_per_night} GEL/ღამე")
        lines.append(f"დარჩენილი ბიუჯეტი: {self.budget:.2f} GEL")
        lines.append(f"დაგროვილი ქულები: {self.reward_points}")
        return "\n".join(lines)


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings_log = []

    def show_available_rooms(self, room_type: str = None) -> list:
        available = [r for r in self.rooms if r.is_available]
        if room_type:
            available = [r for r in available if r.room_type.lower()
                         == room_type.lower()]
        return available

    def _find_room(self, room_number: int):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def calculate_total_booking(self, room_number: int, nights: int, season: str = "regular") -> float:
        room = self._find_room(room_number)
        if room is None:
            return 0.0
        return room.calculate_price(nights, season)

    def book_room_for_customer(self, customer: Customer, room_number: int, nights: int, season: str = "regular") -> bool:
        room = self._find_room(room_number)

        if room is None or not room.is_available:
            return False

        total_price = self.calculate_total_booking(room_number, nights, season)

        if not customer.pay_for_booking(total_price):
            return False

        room.book_room()
        customer.add_room(room)
        self.log_booking(customer, room, total_price)
        return True

    def log_booking(self, customer: Customer, room: Room, total_price: float):
        entry = {
            "customer": customer.name,
            "room_number": room.room_number,
            "room_type": room.room_type,
            "total_price": total_price,
        }
        self.bookings_log.append(entry)
        logger.info(
            f"დაჯავშნა: {customer.name} -> ოთახი #{room.room_number} ({room.room_type}), "
            f"ჯამი: {total_price:.2f} GEL"
        )

    def cancel_booking(self, customer: Customer, room_number: int):
        room = self._find_room(room_number)
        if room is None or room not in customer.booked_rooms:
            return False

        room.release_room()
        customer.remove_room(room)
        logger.info(f"გაუქმება: {customer.name} -> ოთახი #{room.room_number}")
        return True


def build_sample_hotel() -> Hotel:
    hotel = Hotel("Tbilisi Grand Hotel")
    sample_rooms = [
        Room(101, "Single", 80, 1),
        Room(102, "Single", 80, 1),
        Room(201, "Double", 130, 2),
        Room(301, "Suite", 250, 4),
    ]
    hotel.rooms.extend(sample_rooms)
    return hotel


def main():
    hotel = build_sample_hotel()

    print(f"=== კეთილი იყოს თქვენი მობრძანება {hotel.name}-ში ===\n")
    name = input("შეიყვანეთ თქვენი სახელი: ")

    while True:
        try:
            budget = float(input("შეიყვანეთ თქვენი ბიუჯეტი (GEL): "))
            if budget < 0:
                print("Budget cannot be negative.")
                continue
            break
        except ValueError:
            print("Only numbers are allowed.")

    customer = Customer(name, budget)

    while True:
        print("\n1. თავისუფალი ოთახების ნახვა")
        print("2. ოთახის დაჯავშნა")
        print("3. ჩემი დაჯავშნების ნახვა")
        print("4. დაჯავშნის გაუქმება")
        print("0. გასვლა")

        choice = input("\nაირჩიეთ მოქმედება: ")

        if choice == "1":
            room_type = input(
                "ოთახის ტიპი (Single/Double/Suite, ან Enter ყველასთვის): ").strip()
            rooms = hotel.show_available_rooms(
                room_type if room_type else None)
            if not rooms:
                print("\nთავისუფალი ოთახები ვერ მოიძებნა.\n")
            else:
                print("\n--- თავისუფალი ოთახები ---")
                for room in rooms:
                    print(room)

        elif choice == "2":
            try:
                room_number = int(
                    input("რომელი ოთახის ნომერი გსურთ დაჯავშნოთ? "))
            except ValueError:
                print("Only numbers are allowed.")
                continue

            try:
                nights = int(input("რამდენი ღამით? "))
                if nights <= 0:
                    print("Number of nights must be greater than 0.")
                    continue
            except ValueError:
                print("Only numbers are allowed.")
                continue

            season = input(
                "აირჩიეთ სეზონი (high / low / regular): ").strip().lower()
            if season not in ["high", "low", "regular"]:
                season = "regular"

            total = hotel.calculate_total_booking(room_number, nights, season)
            print(f"ჯამური ღირებულება: {total:.2f} GEL")

            success = hotel.book_room_for_customer(
                customer, room_number, nights, season)
            if success:
                print(
                    f"\nდაჯავშნა წარმატებულია! დარჩენილი ბიუჯეტი: {customer.budget:.2f} GEL\n")
            else:
                print(
                    "\nდაჯავშნა ვერ შესრულდა (ოთახი დაკავებულია ან არასაკმარისი ბიუჯეტი).\n")

        elif choice == "3":
            print("\n" + customer.show_booking_summary() + "\n")

        elif choice == "4":
            try:
                room_number = int(
                    input("რომელი ოთახის დაჯავშნის გაუქმება გსურთ? "))
            except ValueError:
                print("Only numbers are allowed.")
                continue

            if hotel.cancel_booking(customer, room_number):
                print("\nდაჯავშნა გაუქმებულია.\n")
            else:
                print("\nეს ოთახი თქვენს დაჯავშნებში ვერ მოიძებნა.\n")

        elif choice == "0":
            print("მადლობა, ნახვამდის!")
            break


if __name__ == "__main__":
    main()
