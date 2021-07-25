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


