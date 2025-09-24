import socket


class UdpSender:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message):
        self.sock.sendto(message.encode("utf-8"), (self.ip, self.port))

    def __str__(self):
        return f"Message send to {self.ip}:{self.port}"
