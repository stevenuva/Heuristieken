import csv
import os

# github link to retrieve CargoList1.csv if necessary
github_link = ("https://github.com/stevenuva/minor-programmeren/blob/"
               "master/CargoList2.csv")

# path to the csv_file
csv_file = "./data/CargoList2.csv"

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
# calculate the kg/m3
# append every dictionary to a list
for row in csv_list[1:]:
    cargo1_dic = {"parcel_id": row[0], "mass": float(row[1]), "volume": float(row[2])}
    cargo1_dic["kg/m3"] = cargo1_dic["mass"] / cargo1_dic["volume"]
    cargo1_list.append(cargo1_dic)

# sort list on volume
cargo1_list = sorted(cargo1_list, key=lambda
                     parcel: parcel["volume"])

# slice list
cargo1_list = cargo1_list[:70]

# of 
# cargo1_list = cargo1_list[:71]


# sort list on kg/m3 ratio
cargo1_list = sorted(cargo1_list, key=lambda
                     parcel: parcel["kg/m3"])

# dictionaries with spaceships mass and volume
Cygnus = {"mass": 2000, "volume": 18.9}
Dragon = {"mass": 2400, "volume": 7.6}
Kounotori = {"mass": 5200, "volume": 14}
Progress = {"mass": 6000, "volume": 10}

# create a list containing all the dictionary spaceships
list_spacecrafts = [Cygnus, Dragon, Kounotori, Progress]

# calculate and add the kg/m3 to every spaceship dictionary
for spacecraft in list_spacecrafts:
    ratio = spacecraft.get("mass") / spacecraft.get("mass")
    spacecraft["kg/m3"] = ratio

# sort list on kg/m3 ratio
list_spacecrafts = sorted(list_spacecrafts, key=lambda
                          spacecraft: spacecraft["kg/m3"])


# create counters
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0

# create spacecraft cargo
c_spacecraft1 = {}
c_spacecraft2 = {}
c_spacecraft3 = {}
c_spacecraft4 = {}

key = 0

# for parcel in cargo1_list:
#     if(parcel["mass"] <= list_spacecrafts[2]["mass"]) and (parcel["volume"] <= list_spacecrafts[2]["volume"]):
#         list_spacecrafts[2]["mass"] -= parcel["mass"]
#         list_spacecrafts[2]["volume"] -= parcel["volume"]
#         counter3 += 1

#     elif(parcel["mass"] <= list_spacecrafts[3]["mass"]) and (parcel["volume"] <= list_spacecrafts[3]["volume"]):
#         list_spacecrafts[3]["mass"] -= parcel["mass"] 
#         list_spacecrafts[3]["volume"] -= parcel["volume"]
#         counter4 += 1
#     elif(parcel["mass"] <= list_spacecrafts[1]["mass"]) and (parcel["volume"] <= list_spacecrafts[1]["volume"]):
#         list_spacecrafts[1]["mass"] -= parcel["mass"]
#         list_spacecrafts[1]["volume"] -= parcel["volume"]
#         counter2 += 1
#     elif(parcel["mass"] <= list_spacecrafts[0]["mass"]) and (parcel["volume"] <= list_spacecrafts[0]["volume"]):
#         list_spacecrafts[0]["mass"] -= parcel["mass"]
#         list_spacecrafts[0]["volume"] -= parcel["volume"]
#         counter1 += 1



# loop to place the parcels in the spaceship when possible
for parcel in cargo1_list:
    if(parcel["mass"] <= list_spacecrafts[0]["mass"]) and (parcel["volume"] <= list_spacecrafts[0]["volume"]):
        list_spacecrafts[0]["mass"] -= parcel["mass"]
        list_spacecrafts[0]["volume"] -= parcel["volume"]
        key += 1 
        c_spacecraft1[key] = parcel
        counter1 += 1

    elif(parcel["mass"] <= list_spacecrafts[1]["mass"]) and (parcel["volume"] <= list_spacecrafts[1]["volume"]):
        list_spacecrafts[1]["mass"] -= parcel["mass"] 
        list_spacecrafts[1]["volume"] -= parcel["volume"]
        key += 1 
        c_spacecraft2[key] = parcel
        counter2 += 1
    elif(parcel["mass"] <= list_spacecrafts[2]["mass"]) and (parcel["volume"] <= list_spacecrafts[2]["volume"]):
        list_spacecrafts[2]["mass"] -= parcel["mass"]
        list_spacecrafts[2]["volume"] -= parcel["volume"]
        key += 1 
        c_spacecraft3[key] = parcel
        counter3 += 1
    elif(parcel["mass"] <= list_spacecrafts[3]["mass"]) and (parcel["volume"] <= list_spacecrafts[3]["volume"]):
        list_spacecrafts[3]["mass"] -= parcel["mass"]
        list_spacecrafts[3]["volume"] -= parcel["volume"]
        key += 1 
        c_spacecraft4[key] = parcel
        counter4 += 1
    else:
        print("remaining: ", parcel)

# print results
print("\nParcels in the first spaceship:", counter1, " ->Remaining:", list_spacecrafts[0], "\n")
print("Parcels in the second spaceship:", counter2, "->Remaining:", list_spacecrafts[1], "\n")
print("Parcels in the third spaceship:", counter3, " ->Remaining:", list_spacecrafts[2], "\n")
print("Parcels in the fourth spaceship:", counter4, "->Remaining:", list_spacecrafts[3], "\n")

counter = counter1 + counter2 + counter3 + counter4

print("Total parcels :", counter)

print("\nSpacecraft1 Cargo: ", c_spacecraft1)
print("\nSpacecraft2 Cargo: ",c_spacecraft2)
print("\nSpacecraft3 Cargo: ", c_spacecraft3)
print("\nSpacecraft4 Cargo: ", c_spacecraft4)


