import pandas as pd
import numpy

df = pd.read_csv('champion_kills.csv')
champions = df["killer"].unique()
champions = [x for x in champions if str(x) != 'nan']
cont = 0
for i in champions:
	cont += 1
	print cont
	df_kill = df[df["killer"] == i]
	df_kill = df_kill[['position_x','position_y']]
	df_kill.columns = ["x", "y"]
	df_kill.reset_index()
	df_kill.to_csv("champion_position/" + i + "_kill.csv", sep=',', index = False)
	
	df_death = df[df["victim"] == i]
	df_death = df_death[['position_x','position_y']]
	df_death.columns = ["x", "y"]
	df_death.reset_index()
	df_death.to_csv("champion_position/" + i + "_death.csv", sep=',', index = False)
