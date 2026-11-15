# T244 research log

Task received: 2026-11-14 21:22 Asia/Tbilisi (17:22 UTC), “push this problem forward by one checkable piece.”

## Orientation and constraints

Read the startup memory, compute governor state (status ok), and the three existing T244 memory cards. They already record exact one-input moments, hypertree leading cumulants, and a provisional two-input scale-locking claim. Those notes are leads, not proofs. No agents, git, external writes, or heavy computation are used. The folder-only instruction supersedes the older instructions to write mesh/checklist/brain state outside this folder.

## Literature check started 17:22 UTC

Searched the web for deep ReLU cumulants, uniform depth expansions, and 2025–2026 developments. Opened Boris Hanin, arXiv:2204.01058, and its 2024 JMLR paper. Its introduction explicitly fixes finite depth for the all-orders width estimates. Opened Mufan Bill Li, Mihai Nica, Daniel M. Roy, arXiv:2106.04013 (ResNets), and Cameron Jakub, Mihai Nica, JMLR 25(239), 2024 (angles).

A recent relevant preprint is Mihai Nica and Janosch Ortmann, “Para-Gaussian Approximations of Random Deep Neural Networks,” arXiv:2610.37388, v2 30 October 2026. Its arXiv page is open; checking the full text next. No whole-problem solution found so far.

## Choice of piece (before proving it)

Prove an all-orders, depth-uniform **resummed one-input expansion**, including all fixed output-coordinate cumulants. At fixed effective depth t=d/n (d is the number of nonlinear propagation steps), expand in 1/n around the non-Gaussian log-normal variance-mixture moments. Give a computable radius and remainder for each cumulant order and expansion order, rather than an unspecified depth-dependent O term. Compute the first finite-width correction explicitly. This adds quantitative uniformity to the already-recorded exact product formula and leading hypertree coefficients. It does not claim the general multi-input theorem.

Reason: for one input the exact moment factors are finite polynomials in 1/n. Taking their logarithms before expanding resums the powers of depth and permits elementary complex-analytic remainder bounds. This avoids treating a fixed-depth remainder as if it were uniform. The same argument may provide a target form for the unresolved multi-input result.

## Literature check completed (within ten minutes)

Opened the full 34-page Nica–Ortmann PDF at https://arxiv.org/pdf/2610.37388. Its main results concern para-Gaussian fourth-cumulant approximations and recursions; it does not state the requested all-orders depth-uniform ReLU result. The fetched PDF identifies itself as v1; the arXiv abstract page reports v2, so conclusions about v2 beyond its abstract remain limited. The check found relevant recent work but no whole-problem settlement. No SOLVED_ELSEWHERE.md is warranted.

Hanin's JMLR Corollary 8, equation (19), explicitly says the width-error constants may depend on L. Appendix B.2.1, equation (76), already records the normal-times-log-normal one-input limit. Thus that limit itself is not claimed as a new result here.

## Proof development

The candidate first logarithmic moment coefficient is
b_j = -25/2 binom(j,2) - 31 binom(j,3).
It follows from E Y^r = 2^(r-1)(2r-1)!! for Y=2 ReLU(G)^2: cumulants of Y start 1, 5, 44, 558. Independent exact checks will use conditioning on the binomial number of active neurons, not this cumulant calculation.

A connected hypergraph representation also gives a direct uniform bound for the one-input cumulants. This will be proved alongside the resummed expansion and used to distinguish the two expansion parameters.

## First independent verification

Command:
```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py > verification.txt
```
The run finished in under one second and used only the Python standard library. Exact output is in verification.txt; complete rational polynomials and high-precision expansion data are in verification.json. All checks passed: 96 independent binomial/chi-square moment comparisons (n=1..12, orders 1..8), 8 independent Catalan cumulant checks, 9 logarithmic coefficient checks, 28 fixed-depth cancellation checks, and 9 explicit connected-hypergraph enumerations (orders 2..4, depths 1..3).

The launch printed `nice: setpriority: Operation not permitted` but still executed the script. Checking the inherited priority before doing further computation; no CPU-intensive run is needed. This limitation must not be silently reported as successful priority enforcement.

## Proof saved

PROOF.md now proves three compatible statements for one input and Gaussian weights:

