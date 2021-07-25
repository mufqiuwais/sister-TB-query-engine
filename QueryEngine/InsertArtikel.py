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
collectionInvInd = db["InvIndex"]


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


# print(sorted(counts.keys()))

# print(counts)

for i in range(1):
    # this will convert
    # the word into tokens
    text_tokens = word_tokenize(teks)
  
tokens_without_sw = [
    word for word in text_tokens if not word in stopwords.words()]

for word in tokens_without_sw:
  kata_freq = word
  frequency = counts[word]
  freqkata = {
    "kata" : kata_freq,
    "id_artikel" : id_artikel,
    "frequency" : frequency
  }
  collectionFreq.insert_one(freqkata)

print("Insert dokumen berhasil")


