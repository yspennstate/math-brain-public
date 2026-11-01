# Exact checks for r19

The numerical script is only a sanity check. The target-valid example has an analytic certificate.

Let

`B=[[1,2],[2,-1]]`, so `B^2=5I`, `det B=-5`, and both singular values are `sqrt(5)`.

Let `C=(1/2)I` and `M=[[B,C],[C,B]]`. Since `B` and `C` commute, the spectrum of `M` is the union of the spectra of `B+C` and `B-C`, namely

`{-sqrt(5)-1/2, -sqrt(5)+1/2, sqrt(5)-1/2, sqrt(5)+1/2}`.

Appending a scalar block `[2]` gives minimum absolute eigenvalue `sqrt(5)-1/2`. Coupling that fifth coordinate to each of the first four with coefficient `1/20` adds a symmetric off-block perturbation `[[0,q],[q^T,0]]` with `||q||_2=sqrt(4*(1/20)^2)=1/10`. Weyl's inequality therefore gives

`min_j |lambda_j(A)| >= sqrt(5)-1/2-1/10 = sqrt(5)-3/5 > 1.63 >1`.

Thus all five eigenvalues actually have modulus greater than one; in particular the three-large-eigenvalue target hypothesis holds.

For the Schur calculation, `B^{-1}=B/5`, so

`S=B-C^T B^{-1}C = B-(1/4)(B/5)=(19/20)B`.

Hence

`Delta=|det B|=5`, `kappa=sqrt(5)`, `s=||S||=(19/20)sqrt(5)`,

and

`Delta*kappa*s = 5*sqrt(5)*(19/20)*sqrt(5)=95/4`.

Therefore Theorem 6.1 gives exactly

`||p_Q||_infinity <= 4sqrt(26)(95/4)^(-1/4) = 9.239123275153592...`.

For the block-diagonal pair corollary (`C=0`), each pair has `(Delta,kappa)=(5,sqrt(5))`, so

`(Delta_1Delta_2)^(-1/8)(kappa_1kappa_2)^(-1/4)=1/sqrt(5)`

and the bound is `K0/sqrt(5)=10.89443512093865...`.
