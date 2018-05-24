import math
import random
import json
from Spacecraft_Classes import Spacecraft
from helper import load_csv_cargolist, sort_and_slice, results, greedy_filling, define_spacecrafts, preload_spacecrafts, hill_climber

from timeit import default_timer as timer
import time

start = timer()
timeout = 500000
counterTime = 0
totalTime = 0

timeout_start = time.time()

cargo1_list = load_csv_cargolist("CargoList2")

combined_list = sort_and_slice(cargo1_list, 96, 93)

cargo1_list = combined_list[0][:]
remain1 = combined_list[1]

# variables

count = 0
repeat = 0


while repeat < 1:
    # while count < 1:
    findings = 0
    # while time.time() < timeout_start + timeout and findings < 100:
    while findings < 100:

        remaining_list = []

        # count += 1

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

        # preload spacecrafts
        boundaries = [130, 20, 45, 150]
        preload_spacecrafts(cargo1_list, spacecrafts, remaining_list, boundaries)

        # remaining lists
        remaining_lists = remaining_list[:] + remain1

        counter = 0

        while(counter < 300):

            # variables
            counter += 1
            total_cost = 0
            total_len = 0
            previous_len = 0
            previous_cost = 0

            parcel = random.choice(remaining_lists)
            spacecraft = random.choice(spacecrafts)

            if (parcel["mass"] <= spacecraft.remaining_mass) and (parcel["volume"] <= spacecraft.remaining_volume):
                spacecraft.add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
                remaining_lists.remove(parcel)
            else:
                continue

        for thespacecraft in spacecrafts:
            total_len += len(thespacecraft.cargo_list)
            total_cost += thespacecraft.cost()

        if previous_len < total_len or total_cost < previous_cost:
            current_spacecrafts = spacecrafts
            previous_cost = total_cost

        if total_len > previous_len:
            previous_len = total_len


        random_greedy_results = results(spacecrafts)

        findings += 1
        print(findings)
    end = timer()
    time = end - start
    totalTime += time
    repeat += 1

averageTime = totalTime/repeat

# print("Total runtime: ", totalTime, "sec")
print("A) Number of parcel we can take with us with the randomgreedy algorithm:", str(random_greedy_results["length"]) + " parcels")
print("B) Minimal total cost (accounted for different FTW) : $" + str(random_greedy_results["cost"]))
print("Average runtime: ", averageTime, "sec")
