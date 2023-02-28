from random import shuffle

mode = 0 # 0 = login, 1 = playing, 2 = game finished
cardcycle = 1
activeplayer = True
draw = bool
players = [0,1]
cards = []
cardvalue = []
cardorder = []
winscore = 21

#Class init
class player:
    def __init__(self, username, password,bet = 0, lost = False, stand = False, score = 0, wins = 0, losses = 0,money = 250):
        self.username = username
        self.password = password
        self.bet = bet
        self.lost = lost
        self.stand = stand
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

def determineCardType(pos):  
    for i in range(4):
        if(pos > i * 13 and pos <= i * 13 + 13):
            return i

def deckempty():
    shuffle(cardorder)
    cardcycle = 1

def checkgamestate():
    for i in players:
        if i.score > 21:
            i.lost = True
            return 2
        else:
            return 1

def handlewin(player):
    if(player != 2): #check draw
        for i in players:
            if (i == player):
                i.money += betpool
            if (i.money <= 0):
                deleteuser(i)

    showendscreen(player)

def showendscreen(winner):
    if(winner == 2):
        #send draw
    else:
        #send win to winner lose to loser
        #showleaderboard(need fileIO module)

def deleteuser(user):
    #need fileIO module
        
def adduser(user):
    #need fileIO module

def updateuser(user):
    #need fileIO module

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
            adduser(players[i])
            break
    if len(players) > 1:
        mode = 1

turn = 1
betpool = 0

#Game Loop
while(mode == 1):     
    if (turn <= 2):
        #get betamount from players
        if (activeplayer):
            players[0].bet = betamount
            players[0].money -= betamount
        elif (not activeplayer):
            players[1].bet = betamount
            players[1].money -= betamount 
        betpool += betamount
        turn += 1
    
    #send player 1 "(username),it's your turn"
    #player 1 sends draw or stand
    if cardcycle > 52:
        deckempty()

    if(draw):
        cardpos = cardorder[cardcycle]
        cardcycle += 1
        card = cards[cardpos]
        if (activeplayer):
            players[0].score += int(cardvalue[cardpos])
        elif (not activeplayer):
            players[1].score += int(cardvalue[cardpos])
        determineCardType(cardpos)
        #send card drawn with score to activeplayer
    if(not draw):
        if (activeplayer):
            players[0].stand = True
        elif (not activeplayer):
            players[1].stand = True

    if(not players[0].stand and not players[1].stand):
        activeplayer = not activeplayer
    elif(players[0].stand and players[1].stand):
        mode = 2 
    elif(players[0].stand):
        activeplayer = False
    elif(players[1].stand):
        activeplayer = True
    mode = checkgamestate()   #check player scores

while(mode == 2):
    for i in players:
        if (i.lost):
            handlewin(i)
    if(winscore - players[0].score < winscore - players[1].score):
        handlewin(players[0])
    elif(winscore - players[0].score > winscore - players[1].score):
        handlewin(players[1])
    elif(winscore - players[0].score == winscore - players[1].score):
        if(players[0].bet < players[1].bet):
            handlewin(players[1])
        elif(players[0].bet > players[1].bet):
            handlewin(players[0])
        elif(players[0].bet == players[1].bet):
            handlewin(2)
    
    




    



   








