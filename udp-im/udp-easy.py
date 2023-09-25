import threading as tl
from socket import *
s = socket(AF_INET, SOCK_DGRAM)
lip = gethostbyname(gethostname())
print("Local IP: " + lip)
p = 65000
un = input("Input your user name > ")
s.bind(("0.0.0.0", p))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
def rm():
    while True:
        try:
            d, a = s.recvfrom(1024)
            m = d.decode("utf-8")
            #print(message, "from", addr)
            print(a, " => ", m)
        except KeyboardInterrupt:
            break
def sm():
    while True:
        try:
            m = input("Input> ")
            if not m:
                continue
            m = un + ": " + m
            d = m.encode("utf-8")
            s.sendto(d, ("255.255.255.255", p))
        except KeyboardInterrupt:
            break
s.sendto(("Client Join ==> " + lip + "( " + un + " )").encode("utf-8"), ("255.255.255.255", p))
rt = tl.Thread(target=rm, daemon=True)
rt.start()
st = tl.Thread(target=sm, daemon=True)
st.start()
rt.join()
st.join()
