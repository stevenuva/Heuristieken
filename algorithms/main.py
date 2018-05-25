"""
Minor programmeren
Heuristiek

Group: Tiangong 2

Main.py

Welcome to our main python file
Main will ask the user which question will be answered
The function used to answer the questions can be found elsewhere

"""


import helper as hlp
import matplotlib.pyplot as plt
from greedy import pre_load_greedy, greedy_filling
from greedy_political import greedy_political
from greedy_no_constraints import greedy_no_constraints
from hill_climber import hill_climber
from random_greedy import random_greedy
from Spacecraft_Classes import Spacecraft

# ask which question needs to be answered
question = "a"  # input("What question do you want to see? (a, b, c, d, e)")

# ask for algorithm to be used for question a, b and c
if question in ["a", "b", "c"]:
    algorithm = "hill climber"  # input("Which algorithm (greedy, random greedy, hill climber)")

# boundaries needed for pre loading cargolists
boundaries_cargo1 = [100, 15, 19, 250]
boundaries_cargo2 = [130, 20, 45, 150]

if question == "a" or question == "b":
    algorithm = "random greedy"

    # answer a and b with greedy algorithm
    if algorithm == "greedy":
        prepared_list = pre_load_greedy("CargoList1", 83, 0)

        # define the properties of the spacecraft
        # the list of spacecrafts is sorted on kg/m3 ratio
        spacecrafts = hlp.define_spacecrafts()
        hlp.greedy_filling(prepared_list, spacecrafts)
        greedy_results = hlp.results(spacecrafts)
        print("Result Greedy, question A:", greedy_results["length"])
        print("Result Greedy, question B:", greedy_results["cost"])

    # highest length found with the random greedy was 83
    # lowest cost found with 83 with the random greedy was 1985465920 dollar
    if algorithm == "random greedy":
        result_rnd_greedy_1 = random_greedy("CargoList1", 83, 0, 1000, boundaries_cargo1)
        print("Result random greedy question A:", result_rnd_greedy_1["length"])
        print("Result random greedy question B:", result_rnd_greedy_1["cost"])

    # highest length found with the hill climber was 83
    # lowest cost found with 83 with the hill climber was 1980951280 dollar
    if algorithm == "hill climber":
        result_hc_1 = hill_climber("CargoList1", 83, boundaries_cargo1, 1000)
        print("Result hill climber question A:", result_hc_1["length"])
        print("Result hill climber question B:", result_hc_1["cost"])

        # visualize hill climber
        plt.show()


if question == "c":
    if algorithm == "greedy":
        prepared_list = pre_load_greedy("CargoList2", 75, 70)

        # define the properties of the spacecraft
        # the list of spacecrafts is sorted on kg/m3 ratio
        spacecrafts = hlp.define_spacecrafts()
        hlp.greedy_filling(prepared_list, spacecrafts)
        greedy_result_2 = hlp.results(spacecrafts)
        print("Result random greedy question C: Lengt is", greedy_result_2["length"],
              "and with a cost of", greedy_result_2["cost"])

    if algorithm == "random greedy":
        # highest length found with the random greedy was 72
        # lowest cost found with 72 with the random greedy was 2001731335 dollar
        result_rnd_greedy_2 = random_greedy("CargoList2", 96, 93, 1000, boundaries_cargo2)
        print("Result random greedy question C: Lengt is", result_rnd_greedy_2["length"],
              "and with a cost of", result_rnd_greedy_2["cost"])

    if algorithm == "hill climber":
        # highest length found with the hill climber was 71
        # lowest cost found with 71 with the hill climber was 1990903555 dollar
        result_hc_2 = hill_climber("CargoList2", 96, boundaries_cargo2, 100)
        print("Result random greedy question C: Lengt is", result_hc_2["length"],
              "and with a cost of", result_hc_2["cost"])

        # visualize hill climber
        plt.show()

if question == "d":
    # uses a greedy algorithm to answer question D
    # lowest used fleets is 12 and lowest amount of spaceships is 58
    # cheapest cost is 41596680920 dollar
    greedy_political("CargoList3")

if question == "e":
    # lowest cost with 37581140235 spaceships was
    # only the Kounotori will be taken into space
    # experiments have shown that this is the cheapest option we can find
    print("Ship used = Kounotori")
    greedy_no_constraints("CargoList3")
