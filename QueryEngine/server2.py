import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.2'
port = 1233
ThreadCount = 0
try:
  ServerSocket.bind((host, port))
except socket.error as e:
  print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
  connection.sendall(str.encode('Connected to server 2'))
  connection.sendall(str.encode('Welcome to the Server'))
  import UtilMongoDB

  # Get the database
  db = UtilMongoDB.get_database()
  collectionInvInd = db["invindex"]
  collectionFreq = db["freqkata"]
  collectionArtikel = db["artikel"]

  # Kata = input("Masukan kata kunci query : ")
  Kata = connection.recv(2048)
  Kata = Kata.decode('utf-8')

  print(Kata)

  queryInvInd = { "kata": Kata }

  InvInd = collectionInvInd.find(queryInvInd)


  for x in InvInd:
    ele = x["id_freq"]
    print(x["id_freq"])
    print(len(ele))
    connection.sendall(str.encode(str(len(ele))))
    for id_freq in x['id_freq']:
      freq = collectionFreq.find({ "_id": id_freq})
      for y in freq:
        artikel = collectionArtikel.find({ "_id": y['id_artikel']})
        for z in artikel:
          print(z)
          connection.sendall(str.encode(z["judul"]))
          connection.sendall(str.encode(z["author"]))
          connection.sendall(str.encode(z["teks"]))
  

  connection.close()

while True:
  Client, address = ServerSocket.accept()
  print('Connected to: ' + address[0] + ':' + str(address[1]))
  start_new_thread(threaded_client, (Client, ))
  ThreadCount += 1
  print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()