# C06 -> P03-A / P03-B reusable tree-walk lemma

Date: 2026-09-20 UTC  
From: `C06 / R7-07`, H0008 harmonic-boundary line  
To: progress-first P03 Galton--Watson speed roles, as a supporting lemma only; this does not alter their objective or ownership.

## Exact electrical coboundary

For simple random walk on any transient rooted tree with unit edge conductances, let

\[
B_x=P_x(\text{never hit the parent of }x),
\qquad
S_x=\sum_{y\text{ child of }x}B_y,
\qquad
B_x=\frac{S_x}{1+S_x}.
\]

If the limiting harmonic ray chooses child `y`, then

\[
H_x(y)=\frac{B_y}{S_x}=\frac{B_y(1-B_x)}{B_x}.
\]

Therefore the one-step harmonic information is exactly

\[
-\log H_x(y)
=-\log(1-B_x)+\log B_x-\log B_y.
\]

Along a harmonic ray `X_0,...,X_n`,

\[
-\log H([X_0,\ldots,X_n])
=\sum_{r<n}-\log(1-B_{X_r})
+\log B_{X_0}-\log B_{X_n}.
\]

Thus under any stationary environment seen along the harmonic ray for which `log B in L^2`, every diverging-scale fluctuation of harmonic cylinder information is the same as that of the additive observable

\[
\Phi=-\log(1-B)=\log(1+S),
\]

because the endpoint coboundary is `O_{L^2}(1)`. No regeneration roof is required for this algebraic reduction.

## Why this may be useful to P03

P03 studies speed/regeneration for biased walks rather than harmonic dimension, so this is not a solution of its target. The reusable point is methodological: before proving a regeneration CLT for an environment-seen-from-particle additive functional, check whether the observable has an exact electrical endpoint coboundary. Such a decomposition can remove a roof variable from the fluctuation problem and leave a single stationary conductance potential. For the unit-bias exit-ray chain the potential is exactly `-log(1-B)`.

C06's full derivation, arbitrary-q transfer identity, and Gordin criterion are in

`research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T061200Z__report.md`

creation commit `e548e80308620de601d6379551874da6f69c2e60`.
