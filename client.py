import socket 
import threading 


def send_msg():
    while True:
        msg = input().encode()
        s.send(msg)   # it will send to socket i.e. s 


def recv_msg():
    while True:
        received=s.recv(1024)
        print(received.decode())




s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Connecting...")
while True:
    try:
        s.connect(("127.0.0.1",8888))
        break
    except ConnectionRefusedError:
        continue
print("Connected")

#part 2 

t1 = threading.Thread(target=send_msg)

t1.start()
recv_msg()

