import pytest
from hotel import Room, Customer, Hotel


@pytest.fixture
def sample_room():
    return Room(room_number=101, room_type="Single", price_per_night=100, max_guests=1)


@pytest.fixture
def sample_customer():
    return Customer(name="Nini", budget=500)


@pytest.fixture
def sample_hotel():
    hotel = Hotel("Test Hotel")
    hotel.rooms = [
        Room(101, "Single", 100, 1),
        Room(102, "Single", 100, 1),
        Room(201, "Double", 150, 2, is_available=False),
        Room(301, "Suite", 300, 4),
    ]
    return hotel


class TestRoom:
    def test_room_starts_available_by_default(self):
        room = Room(101, "Single", 100, 1)
        assert room.is_available is True

    def test_book_room_marks_unavailable(self, sample_room):
        sample_room.book_room()
        assert sample_room.is_available is False

    def test_release_room_marks_available(self, sample_room):
        sample_room.book_room()
        sample_room.release_room()
        assert sample_room.is_available is True

    def test_calculate_price_regular_season(self, sample_room):
        assert sample_room.calculate_price(3, season="regular") == 300.0

    def test_calculate_price_high_season(self, sample_room):
        assert sample_room.calculate_price(2, season="high") == 260.0

    def test_calculate_price_low_season(self, sample_room):
        assert sample_room.calculate_price(2, season="low") == 160.0

    def test_calculate_price_zero_nights(self, sample_room):
        assert sample_room.calculate_price(0) == 0.0

    def test_str_contains_room_number_and_type(self, sample_room):
        text = str(sample_room)
        assert "101" in text
        assert "Single" in text


class TestCustomerPayForBooking:
    def test_successful_payment_reduces_budget(self, sample_customer):
        result = sample_customer.pay_for_booking(200)
        assert result is True
        assert sample_customer.budget == 300.0

    def test_payment_exceeding_budget_is_rejected(self, sample_customer):
        result = sample_customer.pay_for_booking(600)
        assert result is False
        assert sample_customer.budget == 500.0

    def test_payment_equal_to_full_budget_succeeds(self, sample_customer):
        result = sample_customer.pay_for_booking(500)
        assert result is True
        assert sample_customer.budget == 0.0

    def test_payment_awards_reward_points(self, sample_customer):
        sample_customer.pay_for_booking(200)
        assert sample_customer.reward_points == 20

    def test_failed_payment_does_not_award_points(self, sample_customer):
        sample_customer.pay_for_booking(9999)
        assert sample_customer.reward_points == 0

    def test_multiple_payments_accumulate_correctly(self, sample_customer):
        sample_customer.pay_for_booking(100)
        sample_customer.pay_for_booking(150)
        assert sample_customer.budget == 250.0
        assert sample_customer.reward_points == 25


class TestCustomerRoomManagement:
    def test_add_room_appends_to_booked_rooms(self, sample_customer, sample_room):
        sample_customer.add_room(sample_room)
        assert sample_room in sample_customer.booked_rooms

    def test_remove_room_removes_from_booked_rooms(self, sample_customer, sample_room):
        sample_customer.add_room(sample_room)
        sample_customer.remove_room(sample_room)
        assert sample_room not in sample_customer.booked_rooms

    def test_remove_room_not_booked_does_not_raise(self, sample_customer, sample_room):
        sample_customer.remove_room(sample_room)
        assert sample_customer.booked_rooms == []

    def test_show_booking_summary_when_empty(self, sample_customer):
        summary = sample_customer.show_booking_summary()
        assert "Nini" in summary

    def test_show_booking_summary_lists_booked_room(self, sample_customer, sample_room):
        sample_customer.add_room(sample_room)
        summary = sample_customer.show_booking_summary()
        assert "101" in summary


