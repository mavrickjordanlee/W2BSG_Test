from django.http import JsonResponse
import pymongo

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

