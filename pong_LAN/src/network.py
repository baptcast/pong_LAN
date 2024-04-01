import  socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = input("ip du serveur:")
        self.port =5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
        
    def getp(self):
        return self.p
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            self.server = input("\nmauvaise ip \nip du serveur:")
            self.addr = (self.server, self.port)
            return self.connect()
            
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

            