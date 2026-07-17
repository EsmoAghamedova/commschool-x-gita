user_data = {
    "email": "user@mail.com",
    "name": None,
    "nickname": "esmo06",
    "password": "password123",
}


def validate_name(value):
    if not value:
        return False, "Input cannot be empty. Please enter your name."

    if not value.isascii():
        return False, "Only English letters are allowed."

    if not value.isalpha():
        return False, "Please enter letters only."

    if not value.islower():
        return False, "Use lowercase letters only."

    return True, None


def register():

    print("=== Registration ===")
    print(f"Email: {user_data['email']} (Pre-saved)")
    print(f"Nickname: {user_data['nickname']} (Pre-saved)")
    print(f"Password: {user_data['password']} (Pre-saved)\n")

    while True:
        name_input = input(
            "Enter your name (lowercase Latin letters only): ").strip()
        is_valid, message = validate_name(name_input)

        if is_valid:
            user_data["name"] = name_input
            break
        else:
            print(f"Error: {message}\n")

    print("\nRegistration successfully completed!\n")
    print("--- Your Registered Details ---")
    for key, value in user_data.items():
        print(f"{key.title()}: {value}")

    return user_data


register()
