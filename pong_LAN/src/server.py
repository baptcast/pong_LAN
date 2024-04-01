import socket
from _thread import *
import pickle
from player import Player
from ball import *



ip = socket.gethostbyname(socket.gethostname())
port =5555
print("\nserver ip  is:",ip,"\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((ip, port))
except socket.error as e:
    print(e)
    
s.listen(2)
print("Waiting for connection, server started")


players = [Player(20,0, 15, 150 ,(255, 0, 0)), Player(670,0,15, 150,(0,0,255))]
field = Field()
ball = Ball()

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        

        try:
            data = pickle.loads(conn.recv(2048))
            if type(data) is bool:
                ball.start()
            else:
                players[player] = data
                ball.move(players, field)
            
            if not data:
                print("Disconected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
#                 print('Recieved:', reply)
#                 print('sending: ', reply)
                
            conn.sendall(pickle.dumps((reply,ball, field)))
        except:
            pass
        
    print("Lost connection")
    conn.close()
        
currentPlayer = 0
while True:
    
    conn, addr = s.accept()
    print("connected to:", addr)
    
    start_new_thread(threaded_client, (conn,currentPlayer))
    currentPlayer += 1