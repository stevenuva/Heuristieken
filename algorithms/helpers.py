import csv
import os
import random
from Spacecraft_Classes import Spacecraft


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


def remaingingCargo(cargoList, cargo1_list):
    if cargoList == "CargoList1":
        remaining_list = cargo1_list[83:]
    elif cargoList == "CargoList2":
        remaining_list = cargo1_list[71:]
    elif cargoList == "CargoList3":
        remaining_list = cargo1_list[83:]

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
