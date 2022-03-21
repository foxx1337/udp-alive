import socket
from datetime import datetime
import argparse

parser = argparse.ArgumentParser("UDP server to listen for messages")
parser.add_argument("ip6", default="::", help="ipv6 to listen on")
parser.add_argument("port", type=int, default=31337, help="port to listen on")
args = parser.parse_args()

serverSock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

serverSock.bind((args.ip6, args.port))

while True:
    data, addr = serverSock.recvfrom(1024)
    print("{0}: {1}".format(datetime.now(), data))
