# Heuristieken (minor-programmeren)

# Case

Our case is Space Freight. In this case we need to resupply the International Space Station. We got three cargolists that we need to send up as efficient as possible, regarding costs, amount of parcels and fuel. Important is to take into consideration that each spaceship has his own characteristics regarding (base) costs, volume and payload. Making different characteristics more important at certain ships. 

## Getting started

### Prerequisites
All our code is written in in Python version 3.6.5.. 
Needs to be installed: Matplotlib

### Structure  
The folder "algorithms" contains the codes used for the specific subquestions from our case. Spacecraft_classes.py contains our created classes. Main.py has to be run to find all the answers. If ran, main.py asks for user input. This input is related to which answer of a subquestion the user wants to see and with which algorithm he/she wants the answer to be found with. Main.py imports helper.py, Spacecraft_Classes.py, greedy_no_constraints.py, hill_climber.py, random_greedy.py, greedy_political.py and greedy.py.   

The folder "data" contains the cargolists with the csv files. These lists are loaded into our code to answer the questions.     
The folder "presentations" contains the progress presentations given over time.       

## Authors

Michael Hu 11996102  
Steven Kühnen 10305882   
Marc Moorman 10769781
