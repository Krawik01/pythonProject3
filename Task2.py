import random

miasta = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań',
          'Gdańsk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Katowice']

plan_wycieczki = random.sample(miasta, 10)

print("Plan wycieczki:")
for miasto in plan_wycieczki:
    print(miasto)
