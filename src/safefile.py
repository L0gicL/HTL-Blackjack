def create_user(name, password):
    money = 5000
    user = [str(name), str(password), money]
    savefile = open(pathtofile, 'r')
    data = savefile.readlines
    savefile.close
    if user(0) in data:
        return(0)
    elif user(0) not in data:
        try:
            savefile = open(pathtofile, 'w')
            for i in user:
                savefile.writelines("{}\n".format(i))
            savefile.close
            return(1)
        except:
            return(0)

def user_login(name, password):
    savefile = open(pathtofile, 'r')
    data = savefile.readlines
    