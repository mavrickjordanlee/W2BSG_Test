import pymongo

def update_game_data():
    client = pymongo.MongoClient('mongodb+srv://w2b_admin:w2b_admin@w2bsg.dnmytqb.mongodb.net/?retryWrites=true&w=majority&appName=W2BSG')
    db = client['w2bsg_db']
    collection = db['games']

    collection.update_many(
        { 'game_name': game_name },
        { '$set': { 'gameImageUrl': gameImageUrl } }
    )
game_name = "Cyberpunk 2077"
gameImageUrl = 'https://cdn.cloudflare.steamstatic.com/steam/apps/1091500/header.jpg?t=1710761498'
update_game_data()
print("Data updated successfully.")