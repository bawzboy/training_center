def parse_numeric_date(anno_domini):
    m, d, y = anno_domini.split("/")
    try:
        return int(m), int(d), int(y)
    except ValueError:
        print("Please enter valid date") 

def parse_written_date(anno_domini):
    months = [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]
    m, d, y = anno_domini.replace(",", "").split(" ")
    if m in months:
        m = months.index(m) + 1
    try:
        return int(m), int(d), int(y)
    except ValueError:
        print("Please enter valid date") 

def main():
    anno_domini = input("Anno Domini: ")
    try:
        if "/" in anno_domini:
            month, day, year = parse_numeric_date(anno_domini)
        else:
            month, day, year = parse_written_date(anno_domini)
        print(f"{year}-{month:02}-{day:02}")
    except ValueError:
        print("Please enter valid date")

if __name__ == "__main__":
    main()
