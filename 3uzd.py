fails=input("Ievadi teksta faila nosaukumu: ")

with open(fails, 'r', encoding='utf8') as x:
   for rinda in enumerate(x):
    if rinda == 2:
        print(rinda)
    elif rinda > 2:
        break