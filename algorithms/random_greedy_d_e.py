import csv
import helper as hlp
import json
import math
import os
import random
from Spacecraft_Classes import Spacecraft

cargo_list = hlp.load_csv_cargolist("Cargolist3")

returned_list = hlp.sort_and_slice(cargo_list, 1250)

cargo_list = returned_list[0]

remaining_list = []
random_list = []

len_cargo_list = len(cargo_list)
floats_used = 0
total_cost = 0

# political constraint counters
counterUSA = 0
counterEurope = 0
counterRussia = 0
counterJapan = 0
counterChina = 0

while len_cargo_list > 0:
    floats_used += 1

    # parcel counter per ship
    counterProgress = 0
    counterKounotori = 0
    counterDragon = 0
    counterTianZhou = 0
    counterVerneATV = 0

    Progress = Spacecraft(2400, 7.6, 7020, 175000000, 0.74)
    Kounotori = Spacecraft(5200, 14, 10500, 420000000, 0.71)
    Dragon = Spacecraft(6000, 10, 12200, 347000000, 0.72)
    TianZhou = Spacecraft(6500, 15, 13500, 412000000, 0.75)
    Verne_ATV = Spacecraft(7500, 48, 20500, 1080000000, 0.72)

    # create a list containing all the spaceships
    spacecrafts = [Dragon, Kounotori, Progress, TianZhou, Verne_ATV]

    spacecrafts = sorted(spacecrafts, key=lambda
                         spacecraft: spacecraft.ratio)
