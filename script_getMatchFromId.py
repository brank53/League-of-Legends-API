import urllib, json
import json
import time
from pprint import pprint
import io
import pandas as pd

cont = 0
partite_vetrina = []
key = "yourkey"

		
def caricaFile():
	in_file = open("gameid_loaded.txt","r")
	text = in_file.read().splitlines()
	in_file.close()
	return text
	

def salvamatch(data, game):
	
	with io.open('prova 50.000/' + str(game) + '_match.json', 'w', encoding='utf-8') as f:
		f.write(unicode(json.dumps(data, ensure_ascii=False)))
		
def salvatimeline(data, game):
	
	with io.open('prova 50.000/' + str(game) + '_timeline.json', 'w', encoding='utf-8') as f:
		f.write(unicode(json.dumps(data, ensure_ascii=False)))
		
def salvagameid(idGame):
	
	out_file = open("gameid_loaded.txt","a")
	out_file.write(str(idGame))
	out_file.write("\n")
	out_file.close()	


dataset = pd.read_csv("games.csv", delimiter=",")

for game in dataset["gameId"].unique():	
	
	partite_vetrina = caricaFile()
				
	if (str(game) not in partite_vetrina):
	
		url = "https://euw1.api.riotgames.com/lol/match/v3/matches/" + str(game) + "?api_key=" + str(key)
		response = urllib.urlopen(url)
		if (response.getcode() == 200):
			data = json.loads(response.read())
			salvamatch(data, game)
		
		time.sleep(1.5)
		
		url = "https://euw1.api.riotgames.com/lol/match/v3/timelines/by-match/" + str(game) + "?api_key=" + str(key)
		response = urllib.urlopen(url)
		if (response.getcode() == 200):
			data = json.loads(response.read())
			salvatimeline(data, game)
			
		salvagameid(game)
		
		time.sleep(1.5)
		cont += 1
		print cont
	
	else:
		print "loaded"
