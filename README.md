# minor-programmeren

# Case

Our case is Space Freight. In this case we need to resupply the International Space Station. We got three cargolists that we need to send up as efficient as possible, regarding costs, amount of parcels and fuel. 

## Getting started

### Prerequisites

All our code is written in in Python version 3.6.5.. For the moment, no extra installations are needed to run our code.

### Structure  

The folder "data" contains the cargolists with the csv files. These lists are loaded into our code to answer the questions.   
The folder "algorithms" contains the codes used for the specific subquestions from our case.   Spacecraft_classes.py contains our created classes.  
The folder "presentations" contains the progress presentations given over time.   
The folder "test" contains tests for code.   

## Questions

### QUESTION A
Question A asked us if it was possible to load our four spaceships with 84 parcels or more.
Using the greedy algorithm in heurstiek_A.py it is possible to fit 82 parcels in the spacecrafts. For this you will need to load csv file cargolist1.

### QUESTION B
Question B asked us what the greatest amount of parcels is we can fit in our four spaceships and what it would cost taking fuel into consideration.
By running Heuristieken_B.py we found that we can fit 82 parcels. First we calculated the cheapest option by taking the same fuel-to-weight (FtW) ratio for every spaceship. One option hereby is $335,000 cheaper than the second option (Cygnus: 17, Progress: 15, Kounotori: 28, Dragon: 22). The only difference between the options is the shift of one cargeo between Cygnus and Progress. Making the first option the cheapest with $2.009.210.000. We are still working on the part where every spacecraft has his own FtW. 

### Results
| Questions |  Answers (for now) |
|---|---|
|A|82 parcels|
|B|82 parcels, costs: $ 2.009.210.000,-|

## Authors

Michael Hu 11996102  
Steven Kühnen   
Marc Moorman 10769781