class TestHotelBookRoomForCustomer:
    def test_booking_available_room_succeeds(self, sample_hotel, sample_customer):
        result = sample_hotel.book_room_for_customer(
            sample_customer, 101, 2, season="regular")
        assert result is True
        assert sample_customer.budget == 300.0

    def test_booking_high_season_charges_correct_amount(self, sample_hotel, sample_customer):
        result = sample_hotel.book_room_for_customer(
            sample_customer, 101, 2, season="high")
        assert result is True
        assert sample_customer.budget == 240.0

    def test_booking_marks_room_unavailable(self, sample_hotel, sample_customer):
        sample_hotel.book_room_for_customer(sample_customer, 101, 2)
        room = sample_hotel._find_room(101)
        assert room.is_available is False

    def test_cannot_book_already_unavailable_room(self, sample_hotel, sample_customer):
        result = sample_hotel.book_room_for_customer(sample_customer, 201, 1)
        assert result is False
        assert sample_customer.budget == 500.0

    def test_cannot_book_nonexistent_room(self, sample_hotel, sample_customer):
        result = sample_hotel.book_room_for_customer(sample_customer, 9999, 1)
        assert result is False

    def test_booking_fails_when_budget_insufficient(self, sample_hotel):
        poor_customer = Customer("Levani", budget=50)
        result = sample_hotel.book_room_for_customer(poor_customer, 301, 1)
        room = sample_hotel._find_room(301)
        assert result is False
        assert room.is_available is True

    def test_booking_adds_entry_to_bookings_log(self, sample_hotel, sample_customer):
        sample_hotel.book_room_for_customer(sample_customer, 101, 2)
        assert len(sample_hotel.bookings_log) == 1
        assert sample_hotel.bookings_log[0]["customer"] == "Nini"
        assert sample_hotel.bookings_log[0]["room_number"] == 101

    def test_booking_adds_room_to_customer_booked_rooms(self, sample_hotel, sample_customer):
        sample_hotel.book_room_for_customer(sample_customer, 101, 2)
        assert len(sample_customer.booked_rooms) == 1
        assert sample_customer.booked_rooms[0].room_number == 101

    def test_double_booking_same_room_fails_second_time(self, sample_hotel):
        c1 = Customer("Ana", budget=1000)
        c2 = Customer("Beka", budget=1000)
        first = sample_hotel.book_room_for_customer(c1, 101, 1)
        second = sample_hotel.book_room_for_customer(c2, 101, 1)
        assert first is True
        assert second is False


class TestHotelAvailability:
    def test_show_available_rooms_excludes_booked(self, sample_hotel):
        available = sample_hotel.show_available_rooms()
        room_numbers = [r.room_number for r in available]
        assert 201 not in room_numbers
        assert 101 in room_numbers

    def test_show_available_rooms_filters_by_type(self, sample_hotel):
        singles = sample_hotel.show_available_rooms("Single")
        assert all(r.room_type == "Single" for r in singles)
        assert len(singles) == 2

    def test_show_available_rooms_case_insensitive_filter(self, sample_hotel):
        singles = sample_hotel.show_available_rooms("single")
        assert len(singles) == 2

    def test_calculate_total_booking_correct_amount(self, sample_hotel):
        total = sample_hotel.calculate_total_booking(301, 3, season="regular")
        assert total == 900.0

    def test_calculate_total_booking_unknown_room_returns_zero(self, sample_hotel):
        total = sample_hotel.calculate_total_booking(9999, 3)
        assert total == 0.0


class TestHotelCancelBooking:
    def test_cancel_booking_releases_room(self, sample_hotel, sample_customer):
        sample_hotel.book_room_for_customer(sample_customer, 101, 1)
        result = sample_hotel.cancel_booking(sample_customer, 101)
        assert result is True
        room = sample_hotel._find_room(101)
        assert room.is_available is True

    def test_cancel_booking_removes_from_customer_list(self, sample_hotel, sample_customer):
        sample_hotel.book_room_for_customer(sample_customer, 101, 1)
        sample_hotel.cancel_booking(sample_customer, 101)
        assert sample_customer.booked_rooms == []

    def test_cancel_booking_not_actually_booked_fails(self, sample_hotel, sample_customer):
        result = sample_hotel.cancel_booking(sample_customer, 101)
        assert result is False

    def test_cancel_booking_nonexistent_room_fails(self, sample_hotel, sample_customer):
        result = sample_hotel.cancel_booking(sample_customer, 9999)
        assert result is False
