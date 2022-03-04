#need to change the Version of Python to 3.10
import socket 
UDP_PORT = 28000
UDP_IP = "192.168.100.50"

sock = socket.socket(socket.AF_INET,socket.SOCK_RAW)#Internet, UDP

class PythonSwitch:
    def position(self, height):
        default = "move home"
        return getattr(self, 'case_' + str(height), lambda: default)()

    def case_1(self):
        print('moving to the home postion')
        return "home postion"

    def case_2(self):
        return "postion 1"
    
    def case_3(self):
        return "postion 2"

    def case_4(self):
        return "postion 3"

    def case_5(self):
        return "postion 4"

    def case_6(self):
        return "postion 5"

wireLevel=PythonSwitch()
sock.bind((UDP_IP,UDP_PORT))


while True:
    data, addr = sock.recvfrom(1024)#buffer size is 1024 bytes
    print(data)
    print(addr)
    wireLevel.position(1)


    
