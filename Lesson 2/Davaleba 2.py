import math

# დავალება 1

# while True:
#     print("-----------BMI CALCULATOR-----------")
#     try:
#         weight = float(input("შეიყვანეთ თქვენი წონა: "))
#         height = float(input("შეიყვანეთ თქვენი სიმაღლე მეტრებში ( მაგალითად : 1.88): "))
#         BMI = weight / (height ** 2)
#         print("თქვენი BMI არის " + str(round(BMI, 1)))
#         if BMI < 19:
#             print("You are underweight")
#             break
#         elif 19 <= BMI < 25:
#             print("You are normalweight")
#             break
#         elif BMI > 25:
#             print("You are overweight")
#             break
#     except ValueError:
#         print("შეიყვანეთ სწორი ციფრები")



# დავალება 2

# while True:
#     print("---------CALCULATOR-----------")
#
#     try:
#         num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
#         num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
#         operator = input("შეიყვანეთ არითმეტიკული ოპერატორი ( - + / * ): ")
#
#         if operator != "-" and operator != "+" and operator != "/" and operator != "*":
#             print("შეიყვანეთ სწორი ოპერატორი")
#             continue
#         elif operator == "/":
#             # ითვლის განაყოფს და კონსოლში გამოყავს შედეგი
#             sum = num1 / num2
#             print("თქვენი ციფრების განაყოფი არის " + str(sum))
#
#             # პროგრამის გაგრძელება/გათიშვა
#             answer = input("თუ გსურთ გათიშოთ პროგრამა, შეიყვანეთ ,,break'': ")
#             if answer == "break":
#                 break
#             else:
#                 continue
#
#         elif operator == "*":
#             # ითვლის ნამრავლს და კონსოლში გამოყავს შედეგი
#             sum = num1 * num2
#             print("თქვენი ციფრების ნამრავლი არის " + str(sum))
#
#             # პროგრამის გაგრძელება/გათიშვა
#             answer = input("თუ გსურთ გათიშოთ პროგრამა, შეიყვანეთ ,,break'': ")
#             if answer == "break":
#                 break
#             else:
#                 continue
#
#         elif operator == "+":
#             # ითვლის ჯამს და კონსოლში გამოყავს შედეგი
#             sum = num1 + num2
#             print("თქვენი ციფრების ჯამი არის " + str(sum))
#
#             # პროგრამის გაგრძელება/გათიშვა
#             answer = input("თუ გსურთ გათიშოთ პროგრამა, შეიყვანეთ ,,break'': ")
#             if answer == "break":
#                 break
#             else:
#                 continue
#
#         elif operator == "-":
#             # ითვლის სხვაობას და კონსოლში გამოყავს შედეგი
#             sum = num1 - num2
#             print("თქვენი ციფრების სხვაობა არის " + str(sum))
#
#             # პროგრამის გაგრძელება/გათიშვა
#             answer = input("თუ გსურთ გათიშოთ პროგრამა, შეიყვანეთ ,,break'': ")
#             if answer == "break":
#                 break
#             else:
#                 continue
#
#     except ValueError:
#         print("შეიყვანეთ სწორი ციფრები")


# დავალება 3

while True:
    print("--------დავალება 3-----------")

    try:
        num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
        num3 = float(input("შეიყვანეთ მესამე რიცხვი: "))

        numbers = [num1, num2, num3]

        if num1 == num2 or num2 == num3 or num3 == num1:
            print("შეიყვანეთ განსხვავებული ციფრები!")

        highest = numbers[0]

        for i in numbers:
            if i > highest:
                highest = i

        print("უდიდესი რიცხვია:", highest)
        break
    except ValueError:
        print("შეიყვანეთ სწორი ციფრები!")