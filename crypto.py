#Ciera Headley
#CS:1210:0A01
#crypto.py
#Homework 10

import os 

#create a function that coverts the letter to an index
def LetterToIndex(ch):
    #create a varibale for the alphabet
    alpha = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[]{}\\|;:\'",./<>?\n\t '''
    #find the letter in the index
    index = alpha.find(ch)
    #if characater is not in index ch  is an underscore
    if ch not in alpha:
        ch  = '_'
    #return index
    return index
def encrypt():
    #intialize empty string an empty string and empty lists
    word = ""
    myList = []
    aList = []
    finalL = []
    
    #prompt user for keys
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    d = int(input('Enter d: '))        
    #set a varibale for key formula
    key = a*d-c*b 
    #if the key formula equals 1 or -1 the key is vaild and the program can continue else the key is invaild and the progam ends
    if key == 1 or key== -1:
        #prompt the user for the name of the file they would like to encrypt
        fileName = input('Enter the name of file to encrypt: ')
        #if the file exists countinue esle the file doesn'e exist and program stops
        if os.path.isfile(fileName):
            #read the file
            file = open(fileName, 'r')
            #get the lines in the file add lines to an empty string
            for lines in file:
                word = word + lines
                #if the len of the word is odd add a space
                if len(word)%2 ==1:
                    word = word + " " 
            #for the characters in the string change them to an index number
            for i in word:
                index = LetterToIndex(i)
                
                #append the index number to a new list called myList
                myList.append(index)
                
                #create a variable for a list comprehension that will seperate the list into groups of two
                w = [myList[i:i+2]for i in range(0, len(myList), 2)]            
        else:
            return "file " + str(fileName)+ " doesn't exist"
        
        #for the index in w x = the first index on the list and y is the second.
    
        for i in range(len(w)):
            x = w[i][0]
            
            y = w[i][1] 
            #encode is the formula encode the index
            encode = [x*a+y*c , x*b+y*d]
            #append the encoded numbers to a new list aList
            aList.append(encode)
        #for the aList index add the index to a new list finalL to combine the numbers
        for L in aList:
            finalL = finalL +L
        #prompt the use for the name of the saved file to overwrites 
        savedFile = input('Enter a name for the encrypted file: ')
        #if file exists continue else the file doesn't exist
        if os.path.isfile(savedFile):
            overWrite = input('File ' + str(savedFile) +' already exists. Are you sure you want to overwrite it? n or y: ')
            #if the user says yes then write the encryption into the saved file
            if overWrite == 'y':
                print( 'File ' +str(fileName) +' is encrypted and saved to ' + str(savedFile))
                file = open(savedFile,'w')
                file.write(str(finalL))
                file.close()
            else:
                return None
                
        else:
            return 'Invaild. Need an existing file.'
    else:
        return 'Invaild Key'
        
def IndexToLetter(ndx):
    alpha = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[]{}\\|;:\'",./<>?\n\t '''
    if 0 <= ndx < len(alpha):
        #index is valid
        ch = alpha[ndx]
        return ch
    else:
        #index is not valid
        errorMessage = 'Error: {} is not a valid index'
        return errorMessage.format(ndx)   
def decrypt():
    #initiate new lists to hold numbers and and empty string to hold the characters
    newWord = ""
    newL = []
    fileList = []
    finalL = []
    
    #prompt the user for the keys
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    d = int(input('Enter d: '))  
    
    
    #set a variable to key formula
    key = a*d-c*b    
    # if the key is equal to 1 or -1 continue esle key is invaild
    if key == 1 or key ==-1:
        #prompt user for file to decrypt
        fileName = input('Enter the name of the file to decrypt: ')
        #if the file exists continue else return file doesnt exist
        if os.path.isfile(fileName):
            #prompt user for file to place the decryted file
            newFile = input('Enter a name for the decrypted file: ')
            #if file exists continue else return file does not exist
            if os.path.isfile(newFile):
                #prompt user to overwrite file 
                question = input('File ' +str(newFile)+ ' already exists. Are you sure you want to overwrite it?:')
                #if y continue else return none an stop program
                if question == 'y':
                    #open and read file to decrypt
                    file = open(fileName,'rU')
                    #read file lines
                    lineList = file.readline()
                    #create a new list with the numbers of the file and taking away the brakes
                    newList = lineList[1:len(lineList)-1].split(',')
                    #create a new list LL that will change the numbers that are strings to intergers
                    LL= [int(i) for i in newList]
                    #create new keys to convert the decoded numbers to alphabet index numbers
                    newA = key*(d)
                    newB = key*(-b)
                    newC = key*(-c)
                    newD = key*(a)
                    #divide the numbers in LL list into to groups
                    divide =[LL[i:i+2]for i in range(0, len(LL), 2)]
                    
                    #loop through each index
                    for i in range(len(divide)):
                        #in each index get the first number and the second number of the list
                        x = divide[i][0]
                   
                        y = divide[i][1]
                        
                        #decode by using the new key to convert the numbers back the orginal numbers
                   
                        decode = [x*newA+y*newC , x*newB+y*newD]
                        #append the index to a new list newL
                        newL.append(decode)
                    #for in newList concatenate the index to a new list
                    for L in newL:
                        finalL = finalL + L
                    #for each number in the newList convert the numbers to letters in the Alphabet
                    for i in finalL:
                        word = IndexToLetter(i)
                        #add the letters to a string
                        newWord = newWord + word
                    #open and right to the new file
                    f = open(newFile,'w')
                    #write the string to the file
                    f.write(newWord)
                    #close the file
                    f.close()
                    #return the file is saved.
                    return 'File '+str(fileName) + ' decrypted and saved to ' + str(newFile)
                else:
                    return None
            else:
                return "File doesn't exist"
        else:
            return "File doesn't exist"
    else: 
        return 'Invaild Key'
#I created a main fucntion to run through the encryption and decryption
def main():
    #create a variable to prompt the user if the want to ecrypt or decrypt and convert string  to interger
    select=int(input('''
What would you like to do:
    1) Encrypt a file
    2) Decrypt a file
    
Selection: '''))
    #if 1 in is selected encrypt if 2 is selected decrypt else return a statement that the selection is invaild
    if select == 1:
        return encrypt()
    elif select == 2:
        return decrypt()
    else:
        return 'Invaild Selection'