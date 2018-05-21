import csv
import os
import random
from Spacecraft_Classes import Spacecraft

# github link to retrieve CargoList1.csv if necessary
github_link = ("https://github.com/stevenuva/minor-programmeren/blob/"
               "master/CargoList1.csv")

# path to the csv_file
csv_file = "../data/CargoList1.csv"

# check if user has csv at the right path
for path in [csv_file]:
    assert os.path.exists(path), (f"{path} does not exist. Please download file"
                                  f" from {github_link}")

# load csv file into a list
with open(csv_file, "r") as infile:
    reader = csv.reader(infile)
    csv_list = list(reader)

# create an empty list
cargo1_list = []

# loop through store every csv row into a dictionary
# calculate the kg/m3 ratio
# append every dictionary to a list
for row in csv_list[1:]:
    cargo1_dic = {"id": row[0], "mass": float(row[1]), "volume": float(row[2])}
    cargo1_dic["kg/m3"] = cargo1_dic["mass"] / cargo1_dic["volume"]
    cargo1_list.append(cargo1_dic)

# sort list on volume
cargo1_list = sorted(cargo1_list, key=lambda
                     parcel: parcel["volume"])

# slice list
cargo1_list = cargo1_list[:100]

# of
# cargo1_list = cargo1_list[:71]


# sort list on kg/m3 ratio
cargo1_list = sorted(cargo1_list, key=lambda
                     parcel: parcel["kg/m3"])

# define properties spacecrafts
Cygnus = Spacecraft(2000, 18.9, 7400, 390000000, 0.73)
Progress = Spacecraft(2400, 7.6, 7020, 175, 0.74)
Kounotori = Spacecraft(5200, 14, 10500, 420, 0.71)
Dragon = Spacecraft(6000, 10, 12200, 347, 0.72)
TianZhou = Spacecraft(6500, 15, 13500, 412, 0.75)
Verne_ATV = Spacecraft(7500, 48, 20500, 1080, 0.72)


# create a list containing all the dictionary spaceships
spacecrafts = [Cygnus, Dragon, Kounotori, Progress]

# sort list on kg/m3 ratio
spacecrafts = sorted(spacecrafts, key=lambda
                     spacecraft: spacecraft.ratio)

# remaining list
remaining_list = []

for parcel in cargo1_list:
    if (parcel["mass"] <= spacecrafts[0].remaining_mass) and (parcel["volume"] <= spacecrafts[0].remaining_volume):
        spacecrafts[0].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
    elif (parcel["mass"] <= spacecrafts[1].remaining_mass) and (parcel["volume"] <= spacecrafts[1].remaining_volume):
        spacecrafts[1].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
    elif (parcel["mass"] <= spacecrafts[2].remaining_mass) and (parcel["volume"] <= spacecrafts[2].remaining_volume):
        spacecrafts[2].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
    elif (parcel["mass"] <= spacecrafts[3].remaining_mass) and (parcel["volume"] <= spacecrafts[3].remaining_volume):
        spacecrafts[3].add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
    else:
        remaining_list.append(parcel)

# check how many parcels are taken with
counter = 0
for spacecraft in spacecrafts:
    counter += len(spacecraft.cargo_list)
    print("Containing:", spacecraft.cargo_list, "\n", len(spacecraft.cargo_list), 3 * "\n")
print("Parcels loaded:", counter)

print("Cygnus remaining mass & volume:", Cygnus.remaining_mass, Cygnus.remaining_volume)
print("Progress remaining mass & volume:", Progress.remaining_mass, Progress.remaining_volume)
print("Kountori remaining mass & volume:", Kounotori.remaining_mass, Kounotori.remaining_volume)
print("Dragon remaining mass & volume:", Dragon.remaining_mass, Dragon.remaining_volume)

# cargo count of the Cygnus
counter2 = len(Cygnus.cargo_list)
print("Cygnus Cargo count: ", counter2)

repeat = 0

