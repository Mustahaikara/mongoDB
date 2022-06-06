from unittest import result
from pymongo import MongoClient
import passw
import certifi
ca = certifi.where()

password = passw.PASSWORD
#client = pymongo.MongoClient(uri, ssl_cert_reqs=ssl.CERT_NONE)
cluster = "mongodb+srv://elementsofai:"+password+"@albumi-koulu.8xfzscg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster, tlsCAFile=ca)

# db = client['AlbumDB'] - mahdollista tehdä myös näin
db = client.AlbumDB # luo automaattisesti jos ei ole
albums = db.Albums  # luo automaattisesti jos ei ole
                    # mutta näyttää ne vasta kun siellä on dataa
def add_album(artist,album,year,genre):
    # ei palauta mitään, vaan insert_one() metodilla lisätään
    # parametreina tulleet arvot albums-collectioniin
    # katso mallia w3 insert -kohdasta
    albums.insert_one({'artist':artist,'album':album,'year':year,'genre':genre})

def fetch_albums():
    # käy find() metodilla läpi for-loopilla rivi riviltä tulokset ja palauta
    # returnilla tulokset
    # luo tyhjä lista, ja rivi riviltä lisää listaan rivin tiedot
    # halutun listan rivi on muodossa
    # Deep Purple-Fireball-1970-Rock
    empty_list = []
    result = albums.find()
    for elem_ in result:
        empty_list.append(elem_['artist']+'-'+elem_['album']+'-'+str(elem_['year'])+'-'+elem_['genre'])
    return empty_list
    
def remove(selected_album):
    albums.delete_one({'artist':selected_album[0]})
    albums.delete_one({'album':selected_album[1]})
    albums.delete_one({'year':selected_album[2]})
    albums.delete_one({'genre':selected_album[3]})

def update(selected_album, artist, album, year, genre):
    albums.update_one({ "artist": selected_album[0] },{ "$set": { "artist": artist } })
    albums.update_one({ "album": selected_album[1] },{ "$set": { "album": album } })
    albums.update_one({ "year": selected_album[2] },{ "$set": { "year": year } })
    albums.update_one({ "genre": selected_album[3] },{ "$set": { "genre": genre } })
    

               
  
#========================================

# tulostetaan tietokannan collections nimet:
# print(db.list_collection_names())
# kaikkien tietueiden tiedot
# result = albums.find()  # hakee tiedot json muodossa joka on dictionary
# for elem in result:
#     for key_, value_ in elem.items():
#         print(f'{key_} {value_}')
# result1 = albums.find_one({'album':'Tässä albumin nimi'})
# print(result1)