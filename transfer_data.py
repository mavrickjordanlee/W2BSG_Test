import pymongo

def transfer_game_data():
    client = pymongo.MongoClient('mongodb+srv://w2b_admin:w2b_admin@w2bsg.dnmytqb.mongodb.net/?retryWrites=true&w=majority&appName=W2BSG')
    db = client['w2bsg_db']
    source_collection = db['games']
    destination_collection = db['game_list']

    # Define the filter criteria
    filter_criteria = {'date': '2024-03-17'}

    # Find documents matching the filter criteria in the source collection
    documents_to_transfer = source_collection.find(filter_criteria)

    # Transfer the documents to the destination collection
    destination_collection.insert_many(documents_to_transfer)

    # Close the MongoDB connection
    client.close()

transfer_game_data()
print("Data transferred successfully.")