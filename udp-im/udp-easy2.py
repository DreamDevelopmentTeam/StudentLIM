import threading as tl
from socket import *
s = socket(AF_INET, SOCK_DGRAM)
i = gethostbyname(gethostname())
print("Local IP: " + i)
p = 65000
n = input("Input your user name > ")
s.bind(("0.0.0.0", p))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
def r():
    while True:
        try:
            d, a = s.recvfrom(1024)
            m = d.decode("utf-8")
            print(a, " => ", m)
        except KeyboardInterrupt:
            break
def s():
    while True:
        try:
            m = input("Input> ")
            if not m:
                continue
            m = n + ": " + m
            d = m.encode("utf-8")
            s.sendto(d, ("255.255.255.255", p))
        except KeyboardInterrupt:
            break
s.sendto(("Client Join ==> " + i + "( " + n + " )").encode("utf-8"), ("255.255.255.255", p))
rt = tl.Thread(target=r, daemon=True)
rt.start()
st = tl.Thread(target=s, daemon=True)
st.start()
rt.join()
st.join()
