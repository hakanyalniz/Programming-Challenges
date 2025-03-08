# Write a short program that prints each number from 1 to 100 on a new line. 
# For each multiple of 3, print "Fizz" instead of the number. 
# For each multiple of 5, print "Buzz" instead of the number. 
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

def main():
    improvedFizzBuzz()


def ordinaryFizzBuzz():
    for i in range(1, 101):
        if (i % 3) == 0 and (i % 5) == 0:
            print("FizzBuzz")
        elif (i % 3) == 0:
            print("Fizz")
        elif (i % 5) == 0:
            print("Buzz")
        else:
            print(i)


def improvedFizzBuzz():
    fizzRules = {
    15: "FizzBuzz",
    5: "Buzz",
    3: "Fizz",
    }
    for i in range(101):
        for rule in fizzRules:
            if i % rule == 0:
                print(fizzRules[rule])
                break
            elif rule == 3:
                print(i) 
            



if __name__ == "__main__":
    main()
