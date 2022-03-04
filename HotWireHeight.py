import socket


##################################################################
#set up the UDP path and IP addresses
##################################################################
UDP_PORT = 8888
UDP_IP = "192.168.100.108"  #IP address for Server(RaspberryPi)
address = (UDP_IP, UDP_PORT)
print(address)
UDP_IP2 = "172.16.0.27" #IP address for cliant(Clear Core)
address2 = (UDP_IP2, UDP_PORT)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#Internet, UDP
sock.bind(address)

##################################################################
#Switch Case for level adjustment 
##################################################################
class PythonSwitch:
    def position(self, height):
        default = "move home"
        return getattr(self, 'case_' + str(height), lambda: default)()
##################################################################
#cases represent hights of the hotwire
##################################################################
    def case_0(self):
        msg = 'positionHome'
        print('moving to the home postion')
        sock.sendto("this is Raw Data",(address2))

        return "Moving To Home Postion"

    def case_0(self):
        msg = 'positionHome'
        print('moving to the home postion')
        sock.sendto("this is Raw Data",(address2))

        return "Moving To Home Postion"

    def case_2(self):
        msg = 'Position_1'    
        sock.sendto(msg.encode("utf-8"),(address2))
        return "Moving To Postion 1"
 
    def case_3(self):
        msg = 'Position_2'
        sock.sendto(msg.encode("utf-8"),(address2))
        return "Moving To Postion 2"

    def case_4(self):
        msg = 'Position_3'
        sock.sendto(msg.encode("utf-8"),(address2))
        return "Moving To Postion 3"

    def case_5(self):
        msg = 'Position_4'
        sock.sendto(msg.encode("utf-8"),(address2))
        return "Moving To Postion 4"

    def case_6(self):
        msg = 'Position_5'
        sock.sendto(msg.encode("utf-8"),(address2))
        return "Moving To Postion 5"
##################################################################
#User selection of level via HMI
#################################################################
##HMI code goes here
##

##################################################################
#Pi sends message to Controller to move to height
#################################################################
wireLevel = PythonSwitch()

while True:
    userInput = int(input("what is the spa level ? "))
    msg = f'moving to position {userInput}'
    
    if userInput >= 1 and userInput < 7:
        print(wireLevel.position(1))
        sock.sendto(msg.encode("utf-8"),(address2))
    else:
        print(wireLevel.position(0))
        sock.sendto(msg.encode("utf-8"),(address2))
    data, addr = sock.recvfrom(1024)#buffer size is 1024 bytes
    print(data)
    print(addr)
    if userInput >= 1 and userInput < 7:
        print(wireLevel.position(1))
    else:
        print(wireLevel.position(0))

