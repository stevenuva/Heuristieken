import csv
import math
import os
import random
from Spacecraft_Classes import Spacecraft

# github link to retrieve CargoList1.csv if necessary
github_link = ("https://github.com/stevenuva/minor-programmeren/blob/"
               "master/CargoList1.csv")

# path to the csv_file
csv_file = "./data/CargoList1.csv"

# check if user has csv at the right path
for path in [csv_file]:
    assert os.path.exists(path), (f"{path} does not exist. Please download file"
                                  f" from {github_link}")

# load csv file into a list
with open(csv_file, "r") as infile:
    reader = csv.reader(infile)
    csv_list = list(reader)

# create an empty list
cargo1_list = []

# loop through store every csv row into a dictionary
# calculate the kg/m3 ratio
# append every dictionary to a list
for row in csv_list[1:]:
    cargo1_dic = {"id": row[0], "mass": float(row[1]), "volume": float(row[2])}
    cargo1_dic["kg/m3"] = cargo1_dic["mass"] / cargo1_dic["volume"]
    cargo1_list.append(cargo1_dic)

# sort list on volume
cargo1_list = sorted(cargo1_list, key=lambda
                     parcel: parcel["volume"])

# sort list on kg/m3 ratio
cargo1_list = sorted(cargo1_list, key=lambda
                     parcel: parcel["kg/m3"])

# define properties of the spacecrafts
Cygnus = Spacecraft(2000, 18.9, 7400, 390000000, 0.73)
Progress = Spacecraft(2400, 7.6, 7020, 175000000, 0.74)
Kounotori = Spacecraft(5200, 14, 10500, 420000000, 0.71)
Dragon = Spacecraft(6000, 10, 12200, 347000000, 0.72)
TianZhou = Spacecraft(6500, 15, 13500, 412000000, 0.75)
Verne_ATV = Spacecraft(7500, 48, 20500, 1080000000, 0.72)

# create a list containing all the spaceships
spacecrafts = [Cygnus, Dragon, Kounotori, Progress]

# sort list on kg/m3 ratio
spacecrafts = sorted(spacecrafts, key=lambda
                     spacecraft: spacecraft.ratio)

# remaining list
remaining_lists = []
# 105, 315, 371, 600


total_len = 0

while total_len < 85:

    # define properties of the spacecrafts
    Cygnus = Spacecraft(2000, 18.9, 7400, 390000000, 0.73)
    Progress = Spacecraft(2400, 7.6, 7020, 175000000, 0.74)
    Kounotori = Spacecraft(5200, 14, 10500, 420000000, 0.71)
    Dragon = Spacecraft(6000, 10, 12200, 347000000, 0.72)
    TianZhou = Spacecraft(6500, 15, 13500, 412000000, 0.75)
    Verne_ATV = Spacecraft(7500, 48, 20500, 1080000000, 0.72)

    Cygnus.cargo_list = []
    Progress.cargo_list = []
    Kounotori.cargo_list = []
    Dragon.cargo_list = []
    # create a list containing all the spaceships
    spacecrafts = [Cygnus, Dragon, Kounotori, Progress]

    # sort list on kg/m3 ratio
    spacecrafts = sorted(spacecrafts, key=lambda
                         spacecraft: spacecraft.ratio)
    for parcel in cargo1_list:
        if parcel["kg/m3"] < 200:
            spacecrafts[0].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
        elif (300 < parcel["kg/m3"]) and (parcel["kg/m3"] < 330):
            spacecrafts[1].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
        elif (350 < parcel["kg/m3"]) and (parcel["kg/m3"] < 400):
            spacecrafts[2].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
        elif 490 < parcel["kg/m3"]:
            spacecrafts[3].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
        else:
            remaining_lists.append(parcel)
    remaining_list = remaining_lists
    counter = 0
    while(counter < 120):
        counter += 1
        parcel = random.choice(remaining_list)
        spacecraft = random.choice(spacecrafts)
        if (parcel["mass"] <= spacecraft.remaining_mass) and (parcel["volume"] <= spacecraft.remaining_volume):
            spacecraft.add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
        else:
            continue
        total_len = 0
        for thespacecraft in spacecrafts:
            total_len += len(thespacecraft.cargo_list)
        if total_len > 82:
            print("length:", total_len)
            for thespacecraft in spacecrafts:
                print(thespacecraft.cargo_list)