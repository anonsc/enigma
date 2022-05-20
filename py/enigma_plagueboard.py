import sys


#plague_board
def plagueboard (char):
    a = char.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher_alphabet = 'ZQPLAXSOWMKCDENJIVFRBUHYGT'

    ciph = cipher_alphabet[alphabet.find(a)]
    return ciph