import csv
faila_nosaukums=input("Ievadi sava faila nosaukumu: ")
a=[]
with open(faila_nosaukums, 'r', encoding='utf8') as x:
    lasitajs = csv.reader(x)
    for rinda in lasitajs:
            a.append(rinda[1])