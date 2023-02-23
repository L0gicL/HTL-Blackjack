"""
HTL-Blackjack - Networking Module
Author: Nathanael Eiter
Date: 23.02.2023
"""
#import libraries
import socket
import pickle

#parent network class
class Network:
    def __init__(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #create socket
    
    #data send function
    def send(self,data):
        self.connection.send(pickle.dumps(data))
    
    #data recieve function
    def recieve(self,conn,buffer_size=1024):
        while True:
            data = conn[0].recv(buffer_size)
            if not data:
                break
            return pickle.loads(data)

#client network class
class Client_Net(Network):
    def __init__(self):
        super().__init__()
    
    #function to connect to server
    def client_Connect(self,ip,port):
        self.connection.connect((ip,port))

#server network class
class Server_Net(Network):
    def __init__(self):
        super().__init__()
    
    #function to listen for incomming connections from clients
    def server_Listen(self,ip,port):
        self.connection.bind((ip,port))
        self.connection.listen()
        client_connection, client_address = self.connection.accept()
        return client_connection, client_address


#testing
if __name__ == '__main__':
    import threading
    IP = "localhost"
    PORT = 65500
    
    def serverTest():
        server = Server_Net()
        client1 = server.server_Listen(IP,PORT)
        print(server.recieve(client1))
    t = threading.Thread(target=serverTest)
    t.start()
    
    client = Client_Net()
    client.client_Connect(IP,PORT)
    packet = "testing"
    client.send(packet)
    t.join()