import getpass
import random
import statistics
from statistics import mode


ilosc_rund = input("Podaj ilosc rund: ")
ilosc_graczy = int(input("Podaj ilosc graczy: "))
gracz1andPC = None
gracz2 = None
score_list = []


def randomOption():
    options = [1, 2, 3]
    temp = random.sample(options, 1)
    return temp[0]


def optionToString(wybor):
    if wybor == 1:
        return "Papier"
    elif wybor == 2:
        return "Kamien"
    elif wybor == 3:
        return "Nozyce"
    if wybor == 10:
        return "Remis"



def winnerOfRound(wybor1, wybor2): #1 papier, 2 kamien, 3 nozyce
    if wybor1 == 1 and wybor2 == 2:
        return 1
    if wybor1 == 1 and wybor2 == 3:
        return 2
    if wybor1 == 2 and wybor2 == 1:
        return 2
    if wybor1 == 2 and wybor2 == 3:
        return 1
    if wybor1 == 3 and wybor2 == 1:
        return 1
    if wybor1 == 3 and wybor2 == 2:
        return 2
    if wybor1 == wybor2:
        return 10
    return 100



from  statistics import  mode

def winnerIs(list):
    winner = mode(score_list)
    print(winner)
    if winner == 1:
        return gracz1andPC
    if winner == 2:
        return gracz2
    else:
        return "remis"


if ilosc_graczy == 1:
    print("Bedziesz grac z komputerem")
    gracz1andPC = "PC"
    gracz2 = input("Podaj swoj nick: ")

elif ilosc_graczy == 2:
    print("Bedziesz grac w 2 osoby")
    gracz1andPC = input("Podaj nick gracza 1: ")
    gracz2 = input("Podaj swoj nick gracza 2: ")
else:
    print("Nieprawidlowa ilosc graczy")

while len(score_list) != int(ilosc_rund):
    print("1.Papier\n2.Kamien\n3.Nozyce")
    if ilosc_graczy == 1:
        wyborPc = randomOption()
        wybor2 = input("")

        print("PC: ", optionToString(wyborPc))
        print(gracz2, ": " , optionToString(int(wybor2)))

        result = winnerOfRound(wyborPc, int(wybor2))

        if result == 1:
            print("runde wygrywa", gracz1andPC)
        if result == 2:
            print("runde wygrywa", gracz2)
        if result != 10:
            score_list.append(result)
    if ilosc_graczy == 2:
        wyborGracz1 = getpass.getpass("Gracz 1:")
        wyborGracz2 = getpass.getpass("Gracz 2:")

        print(gracz1andPC, ":", optionToString(int(wyborGracz1)))
        print(gracz2, ":", optionToString(int(wyborGracz2)))

        result = winnerOfRound(int(wyborGracz1), int(wyborGracz2))

        if result == 1:
            print("runde wygrywa", gracz1andPC)
        if result == 2:
            print("runde wygrywa", gracz2)
        if result != 10:
            score_list.append(result)

print("gre wygrywa: ", winnerIs(score_list))