import csv
import os
import random
from Spacecraft_Classes import Spacecraft


def load_csv_cargolist(cargolist):
    """Function to load a csv containing the cargolist"""

    # github link to retrieve CargoList1.csv if necessary
    github_link = ("https://github.com/stevenuva/minor-programmeren/blob/"
                   "master/" + str(cargolist) + ".csv")

    # path to the csv_file
    csv_file = "./data/" + str(cargolist) + ".csv"

    # notify user when csv is either missing or misplaced
    for path in [csv_file]:
        assert os.path.exists(path), (f"{path} does not exist. Please download",
                                      f" from {github_link}")

    # load csv file into a list
    with open(csv_file, "r") as infile:
        reader = csv.reader(infile)
        csv_list = list(reader)

    # create an empty list
    cargo_list = []

    # loop through store every csv row into a dictionary
    # calculate the kg/m3 ratio
    # append every dictionary to a list
    for row in csv_list[1:]:
        cargo_dic = {"id": row[0], "mass": float(row[1]), "volume":
                     float(row[2])}
        cargo_dic["kg/m3"] = cargo_dic["mass"] / cargo_dic["volume"]
        cargo_list.append(cargo_dic)

    # sort the list of dictionaries on volume
    cargo_list = sorted(cargo_list, key=lambda
                        parcel: parcel["volume"])

    return cargo_list


def sort_and_slice(cargolist, number, mass = 0):
    """Function to sort list on kg/m3 and slice a list given a number"""

    remaining_list = cargolist[int(number):]

    cargolist = sorted(cargolist[:int(number)], key=lambda
                       parcel: parcel["kg/m3"])

    if mass > 0:
        # sort list on kg/m3 ratio
        cargolist = sorted(cargolist, key=lambda
                            parcel: parcel["mass"])

        cargolist = sorted(cargolist[:int(mass)], key=lambda
                           parcel: parcel["kg/m3"])

        remaining_list = remaining_list + cargolist[int(mass):]
    # put lists together
    combined_list = [cargolist, remaining_list]

    return combined_list


def greedy_filling(cargolists, spacecrafts):
    """
    Function to fill spaceships
    Takes a cargolist and a list with spacecraft to funtion
    List with spacecraft has already have to been sorted on kg/m3
    """

    # loop wich tries to place all the parecels out of the cargo list
    for parcel in cargolists:
        x = 0

        # loop to all the spaceships
        while (x < len(spacecrafts)):

            # check if parcel can be placed in spacecraft x
            if ((parcel["mass"] < spacecrafts[x].remaining_mass) and
                    (parcel["volume"] < spacecrafts[x].remaining_volume)):

                # place parcel and end loop
                spacecrafts[x].add_cargo(parcel["id"], parcel["mass"],
                                         parcel["volume"])
                break

            x += 1


def results(spacecrafts):
    """Calculate the total cost and length of a list of spacecrafts"""
    list_cargo_dicts = []
    results = {}
    total_len = 0
    total_cost = 0
    for spacecraft in spacecrafts:
        if type(spacecraft) != list:
            total_len += len(spacecraft.cargo_list)
            total_cost += (spacecraft.cost())
            list_cargo_dicts.append(spacecraft.cargo_list)
    results = {"length": (total_len), "cost": (total_cost), "total_filled": (list_cargo_dicts)}
    return results


def define_spacecrafts():
    """
    Define the properties of the spacecrafts
    Sorts list of spacecraft on kg/m3 ratio
    Returns a sorted list of spacecrafts
    """

    # define properties of the spacecrafts
    Cygnus = Spacecraft(2000, 18.9, 7400, 390000000, 0.73)
    Progress = Spacecraft(2400, 7.6, 7020, 175000000, 0.74)
    Kounotori = Spacecraft(5200, 14, 10500, 420000000, 0.71)
    Dragon = Spacecraft(6000, 10, 12200, 347000000, 0.72)
    # TianZhou = Spacecraft(6500, 15, 13500, 412000000, 0.75)
    # Verne_ATV = Spacecraft(7500, 48, 20500, 1080000000, 0.72)

    # create a list containing all the spaceships
    spacecrafts = [Cygnus, Dragon, Kounotori, Progress]

    # sort list on kg/m3 ratio
    spacecrafts = sorted(spacecrafts, key=lambda
                         spacecraft: spacecraft.ratio)

    return spacecrafts


def preload_spacecrafts(cargolist, spacecrafts, remaining_list, boundaries=[75, 15, 19, 100]):
    """
    Initial load before start of an algorithm
    Hardcoded values found with experimenting
    """
    for parcel in cargolist:
        if parcel["kg/m3"] < (spacecrafts[0].ratio + boundaries[0]):
            spacecrafts[0].add_cargo(parcel["id"], parcel["mass"],
                                     parcel["volume"])

        elif (spacecrafts[1].ratio - boundaries[1] < parcel["kg/m3"] and parcel["kg/m3"]
              < spacecrafts[1].ratio + boundaries[1]):
            spacecrafts[1].add_cargo(parcel["id"], parcel["mass"],
                                     parcel["volume"])

        elif (spacecrafts[2].ratio - boundaries[2] < parcel["kg/m3"] and parcel["kg/m3"]
              < spacecrafts[2].ratio + boundaries[2]):
            spacecrafts[2].add_cargo(parcel["id"], parcel["mass"],
                                     parcel["volume"])

        elif (spacecrafts[3].ratio - boundaries[3] < parcel["kg/m3"]):
            spacecrafts[3].add_cargo(parcel["id"], parcel["mass"],
                                     parcel["volume"])

        else:
            remaining_list.append(parcel)


def hill_climber(complete_list):
    """
    Hillclimber wich needs a list containing the follow list:
    - list of each (pre-loaded) spacecraft
    - list of unloaded parcels
    """
    # counter variables
    number_found = 0
    previous_cost = 0
    previous_len = 0
    total_len = 0


def swap_list_spacecraft(list, random_object2):
    """
    Function to swap parcels between a list and a spacecraft
    """
    accept = False

    # select random package from the list
    parcel1 = random.choice(list)

    # add package to the spacecraft is possible and change boolean to True to accept the change
    if (parcel1["mass"] < random_object2.remaining_mass) and (parcel1["volume"] < random_object2.remaining_volume):
        random_object2.add_cargo(parcel1["id"], parcel1["mass"], parcel1["volume"])
        accept = True
        list.remove(parcel1)

    # swap unloaded parcel with a loaded parcel if possible
    else:
        parcel2 = random.choice(random_object2.cargo_list)
        random_object2.remove_cargo(parcel2["id"])

        # if situation acceptable, accept the new situation
        if (parcel1["mass"] < random_object2.remaining_mass) and (parcel1["volume"] < random_object2.remaining_volume):
            random_object2.add_cargo(parcel1["id"], parcel1["mass"], parcel1["volume"])
            if random_object2.remaining_volume > 0:
                accept = True
                list.append(parcel2)
                list.remove(parcel1)

        # else return package
        else:
            random_object2.add_cargo(parcel2["id"], parcel2["mass"], parcel2["volume"])

    return accept


def swap_between_spacecraft(random_object, random_object2):
    """
    Function to swap parcels between two spacecraft
    """
    accept = False

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

    return accept
