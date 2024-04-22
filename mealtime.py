def main():
    user_time = convert(input("What time is it? "))
    if 7 <= user_time <= 8:
        print("It's breakfast time!")
    elif 12 <= user_time <= 13:
        print("It's lunch time!")
    elif 18 <= user_time <= 19:
        print("It's lunch time!")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60
    hours = float(hours)
    return hours + minutes

if __name__ == "__main__":
    main()
