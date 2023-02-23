"""
HTL-Blackjack - Networking Module
Author: Nathanael Eiter
Date: 23.02.2023
"""
import socket
import pickle

class Network:
    def __init__(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def send(self,data:dict):
        self.connection.send(pickle.dumps(data))
    
    def recieve(self,conn,buffer_size=1024):
        while True:
            data = conn[0].recv(buffer_size)
            if not data:
                break
            return pickle.loads(data)

class Client_Net(Network):
    def __init__(self):
        super().__init__()
    
    def client_Connect(self,ip,port):
        self.connection.connect((ip,port))


class Server_Net(Network):
    def __init__(self):
        super().__init__()
        
    def server_Listen(self,ip,port):
        self.connection.bind((ip,port))
        self.connection.listen()
        client_connection, client_address = self.connection.accept()
        return client_connection, client_address


if __name__ == '__main__':
    import threading
    IP = "localhost"
    PORT = 65500
    
    def serverTest():
        server = Server_Net()
        client1 = server.server_Listen(IP,PORT)
        print(server.recieve(client1)["test"])
    t = threading.Thread(target=serverTest)
    t.start()
    
    client = Client_Net()
    client.client_Connect(IP,PORT)
    packet = {"test":1235}
    client.send(packet)
    t.join()