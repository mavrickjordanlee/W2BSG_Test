from django.http import JsonResponse
import pymongo

def get_all_latest_game_price():
    client = pymongo.MongoClient('mongodb+srv://w2b_admin:w2b_admin@w2bsg.dnmytqb.mongodb.net/?retryWrites=true&w=majority&appName=W2BSG')
    db = client['w2bsg_db']
    collection = db['game_list']

    '''
    # Get distinct game names from the collection
    game_names = collection.distinct('game_name')

    latest_trends = {}

    for game_name in game_names:
        # Find the latest record for the specified game
        latest_record = collection.find_one({'game_name': game_name}, sort=[('date', pymongo.DESCENDING)])

        if latest_record:
        # Convert ObjectId to string
            latest_record['_id'] = str(latest_record['_id'])
            latest_trends[game_name] = latest_record

    return latest_trends
    '''

    # Retrieve all documents from the collection
    all_records = collection.find()

    games_data = {}

    # Iterate over each document
    for record in all_records:
        # Convert ObjectId to string
        record['_id'] = str(record['_id'])
        game_name = record['game_name']
        # Add to the dictionary using game name as key
        if game_name not in games_data:
            games_data[game_name] = []
        games_data[game_name].append(record)

    return games_data


def games_list(request):
   latest_price_trends = get_all_latest_game_price()
   if latest_price_trends:
        return JsonResponse(latest_price_trends)
   else:
        return JsonResponse({'error': 'No data found for any game'}, status=404)


