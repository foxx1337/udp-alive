import socket
import time
from datetime import datetime
import argparse

parser = argparse.ArgumentParser("UDP client to keep sending messages")
parser.add_argument("ip6", default="::", help="ipv6 to send to")
parser.add_argument("port", type=int, default=31337, help="destination port")
args = parser.parse_args()

MESSAGE = "hello " + args.ip6

clientSock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

while True:
    clientSock.sendto(str.encode(MESSAGE), (args.ip6, args.port))
    print("{0}: sent {1}".format(datetime.now(), MESSAGE))
    time.sleep(1)
