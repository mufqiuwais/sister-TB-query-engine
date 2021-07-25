import UtilMongoDB

# Get the database
dbname = UtilMongoDB.get_database()

print("Initializing Data")
# insert artikel
collection_name = dbname["artikel"]

artikel_1 = {
  "_id" : "1",
  "judul" : "Software Engineer",
  "author" : "Mufqi",
  "teks" : "Software Engineer is a hobby"
}

artikel_2 = {
  "_id" : "2",
  "judul" : "Dwinanda is A Genius",
  "author" : "Dwinanda",
  "teks" : "Dwinanda is a software engineer. He has an IQ over 150"
}
collection_name.insert_many([artikel_1,artikel_2])

# insert artikel
collection_name = dbname["freqkata"]

freqkata_1 = {
  "_id" : "1",
  "kata" : "software",
  "id_artikel" : "1",
  "frequency" : 1
}

freqkata_2 = {
  "_id" : "2",
  "kata" : "engineer",
  "id_artikel" : "1",
  "frequency" : 1
}

freqkata_3 = {
  "_id" : "3",
  "kata" : "hobby",
  "id_artikel" : "1",
  "frequency" : 1
}

freqkata_4 = {
  "_id" : "4",
  "kata" : "dwinanda",
  "id_artikel" : "2",
  "frequency" : 1
}

freqkata_5 = {
  "_id" : "5",
  "kata" : "genius",
  "id_artikel" : "2",
  "frequency" : 1
}

freqkata_6 = {
  "_id" : "6",
  "kata" : "iq",
  "id_artikel" : "2",
  "frequency" : 1
}

freqkata_7 = {
  "_id" : "7",
  "kata" : "software",
  "id_artikel" : "2",
  "frequency" : 1
}

freqkata_8 = {
  "_id" : "8",
  "kata" : "engineer",
  "id_artikel" : "2",
  "frequency" : 1
}
collection_name.insert_many(
  [freqkata_1,freqkata_2,freqkata_3,freqkata_4,
  freqkata_5,freqkata_6,freqkata_7,freqkata_8])

  # insert inverted index
collection_name = dbname["invindex"]

invindex_1 = {
  "_id" : "1",
  "kata" : "software",
  "id_freq" : ["1","7"]
}

invindex_2 = {
  "_id" : "2",
  "kata" : "engineer",
  "id_freq" : ["2","8"]
}
collection_name.insert_many([invindex_1,invindex_2])

print("Data has been Initialized")