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
	file_c = i + '.csv'
	if(os.path.isfile(file_c)):
		result = open("1champions_list_item/" + i + "_item.csv",'w')
		result.write("item" + "\n")
		df = pd.read_csv(file_c)
		for j in range(0,7):
			vet_item = df["item" + str(j)]
		
			for r in vet_item:
				if(r != 0):
					result.write(str(r) + "\n")
        
