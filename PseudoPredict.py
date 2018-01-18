from __future__ import division
import MarkovChain_class
from random import *

# Text File Load
mc = MarkovChain_class.MarkovChain(r'/Users/JeremyKulchyk/PycharmProjects/ThesisProject/DonaldTrump.txt')

# Generate a Sentence for order 1 MC
def GenerateString(firstword, length, dicstruct):
    sentence = firstword
    word1 = firstword
    for i in range(1, length):
        index = randint(0, len(dicstruct[word1])-1)
        secondword = dicstruct[word1][index]
        sentence = sentence + ' ' + secondword
        word1 = secondword
    return sentence

# Generate a Sentence for order 2 MC
def GenerateString_2(firsttwowords, length, dicstruct):
    sentence = firsttwowords
    twowords1 = firsttwowords
    for i in range(1, length):
        index = randint(0, len(dicstruct[twowords1])-1)
        secondword = dicstruct[twowords1][index]
        sentence = sentence + ' ' + secondword
        sentenceList = sentence.split()
        twowords1 = sentenceList[len(sentenceList)-2] + ' ' + sentenceList[len(sentenceList)-1]
    return sentence

MarkovDict = mc.MarkovBuild_1()
MarkovDict2 = mc.MarkovBuild_2()

"""
first2 = 'liangelo ball'
Gensentence = GenerateString_2(first2,10,MarkovDict)
print(Gensentence + '\n')
Gensentence = GenerateString_2(first2,10,MarkovDict)
print(Gensentence + '\n')"""

firstword = 'liangelo ball'

Gensentence = GenerateString(firstword,20,MarkovDict)
print('\n' + Gensentence + '\n')
Gensentence = GenerateString(firstword,20,MarkovDict)
print(Gensentence + '\n')
Gensentence = GenerateString(firstword,20,MarkovDict)
print(Gensentence + '\n')
Gensentence = GenerateString(firstword,20,MarkovDict)
print(Gensentence + '\n' + '\n')

"""
firstword = 'fake news'

Gensentence = GenerateString_2(firstword,20,MarkovDict2)
print(Gensentence + '\n')
Gensentence = GenerateString_2(firstword,20,MarkovDict2)
print(Gensentence + '\n')
Gensentence = GenerateString_2(firstword,20,MarkovDict2)
print(Gensentence + '\n')
Gensentence = GenerateString_2(firstword,20,MarkovDict2)
print(Gensentence + '\n')"""