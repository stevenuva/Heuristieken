import csv
import helper as hlp
import json
import math
import os
import random
from Spacecraft_Classes import Spacecraft


def greedy_political(cargolist):
    """
    Function needed to answer question D
    Checks how many spaceships are needed to send
    a given cargolist to space
    """
    # loading in cargolist
    cargo_list = hlp.load_csv_cargolist(str(cargolist))
    prepared_list = hlp.sort_and_slice(cargo_list, 1250)
    cargo_list = prepared_list[0]

    remaining_list = []

    # counters to keep track during algorithm
    len_cargo_list = len(cargo_list)
    floats_used = 0
    total_cost = 0
    final_cost = 0

    # counters to keep track of political constraint
    counterUSA = 0
    counterEurope = 0
    counterRussia = 0
    counterJapan = 0
    counterChina = 0

    # loop to completely empty the cargolist
    while len_cargo_list > 0:

        # keep track of times we go up
        floats_used += 1

        # parcel counter per ship
        counterProgress = 0
        counterKounotori = 0
        counterDragon = 0
        counterTianZhou = 0
        counterVerneATV = 0

        # spacecrafts
        Progress = Spacecraft(2400, 7.6, 7020, 175000000, 0.74)
        Kounotori = Spacecraft(5200, 14, 10500, 420000000, 0.71)
        Dragon = Spacecraft(6000, 10, 12200, 347000000, 0.72)
        TianZhou = Spacecraft(6500, 15, 13500, 412000000, 0.75)
        Verne_ATV = Spacecraft(7500, 48, 20500, 1080000000, 0.72)

        # create a list containing all the spaceships
        spacecrafts = [Dragon, Kounotori, Progress, TianZhou, Verne_ATV]

        # sorting spacecrafts on density
        spacecrafts = sorted(spacecrafts, key=lambda
                             spacecraft: spacecraft.ratio)

        # empty remaining list to be filled again in greedy algorithm
        remaining_list = []

        # empty spacecrafts
        for spacecraft in spacecrafts:
            spacecraft.cargo_list = []

        # greedy algorithm to fill ships
        for parcel in cargo_list:
            if (parcel["mass"] < spacecrafts[0].remaining_mass) and (parcel["volume"] < spacecrafts[0].remaining_volume):
                spacecrafts[0].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
                len_cargo_list -= 1
                counterVerneATV += 1
            elif(parcel["mass"] < spacecrafts[1].remaining_mass) and (parcel["volume"] < spacecrafts[1].remaining_volume):
                spacecrafts[1].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
                counterProgress += 1
                len_cargo_list -= 1
            elif (parcel["mass"] < spacecrafts[2].remaining_mass) and (parcel["volume"] < spacecrafts[2].remaining_volume):
                spacecrafts[2].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
                counterKounotori += 1
                len_cargo_list -= 1
            elif (parcel["mass"] < spacecrafts[3].remaining_mass) and (parcel["volume"] < spacecrafts[3].remaining_volume):
                spacecrafts[3].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
                counterTianZhou += 1
                len_cargo_list -= 1
            elif (parcel["mass"] < spacecrafts[4].remaining_mass) and (parcel["volume"] < spacecrafts[4].remaining_volume):
                spacecrafts[4].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
                counterDragon += 1
                len_cargo_list -= 1
            else:
                remaining_list.append(parcel)

            # update list to loop through again
            cargo_list = remaining_list

        # calculating costs
        total_cost = 0
        for spacecraft in spacecrafts:
            if spacecraft.cargo_list != []:
                total_cost += (spacecraft.cost())
        final_cost += total_cost

        # if ship is used count up for political constraint
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

    # printing results
    print("Amount of times gone into space with a fleet:", floats_used)
    print("Final costs after bringing all parcels: $", final_cost)
    print("Amount European flights:", counterEurope)
    print("Amount Chinese flights:", counterChina)
    print("Amount Japanese flights:", counterJapan)
    print("Amount USA flights:", counterUSA)
    print("Amount Russian flights:", counterRussia)