- Exact connected hypergraph expansion and coefficient majorant P_{k,h}(d) <= d^h [u^h] exp(S_k(u)), where S_k(u)=sum_{r=2}^k binom(k,r) lambda_r u^(r-1).
- Explicit two-sided constants for kappa_k(Q) of order (d/n)^(k-1), uniformly for all n and 1<=d<=cn, with a uniform truncation bound at every cost order.
- An all-orders expansion kappa_k(Q)=sum_{m=0}^p n^(-m) B_{k,m}(d/n)+E, with a fully specified Cauchy radius and |E| <= (4k W_k/r_k) t exp(kc/r_k) (n r_k)^(-p-1). The first correction is explicit.

The normal-times-log-normal limit is proved directly by a triangular-array CLT, excluding bad factors by a fourth-moment union bound. This avoids two errors: taking log of a zero factor, and identifying a log-normal law from moments alone.

## Adversarial audit and second verification

Checked the normalization independently by deriving scalar Gaussian-mixture cumulants from their even moments: all 8 orders agree with (2k-1)!! times the variance cumulant. Checked the sample-mean cumulants independently from the Catalan generating function, the moments independently from a binomial/chi-square mixture, and the connected cancellation independently by direct enumeration. Checked the first finite-width corrections against a separate partition sum at t=1/10, 1/2, 1 and four increasing widths (36 numerical rows, 90-digit arithmetic).

Re-derived the explicit Cauchy remainder powers: its p=1 specialization has r_k^(-3), not r_k^(-4). The proof now gives r_k^(-3). The earlier r_k^(-4) would have been a valid but unnecessarily weaker bound because r_k<=1.

The second run used the same exact command as above and added 28 exact coefficientwise majorant tests and 8 scalar-output tests. Full output:
Y cumulants: 1, 5, 44, 558, 9264, 190320, 4662720, 132718320
a_2, a_3, a_4: [['1', '5'], ['1', '15', '44'], ['1', '30', '251', '558']]
PASS: 96 exact binomial/chi-square moment comparisons
PASS: 8 Catalan checks and 9 logarithmic-coefficient checks
PASS: 28 fixed-depth cancellation/positivity checks
PASS: 28 exact coefficientwise depth-uniform majorant checks
PASS: 8 independent scalar-output cumulant/pairing-factor checks
PASS: 9 independent connected-hypergraph comparisons
PASS: leading coefficients P_2=5d, P_3=75d^2-31d, P_4=2000d^3-1860d^2+418d
Resummed errors for k=4, t=1/2:
 n=512: n|err0|=290155867, n^2|err1|=1.78478119e+10, n^3|err2|=8.41239306e+11
 n=1024: n|err0|=306813403, n^2|err1|=1.86383078e+10, n^3|err2|=8.73010853e+11
 n=2048: n|err0|=315709980, n^2|err1|=1.90564249e+10, n^3|err2|=8.89717832e+11
 n=4096: n|err0|=320309907, n^2|err1|=1.92715488e+10, n^3|err2|=8.98288114e+11
Data: verification.json
Resources: {'nice_priority': 20, 'elapsed_seconds': 0.06810741702793166, 'max_rss_bytes': 16384000}

Priority is resolved: os.getpriority reports nice priority 20 already inherited. The attempted additional `nice -n 15` increment is denied, but the computation itself stays at the inherited lower priority 20. `ps` was unavailable in this sandbox, so priority was measured inside the Python process. Peak RSS was 16,384,000 bytes, elapsed script time about 0.068 seconds, single standard-library process. No long-running simulation was used.

Cases inspected: d=0; d=1 (leading coefficients reduce to lambda_k); n=1; all-zero next layer; repeated versus distinct output coordinates; nonzero input normalization; t=0; all finite positive t; and the distinction between a fixed-k cumulant expansion and a full source/density series. Only positive multiples of one input reduce to the scalar result. General distinct inputs do not.

The constants are conservative and can be enormous at high cumulant order or effective depth. The data demonstrate the expected orders, not sharp constants. No distributional error rate is claimed; the uniform quantitative rate proved here is for each fixed cumulant/moment order.

## Finished

REPORT.md saved with verdict PROVED for the one-input special case. General multi-input uniformity is explicitly unresolved. Deliverables are PROOF.md, REPORT.md, LOG.md, verify.py, verification.txt, and verification.json. No files outside this folder were edited.

Task: “push this problem forward by one checkable piece” — 2026-11-14 21:22 Asia/Tbilisi.
