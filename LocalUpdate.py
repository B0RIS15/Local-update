from header import *
import os, threading


def scan_Ip(ip):
    addr = net + str(ip)
    comm = ping_com + addr
    response = os.popen(comm)
    data = response.readlines()
    for line in data:
        if 'TTL' in line:
            print(addr, "--> Ping Ok")
            break


input('This program named WSUS_OFFLINE\nPlease, press enter to start\n')
serv = myIp()
print('Your IP address is: ', serv)
ipAddress = '192.168.1.0/24'
while True:
    ans = input('You network is ' + ipAddress + '? y/n ')
    if ans == 'y' or ans == 'Y':
        break
    elif ans == 'n' or ans == 'N':
        ipAddress = input('Please enter correct: ')
        break
while True:
    try:
        scanner(ipAddress)
        break
    except OSError:
        ipAddress = input('Enter correct network: ')

net_split = serv.split('.')
a = '.'
net = net_split[0] + a + net_split[1] + a + net_split[2] + a
start_point = 0
end_point = 255


ping_com = "ping -n 1 "


print('Scanning in Progress:')

for ip in range(start_point, end_point):
    if ip == int(net_split[3]):
       continue
    potoc = threading.Thread(target=scan_Ip, args=[ip])
    potoc.start()

potoc.join()

print('Scanning completed\n')
print('Waiting server and client')
