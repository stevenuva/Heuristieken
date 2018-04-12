import csv
import os

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
    cargo_list1 = list(reader)

# create an empty dictionary
cargo1_dic = {}

# loop through list to store csv data into a dictionary
for row in cargo_list1:
    key = row[0]
    if key in cargo1_dic:
        pass
    cargo1_dic[key] = row[1:]

# csv file turned dictionary
# values: weight(kg), volume(m^3)
print(cargo1_dic)

# gets the values of a parcel with the id "CL1#1"
print(cargo1_dic.get("CL1#1"))
