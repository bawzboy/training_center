import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Wrong number of arguments")

    elif not sys.argv[1].endswith(".py"):
        sys.exit("Wrong file format")

    print("This file contains", count_lines(sys.argv[1]), "Lines of code")
    

def count_lines(file_name):
    try:
        with open(file_name) as file:
            lines = file.readlines()

        lines_of_code = 0

        for line in lines:
            line = line.strip()

            if line and not line.startswith("#"):
                lines_of_code += 1

        return lines_of_code

    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()
