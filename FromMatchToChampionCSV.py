import json
import os
import csv
import pandas as pd
import numpy as np

def parse_match(data):
    # durata del match
    match_duration = data["gameDuration"]
    # id del match
    match_id = data["gameId"]
    dict_champion = {}
    team_100 = []
    team_200 = []
    for i in data["participants"]:
        # associo ad ogni partecipantId del match, il nome, prendendelo dal dizionario creato prima,
        # del campione a cui fa riferimento
        dict_champion[i["participantId"]] = champion_id_name.get(i["championId"])
        if(i["teamId"] == 100):
            team_100.append(champion_id_name.get(i["championId"]))
        else:
            team_200.append(champion_id_name.get(i["championId"]))


    # per ogni campione
    for i in data["participants"]:

        name = champion_id_name.get(i["championId"])
        team = i["teamId"]
        if(i["timeline"]["lane"] == "BOTTOM"):
            ruole = i["timeline"]["role"]
        else:
            ruole = i["timeline"]["lane"]

        winner = i["stats"]["win"]
        level = i["stats"]["champLevel"]
        item0 = i["stats"]["item0"]
        item1 = i["stats"]["item1"]
        item2 = i["stats"]["item2"]
        item3 = i["stats"]["item3"]
        item4 = i["stats"]["item4"]
        item5 = i["stats"]["item5"]
        item6 = i["stats"]["item6"]
        kills = i["stats"]["kills"]
        dKills = i["stats"]["doubleKills"]
        tKills = i["stats"]["tripleKills"]
        qKills = i["stats"]["quadraKills"]
        pKills = i["stats"]["pentaKills"]
        deaths = i["stats"]["deaths"]
        assists = i["stats"]["assists"]
        heal = i["stats"]["totalHeal"]
        goldEarned = i["stats"]["goldEarned"]
        goldSpent = i["stats"]["goldSpent"]
        minionsKilled = i["stats"]["totalMinionsKilled"]
        #towerKill = i["stats"]["towerKills"]
        inhibitorKill = i["stats"]["inhibitorKills"]
        #firstKill = i["stats"]["firstBloodKill"]
        #firstAssist = i["stats"]["firstBloodAssist"]
        #firstTowerKill = i["stats"]["firstTowerKill"]
        #firstInhibitorKill = i["stats"]["firstInhibitorKill"]
		
        attributi = []
        attributi.append(match_id)
        attributi.append(match_duration)
        attributi.append(team)
        attributi.append(ruole)
        attributi.append(winner)
        attributi.append(level)
        attributi.append(item0)
        attributi.append(item1)
        attributi.append(item2)
        attributi.append(item3)
        attributi.append(item4)
        attributi.append(item5)
        attributi.append(item6)
        attributi.append(kills)
        attributi.append(dKills)
        attributi.append(tKills)
        attributi.append(qKills)
        attributi.append(pKills)
        attributi.append(deaths)
        attributi.append(assists)
        attributi.append(heal)
        attributi.append(minionsKilled)
        attributi.append(goldEarned)
        attributi.append(goldSpent)
        #attributi.append(firstKill)
        #attributi.append(firstAssist)
        #attributi.append(firstTowerKill)
        #attributi.append(firstInhibitorKill)
        #attributi.append(towerKill)
        attributi.append(inhibitorKill)

        if(team == 100):
            for i in team_100:
                if(name != i):
                    attributi.append(i)
            for j in team_200:
                attributi.append(j)
        else:
            for i in team_200:
                if (name != i):
                    attributi.append(i)
            for j in team_100:
                attributi.append(j)

        file = 'champion_csv/' + name + '.csv'
        # controllo se il file del campione e' stato creato oppure no
        # se non e' stato creato, lo creo, inserendo il nome delle colonne
        if(not os.path.isfile(file)):
            colonne = ["match_id", "match_duration", "team_id", "role", "winner", "championLevel", "item0", "item1", "item2", "item3","item4",
                       "item5", "item6", "kills", "doubleKill", "tripleKill", "quadraKill", "pentaKill", "deaths","assists",
                       "totalHeal", "minionsKill", "goldEarned", "goldSpent",
                       "inhibitorKills", "champion_friend2", "champion_friend3", "champion_friend4",
                       "champion_friend5", "champion_enemy1", "champion_enemy2", "champion_enemy3", "champion_enemy4", "champion_enemy5"];
            with open(file, 'ab') as f:
                writer = csv.writer(f)
                writer.writerow(colonne)

        with open(file, 'ab') as f:
            writer = csv.writer(f)
            writer.writerow(attributi)
        
	
    return dict_champion


