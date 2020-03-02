# Two-Dimensional Weight-Constrained Codes

A Two-Dimensional Weight-Constrained Codes is a code that holds the following constraint:
The input is an (n − 1) × (m − 1) binary array and the output is a length n × m binary array, which the Hamming weight of every row and column is at most a half of its size.
 
This project is an implementation of the construction for such a code shown in section 3 the of article:
 
E. Ordentlich and R.M. Roth, “Low complexity two-dimensional weight-constrained codes,” IEEE Transactions on Information Theory, vol. 58, no. 6, pp. 3892–3899, Jun. 2012. 

Our implementation includes both an encoder and a decoder.

The encoder has a worst-case complexity of O(m*n) iterative steps therefore the overall complexity is O(m*n*(m+n)).

The decoder has a complexity of O(m+n) iterative steps therefore the overall complexity is O((m+n)^2).

We conducted simulations for different chances for 1's and 0's in the input matrix and different matrices size in order to figure out bounds for the number of iterative steps in the average case.
From our simulations we came to the following conclusions:
- if the chance to write 1 is smaller than 50%, as the dimensions of the input grows the number of iterative steps gets smaller and tends to 0 (as can be seen in the gragh "49p.png").
This can be explained by the fact that with a lesser chance to write 1's, as the number of elements in a row\column grows the chances it will initially hold the constraint grows as well.  
- if the chance to write 1 is bigger than 50%, as the dimensions of the input grows, the number of iterative steps approximates the number of rows\columns (as can be seen in the graph "51p.png").
We are guessing that with a higher chance to write 1's, the bigger the rows\columns are the higher the chance the matrix will hold the constraint after one flip per row.
- if the chance to write 1 is exactly 50%, the number of iterative steps is linear in the number of rows/columns. we ran simulations on matrices with the shape (n*(n\c)) for different c values and found that this assumptions holds for all of them.
Examples can be seen in the graphs "50p.png" (where the numbe the number of iterative steps approximates 1.75n), "50p_1.6c.png" and "50p_2c.png" (where the numbe the number of iterative steps approximates 1.4n)



### Prerequisites

An installation of python 3.7 that includes the numpy library


## Running the simulations

The file simulation.py contains code for running the Encoder on different inputs.

Running show_results.py outputs several graphs showing the running time of different inputs.  

