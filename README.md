# minor-programmeren

# Case

Our case is Space Freight. In this case we need to resupply the International Space Station. We got three cargolists that we need to send up as efficient as possible, regarding costs, amount of parcels and fuel. 

## Getting started

### Prerequisites

All our code is written in in Python version 3.6.5.. For the moment, no extra installations are needed to run our code.

### Structure  

The folder "data" contains the cargolists with the csv files. These lists are loaded into our code to answer the questions.   
The folder "algorithms" contains the codes used for the specific subquestions from our case. Spacecraft_classes.py contains our created classes.  
The folder "presentations" contains the progress presentations given over time.   
The folder "test" contains tests for code.   

## Questions

### QUESTION A
Question A asked us if it was possible to load our four spaceships with 84 parcels or more.
Using the greedy algorithm in main.py it is possible to fit 83 parcels in the spacecrafts. For this you will need to load csv file cargolist1.

### QUESTION B
Question B asked us what the greatest amount of parcels is we can fit in our four spaceships and what it would cost taking fuel into consideration.
By running main.py we found that we can fit 83 parcels only once. The only and thus cheapest, option cost $ 1.989.632.195,-.

### Results
| Questions |  Answers (for now) |
|---|---|
|A|83 parcels|
|B|83 parcels, costs: $ 1.989.632.195,-|

## Authors

Michael Hu 11996102  
Steven Kühnen 10305882   
Marc Moorman 10769781
