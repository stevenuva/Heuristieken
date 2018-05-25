### QUESTION A asked us if it was possible to load our four spaceships with 84 parcels or more.
By running greedy_filling in main.py we could fit 83 parcels from cargolist 1 in the spaceships. The same is the case for our other algorithms greedy-random and our hill climbing algorithm. All algorithms are run from within main.py which can be found in the folder "algorithms". 

### QUESTION B asked us what the greatest amount of parcels is we can fit in our four spaceships and what it would cost taking fuel into consideration.
The results table below shows the options for this question. Our hill climber algorithm gave us the cheapest option. This still sends 83 parcels. However, the hill climber took the longest time of our algorithms to find its best solution. All results are calculated using the corresponding fuel-to-weight ratios. Not with the given overall fuel-to-weigt. 

### QUESTION C is the same as Question B, but instead of using cargolist 1 we now have to fill up the ships using cargolist 2.
Also depicted below are the results for question C. Here the hill climber gives the cheapest option, but not with the highest amount of parcels. Our random-greedy can take more parcels up into space. So here to give a definite answer it has to be decided what the highest priority has, money or parcels. All results are calculated using the corresponding fuel-to-weight ratios. Not with the given overall fuel-to-weigt. 

## Results table A, B, C (compare algorithms)

|Question|Greedy|Hill Climber|Random Greedy|
|---|---|---|---|
|A|83|83|83|
|B|$1989582285|$1980951280|$1985465920|
|C (length)|70|71|72
|C (cost)|$1998043980|$1990903555|$1998124540

## For te following question a political constraint was opposed. No country could go up in the air more or less than one time than the other countries.

### Question D asked us to compose a fleet of spacecrafts to send all the parcels in cargolist 3 up as cheap as possible.
Here we ignored Cygnus. We did this to comply to the restriction. Since the USA has two ships, Cygnus and Dragon. Greedy gave us the following answers: The total costs would be $41,598,083,005 and a fleet would go up 12 times. The political constraint was not broken.
	European flights: 12
	Chinese flights: 11
	Japanese flights: 12
	USA flights: 11
	Russian flights: 12

Here we ignored Dragon. We did this to compare taking different American spacecrafts and still complying with the political restriction. Our greedy algorithm gave the following answers. The total costs of sending the fleet up 13 times is $ 44,414,457,105. The restriction is not violated.
	European flights: 13
	Chinese flights: 12
	Japanese flights: 12
	USA flights: 13
	Russian flights: 12

The cheaper option here is to ignore Cygnus when we use our greedy algortihm and have to take up cargolist 3.

As a test we ran a random program for a thousand times on this same cargolist with constraint that it would be cheaper than our greedy option. This gave 25 random options that were cheaper than our greedy option and also did not break the international political constraint. The cheapest of these options is $40,784,196,030 and also goes up for 12 times with the entire fleet.

### Question E asked us to answer question D but without the political constraints as a restriction.
We tested by using just one ship of all available ships, and let that ship fly up all the time. If we only used Kounotori, TianZhou or Progress we would be cheaper off. Where Kounotori would be the cheapest with $ 37,581,140,235 and flying up 63 times.

Here we also did a random test for ten thousand times. The restriction was that it had to be as least as cheap, as the most expensive of the three cheaper options stated above (Kounotori, Tianzhou and Progress). So the benchmark is TianZhou. If we only fly up this ship it would cost $ 38,116,812,575 for cargolist 3. The random test gave us no cheaper options if we only sent up one ship and fill it randomly.
