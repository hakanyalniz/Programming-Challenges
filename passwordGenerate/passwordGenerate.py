import random

def get_password_length_input() -> int:
    while True:
        raw_length: str = input("Password length: ")
        try:
            return int(raw_length)
        except ValueError:
            print("Please enter a number.\n")

password_length: int = get_password_length_input()
final_password: str = ""

lower_alphabet: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_alphabet: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in range(password_length):
    match random.randint(0, 2):
        case 0:
            final_password += lower_alphabet[random.randint(0,20)]
        case 1:
            final_password += upper_alphabet[random.randint(0,20)]
        case 2:
            final_password += str(numbers[random.randint(0,9)])
        case _: pass

print(final_password)



# 16 long
# optional symbol characters included
# or only characters
# or characters and numbers