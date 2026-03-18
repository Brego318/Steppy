import math
from math import floor

# დავალება 1
while True:
    try:
        kateti1 = float(input("შეიყვანეთ პირველი კათეტი: "))
        kateti2 = float(input("შეიყვანეთ მეორე კათეტი: "))
        hipotenuza = math.sqrt(kateti1 ** 2 + kateti2 ** 2)
        fartobi = (kateti1 * kateti2) / 2
        print("ჰიპოტენუზა არის " + str(hipotenuza))
        print("ფართობის არის " + str(fartobi))
        break
    except ValueError:
        print("შეიყვანეთ სწორი ციფრები")

# დავალება2

wamebi = float(input("შეიყვანეთ წამების რაოდენობა: "))

saati = wamebi // 3600

darchenili = wamebi % 3600

wutebi = darchenili // 60

b_wamebi = darchenili % 60

print(saati, "საათი,", wutebi, "წუთი,", b_wamebi, "წამი")