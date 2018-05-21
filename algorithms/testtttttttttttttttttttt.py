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


# print(len(spacecrafts[0].cargo_list))
# print(spacecrafts[0].remaining_mass)
# print(spacecrafts[0].remaining_volume)


while (len(spacecrafts[0].cargo_list)) > 18:
  # remaining list
  remaining_list = []
  Cygnus.cargo_list = []

  Cygnus = Spacecraft(2000, 18.9, 7400, 390000000, 0.73)

  for parcel in cargo1_list:
    if (parcel["mass"] <= spacecrafts[0].remaining_mass) and (parcel["volume"] <= spacecrafts[0].remaining_volume):
      spacecrafts[0].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
    else:
      remaining_list.append(parcel)

  parcel = random.choice(spacecrafts[0].cargo_list)
  alternative = random.choice(remaining_list)
  remaining_list.remove(alternative)
  spacecrafts[0].remove_cargo(parcel["id"])
  parcel2 = random.choice(spacecrafts[0].cargo_list)
  alternative2 = random.choice(remaining_list)
  if (alternative["mass"] <= spacecrafts[0].remaining_mass) and (alternative["volume"] <= spacecrafts[0].remaining_volume):
    spacecrafts[0].add_cargo(alternative["id"], alternative["mass"], alternative["volume"])
  if (alternative["mass"] <= spacecrafts[0].remaining_mass) and (alternative["volume"] <= spacecrafts[0].remaining_volume):
    spacecrafts[0].add_cargo(alternative2["id"], alternative2["mass"], alternative2["volume"])
  remaining_list.append(parcel)
  remaining_list.append(parcelw)
  for parcel in remaining_list:
    if (parcel["mass"] <= spacecrafts[0].remaining_mass) and (parcel["volume"] <= spacecrafts[0].remaining_volume):
      spacecrafts[0].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])

  print(len(spacecrafts[0].cargo_list))
  print(spacecrafts[0].remaining_mass)
  print(spacecrafts[0].remaining_volume)

  if len(spacecrafts[0].cargo_list) > 18:
    print(spacecrafts[0].cargo_list)
