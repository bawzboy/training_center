grocery_list = {}

while True:
    try:
        grocery_item = input("Item: ").upper()
        if grocery_item not in grocery_list:
            grocery_list[grocery_item] = 1
        else:
            grocery_list[grocery_item] = grocery_list[grocery_item] + 1

    except EOFError:
        for key, value in sorted(grocery_list.items()):
            print(key, value)
        break
