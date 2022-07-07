
from time import sleep
import re
from DataSetElementi import dataSetElementi


def calcoloPesoMolecolare():
 # Inizializzo la stringa del composto
    composto = input("Inserisci Composto:\n")

    # Splitting dei componenti del composto tramite regex
    compostoSplitted = []
    # Appena vede una lettera maiuscola o un numero lo divide
    compostoSplitted = re.findall('[A-Z][^A-Z]*', composto)
    # Inizializzo il peso molecolare
    pesoMolecolare = 0
    # Ciclo for per calcolare il peso
    for i in range(0, len(compostoSplitted)):
        valoreElemento = 0
        # Controllo se c'è un numero nella stringa
        # Se c'è moltiplico per il valore del componente
        if any(chr.isdigit() for chr in compostoSplitted[i]):
            pedice = re.split('(\d+)', compostoSplitted[i])
            valoreElemento = eval(pedice[1]) * dataSetElementi[pedice[0]][1]
            print(dataSetElementi[pedice[0]])
        else:
            valoreElemento = dataSetElementi[compostoSplitted[i]][1]
            print(dataSetElementi[compostoSplitted[i]])
        # Calcolo i valore dei componenti che compongono il composto
        pesoMolecolare = pesoMolecolare + valoreElemento
    print("Calcolo il peso molecolarem di " + composto + "...")
    # Puoi anche togliere questa sleep è per farlo aspettare mentre calcola
    sleep(0.7)
    print("Il peso molecolare di " + composto + " è uguale a: " + str(pesoMolecolare) + " g/mol")