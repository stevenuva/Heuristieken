import csv
import os
import random
from Spacecraft_Classes import Spacecraft
from timeit import default_timer as timer
import time
import json

def getCargoList(cargoList, algorithm):

    # github link to retrieve CargoList1.csv if necessary
    github_link = ("https://github.com/stevenuva/minor-programmeren/blob/"
                 "master/" + cargoList + ".csv")

    # path to the csv_file
    csv_file = "./data/" + cargoList + ".csv"

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

    # check for which algoritm
    if algorithm == "random_greedy":
        return cargo1_list

    if algorithm == "greedy":
        if cargoList == "CargoList1":

            # slice list
            cargo1_list = cargo1_list[:83]

            # sort list on kg/m3 ratio
            cargo1_list = sorted(cargo1_list, key=lambda
                                 parcel: parcel["kg/m3"])

        elif cargoList == "CargoList2":

            cargo1_list = cargo1_list[:71]
            cargo1_list = sorted(cargo1_list, key=lambda
                                 parcel: parcel["kg/m3"])

        elif cargoList == "CargoList3":

            cargo1_list = cargo1_list[:83]
            cargo1_list = sorted(cargo1_list, key=lambda
                                 parcel: parcel["kg/m3"])

        return cargo1_list

def sliceList(cargoList, cargo1_list, slice):

    remaining_list = cargo1_list[slice:]

    return remaining_list

def greedy(cargo1_list, remaining_list, spacecrafts):

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

    return Spacecraft

# def preload()

def randomGreedy(cargo1_list, spacecrafts, remain1, remain2):

    start = timer()

    # timeout variable can be omitted, if you use specific value in the while condition
    timeout = 10  # [seconds]

    timeout_start = time.time()

    # variables
    total_len = 0
    list_length_random = []
    previous_cost = 0
    previous_len = 0
    counter1 = 0
    counter2 = 0
    counterTime = 0

    total_more_limit = 0

    while time.time() < timeout_start + timeout:

        remaining_list = []
        counter2 += 1

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
                list_of_cargo_dict.append(thespacecraft.cargo_list)

            if previous_len < total_len or total_cost < previous_cost:

                with open('outputfile' + str(total_more_limit) + "(" + str(total_len) + ') (' + str(total_cost) + ").txt", 'w') as output:
                    json.dump(list_of_cargo_dict, output)
                    total_more_limit += 1
                    previous_cost = total_cost

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

    return list_of_cargo_dict
