import hashlib
from NetworkModule import Client_Net

client = Client_Net()
client.client_Connect(IP,42069) #IP von Server

mode = 0 #login/register-0, playing-1

checkuser = 'no_user'
playerbet = 0
playeraction = 'action'
cnt = 0

def login(username, password, logorreg):
    #login-0 or register-1 from gui
    client.send(logorreg)
    client.send(username)
    client.send(hashlib.sha256(password.encode()).hexdigest())
    checkuser = client.recieve()
    if (checkuser != 'no_user' or checkuser != 'wrong_password'):
        mode = 1
    

def register(username, password, checkpass, logorreg):
    #login-0 or register-1 from gui
    client.send(logorreg)
    if (password == checkpass):
        client.send(username)
        client.send(hashlib.sha256(password.encode()).hexdigest()) 
        mode = 1
    else:
        return("password isn't the same") #show on gui


while (mode == 1):
    if (cnt == 0):
        playerbet = #amount from gui
        client.send(playerbet)
        cnt = 1

    playerturn = client.recieve()
    if (playerturn == 'turn'):
        #gui: its your turn
        playerturn = 'notturn'
    
    playeraction = #action from gui either draw or stand
    client.send(playeraction)

    cardinfo = client.recieve() #cardinfo how
    #gui cardinfo

    #when game ends set cnt=0
