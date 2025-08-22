# A utility to transform a text file of vocabulary words into a csv file.

# TO DO:
# error handling
# docstrings for all functions

import argparse
import csv
import sys

def main():
    parser = argparse.ArgumentParser(description="Convert text files to CSV files")
    parser.add_argument("-i", "--input", help="Text file to input", required=True)
    parser.add_argument("-c", "--columns", nargs="+", help="Columns to include in CSV")
    parser.add_argument("-s", "--split_on", help="Character to split on (examples: ':', '-', etc)", required=True)
    parser.add_argument("-o", "--output", help="Name of CSV file to save as", required=True)
    args = parser.parse_args()

    list = make_list(args.input, args.columns, args.split_on)
    make_file(list, args.output, args.columns)


def make_list(txt, columns, split_on):
    """
    Creates list of lines in the text file
    
    :param txt: Name of text file
    :type txt: str
    :raise FileNotFoundError: If no such file exists
    :return: A list of dictionaries for each line in file
    :rtype: list
    """
    words = []
    
    try:
        with open(txt) as file:
            for line in file:
                if ":" in line:
                    row = line.strip().split(split_on)
                    dictionary = {}
                    for i in range(len(columns)):
                        dictionary[columns[i]] = row[i].strip()
                    words.append(dictionary)

    except FileNotFoundError:
        sys.exit("File not found.")

    return words # returns list of words


def make_file(list, export_name, columns):
    """Converts list to CSV file"""
    with open(export_name, "a") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(list)


if __name__ == "__main__":
    main()