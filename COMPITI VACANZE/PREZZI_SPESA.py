#DUTTO VITTORIA COMPITI DELLE VACANZE NATALIZIE
"""7. Il file prezzi.csv (separatore ;) contiene le serie storiche mensili dei
prezzi di alcuni generi alimentari dal Settembre 2011 a Dicembre
2016. Immagina una spesa costituita da 5 generi alimentari a tua
scelta e crea una lista contenente la serie storica del prezzo della tua
spesa ottenuta sommando i prezzi dei generi alimentari scelti.
Calcola mese / anno in cui la tua spesa ha costi minimi e massimi."""
import sys

prezzo_spesa = []
lista_mesi=[]

#nomeFile = input("Inserire il nome del file da leggere: ")
file = open("prezzi.csv", "r")

prodotti = []
for i in range (5):
    prodotti.append(int(input(f"Inserire l'indice del {i + 1} prodotto: ")))

righe = file.readlines()

righe.pop(0)

for riga in righe:
    somma = 0
    campi = riga.split(";")
    lista_mesi.append(campi[1] + " " + campi[0])
    for prodotto in prodotti:
        somma += float(campi[prodotto])
    prezzo_spesa.append(somma)

print(prezzo_spesa)
print(lista_mesi)

prezzoMin = 10000
indiceMin = None
prezzoMax = 0
indiceMax = None

for i, prezzo in enumerate(prezzo_spesa):
    if prezzo < prezzoMin:
        prezzoMin = prezzo
        indiceMin = i
for i, prezzo in enumerate(prezzo_spesa):
    if prezzo > prezzoMax:
        prezzoMax = prezzo
        indiceMax = i

print(f"La spesa ha un prezzo minimo di {prezzoMin:.2f} € nel mese di {lista_mesi[indiceMin]}")
print(f"La spesa ha un prezzo massimo di {prezzoMax:.2f} € nel mese di {lista_mesi[indiceMax]}")
