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

#attr = "gold"
attr = "minion"


#	INSERISCO IL NOME DELLE COLONNE NEL FILE CSV
attributi_header = []
attributi_header.append("date")
for name in champion_array:
	attributi_header.append(name)
with open("4champions_average_" + str(attr) + ".csv", 'ab') as f:
	writer = csv.writer(f)
	writer.writerow(attributi_header)


for cont in range(1,80):
	print cont
	attributi = []
	attributi.append(cont)
	for i in champion_array:
		file_c = i + '_' + str(attr) + '.csv'
		if(os.path.isfile(file_c)):
			df = pd.read_csv(file_c)
			media = round(df[str(attr) + "_" + str(cont)].mean(), 2)
			
			attributi.append(media)
			
	with open("4champions_average_" + str(attr) + ".csv", 'ab') as f:
		writer = csv.writer(f)
		writer.writerow(attributi)
        
