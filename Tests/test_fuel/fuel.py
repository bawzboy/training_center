while True:
    top, bottom = input("Fraction: ").split("/")

    try:
        result = round((int(top) / int(bottom)) * 100)
        if result <= 1:
            print("E")
        elif result >= 99:
            print("F")
        else:
            print(result, "%")
        break

    except (ValueError, ZeroDivisionError):
        print("An error occured!")

# if __name__ == "__main__":
#     main()