while counter < 84:

    # if repeat > 10000:
    #     randomChoice += 1

    # Cygnus property
    r_spacecraft1 = random.choice(spacecrafts)

    # random spacecraft
    r_spacecraft2 = random.choice(spacecrafts)

    # check if spacecrafts are not the same
    if r_spacecraft1 != r_spacecraft2:

        r_parcel1 = random.choice(r_spacecraft1.cargo_list)
        r_parcel2 = random.choice(r_spacecraft2.cargo_list)

        spc1_old_weight = r_spacecraft1.remaining_mass
        spc1_old_volume = r_spacecraft1.remaining_volume

        spc2_old_weight = r_spacecraft2.remaining_mass
        spc2_old_volume = r_spacecraft2.remaining_volume


        # first remove cargo's from spacecrafts for possible swap
        r_spacecraft1.remove_cargo(r_parcel1["cargo_id"])
        r_spacecraft2.remove_cargo(r_parcel2["cargo_id"])

        # check if swap is possible
        if (r_parcel1["cargo_weight"] <= r_spacecraft2.remaining_mass) and \
        (r_parcel1["cargo_volume"] <= r_spacecraft2.remaining_volume) and \
        (r_parcel2["cargo_weight"] <= r_spacecraft1.remaining_mass) and \
        (r_parcel2["cargo_volume"] <= r_spacecraft1.remaining_volume):

            # Swap cargo's between Cygnus and r_spacecraft2
            r_spacecraft2.add_cargo(r_parcel1["cargo_id"], r_parcel1["cargo_weight"], r_parcel1["cargo_volume"])
            r_spacecraft1.add_cargo(r_parcel2["cargo_id"], r_parcel2["cargo_weight"], r_parcel2["cargo_volume"])

            spc1_new_weight = r_spacecraft1.remaining_mass
            spc1_new_volume = r_spacecraft1.remaining_volume

            spc2_new_weight = r_spacecraft2.remaining_mass
            spc2_new_volume = r_spacecraft2.remaining_volume

            # accept the swap
            if spc1_new_weight < spc1_old_weight or spc2_new_weight < spc2_old_weight and \
                spc1_new_volume > spc1_old_volume or spc2_new_volume > spc2_old_volume:
                # print("YES")
                # repeat += 1
                continue

            # fix the swap
            else:
                r_spacecraft1.remove_cargo(r_parcel2["cargo_id"])
                r_spacecraft2.remove_cargo(r_parcel1["cargo_id"])

                r_spacecraft2.add_cargo(r_parcel2["cargo_id"], r_parcel2["cargo_weight"], r_parcel2["cargo_volume"])
                r_spacecraft1.add_cargo(r_parcel1["cargo_id"], r_parcel1["cargo_weight"], r_parcel1["cargo_volume"])

            # print("test1")

            for parcels in remaining_list:
                if (parcel["mass"] <= Cygnus.remaining_mass) and (parcel["volume"] <= Cygnus.remaining_volume):
                    Cygnus.add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
                    counter += 1
                elif (parcel["mass"] <= Progress.remaining_mass) and (parcel["volume"] <= Progress.remaining_volume):
                    Progress.add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
                    counter += 1
                elif (parcel["mass"] <= Kounotori.remaining_mass) and (parcel["volume"] <= Kounotori.remaining_volume):
                    Kounotori.add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
                    counter += 1
                elif (parcel["mass"] <= Dragon.remaining_mass) and (parcel["volume"] <= Dragon.remaining_volume):
                    Dragon.add_cargo(parcel["id"], parcel["mass"], parcel["volume"])
                    counter += 1

                    print("Cygnus remaining mass & volume:", Cygnus.remaining_mass, Cygnus.remaining_volume)
                    print("Progress remaining mass & volume:", Progress.remaining_mass, Progress.remaining_volume)
                    print("Kountori remaining mass & volume:", Kounotori.remaining_mass, Kounotori.remaining_volume)
                    print("Dragon remaining mass & volume:", Dragon.remaining_mass, Dragon.remaining_volume)
            # print("test2")
        else:
            r_spacecraft2.add_cargo(r_parcel2["cargo_id"], r_parcel2["cargo_weight"], r_parcel2["cargo_volume"])
            r_spacecraft1.add_cargo(r_parcel1["cargo_id"], r_parcel1["cargo_weight"], r_parcel1["cargo_volume"])





        ## repeat 10000x daarna sets verhogen
