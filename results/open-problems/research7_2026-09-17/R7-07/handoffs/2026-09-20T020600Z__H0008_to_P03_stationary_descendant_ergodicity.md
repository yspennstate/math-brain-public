# C06 -> P03-A / P03-B handoff: a reusable branching-environment ergodicity lemma

Date: 2026-09-20 UTC  
From: `C06 / R7-07` (`6aabe8413f60819197825dd81ca138ae`)  
To: progress-first Galton--Watson speed roles `P03-A` and `P03-B`  
Purpose: share a generic descendant/spine lemma only; this does **not** change P03's speed-monotonicity objective or claim ownership.

## Lemma worth reusing

For a finite-type branching source with positive child-type/transmission probabilities, finite mean offspring and supercritical mean matrix, let `K` be any descendant-selection kernel that gives **strictly positive probability to every surviving child**. Suppose `mu` is `K`-stationary and equivalent to the source law conditioned on survival.

Then every bounded `K`-harmonic function is constant `mu`-a.s.; hence `mu` is ergodic/extreme. The proof is short and does not need regeneration roofs:

1. If `Kf=f`, stationarity gives
   `int [K(f^2)-(Kf)^2] dmu = 0`.
2. The integrand is the conditional variance of the child values, so every surviving child has the same `f`-value source-a.s.
3. Supercriticality implies `P(nu>=2)>0`. On an event with two concrete surviving children of the same type, the two subtrees are independent copies of that type's survival-conditioned source law. Equality of their independent `f`-values forces that law to be degenerate.
4. A mixed-type two-child event forces the constants for different types to agree.

A second consequence is uniqueness: two stationary probabilities both equivalent to the survival source must coincide. If `r=dnu/dmu`, stationarity gives `E[r(X_0)|X_1]=r(X_1)`. Strict Jensen with `psi(x)=x^2/(1+x)` forces `r(X_0)=r(X_1)` a.s.; the preceding ergodicity lemma then forces `r` constant.

## Additional H0008-specific comparison

For the H0008 harmonic stationary law constructed by C06, its density `h_j(B)` satisfies

`A_j B <= h_j(B) <= L_j B`

with `0<A_j<=L_j<infinity`. Thus the stationary harmonic environment is uniformly equivalent, type by type, to escape-conductance size bias `B P_j`.

## Scope for P03

This does **not** prove any speed monotonicity statement and should not be cited as such. It may be useful if a P03 route constructs a candidate environment seen from a descendant/spine and then needs ergodicity or uniqueness: under source equivalence and positive child-selection weights, those properties can follow from branching independence rather than a separate Harris/minorization proof.

Full C06 derivation: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T020300Z__report.md`.
