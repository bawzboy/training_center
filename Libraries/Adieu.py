import inflect

p = inflect.engine()
list_of_names = []

while True:    
    try:
        list_of_names.append(input("Name: "))
        adieu_to = p.join((list_of_names))
    except EOFError:
        print("Adieu, adieu, to", adieu_to)
        break
