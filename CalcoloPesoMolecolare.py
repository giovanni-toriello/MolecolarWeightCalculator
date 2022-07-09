import re
from urllib.request import urlopen
import json

data_json = json.loads(
    urlopen("https://periodic-table-elements-info.herokuapp.com/elements").read())  # lettura del dizionario
atomicMass = [data["atomicMass"] for data in data_json]  # si legge la massa atomica
name = [data["name"] for data in data_json]  # si legge il nome
name = [data["name"] for data in data_json]

dataSetElementi = {}
for data in data_json:  # dati i dati nell'url json
    try:
        atomicMass = data["atomicMass"][0:5].replace('[', '').replace(']',
                                                                      '')  # vengono presi i dati di massa atomica e vengono sostituite le parentesi quadre
        name = data["name"]  # vengono presi i dati del nome
        symbol = data["symbol"]  # vengono presi i simboli
        dataSetElementi.update(
            {symbol: [name, float(atomicMass.replace('[', '').replace(']', ''))]})  # vengono compresi i 3 elementi
    except:
        continue


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
            print("\n")
            # Stampa elemento considerato
            print(dataSetElementi[pedice[0]])
        # False: Sommo normalmente
        else:
            valoreElemento = dataSetElementi[elementiSingoli[i]][1]
            # Stampa elemento considerato
            print(dataSetElementi[elementiSingoli[i]])
        # Calcolo i valore dei componenti che compongono il composto
        pesoMolecolare = pesoMolecolare + valoreElemento
    print("\n")
    print("Calcolo il peso molecolarem di " + composto + "...")
    print("Il peso molecolare di " + composto + " è uguale a: " + str(pesoMolecolare) + " g/mol")


def compostoSplitted(composto):
    # Splitting dei componenti del composto tramite regex
    # Appena vede una lettera maiuscola divide la stringa
    compostoSplitted = re.findall('[A-Z][^A-Z]*', composto)
    return compostoSplitted


def run():
    calcoloPesoMolecolare(input("Inserisci Composto:"))
    while input("\nVuoi continuare?\n[y/n]\n") == 'y':
        calcoloPesoMolecolare(input("Inserisci Composto:\n"))
    print("\nTermino esecuzione...")
