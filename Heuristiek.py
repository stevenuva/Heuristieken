import csv
import os
import itertools


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)



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
    cargo1_dic[key] = row[1:]

# csv file turned dictionary
# values: weight(kg), volume(m^3)
# print(cargo1_dic)

# gets the values of a parcel with the id "CL1#1"
# print(cargo1_dic.get("CL1#1")

# gets the weight of a pacel with the id "CL1#1"
# gets the volume of a pacel with the id "CL1#1"

keys_list = list(cargo1_dic.keys())[1:]
values = list(cargo1_dic.values())[1:]

weight_list = []
volume_list = []

for value in values:
    weight_list.append(value[0])
    volume_list.append(value[1])

# print(keys_list)
# print("-------------")
# print(weight_list)
# print("=-----------------")
# print(volume_list)

print(combinations(keys_list, 84))
