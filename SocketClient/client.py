import socket

ClientSocket = socket.socket()
host1 = '127.0.0.1'
host2 = '127.0.0.2'
host3 = '127.0.0.3'
port = 1233

Input = input('Pilih server: ')
if Input == '1':
  host = host1
elif Input == '2':
  host = host2
elif Input == '3':
  host = host3

print(host)
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()