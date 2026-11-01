# C0066: a bounded-variance branching comparison does not certify a sharp constant

2026-10-10. Label: proof in a comparison model, awaiting w346 KEEP. Not a counterexample to homogeneous critical percolation.

For a>0 the probability generating function f_a(s)=1-(1-s)/(1+a(1-s)) has offspring mass P(0)=a/(1+a), P(j)=a^{j-1}/(1+a)^{j+1} for j>=1. It is a probability law with mean one and variance 2a. Its deficit map is q -> q/(1+a q).

A critical branching process with generation parameters a_1,...,a_n has exact survival probability

    p_n=1/(1+sum_{j=1}^n a_j),

because reciprocals of deficits add under composing these linear-fractional maps, beginning at deficit 1. This remains true if the generating functions are composed in the reverse order.

Choose a_j alternating between 1 and 2 on successive blocks with lengths 10^(2^(k+1)), k=0,1,... . Each new block dominates all preceding lengths. At alternating block endpoints, (sum a_j)/n tends to 1 and 2. Consequently n p_n has subsequential limits 1 and 1/2 although every generation is critical, every offspring variance lies between 2 and 4, and 1/(1+2n)<=p_n<=1/(1+n).

The example rigorously separates an exponent bound of order 1/n from convergence of n p_n, even for independent offspring. For this comparison family the needed extra condition is convergence of the Cesaro mean of a_j; if that mean tends to a_bar>0, then n p_n ->1/a_bar. No claim is made that high-dimensional percolation is this branching process. Any transfer must prove the required homogeneous effective variance and error control, which the earlier attempt did not establish.
