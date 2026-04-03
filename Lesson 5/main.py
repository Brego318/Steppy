import random

# დავალება 1

numbers = [1, 2, 3, 4, 5]
sum = 0

for i in numbers:
    sum += i

print(f"ჯამი: {sum}")
print(f"საშუალო: {sum/5}")

# დავალება 2

sia = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
unikaluri = []

for i in sia:
    if i not in unikaluri:
        unikaluri.append(i)

print(unikaluri)

# დავალება 3

a = -50
b = 50

new = [random.randint(a, b) for _ in range(20)]

luwebi = [i for i in new if i % 2 == 0]

print(new)
print(luwebi)

# დავალება 4
long_names = []
short_names = []

while True:
    answer = input("შეიყვანეთ სახელი: ")


    if len(answer) > 3 and answer not in ["stop", "quit", "exit"]:
        long_names.append(answer.lower().strip().title())
    elif len(answer) < 3 and answer not in ["stop", "quit", "exit"]:
        short_names.append(answer.lower().strip().title())


    if answer.lower() == "stop" or answer.lower() == "quit" or answer.lower() == "exit":
        print(short_names)
        print(long_names)
        break