#Ciera Headley
#isPalindrome.py
#CS:1210
#Homework 9

def isPalindrome():
    
    #Create an alphabet string
    alpha = 'abcdefjhijklmnopqrstuvwxyz'
    
    #create an empty string
    new = ""
    #Ask the User of input
    s = input('Enter some characters:')
    #strip the s of spaces and make them all lower
    lowerCase = s.strip('').lower()
    #Check if the letters in the string are only letters if they are add it to the new string
    for letters in lowerCase:
        if letters in alpha:
            new = new + letters
    #create a variable that reverses the new string
    check = new[::-1]
    #the new string and reverse string are the same return true else return false
    if new == check:
        return True
    else:
        return False