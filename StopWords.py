#You may need to enable these two commandes if your punkt isn't installed
#once dowloaded and installed nltk will work perfectly fine
#import nltk
#nltk.download('punkt')

'''
    Imports:
        - os to acess files
        - The nltk tokenizer is used to split the text into words
    ---------
    Variables returned:
        - a Python Dictionnary is the only data structure we used to return and use variable 
        because it defines the context variable in django that we will use in out templates
    ---------
    Structure of the file:
        - Containes two functs to spot stopwords with two diffrent ways
'''

from nltk.tokenize import word_tokenize
import os
import json


def fromTxt(Path):
    with open(Path, "r") as Text:
        return Text.read()

#funt to compute stopwords in a text using a prewritten list
def StopWords(Text):
    #opening file
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'Stopwords.txt')
    read_file = open(my_file, "r", encoding="utf-8")

    File = read_file.read()
    Results = {}
    #geting lists of: total input wordslist, stopwords from the file.
    WordsList = word_tokenize(Text)
    StopWords = word_tokenize(File)

    #a variable to store the stowords found
    StopsIn = []


    #looping over each word
    for word in WordsList:
        if word in StopWords:
            #if the word is consider as a stopword, we remove it from the input text
            WordsList.pop(WordsList.index(word))
            if word not in StopsIn:
                #if the word found hasn't being saved yet, we save it in StopsIn list
                StopsIn.append(word)

    #rewriting the text
    newText = ""
    for word in WordsList:
        newText = newText + " " + word

    #returning a dict of the new text and the list of stops
    Result["newText"] = newText
    Results["StopsIn"] = StopsIn

    #Saving into a json file
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER,'Stopwords.json')

    write_file = open(my_file, "w")
    json.dump(Results, write_file, indent=2)
    write_file.close()


#funct to spot stopwords in a text using an appearence number
def nStopWords(Text, n):

    #geting lists of: total input wordslist
    WordsList = word_tokenize(Text)

    #a variable to store the stowords found
    StopsIn = []

    #looping over each word
    for word in WordsList:
        if WordsList.count(word) > n:
            #if the word is consider as a stopword (appeared more than n times), we remove it from the input text
            WordsList.pop(WordsList.index(word))
            if word not in StopsIn:
                #if the word found hasn't being saved yet, we save it in StopsIn list
                StopsIn.append(word)
        else:
            #otherwise we continue to the next item in the lsit
            continue
    
    #rewriting the text
    newText = ""
    for word in WordsList:
        newText = newText + " " + word

    #returning a dict of the new text and the list of stops
    Result["newText"] = newText
    Results["StopsIn"] = StopsIn

    #Saving into a json file
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER,'Stopwords.json')

    write_file = open(my_file, "w")
    json.dump(Results, write_file, indent=2)
    write_file.close()