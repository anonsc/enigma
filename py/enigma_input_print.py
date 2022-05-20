import sys
import re
from weakref import ref

#input_output
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


#scrambler1
def scrambler1 (place,process):
    
    _in =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _out = "UWYGADFPVZBECKMTHXSLRINQOJ"
    
    if process == 1:
        a = _in
        b = _out
    
    else:
        a = _out
        b = _in
    
    place = (b.find(a[(place + count1) % 26]) - count1) % 26
    
    
    
    return place


#Scrambler2
def scrambler2 (place,process):
    
    _in =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _out = "AJPCZWRLFBDKOTYUQGENHXMIVS"
    
    if process == 1:
        a = _in 
        b = _out
    
    else:
        a = _out
        b = _in
    
    place = (b.find(a[(place + count2) % 26]) - count2) % 26
    
    return place

#Scrambler3
def scrambler3 (place,process):
    
    _in =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _out = "TAGBPCSDQEUFVNZHYIXJWLRKOM"
    
    
    if process == 1:
        a = _in 
        b = _out
    
    else:
        a = _out
        b = _in
    
    place = (b.find(a[(place + count3) % 26]) - count3) % 26
    
    return place
#reflector
def reflector (place):
    
    _in =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _out = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    
    place = _out.find(_in[place])
    
    return place


#main

cipher = ''



Scrambler_number = 3

original_text = input('文を入力\n')
text = re.sub(r'[^a-zA-Z]','',original_text).upper()#英字のみ抽出,大文字に変換

for count in range(len(text)):
    
    char = text[count]
    count1 = count % 26
    
    count2 = (count//26) % 26
    count3 = (count//26**2) % 26
    
    
    
    place = alphabet.find(char)
    
    place = scrambler1(place,1)
    
    place = scrambler2(place,1)
    
    place = scrambler3(place,1)
    
    place = reflector(place)
    
    place = scrambler3(place,0)
    
    place = scrambler2(place,0)
    
    place = scrambler1(place,0)
    
    char = alphabet[place]
    
    
    cipher += char
    
    


print (cipher)