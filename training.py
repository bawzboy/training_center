def main():
    amount_due : int = 50
    
    while amount_due > 0:
        amount_due = amount_due - check_coin()
        print("Amount due:", amount_due)

def get_coin():
    return int(input("Insert Coin: "))

def check_coin():
    if get_coin() == 5:
        return
    


if __name__ == "__main__":
    main()
