### QUESTION A
Question A asked us if it was possible to load our four spaceships with 84 parcels or more.
Using the greedy algorithm in heurstiek_A.py it is possible to fit 82 parcels in the spacecrafts. For this you will need to load csv file cargolist1. IS HET NIET 83 NU?

### QUESTION B
Question B asked us what the greatest amount of parcels is we can fit in our four spaceships and what it would cost taking fuel into consideration.
By running Heuristieken_B.py we found that we can fit 82 parcels. First we calculated the cheapest option by taking the same fuel-to-weight (FtW) ratio for every spaceship. One option hereby is $335,000 cheaper than the second option (Cygnus: 17, Progress: 15, Kounotori: 28, Dragon: 22). The only difference between the options is the shift of one cargeo between Cygnus and Progress. Making the first option the cheapest with $2.009.210.000. We are still working on the part where every spacecraft has his own FtW.

When using the corresponding FtW we get the following outcomes.
For the first situation we find that it costs $1.984.648.040
For the second situation $1.988.118.230
So, when taking the appropriate FtW ratios, the difference between the options is $3.470.190.

### QUESTION C
Question C is the same as Question B, but instead of using cargolist 1 we now have to fill up the ships using cargolist 2. The highest number of parcels with our greedy algorithm is 70 parcels.

When using one overall FtW (0.73):
If we slice till 70 cargo's, the cargo costs $2.024.810.560. Composition: (Cygnus: 14, Progress: 12, Kounotori: 24, Dragon: 20)
If we slice the cargo list till 71 cargo's, the costs are $2.022.570.545. The composition (Cygnus: 14, Progress: 12, Kounotori: 23, Dragon: 20). This option is the cheapest option with a difference of $2.240.015.

Using corresponding FtW rations:
If we slice the cargo list till 70 parcels, it costs $2.000.095.385. (Cygnus: 14, Progress: 12, Kounotori: 24, Dragon 20)
When we slicte till 71 parcels, it will cost $1.998.095.275. (Cygnus: 14, Progress: 13, Kounotori: 23, Dragon: 20). This is the cheaper option with a difference of $2.000.110.

## Results table A, B, C (compare algorithmes)

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
