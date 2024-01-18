import csv
vards = input("Ievadi savu vārdu: ")
try:
    with open ("lietotajs.csv", "w", encoding="utf8" ) as x:
        csvrakstitajs = csv.writer(x)
        print("Vārds pievienots veiksmīgi")  
except StopIteration:
    print("Failā nekā nav")
except FileNotFoundError:
    print("Fails ar nosaukumu lietotajs.csv netika atrasts")
except Exception as e:
    print(f"Notikusi kļūda {e}")