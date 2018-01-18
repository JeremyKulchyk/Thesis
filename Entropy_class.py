import numpy as np
import string

class Entropy:
    #Init text file
    def __init__(self, file_name):
        file = open(file_name, 'r')
        unsorted_text = file.read()
        self.text = unsorted_text.lower()
        file.close()

    # Find the relative distribution of letters in the engish language
    def single_letter(self):
        # declare dictionary
        single_dictionary = {}
        # Declare list of alphabet
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
        total_counter = 0.0
        i = 0.0
        char_count = []

        # Loop through both the alphabet and text characters to count the matches.
        # This also keeps track of the total number of alphabet characters in the text.
        sum = float(len(self.text))
        for letter in alpha:
            counter = 0.0
            i += 1
            for character in self.text:
                if (letter == character):
                    counter += 1
                    total_counter += 1
            char_count.append(counter)

        # Print the total number of alphabet characters
        #print total_counter

        j = 0
        # Go through and print each frequency in order of alphabet
        for i in range(0, len(char_count)):
            single_dictionary[alpha[j]] = char_count[i] / total_counter
            j += 1

        #print single_dictionary
        print(total_counter)
        return single_dictionary

    # Finds the distribution of n=2 tuples in the English language
    def double(self):
        dicttwotuples = {}

        for i in range(1, len(self.text), 1):
            twotuple = (self.text[i - 1] + self.text[i])
            if twotuple.isalpha() and ' ' not in twotuple:
                if twotuple in dicttwotuples.keys():
                    dicttwotuples[twotuple] += 1
                else:
                    dicttwotuples[twotuple] = 1
        occurences = 0
        for value in dicttwotuples.values():
            occurences = occurences + value

        return dicttwotuples

    # Finds the distribution of n=3 tuples in the Enlgih language
    def triple(self):
        dictthreetuples = {}
        # Declare list of alphabet
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
        for i in range(2, len(self.text), 1):
            threetuple = (self.text[i - 2] + self.text[i - 1] + self.text[i])
            #if threetuple.isalpha() and ' ' not in threetuple:
            if threetuple[0] in string.ascii_lowercase and threetuple[1] in string.ascii_lowercase and threetuple[2] in string.ascii_lowercase:
                if threetuple in dictthreetuples.keys():
                    #print(threetuple)
                    dictthreetuples[threetuple] += 1
                else:
                    #print(threetuple)
                    dictthreetuples[threetuple] = 1
            #print(threetuple)

        occurencesthree = 0
        for value in dictthreetuples.values():
            occurencesthree = occurencesthree + value

        return dictthreetuples

    def quad(self):
        dictfourtuples={}

        for i in range(3, len(self.text), 1):
            fourtuple = (self.text[i-3] + self.text[i-2] + self.text[i-1] + self.text[i])
            if fourtuple.isalpha() and ' ' not in fourtuple:
                if fourtuple in dictfourtuples.keys():
                    dictfourtuples[fourtuple] += 1
                else:
                    dictfourtuples[fourtuple] = 1
                #print(fourtuple)
        #print(dictfourtuples)
        #print(max(dictfourtuples.values()))
        #print(len(dictfourtuples.values()))

        occurencesfour = 0
        for value in dictfourtuples.values():
            occurencesfour = occurencesfour + value

        return dictfourtuples


    def quin(self):
        dictfivetuples={}

        for i in range(4, len(self.text), 1):
            fivetuple = (self.text[i-4] + self.text[i - 3] + self.text[i - 2] + self.text[i - 1] + self.text[i])
            if fivetuple.isalpha() and ' ' not in fivetuple:
                if fivetuple in dictfivetuples.keys():
                    dictfivetuples[fivetuple] += 1
                else:
                    dictfivetuples[fivetuple] = 1

        occurences_five = 0
        for value in dictfivetuples.values():
            occurences_five = occurences_five + value

        return dictfivetuples


    def hex(self):
        dictsixtuples={}

        for i in range(5, len(self.text), 1):
            sixtuple = (self.text[i-5] + self.text[i-4] + self.text[i - 3] + self.text[i - 2] + self.text[i - 1] + self.text[i])
            if sixtuple.isalpha() and ' ' not in sixtuple:
                if sixtuple in dictsixtuples.keys():
                    dictsixtuples[sixtuple] += 1
                else:
                    dictsixtuples[sixtuple] = 1

        occurences_six = 0
        for value in dictsixtuples.values():
            occurences_six = occurences_six + value

        return dictsixtuples

    def sept(self):
        dictsepttuples={}

        for i in range(6, len(self.text), 1):
            septtuple = (self.text[i-6] + self.text[i-5] + self.text[i-4] + self.text[i - 3] + self.text[i - 2] + self.text[i - 1] + self.text[i])
            if septtuple.isalpha() and ' ' not in septtuple:
                if septtuple in dictsepttuples.keys():
                    dictsepttuples[septtuple] += 1
                else:
                    dictsepttuples[septtuple] = 1


        occurences_sept = 0
        for value in dictsepttuples.values():
            occurences_sept = occurences_sept + value

        return dictsepttuples

    def eight(self):
        dicteighttuples={}

        for i in range(7, len(self.text), 1):
            eighttuple = (self.text[i-7] + self.text[i-6] + self.text[i-5] + self.text[i-4] + self.text[i - 3] + self.text[i - 2] + self.text[i - 1] + self.text[i])
            if eighttuple.isalpha() and ' ' not in eighttuple:
                if eighttuple in dicteighttuples.keys():
                    dicteighttuples[eighttuple] += 1
                else:
                    dicteighttuples[eighttuple] = 1


        occurences_eight = 0
        for value in dicteighttuples.values():
            occurences_eight = occurences_eight + value

        return dicteighttuples

    def nine(self):
        dictninetuples={}

        for i in range(8, len(self.text), 1):
            ninetuple = (self.text[i-8] + self.text[i-7] + self.text[i-6] + self.text[i-5] + self.text[i-4] + self.text[i - 3] + self.text[i - 2] + self.text[i - 1] + self.text[i])
            if ninetuple.isalpha() and ' ' not in ninetuple:
                if ninetuple in dictninetuples.keys():
                    dictninetuples[ninetuple] += 1
                else:
                    dictninetuples[ninetuple] = 1


        occurences_nine = 0
        for value in dictninetuples.values():
            occurences_nine = occurences_nine + value

        return dictninetuples
