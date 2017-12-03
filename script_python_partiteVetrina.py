import urllib, json
import json
import time
from pprint import pprint

key = "yourkey"

def caricaFile(region):
	in_file = open("partite_vetrina_" + str(region) + ".txt","r")
	text = in_file.read().splitlines()
	in_file.close()
	return text

def salvaFile(idGame, region):
	out_file = open("partite_vetrina_" + str(region) + ".txt","a")
	out_file.write(idGame)
	out_file.write("\n")
	out_file.close()

def getGameid():
	cont = 0
	partite_vetrina = []
	while(1):
		regions = ["euw1", "eun1", "na1", "jp1"]
		for region in regions:
			
			url = "https://" + str(region) + ".api.riotgames.com/lol/spectator/v3/featured-games?api_key=" + str(key)
			response = urllib.urlopen(url)
			data = json.loads(response.read())

			for item in data["gameList"]:
				
				game_id = item["gameId"]
				partite_vetrina = caricaFile(region)
				
				if (str(game_id) in partite_vetrina):
					print ("gia' esistente")
				else:
					salvaFile(str(game_id), region)
					cont += 1
					
		print(cont)
		time.sleep(300)
	
def main():
	
	getGameid()
	
	
	
if __name__ == "__main__":
    main()
