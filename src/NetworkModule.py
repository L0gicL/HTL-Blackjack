class Network:
    def __init__(self):
        import socket
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
