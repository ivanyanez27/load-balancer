# Class Interface to create a server

import socket

HOST = "127.0.0.1"
PORT = 65342

class Server:
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
            socket.bind((self.host, self.port))
            socket.listen()
            conn, addr = socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

def main():
    server = Server()
    server.start()
    print('Test')

if __name__ == '__main__':
    main()