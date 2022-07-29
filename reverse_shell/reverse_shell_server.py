import socket

HOST = "0.0.0.0"
PORT = 5005
BUFFER_SIZE = 1024 * 128 

with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # avoid 'address in use' error
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    
    with conn as c:
        print(f"Connected from {addr[0]}:{addr[1]}...")
        cwd = c.recv(BUFFER_SIZE).decode()

        while True:
            # input command
            command = input(f" {cwd} #> ")
            # if enter exit, break the loop
            if command == "exit":
                break
            # if enter nothing other than blank, then skip the current loop
            if not command.strip():
                continue
            # send command to client to execute
            c.send(command.encode())
            # get response from client
            output = c.recv(BUFFER_SIZE).decode()
            print(output)

