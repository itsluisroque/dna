import csv
import pandas as pd
from js import document
from pyscript import when

def search(event):
    # Obtem a base de dados que o user escolheu
    input_database = document.getElementById("databases").value
    if input_database == "large":
        database_local = "databases/large.csv"
    else:
        database_local = "databases/small.csv"
    
    # Abre o ficheiro da base de dados
    with open(database_local, 'r') as f:
        database = csv.reader(f)
        all_sequences = next(database)[1:]

        # Obtem a sequencia de DNA que o user fez upload
        sequence_input = document.querySelector("#sequence")
        sequence = document.querySelector("#content").value

        # Contar o numero de STRs na sequencia
        actual_counts = [longest_match(sequence, str(seq)) for seq in all_sequences]

        #Encontrar a pessoa com STR iguais na base de dados
        for row in database:
            name = row[0]
            #lista[indice_inicial:indice_final:passo]
            expected_counts = list(map(int, row[1:]))
            if expected_counts == actual_counts:
                document.querySelector("#result").innerHTML = name
                print(name)
                return

        document.querySelector("#result").innerHTML = "<span>No Match</span>"

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)
    for i in range(sequence_length):
        count = 0
        while True:

            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)
    return longest_run

# Obtem os dados do ficheiro .TXT e coloca-os no campo de texto
@when('change', '#sequence')
async def processFile(*args):
    file = document.getElementById('sequence').files.item(0)
    text = await file.text()
    document.querySelector("#content").value = text
    return text