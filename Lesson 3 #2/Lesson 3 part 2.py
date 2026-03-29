import random

# დავალება 1

# answer = int(input("შეიყვანეთ სასურველი რიცხვი: "))
# result = 1
#
# for i in range(1, answer + 1):
#     result *= i
#     answer -= 1

# print(result)

# დავალება 2

# for i in range(1, 10):
#     for j in range(1, 10):
#         result = i * j
#         print(f"{i} x {j} = {result}")

# დავალება 3


class aparati():
    def __init__(self):
        print("მოგესალმებით, CBT ბანკში!")
        self.balansi = 500
        self.gadasaxadi = 50

        self.pinkodi = 1234
        self.pinkodis_sheyvana()

    def pinkodis_sheyvana(self):
        cda = 4
        while True:
            upasuxe = input("შეიყვანეთ თქვენი პინკოდი: ")
            if upasuxe == str(self.pinkodi):
                self.operacia()
                break
            elif upasuxe != str(self.pinkodi):
                print(f"ცადეთ თავიდან! დაგრჩათ {cda-1} ცდა!")
                cda -= 1
                if cda == 0:
                    print("ავტორიზაცია დაბლოკილია!")
                    break
                continue



    def operacia(self):
        print("აირჩიეთ ოპერაცია:\n"
              "1. ჩემი ბალანსის ნახვა\n"
              "2. გადასახადების გადახდა\n")
        self.answer = input("შეიყვანეთ ოპერაციის ნიშნული( 1 ან 2 ): ")

        if self.answer == "1":
            self.balansis_naxva()
        elif self.answer == "2":
            print(f"თქვენი გადასახადი არის: ${self.gadasaxadi}")
            while True:
                response = input("გსურთ თანხის გადახდა? ( კი / არა ): ")
                if response == "კი":
                    self.gadaxda()
                    break
                elif response == "არა":
                    print("ოპერაცია დასრულებულია!")
                    break
                else:
                    print("შეიყვანეთ კი ან არა!")
                    continue

    def balansis_naxva(self):
        print(f"თქვენი ბალანსი: ${self.balansi}")
        while True:
            answer = input(("გსურთ მენიუში დაბრუნება? ( კი / არა ): "))
            if answer == "კი":
                self.operacia()
                break
            elif answer == "არა":
                print("ოპერაცია დასრულდა!")
                break
            else:
                print("შეიყვანეთ კი ან არა!")
                continue


    def gadaxda(self):
        print(f"გადასახდელი თანხა: {self.gadasaxadi} ლარი")

        while self.gadasaxadi > 0:
            try:
                fuli = int(input("გთხოვთ შეიტანოთ კუპიურა (5, 10, 20): "))
            except ValueError:
                print("შეიტანეთ სწორი კუპიურა!")
                continue

            if fuli not in [5, 10, 20]:
                print("შეიყვანეთ ვალიდური კუპიურა!")
                continue

            self.gadasaxadi -= fuli
            self.balansi -= fuli

            if self.gadasaxadi > 0:
                print(f"დარჩენილი გადასახადი: {self.gadasaxadi}")
            elif self.gadasaxadi == 0:
                print("გადასახადი სრულად გადახდილია!")
            else:
                change = abs(self.gadasaxadi)
                print("გადასახადი გადახდილია!")
                print(f"თქვენი ხურდა არის: {change} ლარი")
                self.balansi += change
                self.gadasaxadi = 0

        while True:
            answer = input("გსურთ მენიუში დაბრუნება? (კი / არა): ")
            if answer == "კი":
                self.operacia()
                break
            elif answer == "არა":
                print("ოპერაცია დასრულდა!")
                break

aparati()