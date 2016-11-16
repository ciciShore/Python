#Ciera Headley 
#CS:1210:0A01
#hw-13.py
#Homework 13


def format(N):
    #change the numbe to a string
    string = str(N)
    #get the length of the string
    num = len(string)
   # if the length of the string doesn't need a comma just return the string
    if num <=3:
        return string
    #else have the function loop though itsels adding commas.
    else:
        return format(string[:-3]) + ',' + string[-3:]
    
def maxList(L):
    #if length of list is on then that is the max number in a list
        if len(L) == 1:
        #return the number of the list
                return L[0]
        else:
        #create a variable of the recursion
                maxNum = maxList(L[1:])
        #return the max number if the number is greater that the first number in the list
        return maxNum if maxNum > L[0] else L[0]
    