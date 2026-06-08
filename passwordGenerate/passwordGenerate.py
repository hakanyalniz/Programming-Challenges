import random

password_length: int = 16
final_password: str = ""

lower_alphabet: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_alphabet: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in range(password_length):
    final_password += "j"


# 16 long
# optional symbol characters included
# or only characters
# or characters and numbers