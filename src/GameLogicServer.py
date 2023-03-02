from random import shuffle
from NetworkModule import Server_Net
import safefile

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
path = 'savefile.txt'

#Class init
class player:
    def __init__(self, username, password, money = 250, wins = 0, losses = 0, bet = 0, lost = False, stand = False, score = 0):
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
    cardvalue.append(11)
    for j in range(4):
        for i in range(2,11):
            cardvalue.append(i)
        for i in range(3):
            cardvalue.append(10)

def determineCardType(pos):  
    for i in range(4):
        if(pos > i * 13 and pos <= i * 13 + 13):
            return i

def deckempty():
    shuffle(cardorder)
    cardcycle = 1

def checkgamestate():
    for i in players:
        if (i.score == 21):
            i.stand = True
            return 2
        elif i.score > 21:
            i.lost = True
            return 2
        else:
            return 1

def handlewin(player):
    if(player != 2): #check draw
        for i in players:
            if (i == player):
                i.money += betpool
                i.wins += 1
            else:
                i.losses += 1
            if (i.money <= 0):
                safefile.delete_user(path,i.username)
            else:
                safefile.update_user(path,i.username)
    showendscreen(player)

def showendscreen(winner):
    if(winner == 2):
        server.send(Clientconnections[0],'2')
        server.send(Clientconnections[1],'2')
    else:
        #send win to winner lose to loser
        for i in players:
            if (winner == i):
                server.send(Clientconnections[i],'1')
            else:
                server.send(Clientconnections[i],'0')
        scoreboard = safefile.user_leaderboard_wins(path)
        #send scoreboardlist
        for i in Clientconnections:
            server.send(Clientconnections[i],scoreboard)


server = Server_Net()
playercount = 0
#Login Process
while(mode == 0):
    for i in range():
        Clientconnections[i] = server.server_Listen(IP,PORT)
        loginornew = server.receive(Clientconnections[i])    # if login-> 0 if new -> 1
        #get login variable from network
        if (loginornew == 0):
            inputusername = server.receive(Clientconnections[i])
            inputpassword = server.receive(Clientconnections[i]) #get input for password from network
            data = safefile.user_login(path,inputusername,inputpassword)
            if (data == 0):
                    server.send(Clientconnections[i],'no_user')
            else:
                server.send(Clientconnections[i],'user_ok')
                players[i] = player(inputusername, inputpassword, data[1], data[2], data[3])
                playercount += 1

        elif (loginornew == 1):
            inputusername = server.receive(Clientconnections[i]) #get input for username from network
            inputpassword = server.receive(Clientconnections[i]) #get input for password from network
            players[i] = player(inputusername,inputpassword) 
            safefile.create_user(path,players[i].username, players[i].password)
            break
    if playercount >= 2:
        mode = 1

turn = 1
betpool = 0

#Game Loop
while(mode == 1):     
    if (turn <= 2):
        server.send(players[activeplayer].money)
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
        Cardinfo.append(cardpos % 13)
        Cardinfo.append(players[activeplayer].score)
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
    
    




    



   








