import csv
import math
import os
import random
import json
from Spacecraft_Classes import Spacecraft

print("1")

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

cargo1_list = cargo1_list[:96]

cargo1_list = sorted(cargo1_list, key=lambda
                     parcel: parcel["mass"])

cargo1_list = cargo1_list[:93]

# sort list on kg/m3 ratio
cargo1_list = sorted(cargo1_list, key=lambda
                     parcel: parcel["kg/m3"])


total_len = 0
limit = 0
list_length_random = []

# init_remaining_list = cargo1_list[83:]

# # slice list
# cargo1_list = cargo1_list[:83]

total_more_limit = 0

while total_len < 85:
    remaining_list = []
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
        if parcel["kg/m3"] < (spacecrafts[0].ratio + 75):
            spacecrafts[0].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
        elif (spacecrafts[1].ratio - 15 < parcel["kg/m3"]) and (parcel["kg/m3"] < spacecrafts[1].ratio + 15):
            spacecrafts[1].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
        elif ((spacecrafts[2].ratio - 19) < parcel["kg/m3"]) and (parcel["kg/m3"] < (spacecrafts[2].ratio + 19)):
            spacecrafts[2].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
        elif ((spacecrafts[3].ratio - 100) < parcel["kg/m3"]):
            spacecrafts[3].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
        else:
            remaining_list.append(parcel)
    remaining_lists = remaining_list[:]
    counter = 0
    while(counter < 300):
        counter += 1
        parcel = random.choice(remaining_lists)
        spacecraft = random.choice(spacecrafts)
        if (parcel["mass"] <= spacecraft.remaining_mass) and (parcel["volume"] <= spacecraft.remaining_volume):
            spacecraft.add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
            remaining_lists.remove(parcel)
        else:
            continue
        total_len = 0
        for thespacecraft in spacecrafts:
            total_len += len(thespacecraft.cargo_list)
        if total_len > limit:
            limit = total_len
            print(limit)
        if total_len > 80:
            print("length:", total_len)
            list_of_cargo_dict = []
            for thespacecraft in spacecrafts:
                print(list_of_cargo_dict.append(thespacecraft.cargo_list))
            with open('outputfile' + str(total_more_limit) + "(" + str(total_len) + ").txt", 'w') as output:
                json.dump(list_of_cargo_dict, output)
                total_more_limit += 1
