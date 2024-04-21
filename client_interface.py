# Class Interface to create a server

import socket

HOST = "127.0.0.1"
PORT = 65342

class Client:
    def __init__(self, port=None):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = HOST
        if not port:
            self.port = PORT
        else:
            self.port = port

    def start(self):
        '''
        Start the server and listen for any requests
        '''
        with self.socket as socket:
            socket.connect((self.host, self.port))
            socket.sendall(b"Hello, world")
            data = socket.recv(1024)

        print(f"Received {data!r}")


def main():
    client = Client()
    client.start()

if __name__ == '__main__':
    main()