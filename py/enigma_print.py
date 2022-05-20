from distutils.log import error
from pickle import TRUE
import sys
import re
from weakref import ref

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
settinglist = []
keylist = []


def scr_edit():
    i = 1 
    
    while True:
        
        print('insert scrambler',i)
        key = input()
        
        if key == 'set':
            print(keylist)
            break
        
        if not set(key) == set(alphabet):
            print('error')
            continue
        
        keylist.append(key)
        i += 1
        
    return keylist

def key_setting():
    
    settinglist = []
    i = 0 
    
    while i < len(keylist):
        
        print('enter the setting number',i+1)
        _setting = input()
        
        if not _setting.isdecimal():
            print('error')
            continue
        
        settinglist.append(int(_setting))
        i += 1
        
    print (settinglist)
    return settinglist

def scrambler (place,process,_count,key):
    
    if process == 1:
        a = alphabet
        b = key
    
    else:
        a = key
        b = alphabet
    
    place = (b.find(a[(place + _count) % 26]) - _count) % 26
    
    return place

def reflector (place):
    
    _ref = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    
    place = _ref.find(alphabet[place])
    
    return place



def enigma (keylist,settinglist):
    cipher = ''
    
    original_text = input('文を入力\n')
    
    text = re.sub(r'[^a-zA-Z]','',original_text).upper()#英字のみ抽出,大文字に変換
    
    for count in range(len(text)):
        
        char = text[count]
        
        place = alphabet.find(char)
        
        for a in range(len(keylist)):
            
            _count = ((count//26**a) + settinglist[a]) % 26
            
            place = scrambler(place,1,_count,keylist[a])
        
        place = reflector(place)
        
        for a in reversed(range(len(keylist))):
            
            _count = ((count//26**a) + settinglist[a]) % 26
            
            place = scrambler(place,0,_count,keylist[a])
        
        char = alphabet[place]
        
        cipher += char
    
    print (cipher)


keylist = scr_edit()
settinglist = key_setting()
enigma(keylist,settinglist)