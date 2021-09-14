from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

movie = list(db.movies.find({'title' : '매트릭스'},{'_id':False}))\

print(movie)
print('======================================================')


print(list(db.movies.find({'star' : movie[0]['star']}, {'_id' : False})))
print('======================================================')

db.movies.update_one({'title' : '매트릭스'}, {'$set' : {'star' : "0"}})