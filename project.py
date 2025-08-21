# A utility to transform a text file of vocabulary words into a csv file.
# Currently configured to work with a list of Japanese words formatted as follows:
# Japanese Word: English Word

# TO DO:
# add user input for:
###### number of columns
###### labels for columns
###### text file
###### character used as seperator (':', etc)
###### save as: "USERINPUT.csv"
# make column names in make_list() generic
# make UI look & feel nice
# function for checking formatting of text file --> runs before other functions & offers suggestions
# error handling
# pytest

import csv
import tkinter

def main():
    root = tkinter.Tk()
    root.title("Text to CSV")
    header = tkinter.Label(root, text="a utility for converting text files to csv")
    header.pack()
    root.mainloop()

    #list = make_list("JLPTN3vocab.txt")
    #make_file(list, "vocab.csv")


def make_list(txt):
    words = []

    with open(txt) as file:
        for line in file:
            if ":" in line:
                japanese, english = line.strip().split(":")
                words.append({'japanese': japanese.strip(), 'english': english.strip()})
    
    return words # returns list of words


def make_file(list, export_name):
    with open(export_name, "a") as file:
        for item in list:
            writer = csv.writer(file)
            writer.writerow(item.values())


if __name__ == "__main__":
    main()