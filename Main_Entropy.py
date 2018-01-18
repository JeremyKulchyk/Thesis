from __future__ import division
import numpy as np
import Entropy_class
import math
import csv


alphabet = 'abcdefghijklmnopqrstuvwxyz'
ec = Entropy_class.Entropy(r'/Users/JeremyKulchyk/PycharmProjects/ThesisProject/SourceText_PeterPan.txt')

def Normalize(dictstruct):
    t6t6normalizers = {}
    for letterset in dictstruct.keys():
        norm = 0
        for subletter in dictstruct[letterset]:
            if letterset in t6t6normalizers.keys():
                t6t6normalizers[letterset] = t6t6normalizers[letterset] + list(subletter.values())[0]
            else:
                t6t6normalizers[letterset] = list(subletter.values())[0]

    t6t6normalized = {}
    x = 0
    for letterset in dictstruct.keys():
        t6t6normalized[letterset] = {}
        for subletter in dictstruct[letterset]:
            t6t6normalized[letterset][(list(subletter.keys())[0])] = list(subletter.values())[0] / t6t6normalizers[letterset]
    return t6t6normalized



#######################  Max Entropy Start  ##################################
print(math.log(26,2))
#######################  Max Entropy End   ##################################

#######################  Entropy i.i.d. Start ##################################
single_dist = ec.single_letter()
entropysingle = 0
for item in single_dist:
    entropysingle = entropysingle - single_dist[item]*math.log(single_dist[item], 2)
print("Entropy n = 1: " + str(entropysingle))
print(len(single_dist))
#######################  Entropy i.i.d. End  ##################################


#######################  Entropy: n = 2 Start ##################################
double_dist = ec.double()
occurencesDOUBLE = 0
for value in double_dist.values():
    occurencesDOUBLE = occurencesDOUBLE + value
t6t6 = {}
for key in double_dist.keys():
    try:
        if key[0] in t6t6.keys():
            t6t6[key[0]].append({key[1] : ((double_dist[key])/occurencesDOUBLE) / single_dist[key[0]] })
        else:
            t6t6[key[0]] = [{key[1] : ((double_dist[key])/occurencesDOUBLE) / single_dist[key[0]] }]
    except:
        continue

t6t6_norm = Normalize(t6t6)
listofentropies = []
entropymeasure2 = 0
for letterset in t6t6_norm.keys():
    for subletter in t6t6_norm[letterset]:
        if subletter >  0:
            entropymeasure2 = entropymeasure2 - (single_dist[letterset] * t6t6_norm[letterset][subletter] * math.log((t6t6_norm[letterset][subletter]), 2))
            listofentropies.append(entropymeasure2)
#print("Entropy n = 2: " + str(entropymeasure2))
print(t6t6_norm)
#######################  Entropy: n = 2 End  ##################################


#######################  Entropy: n = 3 Start  ##################################
triple_dist = ec.triple()

occurencesTRI = 0
for value in triple_dist.values():
    occurencesTRI = occurencesTRI + value

tt = {}
for key in triple_dist.keys():
    try:
        firsttwo  = key[0] + key[1]
        secondtwo = key[2]
        if firsttwo in tt.keys():
            tt[firsttwo].append({secondtwo : (triple_dist[key]/occurencesTRI) / (double_dist[firsttwo]/occurencesDOUBLE) })
        else:
            tt[firsttwo] = [{secondtwo  : (triple_dist[key]/occurencesTRI) / (double_dist[firsttwo]/occurencesDOUBLE) }]

    except:
        continue

tt = Normalize(tt)
listofentropies = []
entropymeasure3 = 0
for letterset in tt.keys():
    for subletter in tt[letterset]:
        if (tt[letterset][subletter])>  0:
            entropymeasure3 = entropymeasure3 - (double_dist[letterset]/occurencesDOUBLE) * (tt[letterset][subletter]) * math.log((tt[letterset][subletter]), 2)
            listofentropies.append(entropymeasure3)

#print("Entropy n = 3: " + str(entropymeasure3))
#######################  Entropy: n = 3 End ##################################

#######################  Entropy: n = 4 Start ##################################
quad_dist = ec.quad()

occurencesQUAD = 0
for value in quad_dist.values():
    occurencesQUAD = occurencesQUAD + value

