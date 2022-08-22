#w taki sposob sa zapisywane notatki:
#---------------[01.01.2022]---------------
# lorem ipsum lorem ipsum lorem ipsumlorem ipsum
#---------------[01.02.2022]---------------

import re

with open('/home/dominik/ubuntu_shared/notatki.txt') as f:
    notatki=f.read()

# podzielenie tekstu w miejscach wystepowania dat
notatki_split = re.split("-{15}\[[0-9][0-9]\.[0-2][0-9]\.2022\]-{15}", notatki)
# stworzenie listy z dat w pliku
daty = re.findall("-{15}\[[0-9][0-9]\.[0-2][0-9]\.2022\]-{15}", notatki)
pattern = r'-{15}'
daty_v2 = [re.sub(pattern, '', i) for i in daty]
pattern = r'\['
daty_v2 = [re.sub(pattern, '', i) for i in daty_v2]
pattern = r'\]'
daty_v2 = [re.sub(pattern, '', i) for i in daty_v2]

#print(f"Data:{daty_v2[0i]} \n {notatki_split[1i+1]}") 
#znalezienie daty w liscie i wyswietlenie notatek z danej daty
date_to_find='22.07.2022'

if date_to_find in daty_v2:
    index = daty_v2.index(date_to_find)
    print(f"Data:{daty_v2[index]} \n {notatki_split[index+1]}") 
else:
    ValueError: print(f"Nie ma wpisu dla danej wartosci: {date_to_find}")

