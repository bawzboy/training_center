def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    result = gauge(percentage)
    print(result)

def convert(fraction):
    top, bottom = fraction.split("/")
    return round((int(top) / int(bottom)) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage} %"

if __name__ == "__main__":
    main()
