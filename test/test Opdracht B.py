import math

Cygnus = {"payload": 2000, "mass": 7400, "basecost": 390000000, "FtW": 0.73}
Progress = {"payload": 2400, "mass": 7020, "basecost": 175000000, "FtW": 0.74}
Kounotori = {"payload": 5200, "mass": 10500, "basecost": 420000000, "FtW": 0.71}
Dragon = {"payload": 6000, "mass": 12200, "basecost": 347000000, "FtW": 0.72}

list_spacecrafts = [Cygnus, Progress, Kounotori, Dragon]

remaining = 0

for i in range(len(list_spacecrafts)):
	FtW = 0.73
	fuelRatio = list_spacecrafts[i]["FtW"] / (1 - list_spacecrafts[i]["FtW"])
	fuel = ((list_spacecrafts[i]["mass"] + (list_spacecrafts[i]["payload"] - remaining)) * fuelRatio)
	print(fuel)
	costs = (math.ceil(fuel * 1000) * 5) + list_spacecrafts[i]["basecost"]
	print(costs)