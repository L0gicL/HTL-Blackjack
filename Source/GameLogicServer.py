import random

mode = 0 # 0 = login, 1 = playing, 2 = game finished
cardcycle = 1
activeplayer = True
players = [0,1]
cards = []
cardvalue = []
cardorder = []

#Class init
class player:
    def __init__(self, username, password, score = 0, wins = 0, losses = 0,money = 250):
        self.username = username
        self.password = password
        self.wins = wins
        self.score = score
        self.losses = losses
        self.money = money

def init_cards():
    for i in range(1,53):
        cardorder.append(i)
    for j in range(4):
        for i in range(2,11):
            cardvalue.append(i)
        for i in range(3):
            cardvalue.append(10)
        cardvalue.append(11)



def deckempty():
    random.shuffle(cardorder)

def checkgamestate():
    for i in players:
        if i.score > 21:
            return 2
        

    
'''
pull data from save file
'''

#Login Process
while(mode == 0):
    for i in range():
        #get login variable from network
        #get input for username from network
        if (loginornew == 0):
            if (inputusername in usernames):
                #get input for password from network
                password = getpassforuser(inputusername)
                if (inputpassword == password):
                    players[i] = player(inputusername,inputpassword)
                    break
        elif (loginornew == 1):
            #get input for username from network
            #get input for password from network
            #input to confirm password and only let through if both are the same
            players[i] = player(inputusername,inputpassword) 
            break
    if len(players) > 1:
        mode = 1

#Game Loop
while(mode == 2):
    #send player 1 "(username),it's your turn"
    #player 1 sends draw or stand
    if cardcycle > 52:
        deckempty()
        cardcycle = 1

    if draw:
        cardpos = cardorder[cardcycle]
        cardcycle += 1
        card = cards[cardpos]
        if (activeplayer):
            players[0].score += int(cardvalue[cardpos])
        elif (not activeplayer):
            players[1].score += int(cardvalue[cardpos])
        mode = checkgamestate()
        #send card drawn with score

    activeplayer = not activeplayer

while(mode == 3):



    



   








