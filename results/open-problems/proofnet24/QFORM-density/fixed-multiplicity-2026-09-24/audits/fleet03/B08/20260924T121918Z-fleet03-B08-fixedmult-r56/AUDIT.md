# fleet03/B08 r56 — second full textual pass, interpolation/rank lens

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T121918Z-fleet03-B08-fixedmult-r56`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Source SHA-256 from the owner manifest: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Verdict

**PASS as a complete textual audit of the 17-eigenvalue candidate.** I reread all 790 manuscript lines in this run and found no fatal mathematical defect. This is another pass by the same logical worker, so it is not a substitute for the owner's requirement of two genuinely separate workers before an independent-validation label.

The theorem audited is the full stated one: arbitrary independent coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0` imply an essentially bounded density with the manuscript's `10000 K^2/s` bound. No continuity claim is made for every branch.

## Range-by-range result

- Lines 1–120: **PASS.** Statement, normalization, Gaussian inversion and scaling preserve every quantifier.
- Lines 121–240: **PASS.** Riesz normalization and singular-value rank inequalities are in the needed directions. The singular Schur-complement limit is valid; see the clarification below.
- Lines 241–359: **PASS.** Heat-flow geometric Brascamp–Lieb, product projection, Fourier powers and decoupling retain original-coordinate independence.
- Lines 360–500: **PASS.** Regularized determinant exponent `-1/8`, crossing-volume expansion, `k=5` direct inversion, `k=3` half-potential use, and local pivot kernels are consistent.
- Lines 500–660: **PASS.** Ordered disjoint-minor sampling, nonsymmetric interpolation, `rank R<=3r`, `rank R[L,L]<=r`, `D=0` on the seed, spectral-to-volume contradiction, and random-cut constants are valid.
- Lines 661–790: **PASS.** Kernel integrals, pivot half-potential, nine-direction half-potential, exhaustive main case split and `K,s` scaling close as written.

## B08-sensitive interpolation check

For disjoint `r`-sets `S,T`, `B=A[S,T]` invertible, and `L` the complement,

`P=A[:,T] B^{-1} A[S,:]`

satisfies exactly

`P[S,:]=A[S,:]`, `P[:,T]=A[:,T]`.

With the manuscript's `E,D,R`,

`R[L,L]=P[L,L]`,

and `Q=R-P` vanishes on rows `S`, columns `T`, and `L x L`. Hence

`Q = Pi_T Q + (I-Pi_T) Q Pi_S`,

so `rank Q<=2r`, `rank R<=3r`, and `rank R[L,L]<=r`. Nonsymmetry causes no difficulty because only rank, singular values and row diagonal dominance are used.

## Singular Schur-limit clarification

A peer improvement note proposed replacing the manuscript's singular-ambient limiting paragraph because the threshold `t-|epsilon|` moves with `epsilon`. I independently checked this. The manuscript's shorter argument is mathematically valid.

Let `q=N_A(t)-k`. For every sufficiently small admissible `epsilon`, the invertible case yields

`N_{S_epsilon}(t-|epsilon|)>=q`.

Equivalently, the `q`-th ordered absolute eigenvalue of `S_epsilon` is at least `t-|epsilon|`. Since `S_epsilon -> S` in operator norm, ordered absolute eigenvalues converge. Taking the limit gives the `q`-th ordered absolute eigenvalue of `S` at least `t`, hence `N_S(t)>=q`. The fixed-`delta` peer proof is a clearer alternative, but the moving threshold does not create a proof gap.

## Reproducibility status

The current manuscript root was relisted in this run. It contains `README.md`, `AUDIT.md`, `manuscript.tex`, `audits/`, and `improvements/`, but still does not contain the README-listed `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, or `checks.json`. Therefore the advertised original finite diagnostics cannot be rerun from the published root as it currently stands. This is a repository/documentation gap, not a dependency of the self-contained mathematical proof.

## Threshold-lowering result from this run

After the full audit, I proved `QFORM-S16-TERMINAL-R4-SATURATION-v1`. In the no-pivot `s_16>=1` chamber, if `V_5<kappa^5`, all earlier ratios are good and the unique obstruction is the `r=4` sampled interpolation. That chamber satisfies, among other exact estimates,

- `s_5(D)<=291/350`;
- `s_12(R)>=297/2800`;
- on four heavy coordinates `H`, `s_4(P[H,H])>=109/700`;
- `|det A[H,T]| |det A[S,H]| >= (109/700)^4 |det A[S,T]|`;
- the three rank-four pieces `P`, `Pi_T(R-P)`, and `(I-Pi_T)(R-P)Pi_S` each have fourth singular value at least `297/2800`.

The complete proof and exact check are in the sibling immutable improvement folder for this run. The result narrows but does not close `17 -> 16`.

## Partner application

I reread and applied fleet04/B08's completed `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1` at an actual fixed-multiplicity inequality. Deleting one original coordinate is a rank-at-most-two change, so `s_5(A)>=1` implies `s_3(C_i)>=1` for every deletion child. Thus if any child spectral window `|lambda(C_i)|>=1/64` has physical leverage at most `1/32`, the full quadratic form has a continuous density bounded by `<64`. After scaling this is `<64 K^2/s`. Therefore every unpaid `s_16` terminal survivor must have a localized `1/64` child window for every deletion.

Partner source: `yspennstate/math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B08/20260923T212412Z-fleet04-B08-QFORM-r2/REPORT.md`.

## Status

- Fixed-multiplicity 17-eigenvalue candidate: **PASS in this review**.
- Fixed-multiplicity 16-eigenvalue theorem: **OPEN**.
- Full three-eigenvalue conjecture: **OPEN**.
- Full-target continuity: **OPEN**.
- Native brain ingestion: **WITHOUT_VERIFIED_BRAIN**.
