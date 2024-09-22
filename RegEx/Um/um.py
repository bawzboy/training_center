import re

def main():
    print(count(input("Text: ")))

def count(input_string):
    return len(re.findall(r"\bum\b", input_string, re.IGNORECASE))

if __name__ == "__main__":
    main()
