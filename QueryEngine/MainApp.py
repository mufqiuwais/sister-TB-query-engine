def mainMenu():
  isStop = False
  while not isStop:
    import socket
    print("Welcome to Query Engine Article!")
    print("1. Search for an article with keyword")
    print("2. Insert an Article")
    print("3. Exit")
    Input = input("Choose : ")
    if Input == "1":
      host = ""
      Keyword = input("Enter the Keyword (only one word and lowercase): ")
      if ord(Keyword[0]) >= 97 and ord(Keyword[0]) <= 105:
        host = "127.0.0.1"
        print("Going to server 1")
      elif ord(Keyword[0]) >= 106 and ord(Keyword[0]) <= 114:
        host = "127.0.0.2"
        print("Going to server 2")
      elif ord(Keyword[0]) >= 115 and ord(Keyword[0]) <= 122:
        host = "127.0.0.3"
        print("Going to server 3")

      ClientSocket = socket.socket()
      port = 1233
      print('Waiting for connection')
      try:
        ClientSocket.connect((host, port))
      except socket.error as e:
        print(str(e))
      
      ConnectedResponse = ClientSocket.recv(2048)
      print(ConnectedResponse.decode('utf-8'))
      WelcomeResponse = ClientSocket.recv(2048)
      print(WelcomeResponse.decode('utf-8'))
      ClientSocket.send(str.encode(Keyword))
      CountResponse = ClientSocket.recv(2048)

      count = int(CountResponse.decode('utf-8'))

      for i in range(count):
        judul = ClientSocket.recv(2048)
        author = ClientSocket.recv(2048)
        teks = ClientSocket.recv(2048)
        print("-------------Artikel " + str(i+1) + "--------------")
        print("Judul : " + judul.decode('utf-8'))
        print("Author : " + author.decode('utf-8'))
        print("Teks : " + teks.decode('utf-8'))


      # print(Response.decode('utf-8'))
      # Response = ClientSocket.recv(2048)
      # print(Response.decode('utf-8'))

      ClientSocket.close()
      print("Connection to Server is Closed")
    elif Input == "2":
      from bson.objectid import ObjectId
      from nltk.tokenize import word_tokenize
      import nltk
      from nltk.corpus import stopwords
      from typing import Collection
      import pymongo
      import UtilMongoDB

      # Get the database
      db = UtilMongoDB.get_database()
      collectionArtikel = db["artikel"]
      collectionFreq = db["freqkata"]
      collectionInvInd = db["invindex"]


      judul =  input("Masukan judul: ") 
      author = input("Masukan author: ") 
      teks = input("Masukan teks: ")
      artikel = {"judul": judul, "author": author, "teks": teks}

      result = collectionArtikel.insert_one(artikel)

      id_artikel = ObjectId(result.inserted_id)

      punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
      for ele in teks:
        if ele in punc:
          teks = teks.replace(ele, " ")

      teks=teks.lower()

      # counting per word in text
      words = teks.split()
      counts = {}
      for word in words:
          if word not in counts:
              counts[word] = 0
          counts[word] += 1

      teks=' '.join(UtilMongoDB.unique_list(teks.split()))
      # print(sorted(counts.keys()))

      # print(counts)

      for i in range(1):
          # this will convert
          # the word into tokens
          text_tokens = word_tokenize(teks)
        
      tokens_without_sw = [
          word for word in text_tokens if not word in stopwords.words()]

      print(tokens_without_sw)

      for word in tokens_without_sw:
        kata_freq = word
        frequency = counts[word]
        freqkata = {
          "kata" : kata_freq,
          "id_artikel" : id_artikel,
          "frequency" : frequency
        }
        resultFreq = collectionFreq.insert_one(freqkata)

        result = collectionInvInd.find({ "kata": kata_freq })
        lists = list(result)
        if len(lists)==0:
          InvIndex = {
            "kata" : kata_freq,
            "id_freq" : [ObjectId(resultFreq.inserted_id)]
          }
          collectionInvInd.insert_one(InvIndex)
        else:
          result = collectionInvInd.find({ "kata": kata_freq })
          id_InvInd = ""
          new_id_freq = ""
          # print("jadi gimana")
          for inv in result:
            id_InvInd = ObjectId(inv["_id"])
            new_id_freq = inv["id_freq"] + [ObjectId(resultFreq.inserted_id)]
            # print(new_id_freq)
          InvIndex ={ "$set" : {
            "id_freq" : new_id_freq
          }}
          collectionInvInd.update_one({ "_id": id_InvInd }, InvIndex)

      print("Insert artikel berhasil")
    elif Input == "3":
      isStop = True

if __name__ == "__main__":
  mainMenu()
