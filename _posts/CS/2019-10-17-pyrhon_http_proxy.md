---
layout: post
title: python http proxy  
categories: [CS, PYTHON]
tags: [python]
---
<!-- more --> 
```python
import os
import socket
import threading
from urllib.parse import urlparse

def fisher(str_0):
    fish = 'today.hit.edu.cn'
    input = 'xhamster.com'
    if str_0 == input:
        return fish
    else:
        return str_0

def forbiden_users(str):
    users = ['no_use']
    users = ['127.0.0.1']
    for fu_i in range(len(users)):
        if users[fu_i] == str:
            return True
    return False

def forbiden_web(str):
    webs = ['pornhub.com']
    for fw_i in range(len(webs)):
        if webs[fw_i] == str:
            return True
    return False

class proxy:
    def __init__(self, host='127.0.0.1', port=13464):
        self.main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_socket.bind((host, port))
        self.main_socket.listen(100)
        self.host = host
        self.port = port

    def start(self):
        print("local host :")
        print(self.host)
        print("local port:")
        print(self.port)
        while True:
            connect, address = self.main_socket.accept()
            proxy_thread = threading.Thread(target=self.handle, args=(connect, address))
            proxy_thread.start()

    def handle(self,client_socket, client_addr ,data_size=13464,wait_time=100):
        rec_data = client_socket.recv(data_size)
        if len(rec_data) == 0:
            return
        rec_data_0 = rec_data.decode().split('\n')[0]
        #防止windows服务器频繁建立连接
        if rec_data_0.startswith('CONNECT'):
            return

        url = urlparse(rec_data_0.split()[1])
        #用户过滤
        if forbiden_users(client_addr[0]):
            client_socket.send(str.encode('You are restricted for internet service'))
            client_socket.close()
            return -1
        #网站过滤
        if forbiden_web(url.hostname):
            client_socket.send(str.encode('Forbiden website'))
            client_socket.close()
            return -1
        #钓鱼
        rec_data = str.encode(rec_data.decode().replace(url.hostname, fisher(url.hostname)))
        rec_data_0 = str.encode(rec_data_0.replace(url.hostname, fisher(url.hostname)))
        url = urlparse(rec_data_0.split()[1])

        filename = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), str(hash((url.netloc + url.path))) + '.txt')
        rec_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rec_connect.settimeout(wait_time)
        rec_connect.connect((url.hostname, 80))  # http服务80端口,模拟建立连接
        rec_connect.sendall(rec_data)
        while True:
            data = rec_connect.recv(data_size)
            if len(data) > 0:
                client_socket.send(data)
                file_handle = open(filename, 'wb')
                file_handle.write(data)
            else:
                break
        file_handle.close()
        client_socket.close()
        rec_connect.close()

if __name__ == '__main__':
    server = proxy('127.0.0.1', 13464)
    server.start()
```
