import csv
import math
import os
import random
import json
from Spacecraft_Classes import Spacecraft
from helpers import getCargoList
from timeit import default_timer as timer
import time

start = timer()

# timeout variable can be omitted, if you use specific value in the while condition
timeout = 10  # [seconds]

timeout_start = time.time()

# choose the cargolist you want in String Format
# "CargoList1" // "CargoList2" // "CargoList3"
CargoList = "CargoList1"

# choose which algorithm you are using
# "greedy" // "random" // "hill_climber"
algorithm = "random"

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

total_len = 0
list_length_random = []

previous_cost = 0
previous_len = 0
counter1 = 0
counter2 = 0
counterTime = 0

total_more_limit = 0

# while counter2 < 100000:
while time.time() < timeout_start + timeout:
    remaining_list = []

    counter2 += 1

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
        if parcel["kg/m3"] < (spacecrafts[0].ratio + 100):
            spacecrafts[0].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])

        elif (spacecrafts[1].ratio - 15 < parcel["kg/m3"]) and (parcel["kg/m3"] < spacecrafts[1].ratio + 10):
            spacecrafts[1].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])


        elif ((spacecrafts[2].ratio - 19) < parcel["kg/m3"]) and (parcel["kg/m3"] < (spacecrafts[2].ratio + 19)):
            spacecrafts[2].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])

        elif ((spacecrafts[3].ratio - 250) < parcel["kg/m3"]):
            spacecrafts[3].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])

        else:
            remaining_list.append(parcel)

    remaining_lists = remaining_list[:] + remain1 + remain2

    counter = 0

    while(counter < 300):
        counter += 1
        total_cost = 0
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
        total_cost += thespacecraft.cost()

    if total_len > 82:
        list_of_cargo_dict = []

        if counterTime < 1:
            end_timefirst = timer()
            print("First 83 found in: ", end_timefirst - start)
            counterTime += 1

        counter1 += 1
        print(counter1)

        for thespacecraft in spacecrafts:
            print(list_of_cargo_dict.append(thespacecraft.cargo_list))

        if previous_len < total_len or total_cost < previous_cost:

            with open('outputfile' + str(total_more_limit) + "(" + str(total_len) + ') (' + str(total_cost) + ").txt", 'w') as output:
                json.dump(list_of_cargo_dict, output)
                total_more_limit += 1
                previous_cost = total_cost

                json.dump(Cygnus.remaining_mass, output)
                json.dump("-", output)
                json.dump(Cygnus.remaining_volume, output)
                json.dump("-", output)
                json.dump(Progress.remaining_mass, output)
                json.dump("-", output)
                json.dump(Progress.remaining_volume, output)
                json.dump("-", output)
                json.dump(Kounotori.remaining_mass, output)
                json.dump("-", output)
                json.dump(Kounotori.remaining_volume, output)
                json.dump("-", output)
                json.dump(Dragon.remaining_mass, output)
                json.dump("-", output)
                json.dump(Dragon.remaining_volume, output)

                json.dump("Cygnus_cost: " + str(Cygnus.cost()), output)
                json.dump(" - ", output)

                json.dump("Progress_cost: "+ str(Progress.cost()), output)
                json.dump(" - ", output)

                json.dump("Kounotori_cost: "+ str(Kounotori.cost()), output)
                json.dump(" - ", output)

                json.dump("Dragon_cost: "+ str(Dragon.cost()), output)
                json.dump(" - ", output)

                # json.dump("Total cost: ", str(total_cost), output)

        if total_len > previous_len:
            previous_len = total_len

end = timer()

print("Total runtime: ", end - start)
