import random

#sets paramaters, including the probability that of the "player's" choices, and starts the game
def test(number, prob_0, prob_1):
    global score, history, count, rock, paper
    score = [0,0,0]
    history = [0,0,0]
    count = [0]
    rock = prob_0
    paper = prob_1
    game(number)

#Returns game result
def judge(sign_1, sign_2):
    result = sign_1 - sign_2
    if abs(result) > 1:
        result = int(-result/2)
    return result

#Strategy. Based on opponent's history, probability of each sign scales with the frequency of the sign it defeats. Chooses rock as first move.
def stratagy():
    if count[0]==1:
        return 0
    choice = random.uniform(0,1)
    if choice < history[2]/(count[0]-1):
        return 0
    if choice > (1-history[0]/(count[0]-1)):
        return 1
    return 2

#player 
def player():
    choice = random.uniform(0,1)
    if choice < rock:
        return 0
    if choice > 1-paper:
        return 1
    return 2

def game(number):
    while count[0] < number:
        count[0] += 1

        #throws signs
        sign = player()
        computer_sign = stratagy()
            
        #store player sign and result
        history[sign] += 1
        score[judge(sign,computer_sign)] += 1

    #prints success/failure
    if score[2]/count[0] < 1/3:
        print("Failure")
    else:
        print("Success")
    if score[2]/count[0]-1/3 < .2:
        print("In range of 1/3")

#An opponent that always chooses the same move (one test for each)
test(1000, 0, 0)
test(1000, 1, 0)
test(1000, 0, 1)

#An opponent that plays with a randomly selected bias. 
for a in range(4):
    rock = random.uniform(0,1)
    paper = random.uniform(0,1-rock)
    test(1000,rock,paper)

#a random opponent
print("Failure here is fine")
test(1000, 1/3, 1/3)