from datetime import date
import inflect

def main():
    print(minutes_since(input("Your Birthdate: ")))

def minutes_since(birthdate):
    year, month, day = birthdate.split("-")
    birthdate = date(int(year), int(month), int(day))
    days_since = date.today() - birthdate
    minutes_since = days_since.days * 24 * 60
    p = inflect.engine()
    return p.number_to_words(minutes_since, andword="")

if __name__ == "__main__":
    main()
