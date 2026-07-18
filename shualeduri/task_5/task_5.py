user_data = {
    "email": "user@mail.com",
    "name": None,
    "nickname": "esmo06",
    "password": "password123",
}


def validate_name(value):
    errors = []

    if not value:
        errors.append("Name cannot be empty.")

    if any(char.isdigit() for char in value):
        errors.append("Numbers are not allowed.")

    if any(not char.isalpha() for char in value):
        errors.append("Symbols are not allowed.")

    if not value.isascii():
        errors.append("Only English letters are allowed.")

    if not value.islower():
        errors.append("Only lowercase letters are allowed.")

    if errors:
        return False, errors

    return True, None


def register():

    print("=== Registration ===")
    print(f"Email: {user_data['email']} (Pre-saved)")
    print(f"Nickname: {user_data['nickname']} (Pre-saved)")
    print(f"Password: {user_data['password']} (Pre-saved)\n")

    while True:
        name_input = input(
            "Enter your name (lowercase Latin letters only): "
        ).strip()

        is_valid, messages = validate_name(name_input)

        if is_valid:
            user_data["name"] = name_input
            break
        else:
            print("\nErrors:")
            for error in messages:
                print(f"- {error}")
            print()

    print("\nRegistration successfully completed!\n")
    print("--- Your Registered Details ---")

    for key, value in user_data.items():
        print(f"{key.title()}: {value}")

    return user_data


register()
