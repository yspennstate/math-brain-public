# One quantified parent gap

This is an unproved obligation for the source lattice, not an additional claimed result.

For the exact Gaussian east/north model in STATEMENT.md, let P_n(g) be its unique maximizing n-vertex path. Let g^t=exp(-t)g+sqrt(1-exp(-2t))g' with g' an independent Gaussian environment, and define R_n(t)=E|P_n(g) intersect P_n(g^t)|.

The single missing estimate is: find fixed delta>0 and C<infinity such that

    R_n(n^-delta) <= C n^(1-delta), for every n>=2.

Why this would close the requested power-improvement target: the established finite-Gaussian covariance identity gives Var(M_n)=integral_0^infinity exp(-t)R_n(t) dt, R_n(0)=n, and R_n(t) is non-increasing. Splitting at t_n=n^-delta yields

    Var(M_n) <= n(1-exp(-t_n))+exp(-t_n)R_n(t_n)
                <= (1+C)n^(1-delta).

Conversely, a bound Var(M_n)<=K n^(1-epsilon) gives R_n(t)<=Var(M_n)/(1-exp(-t)); at t=n^(-epsilon/2), use 1-exp(-t)>=t/2 to obtain R_n(t)<=2K n^(1-epsilon/2). Thus this is a precise equivalent polynomial-scale obligation, up to the exponent's factor of two. These identities and monotonicity use Chatterjee 2008, Lemmas 3.3 and 3.5 and Theorem 3.2, with the finite independent Gaussian environment and Lipschitz maximum hypotheses checked. No independence between the two optimizing paths is asserted.

The bounded-degree graph obstruction in ATTEMPT.md does not supply this estimate on the lattice. No new route has crossed this gap.

NEXT: Prove this fixed-lattice overlap bound using a property absent from the tree-plus-chains family, such as its polynomial layer size and path reconvergence; first-chaos smallness alone is insufficient.
