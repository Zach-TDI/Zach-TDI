import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QApplication, QDialog
import socket
##################################################################
# set up the UDP path and IP addresses
##################################################################
UDP_PORT = 8088
# "192.168.100.108"  #IP address for Server(RaspberryPi)
h_name = socket.gethostname()
UDP_IP = socket.gethostbyname(h_name)
print(h_name)
address = (UDP_IP, UDP_PORT)
print(address)
# "192.168.100.111" #IP address for client(Clear Core)
UDP_IP2 = "192.168.100.50"
address2 = (UDP_IP2, UDP_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet, UDP

sock.bind(address)
##################################################################
# Switch Case for level adjustment
##################################################################


class PythonSwitch:
    def position(self, height):
        default = "move home"
        return getattr(self, 'case_' + str(height), lambda: default)
##################################################################
# cases represent hights of the hotwire
##################################################################

    def case_0(self):
        msg = 'Home Position'
        print('moving to the home postion')
        sock.sendto(msg.encode("utf-8"), (address2))
        motion = "Moving To: " + msg
        return motion

    def case_1(self):
        msg = 'Position_1'
        print('moving to the home postion')
        sock.sendto(msg.encode("utf-8"), (address2))
        motion = "Moving To: " + msg
        return motion

    def case_2(self):
        msg = 'Position_2'
        sock.sendto(msg.encode("utf-8"), (address2))
        motion = "Moving To: " + msg
        return motion

    def case_3(self):
        msg = 'Position_3'
        sock.sendto(msg.encode("utf-8"), (address2))
        motion = "Moving To: " + msg
        return motion

    def case_4(self):
        msg = 'Position_4'
        sock.sendto(msg.encode("utf-8"), (address2))
        motion = "Moving To: " + msg
        return motion

    def case_5(self):
        msg = 'Position_5'
        sock.sendto(msg.encode("utf-8"), (address2))
        motion = "Moving To: " + msg
        return motion

    def case_6(self):
        msg = 'Position_6'
        sock.sendto(msg.encode("utf-8"), (address2))
        motion = "Moving To: " + msg
        return motion

##################################################################
# User selection of level via HMI
#################################################################
# HMI code goes here
##


##################################################################
# Pi sends message to Controller to move to height
#################################################################
wireLevel = PythonSwitch()

while True:
    # user input will equal the input button value
    userInput = int(input("what is the spa level ? "))
    msg = f'moving to position {userInput}'

    if userInput >= 1 and userInput < 7:
        print(wireLevel.position(userInput))
        sock.sendto(msg.encode("utf-8"), (address2))  # encodes the user input
    else:
        print(wireLevel.position(0))
        sock.sendto(msg.encode("utf-8"), (address2))
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print(data)
    print(addr)
    # if userInput >= 1 and userInput < 7:
    #     print(wireLevel.position(1))
    # else:
    #     print(wireLevel.position(0))
