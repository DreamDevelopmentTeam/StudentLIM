from socket import *;s=socket(AF_INET,SOCK_DGRAM);s.bind(("0.0.0.0",65000));s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
while True:
    d,a=s.recvfrom(1024);print(a,"=>", d.decode("utf-8"))