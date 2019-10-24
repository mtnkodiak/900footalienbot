'''
Created on Sep 30, 2019

@author: cj
'''

# Import the modules
import random

def eightball():
    answers = random.randint(1,8)
    answertext=""
    
    if answers == 1:
        answertext="It is certain"
    
    elif answers == 2:
        answertext="Outlook good"
    
    elif answers == 3:
        answertext="You may rely on it"
    
    elif answers == 4:
        answertext="Ask again later"
    
    elif answers == 5:
        answertext="Concentrate and ask again"
    
    elif answers == 6:
        answertext="Reply hazy, try again"
    
    elif answers == 7:
        answertext="My reply is no"
    
    elif answers == 8:
        answertext="My sources say no"
    
    return answertext
