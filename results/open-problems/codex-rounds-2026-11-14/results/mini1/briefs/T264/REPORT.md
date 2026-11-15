VERDICT: PARTIAL Exact two-sample minimum-norm ReLU risk and moment threshold in fixed dimension.

For two independent uniform points on S^{d-1} with independent Rademacher label noise, `PROOF.md` identifies the exact minimum-parameter-norm homogeneous two-layer ReLU interpolant. The width may be any value at least two. The objective is one half the sum of squared parameters in both layers, with no skip or output intercept.

For opposite labels and sample angle theta <= pi/2, the minimum objective is `2/sin(theta)`, and the conditional squared excess risk is exactly

```text
R_d(theta) = [pi - sin(theta) + theta*cos(theta)] / [pi*d*sin(theta)^2].
```

Thus `R_d(theta) ~ 1/(d*theta^2)` at small separation. The proof gives the obtuse-angle formula as well and proves uniqueness as a function through equality in an explicit dual certificate.

Writing `C_d = Gamma(d/2)/(sqrt(pi)*Gamma((d-1)/2))`, the unconditional risk tail is

```text
P(R > t) ~ C_d / [2*(d-1)*d^((d-1)/2)] * t^(-(d-1)/2).
```

Consequently `E[R^q]` is finite exactly when `q < (d-1)/2`. The mean squared excess risk is infinite in d=2 and d=3, and finite and positive in d>=4. Every sampled network has finite conditional risk almost surely. These statements concern sample size two, not a large-sample limit.

Two exact opposite-label conditional means are

```text
d=4: 3/8 + 1/(3*pi) - 13/(9*pi^2) = 0.334750474578...
d=5: 55/256 = 0.21484375.
```

The same tail coefficient and moment threshold hold when hidden biases are included and penalized in the Euclidean parameter norm. The proof gives an explicit minimizer and elementary pointwise bounds. Separately, homogeneity transfers the homogeneous result to a full-dimensional annulus: `X=rho*U`, `Y=rho*epsilon`, with rho uniform on [1,2]. The input density is bounded above and below on the annulus, label noise is bounded and heteroscedastic, and all risks are multiplied by `7/3`.

The bounded literature search found no complete resolution of the stated fixed-dimension problem. Opened primary sources and their scope are listed in `LOG.md`. In particular, [Park, Blöbaum and Kasiviswanathan, arXiv:2410.06191](https://arxiv.org/html/2410.06191v1) require growing dimension; [El Harzli, Nam, Kuzborskij, Cuenca Grau and Louis, arXiv:2602.13910](https://arxiv.org/html/2602.13910v1) give conditional stability results; and [Li, Shi and Zhou, arXiv:2611.01105](https://arxiv.org/html/2611.01105v1) address noise-free variation-space approximation. No `SOLVED_ELSEWHERE.md` was created.

Reproduction, from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_two_point.py > verification_output.txt
```

The final run passed all assertions in 1.57 seconds, with peak RSS 15,826,944 bytes, one thread, and actual nice value 20. The sandbox denied `nice`'s attempted adjustment; the inherited priority already met the requirement, and the script asserts it. Complete output is in `verification_output.txt` and `LOG.md`; data are in `verification_data.json` and `angle_checks.csv`.

Checks include direct circle integration of the network, separate S^2 surface quadrature, exhaustive planar atomic pricing, direct interpolation, biased pointwise bounds, gamma normalizers checked by a sine-integral recurrence, risk-tail constants, and independent quadrature of both finite conditional means and the radial multiplier. The maximum relative circle-risk discrepancy was 2.87e-9. The linear odd component gives a separate analytic derivation of the singular coefficient.

The first audit failed a 3e-5 tolerance with a coarse three-dimensional quadrature grid. Refining that grid resolved the discrepancy. No mathematical claim was changed to accommodate the failure.

What remains uncertain: whether a close pair still forces comparable global risk after arbitrarily many further interpolation constraints; whether corresponding estimates hold for a full-dimensional design with independent homoscedastic noise and penalized biases; and the relationship to GD-selected interpolants. Infinite mean risk at n=2 supplies no conclusion about convergence in probability, or expected risk, as n tends to infinity. No novelty claim is made for the elementary two-point optimization itself.

The next worker should solve the three-constraint atomic problem for a close opposite-label pair and a third point at a fixed nonzero angle. Determine whether the forced odd linear component persists or is canceled by additional optimal atoms. This tests the precise obstruction to extending the present calculation beyond two observations. Any asymptotic statement should specify whether risk is conditional, averaged over training samples, or controlled in probability.

Task: T264, "push this problem forward by one checkable piece" — 2026-11-14, approximately 21:23 +04.
