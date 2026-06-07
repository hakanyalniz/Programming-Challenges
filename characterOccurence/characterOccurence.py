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
    print(key, value)
    if len(sorted_string_list) == 0: # If no element in list, just insert it into index 0
            sorted_string_list.insert(0, (key, value))
            continue
    
    for element in sorted_string_list[:]: # element here is a tuple like ("h", 2), we create a shallow copy or else it will create infinite loop
        print("sorted_string_list", sorted_string_list)
        
        element_index: int = sorted_string_list.index(element)

        if value > element[1]: # If the value is greater than the value present in list, put it before the element
            sorted_string_list.insert(element_index, (key, value))
        elif len(sorted_string_list)-1 == element_index: # If it is not greater than, then place it last
            sorted_string_list.append((key, value))




print(count_string)
print("Sorted", sorted_string_list)

# Look over the dictionary one by one
# Get the largest number and put it into list
# For each check thereafter, compare with the list. If larger, put before the compared number
# If smaller, check the next number. If last number is checked and it is still not larger, put last

# Take the dictionary element, compare it to all list elements. If none are in list, place it first