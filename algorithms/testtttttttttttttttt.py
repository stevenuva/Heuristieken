import helper as hlp
import math
import random
import json
from Spacecraft_Classes import Spacecraft


def random_greedy(cargolist, volume_slicer, mass_slicer, number, boundaries):
    """
        Random Greedy used for questions a, b and class
        Fills the the spacecrafts patially with the best density parcels
        and after that we randomly put packages into the spacecrafts

    """

    # load the cargo list
    cargo_list = hlp.load_csv_cargolist(str(cargolist))

    # slice and sort it on kg/m3 ratio
    combined_list = hlp.sort_and_slice(cargo_list, volume_slicer, mass_slicer)
    cargo_list = combined_list[0][:]
    remain1 = combined_list[1]

    # variables
    cost = 0
    counter = 0
    max_len = 0
    total_len = 0

    # repeat 'number' times
    while counter < number:
        remaining_list = []

        counter += 1

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

        remaining_list = []
        boundaries = boundaries

        # preload the the spacecrafts
        hlp.preload_spacecrafts(cargo_list, spacecrafts, remaining_list, boundaries)

        remaining_lists = remaining_list[:] + remain1

        counter2 = 0

        # repeat the random choices
        while(counter2 < 300):

            counter2 += 1
            total_cost = 0

            # choose random parcel from remaining list and spacecrafts
            parcel = random.choice(remaining_lists)
            spacecraft = random.choice(spacecrafts)

            # check if the swap is possible
            if (parcel["mass"] <= spacecraft.remaining_mass) and (parcel["volume"] <= spacecraft.remaining_volume):
                spacecraft.add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
                remaining_lists.remove(parcel)
            else:
                continue

        # get the results dictionary
        result = hlp.results(spacecrafts)

        # unpack dictionary
        total_len = result["length"]
        total_cost = result["cost"]
        cargo_dicts = result["total_filled"]

        # only write out the best solution
        if (total_len > 70) and (max_len < total_len or total_cost < cost):

            with open("outputfile(" + str(total_len) + ') (' + str(total_cost) + ").txt", 'w') as output:
                json.dump(cargo_dicts, output)
                cost = total_cost

        if total_len > max_len:
            max_len = total_len

        # put cost and length in dictionary
        result = {"length": max_len, "cost": cost}

    return result
