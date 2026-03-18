import math

while True:
    try:
        kateti1 = input("შეიყვანეთ პირველი კათეტი: ")
        kateti2 = input("შეიყვანეთ მეორე კათეტი: ")
        kateti1 = float(kateti1)
        kateti2 = float(kateti2)
        hipotenuza = math.sqrt(kateti1 ** 2 + kateti2 ** 2)
        print("ჰიპოტენუზა არის " + str(hipotenuza))
        break
    except ValueError:
        print("შეიყვანეთ სწორი ციფრები")