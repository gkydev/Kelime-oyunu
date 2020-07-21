# -*- coding: utf-8 -*-
import random, string
from datetime import datetime
global letters,duplicate,db
duplicate = []
#Wordlists
three_letter = []
four_letter = []
five_letter = []
six_letter = []
seven_letter = []
eight_letter = []
nine_letter = []
#Kelimeleri listelere yerleştir
with open("ckelimeler.txt","r") as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip("\n")
        if len(line) == 3:
            three_letter.append(line)
        elif len(line) == 4:
            four_letter.append(line)
        elif len(line) == 5:
            five_letter.append(line)
        elif len(line) == 6:
            six_letter.append(line)
        elif len(line) == 7:
            seven_letter.append(line)
        elif len(line) == 8:
            eight_letter.append(line)
        elif len(line) == 9:
            nine_letter.append(line)
        else:
            pass
db = {
    3: three_letter,
    4: four_letter,
    5: five_letter,
    6: six_letter,
    7: seven_letter,
    8: eight_letter,
    9: nine_letter
}
#Functions 
def check_letter_in_word(letter,word):
    if letter in word:
        return True
    else:
        return False
def find_joker(word,letters):
    for letter in word:
        if letter not in letters:
            return letter
        else:
            pass
    return None
def check_word_duplicate(word):
    word_duplicate = []
    check = 0
    for check_letter in word:
        for letter in word:
            if check_letter == letter:
                check += 1
            else:
                pass
        if check >= 2:
            data = (check_letter,check)
            if data not in word_duplicate:
                word_duplicate.append(data)
        else:
            pass
        check = 0
    return word_duplicate
def compare_duplication(word):
    word_duplicate = check_word_duplicate(word)
    if len(duplicate) > 1 or len(word_duplicate) > 1:
        for w_d in word_duplicate:
            for dup in duplicate:
                if w_d in dup or w_d == dup:
                    return True
        return False
    else:
        if word_duplicate in duplicate or word_duplicate == duplicate:
            return True
        else:
            return False
###
#Main Functions
def random_letters():
    hits = []
    alphabet = string.ascii_lowercase
    letters = []
    for x in range(0,8):
        letter = random.choice(alphabet)
        while letter == "w" or letter == "q" or letter == "x":
            letter = random.choice(alphabet)
        letters.append(letter)
    duplicate = []
    check = 0
    for x in letters:
        for y in letters:
            if y == x:
                check +=1
        if check >=2:
            data = (x,check)
            if data not in duplicate:
                duplicate.append(data)
        else:
            pass
        check = 0
    result = 0
    for num in range(3,10):
        for word in db[num]:
            for letter in letters:
                if check_letter_in_word(letter,word):
                    result += 1
                else:
                    pass
            if result-len(duplicate) >= (num-1):
                joker = find_joker(word,letters)
                if check_word_duplicate(word) != []:
                    if joker == None and compare_duplication(word):
                        word = (word.upper(),"Yok".upper())
                        hits.append(word)
                    elif joker == None and not compare_duplication(word):
                        joker = check_word_duplicate(word)[0]
                        word = (word.upper(),joker[0].upper())
                        hits.append(word)
                else:
                    word = word.upper()
                    joker = str(joker).upper()
                    if joker == "NONE":
                        joker = "YOK"
                    word = (word,joker)
                    hits.append(word)
                result = 0
            else:
                result = 0
    return_data = {"letters": letters, "hits": hits}
    return return_data
def chosen_letters(letters):
    hits = []
    duplicate = []
    check = 0
    for x in letters:
        for y in letters:
            if y == x:
                check +=1
        if check >=2:
            data = (x,check)
            if data not in duplicate:
                duplicate.append(data)
        else:
            pass
        check = 0
    result = 0
    for num in range(3,10):
        for word in db[num]:
            for letter in letters:
                if check_letter_in_word(letter,word):
                    result += 1
                else:
                    pass
            if result-len(duplicate) >= (num-1):
                joker = find_joker(word,letters)
                if check_word_duplicate(word) != []:
                    if joker == None and compare_duplication(word):
                        word = word.upper()
                        word = (word,"YOK")
                        hits.append(word)
                    elif joker == None and not compare_duplication(word):
                        joker = check_word_duplicate(word)[0]
                        joker = joker[0].upper()
                        word = word.upper()
                        word = (word,joker)
                        hits.append(word)
                else:
                    word = word.upper()
                    joker = str(joker).upper()
                    if joker == "NONE":
                        joker = "YOK"
                    word = (word,joker)
                    hits.append(word)
                result = 0
            else:
                result = 0
    return_data = {"letters": letters, "hits": hits}
    return return_data