def saveToFile(file_name, attributes):

    with open(file_name, 'ab') as f:
        writer = csv.writer(f)
        writer.writerow(attributes)

# salvo per ogni campione i seguenti eventi: champion_kill, champion_item_purchased, champion_skill_level_up
def parse_event(data, game_id, dict_particpant_name):

    file_kill = "event_csv/champion_kills.csv"
    file_item = "event_csv/champion_item_purchased.csv"
    file_level = "event_csv/champion_skill_level_up.csv"

    # se non esistono i file csv, le creiamo con il nome delle colonne

    if (not os.path.isfile(file_kill)):
        colonne = ["match_id", "killer", "victim", "timestamp", "position_x", "position_y"];
        with open(file_kill, 'ab') as f:
            writer = csv.writer(f)
            writer.writerow(colonne)

    if (not os.path.isfile(file_item)):
        colonne = ["match_id", "champion", "item", "timestamp"];
        with open(file_item, 'ab') as f:
            writer = csv.writer(f)
            writer.writerow(colonne)

    if (not os.path.isfile(file_level)):
        colonne = ["match_id", "champion", "skill_slot", "timestamp"];
        with open(file_level, 'ab') as f:
            writer = csv.writer(f)
            writer.writerow(colonne)

    match_id = game_id

    # itero su tutti i frames
    for a in range(1, len(data["frames"])):
        # itero su tutti gli eventi di ogni singolo frames
        if ("events" in data["frames"][a]):

            for b in data["frames"][a]["events"]:

                attributes = []

                if(b["type"] == "CHAMPION_KILL"):
                    attributes.append(match_id)
                    attributes.append(dict_particpant_name.get(b["killerId"]))
                    attributes.append(dict_particpant_name.get(b["victimId"]))
                    attributes.append(b["timestamp"])
                    attributes.append(b["position"]["x"])
                    attributes.append(b["position"]["y"])
                    saveToFile(file_kill, attributes)

                elif(b["type"] == "ITEM_PURCHASED"):
                    attributes.append(match_id)
                    attributes.append(dict_particpant_name.get(b["participantId"]))
                    attributes.append(b["itemId"])
                    attributes.append(b["timestamp"])
                    saveToFile(file_item, attributes)

                elif(b["type"] == "SKILL_LEVEL_UP"):
                    attributes.append(match_id)
                    attributes.append(dict_particpant_name.get(b["participantId"]))
                    attributes.append(b["skillSlot"])
                    attributes.append(b["timestamp"])
                    saveToFile(file_level, attributes)
                    
		
		# creo il file per quel minuto di gioco se non esiste
        file = "event_min_csv/timestamp_minute_" + str(a) + ".csv"
        if (not os.path.isfile(file)):
            colonne = ["match_id", "champion", "minion", "gold"];
            with open(file, 'ab') as f:
                writer = csv.writer(f)
                writer.writerow(colonne)

        # itero su tutti gli eventi di ogni singolo frames
        for b in range(1, len(data["frames"][a]["participantFrames"]) + 1):

            nome = dict_particpant_name.get(b)
            minionKills = data["frames"][a]["participantFrames"][str(b)]["minionsKilled"]
            totalGold = data["frames"][a]["participantFrames"][str(b)]["totalGold"]
            attributes = []
            attributes.append(match_id)
            attributes.append(nome)
            attributes.append(minionKills)
            attributes.append(totalGold)

            saveToFile(file, attributes)

