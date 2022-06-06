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

# tulostetaan tietokannan collections nimet:
print(db.list_collection_names())
