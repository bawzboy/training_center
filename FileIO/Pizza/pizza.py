import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Wrong number of arguments")
    
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Wrong file format")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, tablefmt = "grid"))

    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()
