toggle_capital: bool = True if input("Count capital letters as separate instances?\n").lower() == "true" else False

if toggle_capital:
    user_name: str = input("Enter string: ")
else:
    user_name: str = input("Enter string: ").lower()

count_string: dict[str, int] = {}
sorted_string_list: list[tuple[str, int]] = []


for i in range(len(user_name)):
    if user_name[i] in count_string:
        count_string[user_name[i]] += count_string[user_name[i]]
    else:
        count_string[user_name[i]] = 1

for key, value in count_string.items():
    sorted_string_list.insert(0, (key, value))

    print(f"Key: {key}, Value: {value}")

print(count_string)
print(sorted_string_list)

# Look over the dictionary one by one
# Get the largest number and put it into list
# For each check thereafter, compare with the list. If larger, put before the compared number
# If smaller, check the next number. If last number is checked and it is still not larger, put last