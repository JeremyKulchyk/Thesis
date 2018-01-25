from math import *
#Use the class methods

# Define tree object
class tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)


# Build Huffman Tree
def HuffTree(x = [3/8,1/4,1/8,1/8,1/16,1/16], print_on=0):
    x.sort()
    # Convert list of numbers into list of tree nodes
    for i in range(0,len(x)):
        node = tree()
        node.data = x[i]
        x[i] = node

    if print_on: print(x)
    for i1 in range(2,len(x)):
        # Find least two probabilities
        min0 = (1,x[1])
        min1 = (0,x[0])
        for i2 in range(2,min(len(x),i1)):
            if x[i2].data<min0[1].data:
                min1 = min0
                min0 = (i2, x[i2])
            elif x[i2].data<min1[1].data:
                min1 = (i2, x[i2])

        # Remove least two probabilities from list and append to a new node
        if min0[0]>min1[0]:
            x.pop(min0[0])
            x.pop(min1[0])
        else:
            x.pop(min1[0])
            x.pop(min0[0])
        node = tree()
        node.left = min1[1]
        node.right = min0[1]

        # New node has probability equal to the sum of the removed probabilities
        node.data = min0[1].data + min1[1].data

        # Append node to end of list
        x.insert(0,node)
        if print_on: print(x)

    # Attach the two remaining sub-trees to a root node
    root = tree()
    root.left = x[0]
    root.right = x[1]
    root.data = x[0].data + x[1].data
    if print_on: print(root)
    return root


# Generate Huffman Codebook
def getHuffCode(node=tree()):
    # If leaf, return empty list
    leftbook = []
    rightbook = []
    if node.left:
        # Prepend '0' to left-child code words
        leftbook = getHuffCode(node.left)
        if leftbook:
            for i in range(0,len(leftbook)):
                leftbook[i] = [0]+leftbook[i]
        else:
            leftbook = [[0]]
    if node.right:
        # Prepend '1' to right-child code words
        rightbook = getHuffCode(node.right)
        if rightbook:
            for i in range(0,len(rightbook)):
                rightbook[i] = [1]+rightbook[i]
        else:
            rightbook = [[1]]
    # Return codebook for sub-tree (empty list if a leaf)
    codebook = leftbook+rightbook
    return codebook


# Generate letter-to-Huffman codeword dictionary (first order)__________________________________________________________
class Huffman:

    def makeHuffDict(self, codeBook={'a':1/27,'b':1/27,'c':1/27,'d':1/27,'e':1/27,'f':1/27,'g':1/27,'h':1/27,'i':1/27,
                                     'j':1/27,'k':1/27,'l':1/27,'m':1/27,'n':1/27,'o':1/27,'p':1/27,'q':1/27,'r':1/27,
                                     's':1/27,'t':1/27,'u':1/27,'v':1/27,'w':1/27,'x':1/27,'y':1/27,'z':1/27,' ':1/27}):
        # Get list of probabilities and generate Huffman code
        root = HuffTree(list(codeBook.values()))
        bookcde = getHuffCode(root)
        bookcde.sort(key=len)

        # Get list of letters
        def getVal(char, dictt=codeBook): return dictt[char]
        booksym = sorted(codeBook.keys(),key=getVal,reverse=True)

        # Append letters to codewords
        return dict(zip(booksym,bookcde))

    def HuffRate(self, codeBook, HuffBook):
        # Check input
        if len(codeBook)!=len(HuffBook):
            print('Bad input for HuffRate')
            return 0

        # Get order
        order = len(list(codeBook.keys())[0])

        #Calculate average code length
        avgCodeLen = 0
        for letter in codeBook.keys():
            avgCodeLen += codeBook[letter]*len(HuffBook[letter])

        # Return code rate
        return avgCodeLen/order

    def Entropy(self, codeBook):
        # Calculate entropy of the source distribution
        entropy = 0
        for p in codeBook.values():
            entropy += p*log(p)
        return -entropy/log(2)


# Testing code (can be removed)
codeBook = {'e':1/2,'a':1/8,'b':1/8,'c':1/8,'d':1/16,'f':1/16}
temp = Huffman.makeHuffDict(Huffman,codeBook)
print(Huffman.HuffRate(Huffman,codeBook,temp))
print(Huffman.Entropy(Huffman,codeBook))
print(temp.keys())

#To make order 2 Huffman code, input the 2-tuple dictionary



