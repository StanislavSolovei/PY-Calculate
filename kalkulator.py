num1 = int(input("Wprowadz pierwszy numer:"))
operator = input("Wprowadz operator (+,-,*,/):")
num2 = int(input("Wprowadz drugi numer:"))

if operator == "+":
    print(num1, operator, num2,'=',num1+num2)

if operator == "-":
    print(num1, operator, num2,'=',num1-num2)

if operator == "*":
    print(num1, operator, num2,'=',num1*num2)

if operator == "/":
    if num2 != 0:
        print(num1, operator, num2, '=',num1/num2)
    else:
        print("Error! Nie mozna dzielic przez zero.")


