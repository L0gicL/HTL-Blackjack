'''
Safile Functions for GameLogicServer and GameLogicClient
Philipp Frenzel
02.02.2023
'''

def create_user(pathtofile, name, password):
    money = 250                                            #starting money
    win = 0
    lose = 0
    user = [str(name), str(password), money, win, lose]
    savefile = open(pathtofile, 'r')
    data = savefile.readlines()
    savefile.close()
    for i in range(0,len(data)):                            #removing \n from lines
            data[i] = data[i].strip('\n')
    if user(0) in data:                                     #if username already exists -> return 0
        return(0)
    elif user(0) not in data:                               #if not creates user
        try:
            savefile = open(pathtofile, 'a')
            for i in user:
                savefile.writelines("{}\n".format(i))
            savefile.close()
            return(1)                                       #returns 1 after succssesful creation
        except:
            return(0)

def user_login(pathtofile, name, password):
    try:
        savefile = open(pathtofile, 'r')
        data = savefile.readlines()
        savefile.close()
        for i in range(0,len(data)):
            data[i] = data[i].strip('\n')
        
        index = data.index(name)
        if data[index] == name and data[index+1] == password:                   #if username and password are right, the values 
            values = [name, data[index+2], data[index+3], data[index+4]]        #name, money, wins, loses are returned
            return values
        else:
            return 0
    except:
        return 0
    
def update_user(pathtofile,name, money, win, lose):                             #after the game the users money, wins and loses are updated
    try:
        savefile = open(pathtofile, 'r')
        data = savefile.readlines()
        savefile.close()
        for i in range(0,len(data)):
            data[i] = data[i].strip('\n')
        index = data.index(name)

        data[index+2] = money
        data[index+3] = win
        data[index+4] = lose

        savefile = open(pathtofile, 'w')
        data = savefile.writelines()
        savefile.close()
    except:
        return 0

def delete_user(pathtofile,name):                                           #if a user is deleted his name gets replaced by "!!!DELETED!!!"
                                                                            #so noone can login with it anymore
    savefile = open(pathtofile, 'r')
    data = savefile.readlines()
    print(data)
    savefile.close()
    for i in range(0,len(data)):
        data[i] = data[i].strip('\n')
    
    index = data.index(str(name))
    
    data[index] = "!!!DELETED!!!"
    savefile = open(pathtofile,'w')
    for i in range(0,len(data)):
        data[i] = data[i]+('\n')                                            #the \n that was stripped bevore needs to be added again
    savefile.writelines(data)                                               #so the values are written correctly into the savefile
    savefile.close()

    
def user_leaderboard_wins(pathtofile):
    leaderboard = []
    moneylist = []                                                          #temporary list for the money values of all users
    with open(pathtofile, 'r') as savefile:
        data = savefile.readlines()

        for i in range(0,len(data)):
            data[i] = data[i].strip('\n')

        for i in range (2,len(data),5):
            moneylist.append(int(data[i]))

        for i in range(0,5):                                                #appends the 5 players with the most money to leaderboard[]
            print(data)
            val = max(moneylist)
            index = data.index(str(val))
            leaderboard.append(val)
            leaderboard.append(data[index-2])                               #username
            leaderboard.append(data[index+1])                               #wins
            moneylist[moneylist.index(val)] = 0                             #sets money temporarily 0 so users arent choosen twice

        return leaderboard


#testing
if __name__ == '__main__':
    path = "test.txt"
    print(delete_user(path,"nathi"))