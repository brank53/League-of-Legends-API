import pandas as pd
import numpy
import json
import csv
import os
import matplotlib.pyplot as plt

with open('3champion.txt') as data_file:
	champion = json.load(data_file)

champion_array = []
for a in champion["data"]:
	champion_array.append(champion["data"][a]["name"])

champion_array = sorted(champion_array)


for name in champion_array:
	file_c = name + '.csv'
	if(os.path.isfile(file_c)):
		df = pd.read_csv(file_c)
		role = df["role"].value_counts()
		role.plot(kind='bar', color='b', alpha=0.7)
		plt.xlabel(name)
		plt.ylabel(name)
		plt.show()
		
exit(0)

for i in champion_array:
	file_c = i + '.csv'
	if(os.path.isfile(file_c)):
		df = pd.read_csv(file_c)
		avg_kills = round(df["kills"].mean(), 2)
		avg_match = round(df["match_duration"].mean(), 2)
		df2 = df[df["winner"] == True]
		winner = round((float(len(df2))/len(df))*100, 2)
		avg_gold = round(df["goldEarned"].mean(), 2)
		avg_minions = round(df["minionsKill"].mean(), 2)
		popolarity = round((float(len(df))/49642)*100, 2)
		
		
		attributi = []
		attributi.append(i)
		attributi.append(avg_kills)
		attributi.append(avg_minions)
		attributi.append(avg_gold)
		attributi.append(avg_match)
		attributi.append(winner)
		attributi.append(popolarity)
		
		with open("2data_champion_statistics.csv", 'ab') as f:
			writer = csv.writer(f)
			writer.writerow(attributi)
        
		
