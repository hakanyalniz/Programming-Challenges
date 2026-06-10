def input_HUB(prompt: str, input_type: int):
    raw_input: str = input(prompt)

    match input_type:
        case 0:
            return get_password_length_input()
        case 1:
            return include_special_toggle()
        case 2: 
            return read_passwords()
        case _:
            raise ValueError("The case for this input type can not be found!")


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
    """
    A function that returns true or false to toggle special character list. 
    The user can only enter true or false. Only accepts those two inputs.
    """
        
    while True:
        raw_input = input("Include special characters: ")
        try:   
            if raw_input.lower() == "true":
                return True
            elif raw_input.lower() == "false" or raw_input == "":
                return False
        except ValueError:
            print("Please enter True or False")

def write_password_toFile(generated_password: str):
    """
    Writes the selected password into a file.
    """

    raw_input = input("Leave a note for your password: ")

    with open("passwords.txt", "a", encoding="utf-8") as file:
        file.write(f"{generated_password} , Note: {raw_input}\n")

def read_passwords():
    """
    Opens a password.txt file and reads from it, then prints them on screen.
    """

    while True:
        raw_input = input("Read your passwords?: ")
        try:   
            if raw_input.lower() == "true":
                    with open("passwords.txt", "r", encoding="utf-8") as file:
                        print("\n\n")
                        for line in file:
                            # strip() removes the trailing newline character (\n)
                            print(line.strip())
                    print("\n\n")
                    exit()
                            
            elif raw_input.lower() == "false" or raw_input == "":
                return False
        except ValueError:
            print("Please enter True or False")



# Refactor all the code here so the inputs and so on are in one main function
# while the utility is left to the functions themselves
# Where the user can chose to either enter new password, read from it, see them, delete them and so on
# Refactor to change and overhaul the UI