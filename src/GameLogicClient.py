import hashlib
from NetworkModule import Client_Net

client = Client_Net()
client.client_Connect(IP,42069) #IP von Server

mode = 0 #login/register-0, playing-1
logorreg = #login-0 or register-1 from gui
checkuser = 'no_user'
playerbet = 0
playeraction = 'action'
cnt = 0

while (mode == 0):
    client.send(mode) 
    if (logorreg == 0):
        username = #username from gui
        password = #password from gui
        client.send(username)
        client.send(hashlib.sha256(password.encode()).hexdigest())
        checkuser = client.recieve()
        if (checkuser != 'no_user' or checkuser != 'wrong_password'):
            mode = 1
            break

    elif (logorreg == 1):
        username = #username from gui
        password = #password from gui
        checkpass = #check password from gui
        if (password == checkpass):
            client.send(username)
            client.send(hashlib.sha256(password.encode()).hexdigest())
            mode = 1
            break 
        else:
            #to gui password not same


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
    

