# A utility to transform a text file of vocabulary words into a csv file.
# Currently configured to work with a list of Japanese words formatted as follows:
# Japanese Word: English Word

import csv

def main():
    words = []

    with open("JLPTN3vocab-short.txt") as file:
        for line in file:
            if ":" in line:
                japanese, english = line.strip().split(":")
                words.append({'japanese': japanese.strip(), 'english': english.strip()})

    with open("vocab.csv", "a") as file:
        for word in words:
            writer = csv.writer(file)
            writer.writerow(word.values())


if __name__ == "__main__":
    main()