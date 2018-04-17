# kg/m3 ratio
# list of dictionaries sorted by ratio value from low to high

Cygnus = {"mass": 2000, "volume": 18.9}
Dragon = {"mass": 2400, "volume": 7.6}
Kounotori = {"mass": 5200, "volume": 14}
Progress = {"mass": 6000, "volume": 10}

list_spacecrafts = [Cygnus, Dragon, Kounotori, Progress]

for spacecraft in list_spacecrafts:
    ratio = spacecraft.get("mass") / spacecraft.get("volume")
    spacecraft["kg/m3"] = ratio

list_spacecrafts = sorted(list_spacecrafts, key=lambda
                          spacecraft: spacecraft["kg/m3"])
print(list_spacecrafts)
