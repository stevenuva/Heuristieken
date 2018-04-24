import csv
import os

#from spacecrafts import list_spacecrafts

# github link to retrieve CargoList1.csv if necessary
github_link = ("https://github.com/stevenuva/minor-programmeren/blob/"
               "master/CargoList1.csv")

# path to the csv_file
csv_file = "./data/CargoList1.csv"

for path in [csv_file]:
    assert os.path.exists(path), (f"{path} does not exist. Please download file"
                                  f" from {github_link}")

# load csv file into a file
with open(csv_file, "r") as infile:
    reader = csv.reader(infile)
    csv_list = list(reader)

# create an empty dictionary
cargo1_list = []

# loop through list to store csv data into a dictionary
for row in csv_list[1:]:
    cargo1_dic = {"parcel_id": row[0], "mass": float(row[1]), "volume": float(row[2])}
    cargo1_dic["kg/m3"] = cargo1_dic["mass"] / cargo1_dic["volume"]
    cargo1_list.append(cargo1_dic)

cargo1_list = sorted(cargo1_list, key=lambda
                     parcel: parcel["kg/m3"])

Cygnus = {"mass": 2000, "volume": 18.9}
Dragon = {"mass": 2400, "volume": 7.6}
Kounotori = {"mass": 5200, "volume": 14}
Progress = {"mass": 6000, "volume": 10}

list_spacecrafts = [Cygnus, Dragon, Kounotori, Progress]

for spacecraft in list_spacecrafts:
    ratio = spacecraft.get("mass") / spacecraft.get("volume")
    spacecraft["kg/m3"] = ratio

list_spacecrafts = sorted(list_spacecrafts, key=lambda
                          spacecraft: spacecraft["kg/m3"])


list1 = []
list2 = []
list3 = []
list4 = []
listrest = []
for parcel in cargo1_list:
    if 50 <= parcel.get("kg/m3") <= 180:
        list1.append(parcel)
    elif 250 <= parcel.get("kg/m3") < 350:
        list2.append(parcel)
    elif 350 <= parcel.get("kg/m3") <= 425:
        list3.append(parcel)
    elif 500 <= parcel.get("kg/m3") <= 710:
        list4.append(parcel)
    else:
        listrest.append(parcel)


counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0

for parcel in list:
    if(parcel["mass"] <= list_spacecrafts[0]["mass"]) and (parcel["volume"] <= list_spacecrafts[0]["volume"]):
        list_spacecrafts[0]["mass"] -= parcel["mass"]
        list_spacecrafts[0]["volume"] -= parcel["volume"]
        counter1 += 1
    elif(parcel["mass"] <= list_spacecrafts[1]["mass"]) and (parcel["volume"] <= list_spacecrafts[1]["volume"]):
        list_spacecrafts[1]["mass"] -= parcel["mass"]
        list_spacecrafts[1]["volume"] -= parcel["volume"]
        counter2 += 1
    elif(parcel["mass"] <= list_spacecrafts[2]["mass"]) and (parcel["volume"] <= list_spacecrafts[2]["volume"]):
        list_spacecrafts[2]["mass"] -= parcel["mass"]
        list_spacecrafts[2]["volume"] -= parcel["volume"]
        counter3 += 1
    elif(parcel["mass"] <= list_spacecrafts[3]["mass"]) and (parcel["volume"] <= list_spacecrafts[3]["volume"]):
        list_spacecrafts[3]["mass"] -= parcel["mass"]
        list_spacecrafts[3]["volume"] -= parcel["volume"]
        counter4 += 1
    else:
        continue

print(list_spacecrafts)
print("Parcels in the first spaceship:", counter1)
print("Parcels in the second spaceship:", counter2)
print("Parcels in the third spaceship:", counter3)
print("Parcels in the fourth spaceship:", counter4)

counter = counter1 + counter2 + counter3 + counter4

print(counter)
