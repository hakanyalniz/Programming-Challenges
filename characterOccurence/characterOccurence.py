toggle_capital: bool = True if input("Count capital letters as separate instances?\n").lower() == "true" else False

user_name: str = input("Enter string: ")
count_string: dict[str, int] = {}


for i in range(len(user_name)):
    if user_name[i] in count_string:
        count_string[user_name[i]] += count_string[user_name[i]]
    else:
        count_string[user_name[i]] = 1


print(count_string)