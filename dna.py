
import csv
import sys

def main():
    #verificar se o user escreveu os argumentos
    if len(sys.argv) != 3:
        print("ex: python dna.py data.csv sequence.txt")
        sys.exit(1) # 1 = erro

    #Ler a ficheiro CSV
    with open(sys.argv[1], 'r') as f:
        database = csv.reader(f)
        all_sequences = next(database)[1:]
        #Ler a sequência de DNA
        with open(sys.argv[2], 'r') as f:
            sequence = f.read()
        #Encontrar a pessoa com todos STR iguais na base de dados
        actual_counts = [longest_match(sequence, seq) for seq in all_sequences]
        for row in database:
            name = row[0]
            #lista[indice_inicial:indice_final:passo]
            expected_counts = list(map(int, row[1:]))
            if expected_counts == actual_counts:
                print(name)
                return


        print("No match")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
