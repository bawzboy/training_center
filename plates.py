def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return (starting_letters(s) and 
            valid_length(s) and 
            numbers_at_end(s) and 
            no_invalid_characters(s)
            )

def starting_letters(s):
    return (s[0].isalpha() and s[1].isalpha())

def valid_length(s):
    return 1 < len(s) < 7

def numbers_at_end(s):
    for i in range(len(s)):
        if s[i].isdecimal():
            if s[i] == '0':
                return False
            return s[i:].isdecimal()
    return True


def no_invalid_characters(s):
    return s.isalnum()


if __name__ == "__main__":
    main()
