#DUTTO VITTORIA COMPITI DELLA VACANZE NATALIZIE
"""2. Scrivere un programma che data una lista qualsiasi la trasformi in un
      dizionario avente come chiavi gli indici della lista e come valori gli
      elementi."""

lista = []

def main():
    nVolte = int(input("Inserici il numero di elementi da inserire nella lista: "))
    for i in range (nVolte):
          dato = input(f"Inserisci il valore della cella {i}: ")
          lista.append(dato)
    dizionario = {}
    chiave = 0
    for k, elemento in enumerate(lista): #l'enumerate prende in input la lista
        dizionario[chiave] = elemento
    print(dizionario)
if __name__ == "__main__":
    main()
      

     """ dizionario= {x: elemento for x, elemento in enumerate(lista)}""" #dictionary comprension