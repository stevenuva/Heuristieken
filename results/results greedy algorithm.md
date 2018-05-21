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

### Question C
Question C is the same as Question B, but instead of using cargolist 1 we now have to fill up the ships using cargolist 2. The highest number of parcels with our greedy algorithm is 70 parcels. 

When using one overall FtW (0.73):
If we slice till 70 cargo's, the cargo costs $2.024.810.560. Composition: (Cygnus: 14, Progress: 12, Kounotori: 24, Dragon: 20)
If we slice the cargo list till 71 cargo's, the costs are $2.022.570.545. The composition (Cygnus: 14, Progress: 12, Kounotori: 23, Dragon: 20). This option is the cheapest option with a difference of $2.240.015.

Using corresponding FtW rations:
If we slice the cargo list till 70 parcels, it costs $2.000.095.385. (Cygnus: 14, Progress: 12, Kounotori: 24, Dragon 20)
When we slicte till 71 parcels, it will cost $1.998.095.275. (Cygnus: 14, Progress: 13, Kounotori: 23, Dragon: 20). This is the cheaper option with a difference of $2.000.110. 


### Results
| Questions |  Answers (for now) |
|---|---|
|A|83 parcels|
|B|83 parcels, costs: $ 1.989.632.195,-|

## Questions

### QUESTION A
Question A asked us if it was possible to load our four spaceships with 84 parcels or more.
Using the greedy algorithm in main.py it is possible to fit 83 parcels in the spacecrafts. For this you will need to load csv file cargolist1.

### QUESTION B
Question B asked us what the greatest amount of parcels is we can fit in our four spaceships and what it would cost taking fuel into consideration.
By running main.py we found that we can fit 83 parcels only once. The only and thus cheapest, option cost $ 1.989.632.195,-.