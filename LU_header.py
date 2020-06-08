import os, sys, socket
import scapy.all


def myIp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.connect(('<broadcast>', 0))
    return sock.getsockname()[0]


def scanner(ipAddress):
    scapy.all.arping(ipAddress)


def correctNetwork(ipAddress):
    tmp = ipAddress.count('.')
    if tmp != 3:
        print('Incorrectly!\n')
    tmp = ipAddress.count('/')
    if tmp != 1:
        print('No network mask!\n')
