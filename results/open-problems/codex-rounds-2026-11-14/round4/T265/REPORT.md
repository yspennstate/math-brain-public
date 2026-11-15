VERDICT: PARTIAL exact path norm and margin-objective obstruction for the earlier conical interpolants; GD selection remains unresolved

The earlier result holds. An independent derivation and recheck.py
recover its exact interpolation, localization bound, and numerical
excess-risk bound 0.0010691876353647793. The bounded web check found
no verified resolution of the main question; opened primary sources
and scope are in [LITERATURE.md](LITERATURE.md).

The new result evaluates the minimum path norm over **all finite
bias-free ReLU representations** of the earlier scores. For distinct
unoriented unit normals u_k, let

\[
 f(x)=v^Tx+\sum_k\beta_k|u_k^Tx|,
 \qquad Z=\sum_k[-|\beta_k|u_k,|\beta_k|u_k].
\]

Then

\[
 \mathcal P(f)=2\sum_k|\beta_k|+2\operatorname{dist}_2(v,Z).
\]

The infimum is attained. The lower bound allows arbitrary extra
neuron directions and cancellations. Existing pairs can supply a
linear part without extra norm until that part leaves Z. Applied to
the earlier construction, this proves its correction cost is intrinsic,
and gives an exact formula for its full score cost. No novelty claim
for the general norm formula is made; its explicit interpolation
comparison is the contribution here.

For every fixed nondegenerate sample with a nonzero correction,
sufficiently narrowing those cones excludes global minimum-path-norm
interpolation. There is also a concrete example using the round 3
rule exactly: X_1=(1,0), X_2=(1,3), Y_1=1, Y_2=-1. Its prescribed
widths 1/8 give intrinsic norm at least 144; widths 1 interpolate the
same labels with norm at most 81. The exact intrinsic norms evaluate
to 386.3134673380746 and 49.22147835683593. The strict comparison
persists on an open set of samples, hence has positive probability
under any nondegenerate two-dimensional Gaussian mixture.

More locally, the displayed six-neuron-per-cone realization, after
balancing neurons, admits a strict parameter-norm descent while
keeping every fitted label fixed. Proposition 4 excludes its
generalized unit-margin KKT stationarity, including arbitrary ReLU
derivatives at zero. Its unbalanced positive neuron rescalings are
also excluded. This conclusion is about those parameter realizations;
another representation of the same score might satisfy KKT conditions.

Full proofs are in [PROOF.md](PROOF.md). Run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit.py
```

Both exited 0 in under one second. The independent recheck used 96
rational samples, 528 exact interpolations, 9,504 triangular identities,
and direct density integrals. The new audit checked 180 rational
primal/dual certificates, 72 independently calculated polygon
distances, 3,564 exact score identities, and twelve exact gradient
jumps. Ten local descent cases gave 78 exact zero tangent derivatives
and 26 exact widened interpolations. The exact integers 144 and 81
provide a second check independent of floating-point norm evaluations.
Actual niceness was 20 and peak RSS below 17 MB, despite the wrapper's
denied priority adjustment. Details and results are in [LOG.md](LOG.md),
[AUDIT.md](AUDIT.md), and the two results JSON files.

What failed: the naive additive baseline cost overcounts; coincident
hyperplanes must be merged before summing kink costs. The final
formula handles both issues. No final assertion or program run failed.

What remains uncertain: GD selection, stationarity of alternative
representations, population risk of minimum-norm interpolants, and
the random-gap dependence needed for an asymptotic norm comparison
at the prescribed width n^(-3). The finite sample example does not
establish failure of benign overfitting. No GD generalization theorem
or impossibility theorem is proved.

Next worker: determine whether **any** finite representation of one
of these narrow scores can satisfy the unit-margin parameter KKT
conditions. Proposition 4 excludes the displayed realization, while
Theorem 1 describes all intrinsic-cost freedom through the linear
allocation coefficients. Extending the feasible-descent obstruction
across that freedom would make the selection limitation a statement
about the score rather than one parameterization. A separate dynamical
argument would still be needed to settle T265.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 06:26 Asia/Tbilisi.
