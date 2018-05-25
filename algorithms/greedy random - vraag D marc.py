import csv
import math
import os
import random
from Spacecraft_Classes import Spacecraft
import json
import helper as hlp


# github link to retrieve CargoList1.csv if necessary
github_link = ("https://github.com/stevenuva/minor-programmeren/blob/"
               "master/CargoList1.csv")

# path to the csv_file
csv_file = "./data/CargoList3.csv"

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

remaining_list = cargo1_list[:]

# slice list
cargo1_list = cargo1_list[:]

# sort list on kg/m3 ratio
cargo1_list = sorted(cargo1_list, key=lambda
                     parcel: parcel["kg/m3"])

# remaining list
remaining_list = []
randomList = []

# initialize counters
cargoListCounter = len(cargo1_list)
counterGoingUp = 0
finalCost = 0

# political constraint counters
counterUSA = 0
counterEurope = 0
counterRussia = 0
counterJapan = 0
counterChina = 0

# keep going up till cargo list is empty
while cargoListCounter > 0:

  # counter for while condition, when cargolist is empty stop
  counterGoingUp += 1

  # parcel counter per ship
  #counterCygnus = 0
  counterProgress = 0
  counterKounotori = 0
  counterDragon = 0
  counterTianZhou = 0
  counterVerneATV = 0

  #Cygnus = Spacecraft(2000, 18.9, 7400, 390000000, 0.73)
  Progress = Spacecraft(2400, 7.6, 7020, 175000000, 0.74)
  Kounotori = Spacecraft(5200, 14, 10500, 420000000, 0.71)
  Dragon = Spacecraft(6000, 10, 12200, 347000000, 0.72)
  TianZhou = Spacecraft(6500, 15, 13500, 412000000, 0.75)
  Verne_ATV = Spacecraft(7500, 48, 20500, 1080000000, 0.72)

  # create a list containing all the spaceships
  spacecrafts = [Dragon, Kounotori, Progress, TianZhou, Verne_ATV]

  spacecrafts = sorted(spacecrafts, key=lambda
                       spacecraft: spacecraft.ratio)

  print("Length cargo list:", len(cargo1_list))
  print("Cargo countsown counter:", cargoListCounter)

  remaining_list = []
  remaining_list2 = []
  randomList = []

  # empty spacecrafts
  for spacecraft in spacecrafts:
    spacecraft.cargo_list = []

  # greedy algorithm to fill ships
  for parcel in cargo1_list:
    if parcel["kg/m3"] < spacecrafts[0].ratio * 1.25 and \
            parcel["mass"] < spacecrafts[0].remaining_mass and parcel["volume"] < spacecrafts[0].remaining_volume:
      spacecrafts[0].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
      cargoListCounter -= 1
      counterVerneATV += 1
    elif parcel["kg/m3"] < spacecrafts[1].ratio * 1.05 and parcel["kg/m3"] > spacecrafts[1].ratio * 0.95 and \
            parcel["mass"] < spacecrafts[1].remaining_mass and parcel["volume"] < spacecrafts[1].remaining_volume:
      spacecrafts[1].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
      counterProgress += 1
      cargoListCounter -= 1
    elif parcel["kg/m3"] < spacecrafts[2].ratio * 1.1 and parcel["kg/m3"] > spacecrafts[2].ratio * 0.9 and \
            parcel["mass"] < spacecrafts[2].remaining_mass and parcel["volume"] < spacecrafts[2].remaining_volume:
      spacecrafts[2].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
      counterKounotori += 1
      cargoListCounter -= 1
    elif parcel["kg/m3"] > spacecrafts[3].ratio * 1.1 and parcel["kg/m3"] > spacecrafts[3].ratio * 0.9 and \
            parcel["mass"] < spacecrafts[3].remaining_mass and parcel["volume"] < spacecrafts[3].remaining_volume:
      spacecrafts[3].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
      counterTianZhou += 1
      cargoListCounter -= 1
    elif parcel["kg/m3"] > spacecrafts[4].ratio * 0.70 and \
            parcel["mass"] < spacecrafts[4].remaining_mass and parcel["volume"] < spacecrafts[4].remaining_volume:
      spacecrafts[4].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
      counterDragon += 1
      cargoListCounter -= 1
    else:
      remaining_list.append(parcel)

    # update list to loop through again
    cargo1_list = remaining_list[:]
  print("Lengte rem list:", len(randomList))
  randomCounter = 0

  # remaining weer legen
  #remaining_list = []
  randomParcel = 0

  # randon algorithm to fill ship up if not fully loaded
  while randomCounter < 100:
    randomCounter += 1
    # random parcel shipping
    r_parcel = random.choice(cargo1_list)
    r_spacecraft = random.choice(spacecrafts)

    if r_parcel["mass"] < r_spacecraft.remaining_mass and r_parcel["volume"] < r_spacecraft.remaining_volume:
      randomParcel += 1
      r_spacecraft.add_cargo(r_parcel["id"], r_parcel["mass"], r_parcel["volume"])
      cargoListCounter -= 1
    else:
      remaining_list.append(parcel)

    # updating cargo list
    cargo1_list = remaining_list
    print("Random parcels:", randomParcel)

    # calculating costs
    total_cost = 0
    for spacecraft in spacecrafts:
      if spacecraft.cargo_list != []:
        total_cost += (spacecraft.cost())
    finalCost += total_cost
    print("total cost fleet: $", total_cost)

    if Verne_ATV.cargo_list != []:
      counterEurope += 1
    if Kounotori.cargo_list != []:
      counterJapan += 1
    if TianZhou.cargo_list != []:
      counterChina += 1
    if Dragon.cargo_list != []:
      counterUSA += 1
    if Progress.cargo_list != []:
      counterRussia += 1

    #print("cugnus:", counterCygnus)
    print("Progress:", counterProgress)
    print("Kouno:", counterKounotori)
    print("DRAGON:", counterDragon)
    print("TianZhou:", counterTianZhou)
    print("Verne_ATV:", counterVerneATV)
    print("total parcels:", counterProgress + counterKounotori + counterDragon + counterTianZhou + counterVerneATV)

# print if costs or runs are less than first run
# if finalCost < 40229483210:
#   with open('outputfile' + str(counterGoingUp) + "(remainings randomrr" + str(finalCost) + ").txt", 'w') as output:
#     json.dump("Total final cost:", output)
#     json.dump(finalCost, output)
#     json.dump("Went up:", output)
#     json.dump(counterGoingUp, output)
#     json.dump("European flights:", output)
#     json.dump(counterEurope, output)
#     json.dump("Chinese flights", output)
#     json.dump(counterChina, output)
#     json.dump("Japanese", output)
#     json.dump(counterJapan, output)
#     json.dump("USA flights:", output)
#     json.dump(counterUSA, output)
#     json.dump("Russian:", output)
#     json.dump(counterRussia, output)
