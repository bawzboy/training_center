import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Wrong number of arguments")

    try:
        with open(sys.argv[1]) as read_file:
            reader = csv.DictReader(read_file)

            with open(sys.argv[2], "w") as write_file:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(write_file, fieldnames = fieldnames)

                writer.writeheader()

                for row in reader:
                    last_name, first_name = row["name"].split(", ")
                    writer.writerow({"first": first_name, "last": last_name, "house": row["house"]})         

    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()
