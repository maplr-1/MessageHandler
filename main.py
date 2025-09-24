import sys
import os
import shutil

from src.udp_sender import UdpSender
from src.udp_receiver import UdpReceiver


which_mode = int(input("""
1.Udp Sender
2.Udp Receiver
0.exit

choose_mode: """))


match which_mode:

    case 0:
        sys.exit()

    case 1:
        user_ip = str(input("Enter receiver ip: "))
        user_port = int(input("Enter receiver port: "))
        user_message = str(input("Enter the message: "))

        # send
        sender = UdpSender(user_ip, user_port)
        sender.send(user_message)

        # remove the compiled .pyc file
        if os.path.exists('__pycache__'):
            shutil.rmtree('__pycache__')

        print(sender)

    case 2:
        user_ip = str(input("Enter receiver ip: "))
        user_port = int(input("Enter receiver port: "))

        # receive
        receive = UdpReceiver(user_ip, user_port)
        receive.receiver()
        print(receive)
