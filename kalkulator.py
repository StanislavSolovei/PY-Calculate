num1 = int(input("Wprowadź pierwszy numer:"))
# Przykładowe dane wejściowe miałyby następującą postać: '1+2' lub '3-2', itd.
def myCalculator(inputString):
  # Wyodrębnij liczby i operator z inputString

    #++++++Kod poniżej tej linii!-------
    # Wskazówka: Użyj wykrojenia, aby uzyskać liczby i operatora! Następnie użyj konwersji typu, aby uzyskać liczbę i znak!

    #++++++Kod powyżej tej linii-------

 # Argumenty funkcji w tym przykładzie powinny pochodzić z podziału powyższego ciągu wejściowego
  printCalculation(num1,operator,num2) # Oto przykład wartości, które są wprowadzane do funkcji! printCalculation(1,'+',2)

# printCalculation przyjmuje jako argumenty pierwszą liczbę w ciągu, operator, drugą liczbę
def printCalculation(num1,operator,num2):
    if(operator == '+'): # Dodaj pozostałe operatory za pomocą elif 
        print(num1,' ',operator, ' ', num2, ' = ',num1+num2) # Wynik zostanie wyświetlony jako "1 + 2 = 3" na przykład
    else:
        print("Error!") # To tylko sprawdza, czy poprawnie wprowadziłeś dane!

# Wprowadź tutaj!
inputString = input("EG.'1+2' ")

myCalculator(inputString)