from urllib2 import Request, urlopen, URLError
import json
key = '630fcc09-1af2-457b-a192-100ce644acaa'

def get_summoner_info(summoner_name):
    attempt_url = 'https://euw.api.pvp.net/api/lol/euw/v1.4/summoner/by-name/'+summoner_name+'?api_key='+key
    req = Request(attempt_url)
    response = urlopen(req)
    return  json.loads(response.read())

def get_summoner_id(summoner_name):
    summoner_info = get_summoner_info(summoner_name)
    return summoner_info[summoner_name]['id']

def get_recent_games(summoner_id):
    attempt_url = 'https://euw.api.pvp.net/api/lol/euw/v1.3/game/by-summoner/'+str(summoner_id)+'/recent?api_key='+key
    req = Request(attempt_url)
    response = urlopen(req)
    return  json.loads(response.read())


def get_match_history(summoner_id):
    attempt_url = 'https://euw.api.pvp.net/api/lol/euw/v2.2/matchhistory/'+str(summoner_id)+'?api_key='+key
    print attempt_url
    req = Request(attempt_url)
    response = urlopen(req)
    return  json.loads(response.read())

def get_games_won(summoner_name):
    summoner_id = get_summoner_id(summoner_name)
    hist = get_recent_games(summoner_id)
    total_games = 0.
    won_games = 0.
    for i in range(len(hist['games'])):
        if hist['games'][i]['gameMode']=='CLASSIC': 
            total_games += 1. 
            if hist['games'][i]['stats']['win']: 
                won_games += 1
    return won_games, total_games
