it = 4

while it > 1:
    print(it)
    it = it - 1

print("While loop is done")

print(" ================================================ ")

it1 = 4

while it1 > 1:
    if it1 != 3:
        print(it1)
    it1 = it1 - 1

print("Skip 3")

print(" ================================================ ")

it2 = 10

while it2 > 1:
    if it2 == 3:
        break
    print(it2)
    it2 = it2 - 1

print("Break")

print(" ================================================ ")

it3 = 10

while it3 > 1:
    if it3 == 9:
        it3 = it3 - 1
        continue
    if it3 == 3:
        break
    print(it3)
    it3 = it3 - 1

print("Continue Statement")
