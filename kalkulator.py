example = input("Napisz przykład:")

checked = example.split()

if len(checked) == 3:
    a = float(checked[0])
    operator = checked[1]
    b = float(checked[2])

    if operator == "+":
        print("Twój wynik:", a + b)
    elif operator == "-":
        print("Twój wynik:", a - b)
    elif operator == "*":
        print("Twój wynik:", a * b)
    elif operator == "/":
        if b != 0:
            print("Twój wynik:", a / b)
        else:
            print("Błąd nie można dzielić przez zero!")
    else:
        print("Nie wiadoma operacja!")
else:
    print("Nie dobrze napisał przykład!")