tt3 = {}

for key in quad_dist.keys():
    try:
        firstthree  = key[0] + key[1] + key[2]
        secondtwo = key[3]
        if firstthree in tt3.keys():
            tt3[firstthree].append({secondtwo : (quad_dist[key]/occurencesQUAD) / (triple_dist[firstthree]/occurencesTRI) })
        else:
            tt3[firstthree] = [{secondtwo  : (quad_dist[key]/occurencesQUAD) / (triple_dist[firstthree]/occurencesTRI) }]

    except:
        continue

tt3 = Normalize(tt3)
listofentropies = []
entropymeasure4 = 0
for letterset in tt3.keys():
    for subletter in tt3[letterset]:
        if (tt3[letterset][subletter]) >  0:
            entropymeasure4 = entropymeasure4 - (triple_dist[letterset]/occurencesTRI) * (tt3[letterset][subletter]) * math.log((tt3[letterset][subletter]), 2)
            listofentropies.append(entropymeasure4)
#print("Entropy n = 4: " + str(entropymeasure4))
#print(len(tt3))
#######################  Entropy: n = 4 Start ##################################




#######################  Entropy: n = 5 Start ##################################
quin_dist = ec.quin()

occurencesQUIN = 0
for value in quin_dist.values():
    occurencesQUIN = occurencesQUIN + value

tt3 = {}

for key in quin_dist.keys():
    try:
        firstfour  = key[0] + key[1] + key[2] + key[3]
        secondtwo = key[4]
        if firstfour in tt3.keys():
            tt3[firstfour].append({secondtwo : (quin_dist[key]/occurencesQUIN) / (quad_dist[firstfour]/occurencesQUAD) })
        else:
            tt3[firstfour] = [{secondtwo  : (quin_dist[key]/occurencesQUIN) / (quad_dist[firstfour]/occurencesQUAD) }]

    except:
        continue

tt3 = Normalize(tt3)
listofentropies = []
entropymeasure5 = 0
for letterset in tt3.keys():
    for subletter in tt3[letterset]:
        if (tt3[letterset][subletter]) >  0:
            entropymeasure5 = entropymeasure5 - (quad_dist[letterset]/occurencesQUAD) * (tt3[letterset][subletter]) * math.log((tt3[letterset][subletter]), 2)
            listofentropies.append(entropymeasure5)
#print("Entropy n = 5: " + str(entropymeasure5))
#print(len(tt3))
#######################  Entropy: n = 5 Start ##################################

#######################  Entropy: n = 6 Start ##################################
hex_dist = ec.hex()

occurencesHEX = 0
for value in hex_dist.values():
    occurencesHEX = occurencesHEX + value

tt3 = {}

for key in hex_dist.keys():
    try:
        firstfour  = key[0] + key[1] + key[2] + key[3] + key[4]
        secondtwo = key[5]
        if firstfour in tt3.keys():
            tt3[firstfour].append({secondtwo : (hex_dist[key]/occurencesHEX) / (quin_dist[firstfour]/occurencesQUIN) })
        else:
            tt3[firstfour] = [{secondtwo  : (hex_dist[key]/occurencesHEX) / (quin_dist[firstfour]/occurencesQUIN) }]

    except:
        continue

tt3 = Normalize(tt3)
listofentropies = []
entropymeasure6 = 0
for letterset in tt3.keys():
    for subletter in tt3[letterset]:
        if (tt3[letterset][subletter]) >  0:
            entropymeasure6 = entropymeasure6 - (quin_dist[letterset]/occurencesQUIN) * (tt3[letterset][subletter]) * math.log((tt3[letterset][subletter]), 2)
            listofentropies.append(entropymeasure6)
#print("Entropy n = 6: " + str(entropymeasure6))
#print(len(tt3))
#######################  Entropy: n = 6 Start ##################################

#######################  Entropy: n = 7 Start ##################################
sept_dist = ec.sept()

occurencesSEPT = 0
for value in sept_dist.values():
    occurencesSEPT = occurencesSEPT + value

tt3 = {}

