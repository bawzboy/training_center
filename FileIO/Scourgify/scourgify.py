import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Wrong number of arguments")

    try:
        with open(sys.argv[1]) as read_file:
            reader = csv.DictReader(read_file)
        for row in reader:
            last_name, first_name = row["name"].split(", ")
            with open(sys.argv[2], "w") as write_file:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(write_file, fieldnames = fieldnames)

                writer.writerow()         


        # read_csv(sys.argv[1])
        # write_csv(sys.argv[2])

    except FileNotFoundError:
        sys.exit("File not found")

def read_csv(file_to_read):
    with open(file_to_read) as file:
        reader = csv.DictReader(file)
    for row in reader:
        last_name, first_name = row["name"].split(", ")
        return last_name, first_name, row["house"] 
    
def write_csv(file_to_write):
    with open(file_to_write, "w") as file:
        fieldnames = ["first", "last", "house"]

if __name__ == "__main__":
    main()
