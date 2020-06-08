import socket
from header import myIp

print('This is Local_Update!\n')
nameUpdate = input('Enter name of archive with updates: ')

try:
    op = open('update\\' + nameUpdate, 'rb')
except FileNotFoundError:
    input('File not found')
    exit()

serv = myIp()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((serv, 9090))
s.listen(1)
conn, addr = s.accept()

while True:
    print('online {addr}'.format(addr=addr))
    data = op.read(1024)
    if not data:
        exit()
    conn.send(data)
op.close()
