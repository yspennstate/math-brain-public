# P0282 idea before production validation — eighth Plancherel coefficient, group-algebra dual, then row 98

Date: 2026-09-19 UTC  
Track: `proofnet24/NM13-07`  
Canonical claim: `P0282`  
Entry frozen metric: `N_exact = 97`

Retained state on entry: complete all-`n` Chen fixed-defect theorem for `j=n-k<=66`; complete all-`n` binomial-normalized ULC theorem for `j<=32`; rigorous growing-defect theorem `j+1 <= n^(8/9)/8`; source OPEN / worker PARTIAL; P26 and NM13-08 audits not passed.

This note is written before the new production checkers. It records routes to test and does not itself claim a theorem.

## Route A — #11 DUALIZE + #25 COUNT THE SAME THING TWICE

Continue the retained factorization

`ell_{n,n-j}=((n)_j^2/j!) A_j(n)`

with `G_j(t)=log A_j(t)=sum_{m>=1} D_m(j)t^m`, `t=1/n`.

Before assuming that one more term helps, compute the exact eighth coefficient and its Chen discrete curvature. Use the exact cell-content identity

`B_m(mu)=-(1/m) sum_{box in mu} ((j+c(box))^m-(j+c(box)-1)^m)`

for the coefficient of `t^m` in `log R_mu`.

At order eight the new Plancherel expectations appear to reduce to four group-algebra traces:

- `E[C^4]=[e]T^4`, where `T=sum_i X_i` is the transposition class sum;
- `E[C S_5]=[e] T P_5`;
- `E[S_2 S_4]=[e] P_2 P_4`;
- `E[S_3^2]=[e] P_3^2`,

with `P_q=sum_i X_i^q`. Derive these by class/word counting, not numerical fitting. A finite exact word enumerator may be used only to certify the bounded star-word pattern constants (support size at most three).

The route is allowed to fail: if `2D_8(j)-D_8(j-1)-D_8(j+1)` is not nonnegative for all `j>=1`, archive the first exact adverse `j` and stop the exponent-lifting route.

## Route B — #3 PROVE SOMETHING STRONGER only if the sign survives

If the eighth curvature is favorable, combine it with the already proved analytic disk `|t|<=1/(6j)`, `|G_j(t)|<2`. Cauchy gives a tail after order eight of size at most

`4(6j/n)^9 < 2^26 j^9/n^9`

for `n>=12j`; the Chen second-difference costs at most four such errors. Test whether this yields a rigorous sufficient condition of the form

`n^9 >= C (j+1)^10`

and hence a `Theta(n^(9/10))` long-LIS boundary window. Do not call it source closure; the central `j=Theta(n)` regime would remain.

## Route C — finite metric only after structural work

After Route A/B is decided, move the frozen metric from row 97 to row 98 only if an exact Gessel/Toeplitz CRT certificate proves all newly uncovered cells. The retained `j<=66` theorem covers row 98 for `k>=32`, so only `k=2,...,31` are new.

## Section-B accounting planned for this invocation

All thirty methods have already genuinely appeared on P0282, so these are explicitly RECYCLED. The set differs from the preceding invocation's `#27/#26/#14/#7`:

- #11 DUALIZE — replace Plancherel averages by identity coefficients in the symmetric-group algebra;
- #25 COUNT THE SAME THING TWICE — compute the four new moments spectrally and by exact class/star-word counts;
- #3 PROVE SOMETHING STRONGER — only if the eighth curvature is favorable, convert it to a stronger `n^(9/10)` boundary theorem.

The row-98 certificate is bookkeeping after the structural route, not the primary research move.
