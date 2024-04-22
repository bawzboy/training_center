def main():
    amount_due : int = 50
    input_money = insert_coin()
    
    while amount_due > 0:
        amount_due = amount_due - input_money

    print("Amount Due: ", amount_due)

def insert_coin():
    return int(input("Insert Coin: "))

def insert_coin_correct():
    

if __name__ == "__main__":
    main()
