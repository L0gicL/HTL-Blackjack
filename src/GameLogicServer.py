from random import shuffle
from NetworkModule import Server_Net

IP = '0.0.0.0'
PORT = 42069
mode = 0 # 0 = login, 1 = playing, 2 = game finished
cardcycle = 1
activeplayer = True
draw = bool
players = [0,1]
Clientconnections =[]
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
        pass
    else:
        #send win to winner lose to loser
        #showleaderboard(need fileIO module)

def deleteuser(user):
    #need fileIO module
        
def createuser(user):
    #need fileIO module

def updateuser(user):
    #need fileIO module

def loginuser(user):
    #need fileIO module

'''
pull data from save file
'''
server = Server_Net()
#Login Process
while(mode == 0):
    for i in range():
        Clientconnections[i] = server.server_Listen(IP,PORT)
        loginornew = server.receive(Clientconnections[i])    # if login-> 0 if new -> 1
        #get login variable from network
        if (loginornew == 0):
            inputusername = server.receive(Clientconnections[i])
            if (inputusername in usernames):
                server.send(Clientconnections[i],'user_ok')
                password = getpassforuser(inputusername)
                inputpassword = server.receive(Clientconnections[i]) #get input for password from network
                if (inputpassword == password):
                    players[i] = player(inputusername,inputpassword)
                    break
            else:
                server.send(Clientconnections[i],'no_user')
                continue
        elif (loginornew == 1):
            inputusername = server.receive(Clientconnections[i]) #get input for username from network
            inputpassword = server.receive(Clientconnections[i]) #get input for password from network
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
        betamount = server.receive(Clientconnections[turn-1])
        players[activeplayer].bet = betamount
        players[activeplayer].money -= betamount
        betpool += betamount
        turn += 1
    
    server.send(Clientconnections[activeplayer],'turn')    #send player "(username),it's your turn"
    draw = server.receive(Clientconnections[activeplayer]) #player sends draw or stand
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
        Cardinfo = determineCardType(cardpos)
        Cardinfo.append()
        server.send(Clientconnections[activeplayer],Cardinfo)  #send card drawn with score to activeplayer[colour,type,value]
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
    
    




    



   








