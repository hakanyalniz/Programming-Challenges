def get_password_length_input() -> int:
    """
    Returns an integer based on the user input with minimum length of 12.
    If anything else than a number is inserted or if a number less than 12 is inserted it will ask again.
    Pressing enter will return the default length of 16.
    """

    while True:
        raw_length: str = input("Password length: ")
        if raw_length == "":
            return 16

        try:
            int_length: int = int(raw_length)
            if int_length < 12:
                print("Please pick a greater length. \n")
                continue
            return int_length
        except ValueError:
            print("Please enter a number.\n")


def include_special_toggle() -> bool:
    """
    A function that returns true or false to toggle special character list.
    The user can only enter true or false. Only accepts those two inputs.
    """

    while True:
        raw_input = input("Include special characters: ")
        try:
            if raw_input.lower() == "yes":
                return True
            elif raw_input.lower() == "no" or raw_input == "":
                return False
        except ValueError:
            print("Please enter Yes or No")


def write_password_toFile(generated_password: str):
    """
    Writes the selected password into a file.
    """

    raw_input = input("Leave a note for your password: ")

    with open("passwords.txt", "a", encoding="utf-8") as file:
        file.write(f"{generated_password} , {raw_input}\n")


def read_passwords():
    """
    Opens a password.txt file and reads from it, then prints them on screen.
    Exit the program after showing the passwords.
    """

    while True:
        raw_input = input("Read your passwords?: ")
        try:
            if raw_input.lower() == "yes":
                with open("passwords.txt", "r", encoding="utf-8") as file:
                    print("\n\n")
                    for line in file:
                        # strip() removes the trailing newline character (\n)
                        print(line.strip())
                print("\n\n")
                exit()

            elif raw_input.lower() == "no" or raw_input == "":
                return False
        except ValueError:
            print("Please enter Yes or No")


def delete_password():
    """
    The user can select a password based on row and delete it.
    """

    with open("passwords.txt", "r", encoding="utf-8") as file:
        print("\n\n")
        for line in file:
            # strip() removes the trailing newline character (\n)
            print(line.strip())


# Where the user can chose to either enter new password, read from it, see them, delete them and so on
