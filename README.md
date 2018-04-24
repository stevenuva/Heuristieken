# minor-programmeren

Michael Hu 11996102  
Steven Kühnen  
Marc Moorman 10769781  


20-04-2018  
The folder "presentations" contains our weekly presentations.  
The folder "data" contains the cargolists with the csv files, which has to be loaded into the code. 
Heuristiek.py contains the code for our greedy algorithm. 

QUESTION A
Question a asked us if it was possible to load our four spaceships with 84 parcels or more. Using our greedy algorithm in heurstiek.py we can fit 82 parcels in total in our spacecrafts. In this code we loaded the csv file cargolist1 and wrote in a list of dictionaries. For the moment there is no need for extra installations to run our code. 

24-04-2018
Created classes in "Spacecraft classes.py" to be used for following questions. The classes can add cargo, calculate costs and keeps track of spacecraft remaining volume and mass. 

Started with question b in "Opdracht B.py" in folder "Opdracht B". Question is how many parcels we can take with us as a maximum and which way of distributing the parcels is cheapest. So far we can take 82 parcels and have two options of cargo distribution. If we don't take into consideration the FtW per craft, our first option (Cygnus: 18, Progress: 14, Kounotori: 28, Dragon: 22) is $335,000 cheaper than the second option (Cygnus: 17, Progress: 15, Kounotori: 28, Dragon: 22). The only difference between the options is the shift of one cargeo between Cygnus and Progress. We are working on the answer where we do take FtW per craft into consideration. 

We also started with the first part of question c in Heuristiek-C.py. The question is how many parcels the spaceships can take if Cargolist2 is loaded. We used the algorithm as we used for Cargolist1 which lead us to the answer 70 parcels. The next step is to use the Hill Climber algorithm to maybe get to a better solution. We made dictionaries for each spacecraft to get a better visualisation of which parcels are in which spacecraft, so that we can exchange parcels between spacecrafts more easily. 