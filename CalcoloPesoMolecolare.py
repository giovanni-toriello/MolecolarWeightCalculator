from time import sleep
import re
from DataSetElementi import dataSetElementi


def calcoloPesoMolecolare(composto):
    elementiSingoli = compostoSplitted(composto)
    # Inizializzo il peso molecolare
    pesoMolecolare = 0
    # Ciclo for per calcolare il peso
    for i in range(0, len(elementiSingoli)):
        # Ogni ciclo metto a 0 il valore dell'elemento che considero
        # Controllo se c'è un numero nella stringa
        # True: moltiplico per il valore del componente
        if any(chr.isdigit() for chr in elementiSingoli[i]):
            pedice = re.split('(\d+)', elementiSingoli[i])
            valoreElemento = eval(pedice[1]) * dataSetElementi[pedice[0]][1]
            # Stampa elemento considerato
            print(dataSetElementi[pedice[0]])
        # False: Sommo normalmente
        else:
            valoreElemento = dataSetElementi[elementiSingoli[i]][1]
            # Stampa elemento considerato
            print(dataSetElementi[elementiSingoli[i]])
        # Calcolo i valore dei componenti che compongono il composto
        pesoMolecolare = pesoMolecolare + valoreElemento
    print("Calcolo il peso molecolarem di " + composto + "...")
    # Puoi anche togliere questa sleep è per farlo aspettare mentre calcola
    sleep(0.7)
    print("Il peso molecolare di " + composto + " è uguale a: " + str(pesoMolecolare) + " g/mol")


def compostoSplitted(composto):
    # Splitting dei componenti del composto tramite regex
    # Appena vede una lettera maiuscola divide la stringa
    compostoSplitted = re.findall('[A-Z][^A-Z]*', composto)
    return compostoSplitted


def run():
    calcoloPesoMolecolare(input("Inserisci Composto:\n"))
    while input("\nVuoi continuare?\n[y/n]\n") =='y':
        calcoloPesoMolecolare(input("Inserisci Composto:\n"))
    print("\nTermino esecuzione...")
    sleep(1)
