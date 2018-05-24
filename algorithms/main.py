import matplotlib.pyplot as plt
import helper as hlp
from Spacecraft_Classes import Spacecraft
from hill_climber import hill_climber
from random_greedy import random_greedy

# question = input("What question do you want to see?")
# print(question)

# boundaries needed for pre loading cargolists
boundaries_cargo1 = [100, 15, 19, 250]
boundaries_cargo2 = [130, 20, 45, 150]

# highest length found with the random greedy was 72
# lowest cost found with 72 with the random greedy was 2001731335 dollar
print("random_greedy")
result_rnd_greedy_1 = random_greedy("CargoList1", 83, 0, 1000, boundaries_cargo1)
result_rnd_greedy_2 = random_greedy("CargoList2", 96, 93, 1000, boundaries_cargo2)
print(result_rnd_greedy_1)
print(result_rnd_greedy_2)

#### QUESTIONS A, B, C #################################

# load the first cargo list
cargo1_list = hlp.load_csv_cargolist("CargoList1")

# slice list and sort it on kg/m3 ratio
combined_list = hlp.sort_and_slice(cargo1_list, 83)
cargo1_list = combined_list[0][:]
remaining_list = combined_list[1][:]

# define the properties of the spacecraft
# the list of spacecrafts is sorted on kg/m3 ratio
spacecrafts = hlp.define_spacecrafts()

# fill spacecraft with parcels from the first cargo list
hlp.greedy_filling(cargo1_list, spacecrafts)

# check how many parcels are taken with
greedy_results = hlp.results(spacecrafts)

print("Results A and B with a Greedy Algorithm:")
print("A) Number of parcel we can take with us with the greedy algorithm:", str(greedy_results["length"]) + " parcels")
print("B) Minimal total cost when taking 83 parcels to space (accounted for different FTW) : $" + str(greedy_results["cost"]))

# returns result of running a hill climber 1000 times
result_hc_1 = hill_climber("CargoList1", 83, boundaries_cargo1, 1000)
result_hc_2 = hill_climber("CargoList2", 96, boundaries_cargo2, 1000)
# plt.show(block=False)

# highest length found with the hill climber was 83
# lowest cost found with 83 with the hill climber was 1980951280 dollar
print("QUESTION A: Length =", result_hc_1["length"])
print("QUESTION B: Length =", result_hc_1["length"], "and Cost =", result_hc_1["cost"])
print("QUESTION C: Length =", result_hc_2["length"], "and Cost =", result_hc_2["cost"])

#### QUESTIONS D, E #################################
