def Dice_Game():
    reward = 0
    dice1, dice2, dice3 = map(int, (input().split()))

    if(dice1 == dice2 == dice3):
        reward = 10000 + (dice1 * 1000)
        print(reward)
    else:
        if dice1 == dice2:
            reward = 1000 + (dice1 * 100)  
            print(reward)
        elif dice2 == dice3:
            reward = 1000 + (dice2 * 100)
            print(reward)
        elif dice1 == dice3:
            reward = 1000 + (dice1 * 100)
            print(reward)
        else :
            reward = max(dice1, dice2, dice3) * 100
            print(reward)    

Dice_Game()