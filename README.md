# Two-Dimensional Weight-Constrained Codes

A Two-Dimensional Weight-Constrained Codes is a code that holds the following constraint:
The input is an (n − 1) × (m − 1) binary array and the output is a length n × m binary array, which the Hamming weight of every row and column is at most a half of its size.
 
This project is an implementation of the construction for such a code shown in section 3 the of article: E. Ordentlich and R.M. Roth, “Low complexity two-dimensional weight-constrained codes,” IEEE Transactions on Information Theory, vol. 58, no. 6, pp. 3892–3899, Jun. 2012. 

Our implementation includes both an encoder and a decoder.
The encoder has a worst-case complexity of O(m*n) iterative steps therefore the overall complexity is O(m*n*(m+n)).
From simulations we performed we deducted that the average case complexity is O(m+n) iterative steps and therefore the averege complexity is O((m+n)^2).
The decoder has a complexity of O(m+n) iterative steps therefore the overall complexity is O((m+n)^2).


### Prerequisites

An installation of python 3.7 that includes the numpy library


## Running the simulations

The file simulation.py contains code for running the Encoder on different inputs.

Running show_results.py outputs several graphs showing the running time of different inputs.  

