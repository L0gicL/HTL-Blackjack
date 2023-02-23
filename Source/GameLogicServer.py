
mode = 0 # 0 = login, 1 = playing, 2 = game finished
players = []


#Class init
class player:
    def __init__(self, username, password, wins = 0, losses = 0,money = 250):
        self.username = username
        self.password = password
        self.wins = wins
        self.losses = losses
        self.money = money



'''
pull data from save file
'''

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





