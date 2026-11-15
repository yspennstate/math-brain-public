VERDICT: PROVED Finite mean risk at every fixed sample size in d >= 4 for homogeneous minimum-norm ReLU interpolation on the sphere.

Option B is resolved for the predecessors' model. For iid uniform inputs on
S^(d-1), independent Rademacher labels, and every measurable minimum-norm
selection, E[R_n] is finite and strictly positive for every fixed n>=2 and
d>=4. Width is unrestricted or fixed at any m>=n. The objective is one half
the sum of squared parameters in both layers, with no biases, skips or
output intercepts; risk is squared error against the zero regression function.

More generally, the new upper bound proves finite moments for
r<(d-1)/2. Combined with the round-5 lower theorem, this gives, for every
fixed n>=3 and d>=2,

```text
E[R_n^r] < infinity if and only if 0 < r < (d-1)/2,
P(R_n > t) = Theta_{n,d}(t^(-(d-1)/2)).
```

The tail statement gives matching powers, not an exact constant. The
divergence direction is imported from round 5; finiteness and the upper
tail bound are the result beyond the previous reports.

The proof constructs three-ReLU ridge tents that interpolate one sample
and vanish at the others. A tangent-direction lemma controls their cost by
reciprocal projective separation. Linear dependence elimination reduces
the competitor to at most n units without increasing cost. If

```text
delta = min_{i<j} sqrt(1-(x_i.x_j)^2),
K(n,d) = n [2+32(n-1)sqrt(d-1)],
```

every minimum obeys R_n <= K(n,d)^2/(2d delta^2). A spherical pair has
E[sin(angle)^(-2)]=(d-2)/(d-3) for d>=4. Consequently

```text
E[R_n] <= K(n,d)^2/(2d) * binom(n,2) * (d-2)/(d-3) < infinity.
```

PROOF.md includes all construction, compression, existence and integration
steps. The tangent constant has two proofs, and the pair factor is derived
by both integration by parts and beta/gamma identities. This rules out a
second mechanism making the mean infinite at fixed n in d>=4.

The round-6 antipodal result holds. A fresh analytic recheck and independent
scalar verifier recover its dual certificate, minimum cost, cancellation
and finite collision-limit risk. No predecessor file was changed.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 recheck_round6.py > prior_output.txt
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_finite_moments.py > verification_output.txt
```

Both passed. The extension verifier checks 51 configurations in dimensions
2,3,4,5,8,12, including close pairs, near-antipodes, whole clusters and
planar samples in higher dimension. Eleven exact rational compressions
preserve sample responses and reduce cost using at most n units. The
maximum uncompressed interpolation error is 7.45e-10. These are explicit
competitors, not numerical minima. Independent angular integrals verify
the pair factors, both projective caps, and the moment endpoint.
Full outputs, per-case data and resource records are saved in this folder.
The final extension run took 0.1363 seconds and used 17,055,744 bytes peak
RSS, one thread, actual nice 20. The prior recheck took 0.0787 seconds and
used 15,400,960 bytes peak RSS.

What failed: no mathematical check failed. The sandbox denied nice's
attempted adjustment; every run checked inherited nice 20 before computing.
The bounded literature check found no later full resolution; opened primary
sources are listed in LOG.md. No SOLVED_ELSEWHERE.md was warranted.

What remains uncertain: the limit as n tends to infinity in d>=4, typical
risk in every fixed dimension, GD selection, biases, narrower widths, and
other input laws. The displayed mean bound grows with n; fixed-n finiteness
does not establish tempered overfitting. No broader novelty claim is made.

Next worker: use option A to seek a positive lower bound in probability,
or obtain a bound on mean/typical risk uniform in n. The ridge tents here
settle fixed-n integrability but their norm bound is too large for either
large-sample conclusion. Any sharper bound should retain control of both
near-coincident and near-antipodal configurations.

Task: T264, “take the NEXT checkable step on this problem, building on that work” — 2026-11-15 19:25 +04.
