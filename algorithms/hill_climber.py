import copy
import csv
import json
import random
import matplotlib.pyplot as plt
import helper as hlp
from Spacecraft_Classes import Spacecraft


def hill_climber(cargo_list_csv, slice, boundaries, number):
    """
        Hill climber used for questions a, b and c
        Swaps parcels between spaceships and cargolists
    """

    # load the first cargo list
    cargo1_list = hlp.load_csv_cargolist(str(cargo_list_csv))

    # slice list and sort it on kg/m3 ratio
    combined_list = hlp.sort_and_slice(cargo1_list, slice)
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
    hlp.preload_spacecrafts(cargo1_list, spacecrafts, remaining_list, boundaries)

    # organize data with list
    # make copy of list also for the hill climber
    spacecrafts.append(remaining_list)
    copy_spacecrafts = spacecrafts[:]

    # counter variables
    counter = 0
    number_found = 0
    cost = 0
    previous_len = 0
    total_len = 0

    # list needed to save data for matplotlib
    counter_list = []
    total_len_list = []

    while counter < number:  # total_len < 90:
        # counter needed for the visualization
        counter += 1
        counter_list.append(counter)
        #  boolean which can turn true if the hill climber wants it to
        accept = False

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
                accept = hlp.swap_list_spacecraft(random_object, random_object2)

            elif type(random_object2) == list:
                accept = hlp.swap_list_spacecraft(random_object2, random_object)

            else:
                accept = hlp.swap_between_spacecraft(random_object, random_object2)

        # double-check total length cargo float and remaining weight and volume
        result_dic = hlp.results(spacecrafts)
        total_len = result_dic["length"]
        total_cost = result_dic["cost"]
        total_filled = result_dic["total_filled"]

        # check if score will be accepted
        if (accept == True):
            if ((total_len > previous_len) or (total_cost < cost)):
                previous_len = total_len
                cost = total_cost
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

        # store best result in a textfile if higer than 83
        if (total_len > 83) and (cost < total_cost):
            with open("output.txt", 'w') as output:
                number_found += 1
                json.dump(total_filled, output)

        total_len_list.append(total_len)

    plt.plot(counter_list, total_len_list)
    # plt.show(block=False)
    plt.draw()

    result = {"length": total_len, "cost": cost}

    return result
