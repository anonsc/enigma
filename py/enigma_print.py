from pickle import TRUE
import sys
import re
from weakref import ref
import configparser
import random

inifile = configparser.ConfigParser()
inifile.read('config.ini','UTF-8')

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ScramblerSetting_list = inifile['General']['ScramblerSetting_list']
Scrambler_list = inifile['General']['Scrambler_list']
_ref = inifile['General']['Reflector']

scr_lis = Scrambler_list.split(':')
scr_set_lis = ScramblerSetting_list.split(':')


def ref_edit():
    global _ref
    print('insert a reflector')
    _ref = input()

    if _ref == 'random':
        _ref = ''.join(random.sample(alphabet,len(alphabet)))#ランダムなa~z文字列を生成

    if not set(_ref) == set(alphabet):
            print('error\n"random"is available')

    inifile['General']['Reflector'] = _ref

    with open ('config.ini','w') as configfile:
        inifile.write(configfile)
    
    return  print(_ref)


def scr_edit():

    i = 1
    
    global scr_lis
    
    while True:
        
        print('insert scrambler',i)
        _scr = input()
        
        if _scr == 'set':

            break

        if _scr == 'random':
            _scr = ''.join(random.sample(alphabet,len(alphabet)))
            
        if not set(_scr) == set(alphabet):
            print('error\n"random"is available')
            continue
        scr_lis.append(_scr)
        i += 1

    Scrambler_list = ':'.join(scr_lis)
    inifile['General']['Scrambler_list'] = Scrambler_list

    with open ('config.ini','w') as configfile:
        inifile.write(configfile)
    
    return print(scr_lis)

def scr_set():

    global scr_set_lis 
    
    i = 0 
    
    while i < len(scr_lis):
        
        print('enter the setting number',i+1)
        _setting = input()
        
        if not _setting.isdecimal():
            print('error')
            continue
        
        scr_set_lis.append(_setting)
        i += 1

    Setting_list = ':'.join(scr_set_lis)
    inifile['General']['setting_list'] = Setting_list

    with open ('config.ini','w') as configfile:
        inifile.write(configfile)
    
    return print(scr_set_lis)

def scrambler (place,process,_count,_scr):
    
    if process == 1:
        a = alphabet
        b = _scr
    
    else:
        a = _scr
        b = alphabet
    
    place = (b.find(a[(place + _count) % 26]) - _count) % 26
    
    return place

def reflector (place):
    
    place = alphabet.find(_ref[25 - _ref.find(alphabet[place])])#A~Zの2文字を1組として入れ替え。ex.文字列_refの前からx番目と、後ろからx番目が組となって入れ替わる
    
    return place


def enigma ():
    cipher = ''
    set_lis = [int(s) for s in set_lis_a]
    original_text = input('文を入力\n')
    
    text = re.sub(r'[^a-zA-Z]','',original_text).upper()#英字のみ抽出,大文字に変換
    
    for count in range(len(text)):
        
        char = text[count]
        
        place = alphabet.find(char)
        
        for a in range(len(scr_lis)):
            
            _count = ((count//26**a) + set_lis[a]) % 26
            
            place = scrambler(place,1,_count,scr_lis[a])
        
        place = reflector(place)
        
        for a in reversed(range(len(scr_lis))):
            
            _count = ((count//26**a) + set_lis[a]) % 26
            
            place = scrambler(place,0,_count,scr_lis[a])
        
        char = alphabet[place]
        
        cipher += char
    
    print (cipher)

def help():
    print('ref_edit\nscr_edit\nscr_set\nenigma\nquit')

def setting():
    print('Reflector:',_ref,'\nScranbler:',scr_lis,'\nscr_set:',scr_set_lis)
#main
print('hello')

while True:
    try:
        _input = input()
        eval(_input)()
        
    except (TypeError,ValueError,SyntaxError):
        print('Error\nEnter "help" to display valid input values')