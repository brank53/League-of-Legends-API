import pandas as pd
import numpy
import json
import csv
import os

with open('3champion.txt') as data_file:
	champion = json.load(data_file)

champion_array = []
for a in champion["data"]:
	champion_array.append(champion["data"][a]["name"])

champion_array = sorted(champion_array)
cont = 0
for i in champion_array:
	cont += 1
	print cont
	file_c = i + '_item.csv'
	if(os.path.isfile(file_c)):
		data = pd.read_csv(file_c)
		#data["count"] = data.groupby('item')['item'].transform('count')
		data = data.groupby(["item"])["item"].count().reset_index(name="count")
		#	matches mi serve per sapere quante partite si hanno per un determinato champion
		matches = pd.read_csv("D:/Users/fscigliuzzo/Desktop/datasets league of legends/champion_csv/" + i + ".csv")
		attributi = []
		attributi = ["item", "count", "percentage"]
		with open("1champion_list_item_percentage/" + i + "_item_percentage.csv", 'a') as f:
				writer = csv.writer(f)
				writer.writerow(attributi)
		
		for index, row in data.iterrows():
			attributi = []
			attributi.append(row['item'])
			attributi.append(row['count'])
			percentage = (float(float(row["count"])/len(matches)))*100
			percentage = round(percentage, 2)
			attributi.append(percentage)
			
			with open("1champion_list_item_percentage/" + i + "_item_percentage.csv", 'a') as f:
				writer = csv.writer(f)
				writer.writerow(attributi)
			
	
