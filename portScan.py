import socket

target = "197.23.201.47"

def portscan(port):
    try:
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM # means using TCP
        )  
        sock.connect((target, port))
        return True
    except: 
        return False

#print(portscan(80))
i = 0
t = dict()
for port in range(1, 104):
    result = portscan(port)
    if result:
        print("port {} is open".format(port))
        t[i] = port
        i += 1
    else:
        print("port {} is closed".format(port)) 
print(t)