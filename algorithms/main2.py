import csv
import math
import os
import random
from Spacecraft_Classes import Spacecraft
from helpers import getCargoList, remaingingCargo

# choose the cargolist you want in String Format
CargoList = "CargoList1"

# get the cargolist
cargo1_list = getCargoList(CargoList)

# get the remaining list
remaining_list = remaingingCargo(CargoList, cargo1_list)


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
remaining_list = []

for parcel in cargo1_list:
  if (parcel["mass"] <= spacecrafts[0].remaining_mass) and (parcel["volume"] <= spacecrafts[0].remaining_volume):
    spacecrafts[0].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
  elif (parcel["mass"] <= spacecrafts[1].remaining_mass) and (parcel["volume"] <= spacecrafts[1].remaining_volume):
    spacecrafts[1].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
  elif (parcel["mass"] <= spacecrafts[2].remaining_mass) and (parcel["volume"] <= spacecrafts[2].remaining_volume):
    spacecrafts[2].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
  elif (parcel["mass"] <= spacecrafts[3].remaining_mass) and (parcel["volume"] <= spacecrafts[3].remaining_volume):
    spacecrafts[3].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
  else:
    remaining_list.append(parcel)

# check how many parcels are taken with
counter = 0
total_cost = 0
for spacecraft in spacecrafts:
  counter += len(spacecraft.cargo_list)
  total_cost += (spacecraft.cost())
print("Results:")
print("A) Number of parcel we can take with us with the greedy algorithm:", counter, "parcels")
print("B) Minimal total cost when taking 83 parcels to space (accounted for different FTW) : $" + str(total_cost))

print(len(Cygnus.cargo_list))
print(len(Progress.cargo_list))
print(len(Kounotori.cargo_list))
print(len(Dragon.cargo_list))
