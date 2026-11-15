VERDICT: PROVED one-input uniform cumulant bounds and an all-orders resummed 1/width expansion

For a critical zero-bias ReLU network with independent Gaussian weights, one nonzero input, and any fixed finite set of preactivation coordinates, PROOF.md gives an explicit remainder uniform for d<=cn, where d=L−1 is the number of nonlinear propagation steps. This settles a special case of T244, not the general multi-input problem.

The exact normalized output cumulant is

κ₂ₖ(Z)/Var(Z)^k=(2k−1)!! κₖ(Q),
Q=∏_{ℓ=1}^d [(1/n)∑_{i=1}^n 2 ReLU(G_{ℓi})²].

What is proved:

- An exact finite expansion κₖ(Q)=∑_{h>=k−1}Pₖ,h(d)n^(−h), with nonnegative coefficients and an explicit coefficient majorant. Equation (14) gives a uniform remainder after every truncation. Equation (17) gives explicit positive lower and upper constants times (d/n)^(k−1), valid at every width and 1<=d<=cn.
- A resummed expansion κₖ(Q)=∑_{m=0}^p n^(−m)Bₖ,m(t)+E, t=d/n. Equations (19)–(23) specify every coefficient and give
  |E| <= (4kWₖ/rₖ)t exp(kc/rₖ)(nrₖ)^(−p−1), n>=2/rₖ.
  The finite constants Wₖ and rₖ are explicit. The first finite-width correction appears in (25). This series is in 1/n around the non-Gaussian effective-depth limit.
- The fixed-d expansion is in 1/n; its uniform size estimates use d/n. The leading fixed-depth coefficients are 5d, 75d²−31d, and 2000d³−1860d²+418d. Their finite-depth corrections cannot be discarded when d stays small.
- A direct proof of Q ⇒ exp(√(5t)N−5t/2), including the zero-factor event. The output limit is a Gaussian times an independent log-normal scale. Its normalized fourth cumulant is 3(e^(5t)−1). This limiting law is established background; no novelty is claimed for it.
- There is no finite positive breakdown value of t for this fixed-order resummed expansion: every finite c is allowed. Gaussian leading-order asymptotics require t→0. Fixed-k limiting cumulants are entire in t, but a full source/moment series has zero radius for every t>0. These statements must be kept separate.

Verification command, run in this folder:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py > verification.txt
```

All checks passed. They include 96 exact comparisons against the independent binomial/chi-square representation, 8 Catalan cumulant checks, 9 logarithmic coefficient checks, 28 fixed-depth cancellation checks, 28 coefficient-majorant checks, 8 independent output normalization checks, and 9 direct connected-hypergraph enumerations. There are 36 high-precision effective-depth/width/order rows checking the first two corrections. Exact output is in verification.txt and all data are in verification.json. Runtime was about 0.068 seconds and peak RSS 16,384,000 bytes. The inherited nice priority was 20; `nice` could not add another 15 and printed a warning, but the computation already ran at the lower priority 20. Only standard-library Python was used, with no worker threads or subprocesses.

The audit re-derived the first correction through an independent logarithmic recurrence, checked the pairing normalization directly from scalar even moments, and inspected d=0, d=1, n=1, extinct layers, t=0, and repeated or distinct output indices. It corrected the displayed p=1 remainder specialization to the sharper power rₖ^(−3). LOG.md contains the steps and complete output.

Literature check: within ten minutes, opened Boris Hanin's arXiv:2204.01058 and 2024 JMLR article, and the recent Mihai Nica–Janosch Ortmann preprint arXiv:2610.37388. The former explicitly permits depth-dependent width-error constants in Corollary 8; the latter develops fourth-cumulant approximations and recursions. No whole-problem settlement was found. The fetched recent PDF was marked v1, whereas its arXiv page reports v2; the full revised text was not verified. References and links are in PROOF.md. No SOLVED_ELSEWHERE.md was created.

What did not extend: for different inputs, the conditional covariance is a random matrix. Its entries do not share the independent scalar-factor representation used here. The provisional scale-locking claims in earlier T244 memory cards were not used as premises. No general multi-input limiting law or cumulant expansion has been proved in this session.

Limitations and uncertainty: Gaussian weights are assumed; the variance specification alone does not define a universal finite-width law. Constants are conservative and can be very large. The remainder estimates are for fixed moment/cumulant order, not for densities or growing cumulant order. No distributional convergence rate or novelty priority is claimed.

Next worker: start with the multi-input fourth cumulant. If K_ab is the conditional output covariance and q_a the single-input variance, seek

|Cov(K_ab,K_cd)| <= C_c (d/n) sqrt(q_a q_b q_c q_d)

uniformly for d<=cn. Conditional Gaussianity converts this into a uniform fourth-cumulant bound. Higher covariance cumulants would then be the exact targets for the remaining all-orders question. The scalar formulas here provide regression checks and an explicit benchmark for the remainder convention.

Task: “push this problem forward by one checkable piece” — 2026-11-14 21:22 Asia/Tbilisi.
