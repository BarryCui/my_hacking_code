import socket
import sys

SERVER_HOST = sys.argv[1]
# SERVER_HOST = "1.1.1.1"
SERVER_PORT = 5005

# create the socket object
with socket.socket() as s:
    # connect to the server
    s.connect((SERVER_HOST, SERVER_PORT))
    filename = s.recv(4096)
    with open(filename, 'wb') as f:
        while True:
            data = s.recv(4096)
            if not data:
                break
            f.write(data)

    





