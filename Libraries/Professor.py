from random import randint

def main():
    level = get_level()
    count = 0
    for i in range(10):
        first_number = generate_integer(level)
        second_number = generate_integer(level)
        for i in range(3):
            try:
                answer = int(input(f"{first_number} + {second_number} = "))
                if answer == first_number + second_number:
                    count += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("An error occured")
                                                                                    #  print("Correct answer is: ", (first_number + second_number))
    print(f"You gave {count} correct answers")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            print("An error occured")

def generate_integer(level):
    match level:
        case 1:
            generated_integer = randint(0, 9)
        case 2:
            generated_integer = randint(10, 99)
        case 3:
            generated_integer = randint(100, 999)
    return generated_integer

if __name__ == "__main__":
    main()
