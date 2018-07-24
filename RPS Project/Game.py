import sys
import random

score = [0,0,0]
history = [0,0,0]
count = [0]

#Friendly greeting
input("Good Lobning. Press enter.")
print("Choices: \n 0 = Rock \n 1 = Paper \n 2 = Scissors \n 3= exit")

#Returns game result
def judge(sign_1, sign_2):
    result = sign_1 - sign_2
    if abs(result) > 1:
        result = int(-result/2)
    return result

#Strategy. Based on opponent's history, probability of each sign scales with the frequency of the sign it defeats. Chooses rock as first move.
def stratagy():
    if count[0] == 1:
        return 0
    choice = random.uniform(0,1)
    if choice < history[2]/(count[0]-1):
        return 0
    if choice > (1-history[0]/(count[0]-1)):
        return 1
    return 2

#takes in user input
def game():
    count[0] += 1
    sign = int(input(""))
    computer_sign = stratagy()

    #incompetence checks
    if int(sign) not in [0,1,2,3]:
        sys.exit("Program terminated due to user incompetence")
    if sign == 3:
        sys.exit("Have a nice day")
        
    #stores user sign
    history[sign] += 1

    winner = judge(sign,computer_sign)

    #prints result
    if winner==0:
        print("Draw.")
    elif winner == 1:
        print("You win")
    else:
        print("You lose. You suck.")
    
    #stores and prints cumulative score
    score[winner] += 1
    print("Games: ", count[0])
    print("Result: \n draw, win, loss = ", score)
    game()
game()