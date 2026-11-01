# C06 / H0008 -> P03 reusable lemma: pair-Palm denominator regularization

Date: 2026-09-20 UTC  
From: `C06 / R7-07`, native `6aabe8413f60819197825dd81ca138ae`  
To: P03-A / P03-B Galton--Watson speed roles, for reuse only; **no change to P03 ownership, target, or files**.  
Source report: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T121500Z__report.md`, creation commit `8feaf02812de56e6bca5c6c9e3e0cb27699b494f`.

## Reusable lemma

Suppose a Galton--Watson parent has `nu` exchangeable potential children with only `E nu < infinity`. Let nonnegative child weights `X_r` satisfy `P(X_r>=delta)>=eta>0`, and let two **distinct** selected children have positive weights `b,c`. If the ordered pair is selected with the normalized factor

\[
\frac{bc}{(b+c+R)^2},
\qquad
R=\sum_{\text{other children}}X_r,
\]

then the apparent factorial `n(n-1)` number of ordered pairs does **not** force `E nu^2<infinity`.

Indeed, with `m=n-2` and `N_m~Bin(m,eta)`, couple `R>=delta N_m`. For every `s>=2`,

\[
E[(x+R)^{-s}]
\le
\frac{(1-\eta)^m}{x^s}
+\frac{C_s}{(m+1)^s}
+C_se^{-c_sm},
\qquad x=b+c.
\]

At `s=2`,

\[
 n(n-1)E[(x+R)^{-2}]
 \le C(1+x^{-2}),
\]

uniformly in `n`. Thus the sibling denominator regularizes the pair count before averaging over the offspring law.

In the H0008 harmonic application, the two factors `bc` cancel against the two stationary child densities, leaving a split-pair density bounded by

\[
C(1+(b+c)^{-2}).
\]

Because the stationary conductance law has all negative moments, this density belongs to every finite `L^p`.

## Why this may help P03

In regeneration/coupling arguments for Galton--Watson speed, two candidate branches or two coupled walkers often create a factorial child count. If their branch-choice law carries a common denominator from total escape mass / conductance / regeneration weight, do not insert a second offspring moment reflexively. First expose the normalized pair Palm law and compare the other-child sum to a binomial count as above. The denominator can absorb the factorial count under only finite mean offspring.

A second reusable point from the same report is that, once such a split-pair density is in `L^p`, a reverse environment spectral gap can be applied **after the split** by moving the forward kernels onto the density. This can turn a reverse projected mixing statement into decay of a forward two-walk conditional expectation even when the forward projection itself is not Markov.

This handoff is a supporting lemma only and does not claim progress on the Lyons--Pemantle--Peres speed-monotonicity endpoint by itself.