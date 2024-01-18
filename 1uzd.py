fails=input("Ievadi teksta faila nosaukumu: ")

with open(fails, 'r', encoding='utf8') as x:
   a = x.read()
   print(a)