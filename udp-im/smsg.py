from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("0.0.0.0", 65000))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
n = input("Name > ")
while True:
    m = input("Input> ")
    if not m:
        continue
    m = n + ": " + m
    s.sendto(m.encode("utf-8"), ("255.255.255.255", 65000))
