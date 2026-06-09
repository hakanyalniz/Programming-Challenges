import random
from helpers import include_special_toggle, get_password_length_input, write_password_toFile


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

write_password_toFile(final_password)

print(final_password)



# store selected passwords in a notepad
# read from the notepad to show all selected passwords
# add note to the selected passwords, so the user can note where they belong
# later change the notepad design to encrypted