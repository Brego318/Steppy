import random

lives = 5

print("-----------GUESSING GAME-----------")

while True:
    random_number = random.randint(1, 101)
    try:
        answer = int(input("შეიყვანეთ ციფრი ერთიდან ასამდე: "))
    except ValueError:
        print("შეიყვანეთ სწორი რიცხვი ერთიდან ასამდე!")
        continue

    if answer == random_number:
        print(f"გილოცავთ, თქვენ მოიგეთ! სწორი ციფრი იყო {random_number}")
        break
    elif answer <= 0 or answer > 100:
        print("შეიყვანეთ სწორი რიცხვი!")
        if lives == 0:
            print(f"სამწუხაროა, თქვენ წააგეთ! სწორი რიცხვი იყო {random_number}")
            print("-------------------GAME OVER-------------------")
            break
        continue
    elif answer > random_number:
        print("თქვენი პასუხი მეტია რანდომ რიცხვზე!")
        print("თქვენ დაგაკლდათ 1 სიცოცხლე.")
        lives -= 1
        print(f"დარჩენილი სიცოცხლეები {lives}")
        if lives == 0:
            print(f"სამწუხაროა, თქვენ წააგეთ! სწორი რიცხვი იყო {random_number}")
            print("-------------------GAME OVER-------------------")
            break
        continue
    elif answer < random_number:
        print("თქვენი ციფრი ნაკლებია რანდომ რიცხვზე!")
        print("თქვენ დაგაკლდათ 1 სიცოცხლე.")
        lives -= 1
        print(f"დარჩენილი სიცოცხლეები {lives}")
        if lives == 0:
            print(f"სამწუხაროა, თქვენ წააგეთ! სწორი რიცხვი იყო {random_number}")
            print("-------------------GAME OVER-------------------")
            break
        continue

