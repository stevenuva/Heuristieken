import csv
import helper as hlp
import json
import math
import os
import random
from Spacecraft_Classes import Spacecraft


def greedy_no_constraints(cargolist):

  # loading in cargolist
  cargo_list = hlp.load_csv_cargolist(str(cargolist))
  returned_list = hlp.sort_and_slice(cargo_list, 1250)
  cargo_list = returned_list[0]

  remaining_list = []

  # counters to keep track during algorithm
  len_cargo_list = len(cargo_list)
  floats_used = 0
  total_cost = 0
  final_cost = 0

  remaining_list = []

  # keep filling ship till cargo list is empty
  while len_cargo_list > 0:

    # times fleet goes up
    floats_used += 1

    # spacecrafts
    Cygnus = Spacecraft(2000, 18.9, 7400, 390000000, 0.73)
    Progress = Spacecraft(2400, 7.6, 7020, 175000000, 0.74)
    Kounotori = Spacecraft(5200, 14, 10500, 420000000, 0.71)
    Dragon = Spacecraft(6000, 10, 12200, 347000000, 0.72)
    TianZhou = Spacecraft(6500, 15, 13500, 412000000, 0.75)
    Verne_ATV = Spacecraft(7500, 48, 20500, 1080000000, 0.72)

    # for quetion E one spacecraft has to be chosen from the list of spacecrafts above
    spacecrafts = [Kounotori]

    # empty remaining list to fill again after for loop
    remaining_list = []

    # empty spacecraft
    for spacecraft in spacecrafts:
      spacecraft.cargo_list = []

    # algortihm to fill ship
    for parcel in cargo_list:
      if (parcel["mass"] <= spacecrafts[0].remaining_mass) and (parcel["volume"] <= spacecrafts[0].remaining_volume):
        spacecrafts[0].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
        len_cargo_list -= 1
      else:
        remaining_list.append(parcel)

      # update list to loop through again
      cargo_list = remaining_list

    # calculating costs
    total_cost = 0
    for spacecraft in spacecrafts:
      total_cost += (spacecraft.cost())
    final_cost += total_cost

  # results for question
  print("Amount of times ship flew up:", floats_used)
  print("Final costs after bringing all parcels: $", final_cost)
