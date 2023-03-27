
numbers = input("Podaj liczby oddzielone przecinkami:\n ")
number_list = numbers.split(",")

maxNumber = -float("inf")
minNumber = float("inf")

for e in number_list:
    e = int(e)
    if e > maxNumber:
        maxNumber = e
    if e < minNumber:
        minNumber = e

print("Największa liczba to:", maxNumber)
print("Najmniejsza liczba to:", minNumber)
