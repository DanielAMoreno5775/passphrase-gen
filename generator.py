#This program will generate very memorable but random passwords
#by Daniel Moreno

import sys #used for exit()
import random

#read the file and return the list of words within the file
def getWordsFromLibrary():
    #try to open the file and throw exception if it fails
    try:
        libFile = open("lib.txt", "r")
    except:
        sys.exit("An error occurred while opening the file")

    #create the array to store everything with one extra spot for numOfWords
    #can handle up to 100 words as that is a reasonable number as defined by the instructions
    listOfWords = [""] * 101

    #start reading the file and importing words into the array
    numOfWords = 0
    linesList = libFile.readlines()
    for line in linesList:
        if ((line != "") and (line != "\n") and (numOfWords < 101)):
            tempWord = ""
            for char in line:
                if (char != "\n"):
                    tempWord += char
            listOfWords[numOfWords] = tempWord
            numOfWords += 1

    #store the number of words in the last spot of the list
    listOfWords[100] = str(numOfWords)

    #return the list and close the file
    libFile.close()
    return listOfWords

#pass the list of words to this function from which it will generate a pass phrase of the specified length
def generatePassPhrase(listOfWords, desiredLength):
    #initialize variables and handle the type of desiredLength
    i = 0
    finalPassPhrase = ""
    desiredLength = int(desiredLength)
    #retrieve the number of words
    numOfWords = int(listOfWords[100])

    #check to see whether the desired number of words is greater than the number of words in the list
    if (desiredLength > numOfWords):
        #until you get the requested number of words, keep iterating
        while (i < desiredLength):
            #generate random index from the list
            index = random.randint(0,(numOfWords - 1))
            finalPassPhrase += listOfWords[index]
            i += 1
    else:
        #initialize variables that are only necessary for this condition
        usedIndexes = []

        #until you get the requested number of words, keep iterating
        while (i < desiredLength):
            #reset the variable after each loop since the new index hasn't even been generated yet
            indexUsed = False

            #generate random index from the list
            index = random.randint(0,(numOfWords - 1))

            #check to make sure that index has not been used before
            #if it has, restart the loop and generate a new index
            for entry in usedIndexes:
                if ((entry == index) and (not indexUsed)):
                    indexUsed = True

            #if the index has not been used, add the index to the list of used ones and append the latest word
            if (not indexUsed):
                usedIndexes.append(index)
                finalPassPhrase += listOfWords[index]
                i += 1
            

    #print final result
    print("The result phrase: " + finalPassPhrase)


#read the file
listOfWords = getWordsFromLibrary()

#ask user how many words they want
userInput = float(input("Please enter the number of words in the phrase: "))
#keep asking for input until a number greater than or equal to 1 is provided
while (userInput < 1):
    print("That is an invalid quantity. The number of words should be greater than or equal to 1")
    userInput = float(input("Please enter the number of words in the phrase: "))

#generate the pass phrase and print it
generatePassPhrase(listOfWords,userInput)