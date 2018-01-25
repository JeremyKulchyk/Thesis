# Convert a character into a codeword, and vice-versa.

# 'alphabet' is the list of possible characters -- order matters.
# 'code_len' is the length of all codewords, = roundup(log(len(alphabet))/log(2))
# 'char' is the character to convert into a codeword
# 'codeword' is the bit-list to convert into a character
# 'shift' allows access to other codewords when 'char' maps to more than one 'codeword'


class CodeBook:

    # Converts a character's index from an alphabet list into a binary list
    def define(self, char, code_len=5, alphabet='abcdefghijklmnopqrstuvwxyz ', shift=0):
        # First, find char in alphabet, and return the index
        index = str.find(alphabet, char)
        # For aliasing, access other codewords through shift
        while shift > 0:
            shift -= 1
            index = str.find(alphabet, char, index+1)

        # Second, convert index into a binary list
        codeword = []
        for i in range(1, code_len + 1):
            codeword.append((index >> (code_len - i)) & 1)

        return codeword

    # Converts a binary list into an index, retrieves char from alphabet
    def retrieve(self, codeword, code_len=5, alphabet='abcdefghijklmnopqrstuvwxyz '):
        # First, convert the bit list into an index
        index = 0
        i = code_len - 1
        for bit in codeword:
            index += bit << i
            i -= 1

        # retrieve the related character from the alphabet
        char = alphabet[index]

        return char

