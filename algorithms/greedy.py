import csv
import helper as hlp
from Spacecraft_Classes import Spacecraft


def pre_load_greedy(cargo_list_csv, volume, mass):
    """
    Loads and slice a cargolist which is retrieved from a csv
    Returns a optimalized list for the greedy algorithm
     """
    cargo_list = hlp.load_csv_cargolist(str(cargo_list_csv))

    combined_list = hlp.sort_and_slice(cargo_list, volume, mass)

    prepared_list = combined_list[0][:]

    return prepared_list


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
