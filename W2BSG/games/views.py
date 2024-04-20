from django.http import JsonResponse
import pymongo

client = pymongo.MongoClient('mongodb+srv://w2b_admin:w2b_admin@w2bsg.dnmytqb.mongodb.net/?retryWrites=true&w=majority&appName=W2BSG')
db = client['w2bsg_db']
collection = db['game_list']
price_collection = db['games']

def get_all_games():

    games_list = {}

    for game_record in collection.find():
        game_name = game_record['game_name']
        game_record['_id'] = str(game_record['_id'])
        games_list[game_name] = game_record

    return games_list

def get_price_history():
    
    games_price_history = {}

    for game_record in collection.find():
        game_id = str(game_record['_id'])
        game_name = game_record['game_name']
        game_record['_id'] = game_id
        games_price_history[game_id] = game_record
        # Initialize price history for each game
        games_price_history[game_id]['history'] = {}

    # Retrieve price information and add to the game record
    for record in price_collection.find():
        game_name = record['game_name']
        price = record['price']
        date = record['date']
        # Update price history for each game
        for game_id, game_info in games_price_history.items():
            if game_name == game_info['game_name']:
                game_info['history'][date] = price

    return games_price_history

def games_list(request):
   latest_price_trends = get_all_games()
   if latest_price_trends:
        return JsonResponse(latest_price_trends)
   else:
        return JsonResponse({'error': 'No data found for any game'}, status=404)

def search_game(request, game_name):
        latest_price_trends = get_all_games()
        if latest_price_trends:
            game_info = latest_price_trends.get(game_name)
            if game_info:
                return JsonResponse(game_info)
            else:
                return JsonResponse({}, status=404)
        else:
            return JsonResponse({'error': 'No data found for any game'}, status=404)
        
def game_details(request, _id):
    price_history= get_price_history()
    if price_history:
        game_info = price_history.get(_id)
        if game_info:
            return JsonResponse(game_info)
        else:
            return JsonResponse({}, status=404)
    else:
        return JsonResponse({'error': 'No data found for any game'}, status=404)

