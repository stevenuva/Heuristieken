import csv
import math
import os
import random
import json
from Spacecraft_Classes import Spacecraft
from helpers import getCargoList
from timeit import default_timer as timer
import time
from helpers import getCargoList, remaingingCargo, greedy, randomGreedy


start = timer()

# timeout variable can be omitted, if you use specific value in the while condition
timeout = 10  # [seconds]

timeout_start = time.time()

# choose the cargolist you want in String Format
# "CargoList1" // "CargoList2" // "CargoList3"
CargoList = "CargoList1"

# choose which algorithm you are using
# "greedy" // "random" // "hill_climber"
algorithm = "random_greedy"

cargo1_list = getCargoList(CargoList, algorithm)

cargo1_list = cargo1_list[:96]
remain1 = cargo1_list[96:]

cargo1_list = sorted(cargo1_list, key=lambda
                     parcel: parcel["mass"])

cargo1_list = cargo1_list[:93]
remain2 = cargo1_list[93:]

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

list_of_cargo_dict = randomGreedy(cargo1_list, spacecrafts, remain1, remain2)

# check how many parcels are taken with
counter = 0
total_cost = 0
for spacecraft in spacecrafts:
  counter += len(spacecraft.cargo_list)
  total_cost += (spacecraft.cost())


print("Results:")
print("A) Number of parcel we can take with us with the greedy algorithm:", counter, "parcels")
print("B) Minimal total cost when taking 83 parcels to space (accounted for different FTW) : $" + str(total_cost))

end = timer()

print("Total runtime: ", end - start)
