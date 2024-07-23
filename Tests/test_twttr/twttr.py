def main():
    message = input("Input: ")
    message = shorten(message)
    print("Output:", message)
    
def shorten(text):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

    for char in text:
        if char in vowels:
            text = text.replace(char, "")
    return text

if __name__ == "__main__":
    main()
