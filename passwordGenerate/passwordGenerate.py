import random

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
            if (int_length < 12):
                print("Please pick a greater length. \n")
                continue
            return int_length
        except ValueError:
            print("Please enter a number.\n")

def include_special_toggle() -> bool:
    while True:
        raw_input = input("Include special characters:")
        try:   
            if raw_input.lower() == "true":
                return True
            elif raw_input.lower() == "false":
                return False
        except ValueError:
            print("Please enter True or False")

input("You will be asked the following. You can also press enter for default:\n" \
"To include special characters in password generation or not. (True or False) (!, @, # and so on) \n" \
"Password length. Minimum is 12 length.\n" \
"Press enter to continue.\n" \
)

# If we toggle true, use 1 or else use 0. Then add it to the random number upper limit. This will include symbols list or not
special_char_toggle = 1 if include_special_toggle() else 0 
password_length: int = get_password_length_input()
final_password: str = ""

lower_alphabet: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_alphabet: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols: list[str] = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "+", "="]

for index in range(password_length):
    match random.randint(0, 2 + special_char_toggle):
        case 0:
            final_password += lower_alphabet[random.randint(0,20)]
        case 1:
            final_password += upper_alphabet[random.randint(0,20)]
        case 2:
            final_password += str(numbers[random.randint(0,9)])
        case 3:
            final_password += symbols[random.randint(0, 11)]
        case _: pass

print(final_password)



# 16 long
# optional symbol characters included
# or only characters
# or characters and numbers
# store selected passwords in a notepad
# read from the notepad to show all selected passwords
# add note to the selected passwords, so the user can note where they belong
# later change the notepad design to encrypted