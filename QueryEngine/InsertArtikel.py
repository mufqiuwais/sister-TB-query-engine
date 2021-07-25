from typing import Collection
import pymongo
import UtilMongoDB

# Get the database
db = UtilMongoDB.get_database()
collection_name = db["artikel"]

# id = input("Masukan id: ")
judul =  input("Masukan judul: ") 
author = input("Masukan author: ") 
teks = input("Masukan teks: ")
artikel = {"judul": judul, "author": author, "teks": teks}
insert = collection_name.insert_one(artikel)

print("Insert dokumen berhasil")


