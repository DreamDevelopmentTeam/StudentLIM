#import socket
import threading
from socket import *
sock = socket(AF_INET, SOCK_DGRAM)
local_ip = gethostbyname(gethostname())
print("Local IP: " + local_ip)
port = 25565
username = input("Input your user name > ")
sock.bind(("0.0.0.0", port))
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
def receive_message():
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            message = data.decode("utf-8")
            #print(message, "from", addr)
            print(addr, " => ", message)
        except KeyboardInterrupt:
            break
def send_message():
    while True:
        try:
            message = input("Input> ")
            if not message:
                continue
            message = username + ": " + message
            data = message.encode("utf-8")
            sock.sendto(data, ("255.255.255.255", port))
        except KeyboardInterrupt:
            break
sock.sendto(("Client Join ==> " + local_ip + "( " + username + " )").encode("utf-8"), ("255.255.255.255", port))
receive_thread = threading.Thread(target=receive_message, daemon=True)
receive_thread.start()
send_thread = threading.Thread(target=send_message, daemon=True)
send_thread.start()
receive_thread.join()
send_thread.join()
