import socket

some_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
some_socket.connect(('www.py4inf.com', 80))
request = 'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'
some_socket.send(request.encode('utf-8'))
data = ['', '']
while len(data) >= 1:
    data = some_socket.recv(512)
    print(data)
some_socket.close()