for key in sept_dist.keys():
    try:
        firstfour  = key[0] + key[1] + key[2] + key[3] + key[4] + key[5]
        secondtwo = key[6]
        if firstfour in tt3.keys():
            tt3[firstfour].append({secondtwo : (sept_dist[key]/occurencesSEPT) / (hex_dist[firstfour]/occurencesHEX) })
        else:
            tt3[firstfour] = [{secondtwo  : (sept_dist[key]/occurencesSEPT) / (hex_dist[firstfour]/occurencesHEX) }]

    except:
        continue

tt3 = Normalize(tt3)
listofentropies = []
entropymeasure7 = 0
for letterset in tt3.keys():
    for subletter in tt3[letterset]:
        if (tt3[letterset][subletter]) >  0:
            entropymeasure7 = entropymeasure7 - (hex_dist[letterset]/occurencesHEX) * (tt3[letterset][subletter]) * math.log((tt3[letterset][subletter]), 2)
            listofentropies.append(entropymeasure7)
#print("Entropy n = 7: " + str(entropymeasure7))
#print(len(tt3))
#######################  Entropy: n = 7 Start ##################################

#######################  Entropy: n = 8 Start ##################################
eight_dist = ec.eight()

occurencesEIGHT = 0
for value in eight_dist.values():
    occurencesEIGHT = occurencesEIGHT + value

tt3 = {}

for key in eight_dist.keys():
    try:
        firstfour  = key[0] + key[1] + key[2] + key[3] + key[4] + key[5] + key[6]
        secondtwo = key[7]
        if firstfour in tt3.keys():
            tt3[firstfour].append({secondtwo : (eight_dist[key]/occurencesEIGHT) / (sept_dist[firstfour]/occurencesSEPT) })
        else:
            tt3[firstfour] = [{secondtwo  : (eight_dist[key]/occurencesEIGHT) / (sept_dist[firstfour]/occurencesSEPT) }]

    except:
        continue

tt3 = Normalize(tt3)
listofentropies = []
entropymeasure8 = 0
for letterset in tt3.keys():
    for subletter in tt3[letterset]:
        if (tt3[letterset][subletter]) >  0:
            entropymeasure8 = entropymeasure8 - (sept_dist[letterset]/occurencesSEPT) * (tt3[letterset][subletter]) * math.log((tt3[letterset][subletter]), 2)
            listofentropies.append(entropymeasure8)
#print("Entropy n = 8: " + str(entropymeasure8))
#print(len(tt3))
#######################  Entropy: n = 8 Start ##################################

#######################  Entropy: n = 9 Start ##################################
nine_dist = ec.nine()

occurencesNINE = 0
for value in nine_dist.values():
    occurencesNINE = occurencesNINE + value

tt3 = {}

for key in nine_dist.keys():
    try:
        firstfour  = key[0] + key[1] + key[2] + key[3] + key[4] + key[5] + key[6] + key[7]
        secondtwo = key[8]
        if firstfour in tt3.keys():
            tt3[firstfour].append({secondtwo : (nine_dist[key]/occurencesNINE) / (eight_dist[firstfour]/occurencesEIGHT) })
        else:
            tt3[firstfour] = [{secondtwo  : (nine_dist[key]/occurencesNINE) / (eight_dist[firstfour]/occurencesEIGHT) }]

    except:
        continue

tt3 = Normalize(tt3)
listofentropies = []
entropymeasure9 = 0
for letterset in tt3.keys():
    for subletter in tt3[letterset]:
        if (tt3[letterset][subletter]) >  0:
            entropymeasure9 = entropymeasure9 - (eight_dist[letterset]/occurencesEIGHT) * (tt3[letterset][subletter]) * math.log((tt3[letterset][subletter]), 2)
            listofentropies.append(entropymeasure9)
#print("Entropy n = 9: " + str(entropymeasure9))
#print(tt3)
#######################  Entropy: n = 9 Start ##################################


listofentropies = [4.7, entropysingle, entropymeasure2, entropymeasure3, entropymeasure4, entropymeasure5, entropymeasure6, entropymeasure7, entropymeasure8, entropymeasure9]
xvalues = [0,1,2,3,4,5,6,7,8,9]
#print (len(listofentropies))
import matplotlib.pyplot as plt
plt.plot(xvalues, listofentropies)
plt.title("Entropy & Conditioning")
#plt.show()

