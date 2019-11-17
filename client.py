import socket


class Client(object):

    version = '160425.01'

    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.socket = socket.socket()
        self.running = True

    def debug(self, message):
        print('[{}] {}'.format(self.server, message))

    def connect(self):
        self.socket.connect((self.server, self.port))
        self.debug('Connected to {}:{}'.format(self.server, self.port))

    def start(self):
        self.started()
        while self.running:
            for i in self.socket.recv(1024).decode().split('\n'):
                split = i.split(',')
                if not split[0]:
                    continue
                self.receive(split[0], split[1:])
        self.socket.close()

    def started(self):
        pass

    def receive(self, message, args):
        pass

    def send(self, message):
        message = message + '\n'
        message = message.encode()
        self.socket.send(message)
