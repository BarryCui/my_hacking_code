import socket

HOST = "0.0.0.0"
PORT = 5005

with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print(f"Connected from {addr[0]}:{addr[1]}...")
        filename = input(" File to be uploaded: ")
        if filename == 'exit':
            break
        elif not filename.strip():
            continue
        else:
            conn.send(filename.encode())
        f = open(filename, 'rb')
        content = f.read(4096)
        while (content):
            conn.sendall(content)
            content = f.read(4096)
        f.close()

        print('Done sending.')
        conn.close()
