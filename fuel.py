top, bottom = input("Fraction: ").split("/")

try:
    print(int(top) / int(bottom), "%")
except (ValueError, ZeroDivisionError):
    ...

# if __name__ == "__main__":
#     main()
