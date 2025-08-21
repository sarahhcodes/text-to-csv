# A utility to transform a text file of vocabulary words into a csv file.
# Currently configured to work with a list of Japanese words formatted as follows:
# Japanese Word: English Word

# TO DO:
# add all the flags, including:
###### number of columns
###### labels for columns
###### text file
###### character used as seperator (':', etc)
###### save as: "USERINPUT.csv"
# make column names in make_list() generic
# function for checking formatting of text file --> makes sure that file EXISTS and that it's formatted as per user's request
###### runs before other functions & offers suggestions
# error handling
# pytest

import argparse
import csv

def main():
    parser = argparse.ArgumentParser(description="Convert text files to CSV files")
    parser.add_argument("-i", "--input", help="text file to input", required=True)
    args = parser.parse_args()

    list = make_list(args.input)
    make_file(list, "vocab.csv")


def make_list(txt):
    """
    Creates list of lines in the text file
    
    :param txt: Name of text file
    :type txt: str
    :raise ValueError: If no such file exists
    :return: A list of dictionaries for each line in file
    :rtype: list
    """
    words = []

    # add exception for ValueError - no such file found
    with open(txt) as file:
        for line in file:
            if ":" in line:
                japanese, english = line.strip().split(":")
                words.append({'japanese': japanese.strip(), 'english': english.strip()})
    
    return words # returns list of words


def make_file(list, export_name):
    """Converts list to CSV file"""
    with open(export_name, "a") as file:
        for item in list:
            writer = csv.writer(file)
            writer.writerow(item.values())


if __name__ == "__main__":
    main()