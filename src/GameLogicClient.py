import hashlib
from NetworkModule import Client_Net

client = Client_Net()
client.client_Connect(IP,42069) #IP von Server
client.send("Hello from Client!")
print(client.recieve())

mode = #login-0 or register-1 from gui

client.send(mode) 
if (mode == 0):
    username = #username from gui
    password = #password from gui
    client.send(username)
    client.send(hashlib.sha256(password.encode()).hexdigest())

elif (mode == 1):
    username = #username from gui
    password = #password from gui
    checkpass = #check password from gui
    if (password == checkpass):
        client.send(username)
        client.send(hashlib.sha256(password.encode()).hexdigest()) 
    else:
        #password not same


