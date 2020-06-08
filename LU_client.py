import socket


print('ask your administrator for his ip address!\n')

serv = input('IP address: ')

s = socket.socket()

s.connect((serv, 9090))

op = open('myUndate.zip', 'wb')
while True:
    data = s.recv(1024)
    if not data:
        exit()
    op.write(data)
op.close()
s.shutdown(socket.SHUT_WR)
