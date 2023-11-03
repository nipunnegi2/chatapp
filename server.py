import socket 
import threading 

def send_msg():
    while True:
        msg = input().encode()
        client.send(msg)

def recv_msg():
    while True:
        received = client.recv(1024)
        print(received.decode())

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #this will tell that yu have to use IPV$ and TCP 
#to remove reuse address  
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#Now we will bind  IP and port 
s.bind(("127.0.0.1",8888))
print("Listening.....")

s.listen(1)   #we have to listen to 1 client that's why we have used 1 


#now Server has to accept the connection 

client,addr = s.accept()
print("Connected")


t1 = threading.Thread(target=send_msg)
t1.start()

recv_msg()










