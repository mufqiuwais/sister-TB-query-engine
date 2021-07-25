import UtilMongoDB

# Get the database
db = UtilMongoDB.get_database()
collectionInvInd = db["invindex"]
collectionFreq = db["freqkata"]
collectionArtikel = db["artikel"]

Kata = input("Masukan kata kunci query : ")

queryInvInd = { "kata": Kata }

InvInd = collectionInvInd.find(queryInvInd)

for x in InvInd:
  print(x['id_freq'])
  for id_freq in x['id_freq']:
    freq = collectionFreq.find({ "_id": id_freq})
    for y in freq:
      artikel = collectionArtikel.find({ "_id": y['id_artikel']})
      for z in artikel:
        print(z)
