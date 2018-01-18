import DecodeText

class MarkovChain:
    #Init text file
    def __init__(self, file_name):
        file = open(file_name, 'r')
        unsorted_text = file.read()
        self.text = unsorted_text.lower()
        file.close()

    def MarkovBuild_1(self):
        WordStore = []
        Dict = {}
        tuple = ''
        for i in range(0, len(self.text), 1):
            character = self.text[i]
            if character is not ' ':
                tuple = tuple + (character)
            else:
                try:
                    tuple = DecodeText.unicodetoascii(tuple)
                except:
                    x = 0
                WordStore.append(tuple)
                tuple = ''

        #print WordStore
        flag = 0
        for word1 in WordStore:
            for word2 in WordStore:
                if flag is 1:
                    if word1 in Dict.keys():
                        Dict[word1].append(word2)
                    else:
                        Dict[word1] = []
                        Dict[word1].append(word2)
                    flag = 0

                if word2 is word1:
                    flag = 1

        #print(Dict)
        return(Dict)

    def MarkovBuild_2(self):
        WordStore = []
        WordStore2 = []
        Dict = {}
        tuple = ''
        for i in range(0, len(self.text), 1):
            character = self.text[i]
            if character is not ' ':
                tuple = tuple + (character)
            else:
                try:
                    tuple = DecodeText.unicodetoascii(tuple)
                except:
                    x = 0
                WordStore.append(tuple)
                tuple = ''

        flag = 0
        for word1 in WordStore:
            for word2 in WordStore:
                if flag is 1:
                    #DictKeyTuples = [word1,word2]
                    twowords = word1 + ' ' + word2
                    #print twowords
                    if twowords in Dict.keys():
                        x = 0
                    else:
                        Dict[twowords] = []
                        WordStore2.append(twowords)
                    flag = 0

                if word2 is word1:
                    flag = 1

        #rint(WordStore)

        flag = 0
        for word1 in WordStore2:
            strlist = word1.split()
            for word2 in WordStore:
                if flag is 2:
                    Dict[word1].append(word2)
                    flag = 0
                    continue
                if word2 in strlist:
                    flag = flag + 1
                else:
                    flag = 0

        #print(Dict)
        return(Dict)









