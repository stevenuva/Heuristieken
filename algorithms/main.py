import copy
import csv
import json
import math
import matplotlib.pyplot as plt
import os
import random
from helper import load_csv_cargolist, sort_and_slice, results, greedy_filling, define_spacecrafts, preload_spacecrafts, hill_climber
from Spacecraft_Classes import Spacecraft
from hill_v4 import hill_climber

# load the first cargo list
cargo1_list = load_csv_cargolist("CargoList1")

# slice list and sort it on kg/m3 ratio
combined_list = sort_and_slice(cargo1_list, 83)
cargo1_list = combined_list[0][:]
remaining_list = combined_list[1][:]

# define the properties of the spacecraft
# the list of spacecrafts is sorted on kg/m3 ratio
spacecrafts = define_spacecrafts()

# fill spacecraft with parcels from the first cargo list
greedy_filling(cargo1_list, spacecrafts)

# check how many parcels are taken with
greedy_results = results(spacecrafts)

print("Results A and B with a Greedy Algorithm:")
print("A) Number of parcel we can take with us with the greedy algorithm:", str(greedy_results["length"]) + " parcels")
print("B) Minimal total cost when taking 83 parcels to space (accounted for different FTW) : $" + str(greedy_results["cost"]))

# reset values for next question
spacecrafts = define_spacecrafts()
cargo1_list = combined_list[0][:]
remaining_list = combined_list[1][:]

# initial loading before hill climber
boundaries_cargo1 = [75, 15, 19, 100]
boundaries_cargo2 = [130, 20, 45, 150]

preload_spacecrafts(cargo1_list, spacecrafts, remaining_list)

# complete_list = spacecrafts + remaining_list
hill_climber("CargoList1", 83, boundaries_cargo1)
# hill_climber("CargoList2", 96, boundaries_cargo2)
