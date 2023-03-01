import hashlib
from NetworkModule import Client_Net

client = Client_Net()
client.client_Connect(IP,42069) #IP von Server
client.send("Hello from Client!")
print(client.recieve())

mode = 0 #login/register-0, playing-1
logorreg = #login-0 or register-1 from gui
checkuser = 'no_user'

while (mode == 0):
    client.send(mode) 
    if (logorreg == 0):
        username = #username from gui
        password = #password from gui
        client.send(username)
        client.send(hashlib.sha256(password.encode()).hexdigest())
        client.recieve(checkuser)
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
