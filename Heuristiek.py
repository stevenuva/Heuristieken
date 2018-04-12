
# coding: utf-8

# In[3]:


import csv

# change to github link
csv_file = "C:/Users/steve/Desktop/Heuristieken/CargoList1.csv"

# load csv file into a file
with open(csv_file, 'r') as infile:
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




