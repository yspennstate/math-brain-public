# account02/B12 early mathematical checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Status: supporting theorem in progress; full target open.

## First unpaid implication attacked

The current account03/B12 reduction leaves, after at most one original-coordinate scalar Schur step, a three-large-eigenvalue residual unless an already-paid pair/ridge exit fires. I attack stability of a localized physical triple in that residual under (i) one arbitrary-magnitude signed rank-one spectral change and (ii) an arbitrary full-rank operator-norm tail, without treating the quadratic random tail as small.

## Core calculation

Let B be an invertible physical 3x3 block and u the compression of a spectral direction. Put q=u^T B^{-1}u. For a scalar tau with tau*q>=0,

(B+tau uu^T)^{-1}=B^{-1}-[tau/(1+tau q)]B^{-1}u u^T B^{-1}.

Hence

|| (B+tau uu^T)^{-1} ||op <= ||B^{-1}||op + ||B^{-1}u||^2/|q|,

uniformly in |tau|. Thus a core with q>0 is safe for every tau>=0, while a second core with q<0 is safe for every tau<=0. If the reciprocal bound is 1/(beta L), an arbitrary symmetric dense tail T with ||T||op<=delta L leaves the selected final physical triple with sigma_min >= (beta-delta)L. The completed e5f Theorem A then gives the real final inequality

||p_Q||infinity <= 6 sqrt(pi)/[(beta-delta)L].

No spectral-coordinate random variable is used.

## Dense-tail propagation through one preceding physical scalar pivot

For a block-diagonal baseline pivot a0 with |a0|>=alpha L and a full symmetric perturbation T of norm <=delta L, write the actual first row/column perturbation as t00,c and the remaining compression as E. If delta<alpha, then the actual Schur remainder differs from its baseline remainder by

E - cc^T/(a0+t00),

so its operator norm is at most

delta_eff L,  delta_eff = delta + delta^2/(alpha-delta) = alpha*delta/(alpha-delta).

This is a matrix-level stability statement, not a probabilistic bound on X^T T X. Combining the localized triple terminal with the completed account03/B12 one-sided scalar compiler will give

||p_Q||infinity <= [2/L] sqrt( 6 sqrt(pi) / ((alpha-delta)(beta-delta_eff)) ).

The final report will prove the sign-routing theorem carefully, give an exact target-class family with tau of arbitrary sign/magnitude and a full-rank dense tail, and record the precise partner application.
