from encodings import utf_8
import socket;
import random;




def client(ip: str, port: int, name: str):
    
    cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cl.connect((ip, port))
    while True:
        data = cl.recv(1024)
        print(data.decode("utf-8"))
        strt = f"{name} > " + input(f"{name} > ")
        cl.send(strt.encode("utf-8"))
    
def host_client(ip: str, port: int, name: str):
    server = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    user, adres = server.accept()
    while True:
        
        print(f"user var: {user}\nadres var: {adres}")
        strt = f"{name} > " + input(f"{name} > ")
        user.send(strt.encode("utf_8"))
        data = user.recv(1024)
        print(data.decode("utf-8"))




def run():
    
    print("Help: \n  host (ip) (port) (user name) - host a server \n  connect (ip) (port) (user name) - connect to server")
    while True:
        action = input("> ")
        splt_action = action.split()
        if splt_action[0] == "host":
            host_client(splt_action[1], int(splt_action[2]), splt_action[3])
        if splt_action[0] == "connect":
            client(splt_action[1], int(splt_action[2]), splt_action[3])
    
            
