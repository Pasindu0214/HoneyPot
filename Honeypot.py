#!/usr/bin/env python3

import socket

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('', 2222))
    server_sock.listen(127)

    client_sock, client_addr = server_sock.accept()
    print (f"Connection from {client_addr[0]}:{client_addr[1]})
    client_sock.send(b"Hello, World!\n")
    print(client_sock.recv(256).decode())

if __name__ == "__main__":
    main() 
