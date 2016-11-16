#Ciera Headley
#rpslsGame.py
#Course CS:1210:0A01
#HW 8
import random 

#covert numbers to names
def names(num):
    if num == 0:
        return "Rock"
    elif num == 1:
        return "Paper"
    elif num ==2:
        return "Scissors"
    elif num ==3:
        return "Lizard"
    elif num == 4:
        return "Spock"

def rpslsGame():

    #Let the computer randomly select a term
    computer = random.randrange(0,5)
    
    #Ask user to select a term 
    user = input('''Type in one of the following number: 
1) Rock 
2) Paper 
3) Scissors 
4) Lizard 
5) Spock
Entry:''')
    
   #change user to easier numbers to score if number is not there user is undefined
    if user == 1:
        user = 0
    elif user == 2:
        user = 1
    elif user ==3:
        user = 2
    elif user==4:
        user = 3
    elif user ==5:
        user = 4
    else:
        return 'The computer is ' + str(names(computer)) +'. You are Undefined. Invalid game. Outcome is undefined.'
        
    
    #figure out score
    score = (user - computer) % 5
    print (score)
    print(user)
    print(computer)

    #return outcome

    if score == 0: 
        return 'The computer is '+ str(names(computer))+'. You are '+ str(names(user))+ ' Draw. Neither wins.'
    elif score <= 2:
        return 'The computer is ' + str(names(computer))+'. You are '+ str(names(user))+ ' You win.' 
    else:                 
        return 'The computer is ' + str(names(computer))+'. You are '+ str(names(user))+ ' The computer wins.'
        
p