# salvo su file gli eventi(minionsKilled e totalGold) avvenuti minuto per minuto
def frames_minute(data, game_id, dict_particpant_name):

    match_id = game_id

    for a in range(1, len(data["frames"])):

        # creo il file per quel minuto di gioco se non esiste
        file = "event_min_csv/timestamp_minute_" + str(a) + ".csv"
        if (not os.path.isfile(file)):
            colonne = ["match_id", "champion", "minion", "gold"];
            with open(file, 'ab') as f:
                writer = csv.writer(f)
                writer.writerow(colonne)

        # itero su tutti gli eventi di ogni singolo frames
        for b in range(1, len(data["frames"][a]["participantFrames"]) + 1):

            nome = dict_particpant_name.get(b)
            minionKills = data["frames"][a]["participantFrames"][str(b)]["minionsKilled"]
            totalGold = data["frames"][a]["participantFrames"][str(b)]["totalGold"]
            attributes = []
            attributes.append(match_id)
            attributes.append(nome)
            attributes.append(minionKills)
            attributes.append(totalGold)

            saveToFile(file, attributes)

# aggrego per ogni campione e match_id gli eventi avvenuti minuto per minuto
def merge_event_min():

    df = pd.read_csv('event_min_csv/timestamp_minute_1.csv')
    vet = []
    for i in range(2,80):
        vet.append(pd.read_csv("event_min_csv/timestamp_minute_" + str(i) + ".csv"))

    match_ids = []
    for i in df["match_id"].unique():
        match_ids.append(i)

    count = 0
    print len(match_ids)
    for m in match_ids:
        count += 1
        print count
        df_temp = df[df["match_id"] == m]
        for v in vet:
            if m in v["match_id"].unique():
                v_temp = v[v["match_id"] == m]
                df_temp = pd.merge(df_temp, v_temp, how='outer', on=['match_id', 'champion'])
                if len(df_temp) > 10:
                    break;

            else:
                with open("champion_event_min_csv/champion_event_min.csv", 'ab') as f:
                    df_temp.to_csv(f, header=False)
                break;


def splitInChampionsFromMerge():

    df = pd.read_csv("champion_event_min_csv/champion_event_min.csv")

    vet_minion = ["match_id", "champion"]
    vet_gold = ["match_id", "champion"]
    for i in range(1, 80):
        vet_minion.append("minion_" + str(i))
        vet_gold.append("gold_" + str(i))


    for name in df["champion"].unique():

        df_champion = df[df["champion"] == name]
        df_champion[vet_minion].to_csv("champion_event_min_csv/" + name + "_minion.csv")
        df_champion[vet_gold].to_csv("champion_event_min_csv/" + name + "_gold.csv")

def caricaFile():
	in_file = open("games_parsed.txt","r")
	text = in_file.read().splitlines()
	in_file.close()
	return text
	
def salvagameid(idGame):
	
	out_file = open("games_parsed.txt","a")
	out_file.write(str(idGame))
	out_file.write("\n")
	out_file.close()

def main():

    # carico il file dei campioni con all'interno il loro id e il nome
    with open('champion.txt') as data_file:
        champion = json.load(data_file)
    # creo un dizionario dove ci sara l'id del campione e il suo nome

    for a in champion["data"]:
        # associo ad ogni id, il nome del campione
		champion_id_name[champion["data"][a]["id"]] = champion["data"][a]["name"]
		
    count = 0
    game_id = pd.read_csv("games_id.csv", delimiter=",")
    game_id = game_id["gameId"].unique()
    
    games_parsed = caricaFile()
    
    for game in game_id:
		
		if(str(game) not in games_parsed):
			
			dict_participant = {}
			file_game = "games 50.000/" + str(game) + "_match.json"
			file_timeline = "games 50.000/" + str(game) + "_timeline.json"
			if (os.path.isfile(file_game) and os.path.isfile(file_timeline)):
				
				count += 1
				print count
				
				with open(file_game) as data_file:
					data = json.load(data_file)
					
					# crea un csv per ogni campione
					dict_participant = parse_match(data)
				
				# crea un csv con gli eventi	
				with open(file_timeline) as data_file2:
					
					data2 = json.load(data_file2)
					
					# i 3 eventi principali
					parse_event(data2, game, dict_participant)
					
					# eventi minuto per minuto
					#frames_minute(data2, game, dict_participant)
				
				
				salvagameid(game)
						
			else:
				print game


champion_id_name = {}

if __name__ == "__main__":
	
    #main()
    #merge_event_min()
    #exit(0)
    # prima di chiamare questa funzione si devono inserire i nomi delle colonne all'interno del dataset
    # creato dalla funzione merge_event_min()
    splitInChampionsFromMerge()
    exit(0)
