def main():
    amount_due = 50
        
    while amount_due > 0:
        coin = get_coin()
        amount_due = amount_due - coin
        if amount_due > 0:
            print("Amount due:", amount_due)
        else:
            change_owed = 0 - amount_due
            print("Change Owed: ", change_owed)

def get_coin():
    c = int(input("Insert Coin: "))
    while c not in [5, 10, 25]:
        c = int(input("Insert Coin: "))    
    else:
        return c

if __name__ == "__main__":
    main()
