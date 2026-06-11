import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


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
            print("Please enter Yes or No.")


def write_password_toFile(generated_password: bytes):
    """
    Writes the selected password into a file.
    """

    raw_input = input("Leave a note for your password: ")

    with open("passwords.txt", "a", encoding="utf-8") as file:
        file.write(f"{generated_password} , {raw_input}\n")


def read_passwords():
    """
    Opens a password file and reads from it, then prints them on screen.
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
                        clean_line = line.strip()
                        split_password = clean_line.split(",", maxsplit=1)[0]

                        print(split_password)

                print("\n\n")
                exit()

            elif raw_input.lower() == "no" or raw_input == "":
                return False
        except ValueError:
            print("Please enter Yes or No.")


def delete_password():
    """
    The user can select a password based on row and delete it.
    This works on index number, therefore the argument it accepts is an index.
    Exits the program after deleting a password.
    """

    while True:
        raw_input = input("Delete a password?: ")

        try:
            if raw_input.lower() == "yes":
                line_to_delete = int(
                    input("Which password to delete (Use row number)?: ")
                )

                # Account for index numbering starting from 0
                line_to_delete = line_to_delete - 1

                # Read from the file
                with open("passwords.txt", "r", encoding="utf-8") as file:
                    lines = file.readlines()

                # Delete the specific line
                # Check to make sure index below 0 is not selected and also that such an index exists in the lines
                if 0 <= line_to_delete < len(lines):
                    del lines[line_to_delete]
                else:
                    print("Please enter an index number that matches the password row.")
                    continue

                # Rewrite/Overwrite into the file
                with open("passwords.txt", "w") as file:
                    file.writelines(lines)

                print("Password deleted!")
                exit()
            elif raw_input.lower() == "no" or raw_input == "":
                return False

        except ValueError:
            print("Please enter Yes or No.")


def log_user():
    salt = b"\x92\xfa\xbc\x12\x88\x34\x11\x09"  # Salt to add when hashing password

    master_password = input("Please enter your master password: ")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,  # Makes it computationally slow to guess
    )

    # Derive the key and encode it for Fernet
    derived_key = base64.urlsafe_b64encode(kdf.derive(master_password.encode("utf-8")))
    cipher_suite = Fernet(derived_key)
    return cipher_suite
