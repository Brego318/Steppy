# დავალება 1

in1 = input("შეიყვანეთ წინადადება: ")
word1 = input("შეიყვანეთ პირველი სიტყვა რომელიც უნდა ჩანაცვლდეს: ")
word2 = input("შეიყვანეთ მეორე სიტყვა რითაც უნდა ჩანაცვლდეს: ")

new = in1.replace(word1, word2)
print(new)

# დავალება 2

sent = input("შეიყვანეთ წინადადება: ")
split = sent.split()
longest = split[0]

for i in split:
    if len(i) > len(longest):
        longest = i

print(i)

# დავალება 3
word1 = input("შეიყვანე პირველი სიტყვა: ").lower()
word2 = input("შეიყვანე მეორე სიტყვა: ").lower()

if len(word1) != len(word2):
    print("არ არის ანაგრამა")
else:
    count = {}

    for letter in word1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in word2:
        if letter in count:
            count[letter] -= 1
        else:
            print("არ არის ანაგრამა")
            break

    for value in count.values():
        if value != 0:
            print("არ არის ანაგრამა")
            break
    else:
        print("არის ანაგრამა")