import socket


class UdpReceiver:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def receiver(self):
        self.sock.bind((self.ip, self.port))
        self.message, self.addr = self.sock.recvfrom(1024)

    def __str__(self):
        ip, port = self.addr

        msg = self.message.decode(errors="replace")
        return f"Message from {ip}:{port} → \"{msg}\""
