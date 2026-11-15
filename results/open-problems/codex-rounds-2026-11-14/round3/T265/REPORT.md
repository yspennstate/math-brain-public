VERDICT: PARTIAL explicit Bayes-consistent bias-free ReLU interpolation when n/d diverges; GD selection remains unresolved

The earlier affine obstruction is correct. An independent likelihood derivation recovers its interpolation bound; recheck.py verifies its numerical example and ten exact lower-tail inequalities. The bounded literature check found no verified solution of the main GD/ReLU question. Opened sources and their scope are in [LITERATURE.md](LITERATURE.md).

The new result is an explicit *data-only* interpolation rule for the same noisy Gaussian mixture, in every d>=2. It uses at most 6n+2 bias-free two-layer ReLU neurons and satisfies f_n(X_i)=Y_i exactly. It starts with the sample-mean linear score g_n(x)=(n^{-1}sum_i Y_i X_i)^T x, then adds triangular corrections on pairs of narrow antipodal cones. The conditional population probability that f_n and g_n differ as scores is at most

\[
\frac{2C_s}{n^2},\qquad C_s=\frac1\pi+\frac{s}{\sqrt{2\pi}},
\quad s=\|\mu\|/\sigma.
\]

Let alpha=eta+(1-2eta)Phi(-s), the Bayes classification risk, and V=(d+4eta(1-eta)s^2)/n. For s>0,

\[
\mathbb E R(f_n)-\alpha\le
\sqrt{\frac2\pi}\min\left\{\sqrt V,
\frac{V}{(1-2\eta)s}\right\}+\frac{2C_s}{n^2}.
\]

The square-root bound remains valid at s=0. Thus the rule is Bayes consistent for bounded signal strength when n/d tends to infinity, and has an O(d/n+n^{-2}) excess-risk bound for fixed s>0 and fixed eta<1/2. Combined with the earlier result, this gives a concrete interpolating classifier that differs from every affine classifier on Theta(n) training decisions while disagreeing with its own affine baseline on vanishing population probability. This settles the representational part of the earlier localization target. It does not provide the GD trajectory requested in the main problem.

For the earlier example n=10000,d=20,s=2,eta=0.1, the width bound is 60002, the score-disagreement bound is 2.2323889e-8, and expected excess classification risk is at most 0.00106918764. Bayes risk is 0.11820010556. These are evaluations of proved bounds, not training measurements.

The full proof, including the zero-signal and zero-baseline cases, measurability, exact neuron coefficients, and parameter costs, is in [PROOF.md](PROOF.md). This is an elementary construction; no novelty claim relative to all prior interpolation constructions is made.

Run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit.py
```

Both exited 0. The final construction audit checked 360 exact triangular identities, 139 exact network evaluations, 42 Gaussian density values, six density normalizations, 18 cone-mass bounds, exact sample-mean moments, and 72 baseline-risk cases. Cartesian and polar calculations independently verify the density constant; exact rational arithmetic checks the finite networks and the numerical risk factor. Output is in [LOG.md](LOG.md), [recheck_results.json](recheck_results.json), and [audit_results.json](audit_results.json). Both runs took less than a second, used about 15–16 MB RSS, and verified actual niceness 20 despite the sandbox denying the wrapper's priority adjustment.

What failed: isolated one-sided cones conflict with the shallow network's linear odd part; paired cones are necessary for this construction. Exact projected ray collisions cannot be handled in general, though they occur with probability zero here. A nearly antipodal test originally needed no correction; changed labels forced nonzero corrections and the revised audit passed. No failed mathematical assertion remained. See [AUDIT.md](AUDIT.md).

What remains uncertain: GD selection, fixed-width behavior, norm control, and finite-precision stability. The construction can have enormous path norm; one stress sample reaches about 2.56e26. Nothing here shows that a margin or norm minimizing GD limit chooses these cones. No population squared-loss or minimax-rate claim is made.

Next worker: analyze the implicit objective before attempting a trajectory theorem. Determine whether a maximum-margin or minimum-path-norm bias-free ReLU interpolant can have the required paired-cone localization. Compare its norm against a less localized interpolant; Section 7 supplies exact costs and a lower bound for the constructed corrections. A GD result requires a separate selection or dynamical argument. Existence alone is now verified for this mixture.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 03:40 Asia/Tbilisi.
