import hashlib
from NetworkModule import Client_Net

client = Client_Net()

mode = 0 #login/register-0, playing-1
checkuser = 'no_user'
playerbet = 0
playeraction = 'action'
cnt = 0

def connecttoserver(IP):
    client.client_Connect(IP,42069) #IP von Server

def login(username, password, logorreg):
    #login-0 or register-1 from gui
    client.send(logorreg)
    client.send(username)
    client.send(hashlib.sha256(password.encode()).hexdigest())
    checkuser = client.recieve()
    if (checkuser != 'no_user' or checkuser != 'wrong_password'):
        mode = 1
    
    
def register(username, password,logorreg):
    #login-0 or register-1 from gui
    client.send(logorreg)
    client.send(username)
    client.send(hashlib.sha256(password.encode()).hexdigest()) 
    mode = 1



