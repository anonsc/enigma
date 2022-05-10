import sys

#plague_board
def plagueboard (char):
    a = char.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher_alphabet = 'ZQPLAXSOWMKCDENJIVFRBUHYGT'

    ciph = cipher_alphabet[alphabet.find(a)]
    return ciph

#input_output
a = input('enter a string\n')

cipher =""

num = 0

while num < len(a):
    
    p = str(a[num])
    
    ciph = plagueboard(p)

    cipher += ciph

    num += 1
    
print (cipher)