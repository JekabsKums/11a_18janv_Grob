import csv
import json
faila_nosaukums = input("Ievadi faila nosaukumu: ")

try:
    with open(faila_nosaukums, 'r', encoding='utf8') as fails:
        print(fails.read())







except FileNotFoundError:
    print("Fails netika atrasts")
except StopIteration:
    print("Fails ir tukšs")
except Exception as e:
    print(f"Radusies kļūda {e}")