import csv
import math
import os
import random
from Spacecraft_Classes import Spacecraft

CargoList1 = "CargoList3"

# github link to retrieve CargoList1.csv if necessary
github_link = ("https://github.com/stevenuva/minor-programmeren/blob/"
               "master/" + CargoList1 + ".csv")

# path to the csv_file
csv_file = "./data/" + CargoList1 + ".csv"

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

# remaining list
remaining_list = []

# for spacecraft in spacecrafts:
#   counter += len(spacecraft.cargo_list)
counter = 0

remaining_list = []

while len(cargo1_list) != 0:
  counter += 1

  remaining_list = []

  # define properties of the spacecrafts
  Progress = Spacecraft(2400, 7.6, 7020, 175000000, 0.74)
  Kounotori = Spacecraft(5200, 14, 10500, 420000000, 0.71)
  Dragon = Spacecraft(6000, 10, 12200, 347000000, 0.72)
  TianZhou = Spacecraft(6500, 15, 13500, 412000000, 0.75)
  Verne_ATV = Spacecraft(7500, 48, 20500, 1080000000, 0.72)

  # create a list containing all the spaceships
  spacecrafts = [TianZhou, Verne_ATV, Dragon, Kounotori, Progress]

  # sort list on kg/m3 ratio
  spacecrafts = sorted(spacecrafts, key=lambda
                       spacecraft: spacecraft.ratio)

  for thespacecraft in spacecrafts:
    thespacecraft.cargo_list = []

  for parcel in cargo1_list:
    # print("test3")
    if (parcel["mass"] <= spacecrafts[0].remaining_mass) and (parcel["volume"] <= spacecrafts[0].remaining_volume):
      spacecrafts[0].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
    elif (parcel["mass"] <= spacecrafts[1].remaining_mass) and (parcel["volume"] <= spacecrafts[1].remaining_volume):
      spacecrafts[1].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
    elif (parcel["mass"] <= spacecrafts[2].remaining_mass) and (parcel["volume"] <= spacecrafts[2].remaining_volume):
      spacecrafts[2].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
    elif (parcel["mass"] <= spacecrafts[3].remaining_mass) and (parcel["volume"] <= spacecrafts[3].remaining_volume):
      spacecrafts[3].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
    else:
      # print("else")
      remaining_list.append(parcel)

  cargo1_list = remaining_list
  print(len(cargo1_list))

print(counter)
