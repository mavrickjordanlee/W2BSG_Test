from django.http import JsonResponse
import pymongo
from bson import ObjectId

def get_all_games():
    client = pymongo.MongoClient('mongodb+srv://w2b_admin:w2b_admin@w2bsg.dnmytqb.mongodb.net/?retryWrites=true&w=majority&appName=W2BSG')
    db = client['w2bsg_db']
    collection = db['game_list']

    games_list = {}

    for game_record in collection.find():
        game_name = game_record['game_name']
        game_record['_id'] = str(game_record['_id'])
        games_list[game_name] = game_record

    return games_list

def games_list(request):
   games = get_all_games()
   if games:
        return JsonResponse(games)
   else:
        return JsonResponse({'error': 'No data found for any game'}, status=404)

def search_game(request, game_name):
    games = get_all_games()
    if games:
        game_info = games.get(game_name)
        if game_info:
            return JsonResponse(game_info)
        else:
            return JsonResponse({}, status=404)
    else:
        return JsonResponse({'error': 'No data found for any game'}, status=404)

def get_game_price_history(game_name):
    client = pymongo.MongoClient('mongodb+srv://w2b_admin:w2b_admin@w2bsg.dnmytqb.mongodb.net/?retryWrites=true&w=majority&appName=W2BSG')
    db = client['w2bsg_db']
    collection = db['games']

    # Query documents with game_name = "Grand Theft Auto V"
    cursor = collection.find({"game_name": game_name})

    # Initialize history dictionary
    history = {}

    # Iterate over the cursor and populate history
    for document in cursor:
        date = document['date']
        price = document['price']
        history[date] = price

    # Update the original dictionary with the populated history
    # Convert history dictionary to JSON

    # Print or return the JSON
    return history

def get_game_details(request, _id):
    client = pymongo.MongoClient('mongodb+srv://w2b_admin:w2b_admin@w2bsg.dnmytqb.mongodb.net/?retryWrites=true&w=majority&appName=W2BSG')
    db = client['w2bsg_db']
    collection = db['game_list']

    # Find the document with the provided game_id
    game_document = collection.find_one({"_id": ObjectId(_id)})
    
    if game_document:
        # Extract the game_name from the document
        game_name = game_document.get("game_name")
        price_history = get_game_price_history(game_name)

        game_details = {
            "id": str(game_document.get("_id")),
            "price": game_document.get("price"),
            "date": game_document.get("date"),
            "time": game_document.get("time"),
            "game_name": game_document.get("game_name"),
            "gameImageUrl": game_document.get("gameImageUrl"),
            "history": price_history  # Include price history in the dictionary
        }

        return JsonResponse(game_details)
    else:
        # Handle the case when the game with the provided ID is not found
        return JsonResponse({"error": "Game not found"}, status=404)
