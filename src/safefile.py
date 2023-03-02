"""
savefile functions
philipp frenzel
02.03.2023
"""


def create_user(name, password):
    money = 5000
    win = 0
    lose = 0
    user = [str(name), str(password), money, win, lose]
    savefile = open(pathtofile, 'r')
    data = savefile.readlines
    savefile.close
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

def user_login(name, password):
    try:
        savefile = open(pathtofile, 'r')
        data = savefile.readlines
        savefile.close
        
        index = data.index(name)
        if data[index] == name and data[index+1] == password:
            values = [name, data[index+2], data[index+3], data[index+4]]
            return values
        else:
            return 0
    except:
        return 0
    
def update_user(name, money, win, lose):
    try:
        savefile = open(pathtofile, 'r')
        data = savefile.readlines
        savefile.close
        index = data.index(name)

        data[index+2] = money
        data[index+3] = win
        data[index+4] = lose

        savefile = open(pathtofile, 'w')
        data = savefile.writelines
        savefile.close
    except:
        return 0

def delete_user(name):
    try:
        savefile = open(pathtofile, 'r')
        data = savefile.readlines
        savefile.close
        index = data.index(name)

        data[index] = "!!!DELETED!!!"

        savefile = open(pathtofile, 'w')
        data = savefile.writelines
        savefile.close
    except:
        return 0
    
