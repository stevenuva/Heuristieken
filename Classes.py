import csv
import os

# github link to retrieve CargoList1.csv if necessary
github_link = ("https://github.com/stevenuva/minor-programmeren/blob/"
               "master/CargoList1.csv")

# path to the csv_file
csv_file = "./data/CargoList1.csv"

# check if user has csv at the right path
for path in [csv_file]:
    assert os.path.exists(path), (f"{path} does not exist. Please download file"
                                  f" from {github_link}")

# load csv file into a list
with open(csv_file, "r") as infile:
    reader = csv.reader(infile)
    csv_list = list(reader)

print(csv_list)
