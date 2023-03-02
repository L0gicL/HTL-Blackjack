
def create_user(pathtofile, name, password):
    money = 5000
    win = 0
    lose = 0
    user = [str(name), str(password), money, win, lose]
    savefile = open(pathtofile, 'r')
    data = savefile.readlines
    savefile.close
    for i in range(0,len(data)):
            data[i] = data[i].strip('\n')
    if user(0) in data:
        return(0)
    elif user(0) not in data:
        try:
            savefile = open(pathtofile, 'a')
            for i in user:
                savefile.writelines("{}\n".format(i))
            savefile.close
            return(1)
        except:
            return(0)

def user_login(pathtofile, name, password):
    try:
        savefile = open(pathtofile, 'r')
        data = savefile.readlines
        savefile.close
        for i in range(0,len(data)):
            data[i] = data[i].strip('\n')
        
        index = data.index(name)
        if data[index] == name and data[index+1] == password:
            values = [name, data[index+2], data[index+3], data[index+4]]
            return values
        else:
            return 0
    except:
        return 0
    
def update_user(pathtofile,name, money, win, lose):
    try:
        savefile = open(pathtofile, 'r')
        data = savefile.readlines
        savefile.close
        for i in range(0,len(data)):
            data[i] = data[i].strip('\n')
        index = data.index(name)

        data[index+2] = money
        data[index+3] = win
        data[index+4] = lose

        savefile = open(pathtofile, 'w')
        data = savefile.writelines
        savefile.close
    except:
        return 0

def delete_user(pathtofile,name):

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
        data[i] = data[i]+('\n')
    savefile.writelines(data)
    savefile.close()

    
def user_leaderboard_wins(pathtofile):
    leaderboard = []
    moneylist = []
    with open(pathtofile, 'r') as savefile:
        data = savefile.readlines()

        for i in range(0,len(data)):
            data[i] = data[i].strip('\n')

        for i in range (2,len(data),5):
            moneylist.append(int(data[i]))

        for i in range(0,5):
            print(data)
            val = max(moneylist)
            index = data.index(str(val))
            leaderboard.append(val)
            leaderboard.append(data[index-2])
            leaderboard.append(data[index+1])
            moneylist[moneylist.index(val)] = 0

        return leaderboard


#testing
if __name__ == '__main__':
    path = "test.txt"
    print(delete_user(path,"nathi"))