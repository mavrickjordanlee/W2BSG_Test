import pymongo

def update_game_data():
    client = pymongo.MongoClient('mongodb+srv://w2b_admin:w2b_admin@w2bsg.dnmytqb.mongodb.net/?retryWrites=true&w=majority&appName=W2BSG')
    db = client['w2bsg_db']
    collection = db['game_list']

    collection.update_many(
        { 'game_name': game_name },
        { '$set': { 'date': date, 'time': time} }
    )
game_name = "Age of Empires IV: Anniversary Edition"
date = "2021-10-28"
time = "40"
update_game_data()
print("Data updated successfully.")