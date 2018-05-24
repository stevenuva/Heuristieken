import copy
import csv
import json
import math
import random
import os
import matplotlib.pyplot as plt
from helper import load_csv_cargolist, swap_list_spacecraft, preload_spacecrafts, sort_and_slice
from Spacecraft_Classes import Spacecraft

# load the first cargo list
cargo1_list = load_csv_cargolist("CargoList1")

# slice list and sort it on kg/m3 ratio
combined_list = sort_and_slice(cargo1_list, 83)
cargo1_list = combined_list[0][:]
remaining_list = combined_list[1][:]

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

# experiment: start hill climber with some cargo already pre-loaded
preload_spacecrafts(cargo1_list, spacecrafts, remaining_list)

# organize data with list
# make copy of list also for the hill climber
spacecrafts.append(remaining_list)
copy_spacecrafts = spacecrafts[:]

# counter variables
number_found = 0
previous_cost = 0
previous_len = 0
total_len = 0

""""
HILLCLIMBER
"""
total_len_list = []
counter_list = []
counter = 0

while total_len < 81:  # total_len < 90:
    counter += 1
    counter_list.append(counter)
    #  boolean which can turn true if the hill climber wants it to
    accept = False
    cheaper = False
    longer = False

    # copy all list incase hill climber wants to go back
    alt_Cygnus = copy.deepcopy(Cygnus.cargo_list)
    alt_Dragon = copy.deepcopy(Dragon.cargo_list)
    alt_Kounotori = copy.deepcopy(Kounotori.cargo_list)
    alt_Progress = copy.deepcopy(Progress.cargo_list)

    # choose random object
    random_object = random.choice(copy_spacecrafts)
    random_object2 = random.choice(copy_spacecrafts)

    # check if random object is not selected twice
    if random_object != random_object2:

        # if random object is a list, it is the list containing the remaining parcels
        # loop to load these remaining parcels into a random spacecraft
        if type(random_object) == list:
            swap_list_spacecraft(random_object, random_object2)

        elif type(random_object2) == list:
            if random_object == Cygnus:
                parcel2 = random.choice(random_object2)

                if (parcel2["mass"] < random_object.remaining_mass) and (parcel2["volume"] < random_object.remaining_volume):
                    random_object.add_cargo(parcel2["id"], parcel2["mass"], parcel2["volume"])
                    accept = True
                    random_object2.remove(parcel2)

                else:
                    parcel1 = random.choice(random_object.cargo_list)
                    random_object.remove_cargo(parcel1["id"])

                    if (parcel2["mass"] < random_object.remaining_mass) and (parcel2["volume"] < random_object.remaining_volume):
                        random_object.add_cargo(parcel2["id"], parcel2["mass"], parcel2["volume"])
                        if random_object.remaining_mass > 0:
                            accept = True
                            random_object2.append(parcel1)
                            random_object2.remove(parcel2)

                    else:
                        random_object.add_cargo(parcel1["id"], parcel1["mass"], parcel1["volume"])
            else:
                parcel2 = random.choice(random_object2)

                if (parcel2["mass"] < random_object.remaining_mass) and (parcel2["volume"] < random_object.remaining_volume):
                    random_object.add_cargo(parcel2["id"], parcel2["mass"], parcel2["volume"])
                    accept = True
                    random_object2.remove(parcel2)

                else:
                    parcel1 = random.choice(random_object.cargo_list)
                    random_object.remove_cargo(parcel1["id"])

                    if (parcel2["mass"] < random_object.remaining_mass) and (parcel2["volume"] < random_object.remaining_volume):
                        random_object.add_cargo(parcel2["id"], parcel2["mass"], parcel2["volume"])
                        if random_object.remaining_volume > 0:
                            accept = True
                            random_object2.append(parcel1)
                            random_object2.remove(parcel2)

                    else:
                        random_object.add_cargo(parcel1["id"], parcel1["mass"], parcel1["volume"])

        else:
            parcel1 = random.choice(random_object.cargo_list)
            parcel2 = random.choice(random_object2.cargo_list)

            if (parcel2["mass"] < random_object.remaining_mass) and (parcel2["volume"] < random_object.remaining_volume):
                random_object.add_cargo(parcel2["id"], parcel2["mass"], parcel2["volume"])
                random_object2.remove_cargo(parcel2["id"])
                if random_object.remaining_volume > 0:
                    accept = True
                else:
                    accept = False

            if (parcel1["mass"] < random_object2.remaining_mass) and (parcel1["volume"] < random_object2.remaining_volume):
                random_object2.add_cargo(parcel1["id"], parcel1["mass"], parcel1["volume"])
                random_object.remove_cargo(parcel1["id"])
                if random_object2.remaining_volume > 0:
                    accept = True
                else:
                    accept = False

    # double-check total length cargo float and remaining weight and volume
    total_len = 0
    list_of_cargo_dict = []
    total_cost = 0
    for thespacecraft in spacecrafts:
        if type(thespacecraft) == list:
            continue
        # print(thespacecraft.remaining_volume)
        total_cost += thespacecraft.cost()
        total_len += len(thespacecraft.cargo_list)
        if (thespacecraft.remaining_volume < 0):
            accept = False
        if (thespacecraft.remaining_mass < 0):
            accept = False
        if thespacecraft.filled_volume > thespacecraft.volume:
            accept = False
        list_of_cargo_dict.append(thespacecraft.cargo_list)

    # if new situation is better accept new situation
    if (accept == True) and ((total_len >= previous_len) or (total_cost < previous_cost)):
        previous_len = total_len
        cheaper = True
        if type(random_object) != list:
            random_object.cargo_list = random_object.cargo_list
        if type(random_object2) != list:
            random_object2.cargo_list = random_object2.cargo_list
    else:
        accept == False

    # if new situation is not better return to old situation
    if (accept == False) or (total_len < previous_len):
        Cygnus.cargo_list = alt_Cygnus
        Dragon.cargo_list = alt_Dragon
        Kounotori.cargo_list = alt_Kounotori
        Progress.cargo_list = alt_Progress

    print("Length filled + unfilled: ", len(Cygnus.cargo_list) + len(Dragon.cargo_list) + len(Kounotori.cargo_list) + len(Progress.cargo_list) + len(remaining_list))
    print("Parecels filled: ", total_len)
    print("Parecels cost: ", total_cost)

    # send result to a textfile
    if (total_len > 82) and (cheaper == True):
        with open("( " + str(total_cost) + ") (" + str(number_found) + "x) (" + str(total_len) + ").txt", 'w') as output:
            number_found += 1
            json.dump(list_of_cargo_dict, output)

    # check if hill climber accepts the change
    print(accept)
    print("---------------------------")
    total_len_list.append(total_len)


plt.plot(counter_list, total_len_list)

plt.show()
