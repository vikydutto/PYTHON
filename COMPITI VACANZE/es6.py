#DUTTO VITTORIA COMPITI DELLE VACANZE NATALIZIE
"""6. Il file covid-19_gen1.txt contiene la sequenza genomica RNA di un
virus SARS-COV-2. L&#39;RNA è una sequenza in cui si alternano 4
simboli (detti nucleotidi): A, T, C, G. L&#39;RNA del virus SARS-COV-2
contiene 29903 nucleotidi. Leggi covid-19_gen1.txt il file e crea un
dizionario Python avente come chiavi i nucleotidi A, T, C, G e come
valori i rispettivi conteggi."""

contatore = {"A":0, "T": 0, "C": 0, "G": 0}
nomeFile = input("Inserire il nome del file da leggere: ")
file = open(nomeFile, "r")

righe = file.readlines()

for riga in righe:
    for i in range (len(riga)):
        if riga[i] != "\n":
            contatore[riga[i]] += 1

print(contatore)
