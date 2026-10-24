# account03/B10 r11 — end-to-end fixed-multiplicity audit and exact-arithmetic review

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T141329Z-account03-B10-QFORM-FM-audit-r11`  
Role lens: constants, exact arithmetic, adversarial finite examples, with account03 emphasis on exact identities and alternative derivations.  
Pinned manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Executive verdict

**Pinned 17-eigenvalue manuscript: PASS in this independent B10 mathematical audit.** I read the complete 790-line source and support package and independently rechecked the dependency chain used by the main theorem. I found no fatal mathematical defect in the stated theorem

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary dimension, real symmetric `A`, arbitrary affine terms, and independent real coordinate densities bounded by `K`.

This is one worker review, not formal verification. The manuscript's baseline conclusion is an essentially bounded density; it does not claim global continuity. The unrestricted three-eigenvalue conjecture is not proved by the manuscript.

A separate improvement artifact from this same run proves a sharpened invertible-seed overlap-one compiler and pushes the **structural** no-pivot terminal boundary to `s_7`; it does not close the bounded-density theorem at seven.

## Line-by-line proof-map verdict

| Source range / label | Verdict | Independent check |
|---|---|---|
| 1–83, theorem statement and architecture | PASS | Quantifiers retain arbitrary dimension, signature, residual spectrum, affine terms and rough independent coordinate laws. Scaling target is `K^2/s`; no rotation-independence shortcut is asserted. |
| 84–120, `lem:fourier` | PASS | Fourier convention, Gaussian transform, approximate identity, Plancherel factor `2pi`, inversion factor `1/(2pi)`, and Gaussian smoothing identity are consistent. |
| 122–130, `lem:envelope` | PASS | `int min(1,(a/|t|)^p)=2ap/(p-1)`; inversion gives `ap/[pi(p-1)]`. |
| 132–160, `lem:riesz` | PASS | Gamma representation and substitution yield coefficient `1/sqrt(2pi)`; weighted power-envelope integral is `12 sqrt(u)`. |
| 169–181, `lem:rank` | PASS | Both statements follow from Eckart–Young/min-rank approximation and are valid for nonsymmetric auxiliary matrices. |
| 183–207, `lem:schur` | PASS | Singular ambient case is valid. Equivalently, the exact rank decomposition `A=UBU^T+diag(0,S)` gives `s_{j+k}(A)<=s_j(S)` directly; no symmetry of the auxiliary low-rank term is required. |
| 209–217, diagonal dominance | PASS | Standard max-coordinate proof; applies to nonsymmetric `R[H,H]`. |
| 221–255, geometric BL | PASS | Heat-flow sign is correct from the Parseval-frame contraction; large-time normalization uses `sum c_i=d`; small-time step is justified a.e. and then monotone approximation. |
| 258–282, product projections | PASS | Deterministic orthogonal change is only in the integral. `b_i=0` factors are safely dropped; the entropy estimate yields `e^{d/2}` without claiming projected independence. |
| 284–301, scalar Fourier powers | PASS | Difference density is cap one; the even-power characteristic function is integrable; projection of `2m` signed independent coordinates has coefficient norm `sqrt(2m)`. Constant `2pi sqrt(2e)/sqrt(p)` follows from `m=floor(p/2)>=p/4`. |
| 310–324, decoupling | PASS | Cauchy–Schwarz and independent copy are applied to original product coordinates. The fourth-power line follows by Jensen after the second-power bound. |
| 326–373, regularized determinant | PASS | Frame identity, Jacobian `det(H)^(-1/2)`, weights `c_j,d_i`, scalar Fourier power at `p=2/d_i`, entropy factor, and `alpha=(2pi e)^2` cancel correctly. Fourth root gives exponent `-1/8`. |
| 386–400, volume envelopes | PASS | Cauchy–Binet coefficient is `Z_k`; keeping the `k`th term gives exponent `k/4`. `k=5` gives `5e Z_5^{-1/10}` and `k=3` gives the stated half-Riesz bound. |
| 404–414, square profile | PASS | Two inverse branches give the `|z-v|^{-1/2}` envelope; interval-preimage length constant is valid. |
| 423–434, definite pair | PASS | Completion and deterministic diagonalization are legal; Jacobian in `(delta,theta)` is `1/(2 sqrt(det B))`, giving `pi M/sqrt(det B)`. |
| 437–482, hyperbolic pair | PASS | Hyperbolic parameterization and Jacobian check. Original-coordinate tail selection avoids rotated-independence claims. Tail rearrangement uses only density cap and mass one. Final `Lambda>=2/sqrt(D)` substitution is in the correct direction. |
| 485–525, quarter-power concentration | PASS | Large diagonal branch is direct. Off-diagonal sign cut gives `||M||>=L/4`; determinant theorem gives the `1/4` Fourier power. Gaussian small-ball integration scales as `(rho/L)^{1/4}`. Layer cake gives `4+4 log 16`. |
| 528–564, sampled interpolation | PASS | Ordered disjoint-minor convention is consistent. Bordering identity is exact for nonsingular seeds; singular seeds explain why the aggregate count is an inequality. Multiplicity at most `(r+1)^2` is correct. |
| 566–580, completion | PASS | `D` vanishes on seed, `E` has zero diagonal, `R[L,L]=P[L,L]`, restricted rank `<=r`, and global `rank R<=3r`. Nonsymmetry is harmless because later perturbation is in singular values. |
| 582–619, spectral-to-volume | PASS | Telescoping ratio selection is correct including first-zero volume. For `r>=1`, `m=4k-3>=4r+1` forces `r+1` large entries of diagonal `D` outside the seed. Exact dominance slack is positive; restricted rank then contradicts invertibility. |
| 621–630, random cut | PASS | Each ordered disjoint pair crosses in the prescribed orientation with probability `4^{-k}`. |
| 632–645, no-pivot consequences | PASS | `Z_k^{-1/(2k)}<=160`; constants `<200` and `<2400` follow from the earlier envelopes. |
| 654–674, singular kernels | PASS | Near/far split gives the displayed safe constants. The logarithmic-kernel rearrangement is valid through superlevel intervals and Tonelli. |
| 676–714, pivot half potential | PASS | Scalar branch correctly uses a surviving Schur eigenvalue only to control the logarithmic moment of the remainder; definite and indefinite pair branches are uniform after conditioning on original coordinates. |
| 716–724, nine-direction half potential | PASS | No-pivot branch supplies a full half-potential; pivot branch supplies truncated potential plus the outside-kernel bound one. No truncated/full confusion remains. |
| 726–749, main theorem | PASS | No-pivot `s17`, scalar pivot leaving at least 16 (hence 9), definite pair, and indefinite pair leaving at least 15 (hence one) exhaust the cases. Final normalized maximum is `6010<10000`. |
| 751–790, scaling and limitations | PASS | `Y=KX`, `A/s`, and `Q=(s/K^2) Qtilde` yield exactly `K^2/s`. The manuscript correctly limits itself to essential boundedness and does not claim `s3`. |

No source range in the pinned manuscript remains `UNCHECKED` in this run.

## Exact arithmetic checks

The numerical margins used in the most sensitive algebraic passage check exactly:

\[
1-\frac1{16}-\frac1{100}=\frac{371}{400},
\]

\[
4\left(\frac17+\frac1{16}\right)=\frac{23}{28},
\]

and therefore

\[
\frac{371}{400}-\frac{23}{28}=\frac{297}{2800}>0.
\]

Also `(r+1)/80<=5/80=1/16` for the only required `r<=4`, `2eta=1/50<1/49`, and the final scalar-pivot branch is exactly bounded by `10*601=6010<10000`.

The repository's supplied finite checker reports 534 exact interpolation seeds, 18 exact volume comparisons, 240 numerical Schur-threshold cases and 30 graph-weight cases. I treat these only as diagnostics; the verdict above comes from the analytic reconstruction.

## A real proof-interface correction in a newer supporting report

I compared the current multiplicity-eight overlap work. A contemporaneous account03/B16 supporting report writes

`W_{2,1}/V_2 = E sum_h D_h^2`

for the **unrestricted** overlap-one volume. That equality is not generally valid: determinant-squared seed sampling omits singular order-two seeds, while a singular seed can have a nonzero same-index bordered order-three minor. The correct statements are

\[
\frac{W_{2,1}}{V_2}\ge\mathbb E\sum_hD_h^2
\]

or the exact identity with the invertible-seed volume `W^times_{2,1}`. This does not invalidate the reported lower bound, because replacing equality by `>=` only strengthens the conclusion. It does matter for later algebraic shears, where invertibility of the seed is required.

The improvement artifact in this run uses `W^times_{2,1}` throughout and therefore has an exact source-preserving identity.

## New structural improvement from this audit

The separate file

`improvements/account03/B10/20260924T141329Z-account03-B10-QFORM-FM-audit-r11/S7_OVERLAPONE_SHARPENING.md`

proves

\[
W^{\times}_{2,1}(A)
\ge V_2(A)\left(s-3\sqrt{V_3(A)/V_2(A)}\right)_+^2
\quad\text{if }s_7(A)\ge s,
\]

and twice that right side if `s_8(A)>=s`. In the normalized no-pivot `s7` state this yields the exact dichotomy

\[
V_3\ge\kappa^3
\quad\text{or}\quad
W^{\times}_{2,1}>\frac{5929}{262144000000}.
\]

The proof retains the positive quadratic term by convexity/Jensen and reveals that one forced diagonal residual already appears at spectral count seven after the global rank-six interpolation correction. This is a structural reduction only. A product-preserving overlap-one density receiver is still missing.

I also supplied an explicit `r=1` completion with `rank R=3`, showing the manuscript's global `3r` rank cost is already sharp for the present algebraic construction. Therefore simply claiming a `2r` global correction cannot lower the threshold.

## Status after this run

- Pinned 17-eigenvalue theorem: **PASS** in this independent audit.
- Nine-eigenvalue replacement found in the repository: appears complete and separately reconstructed by multiple workers; release/promote status belongs to owner/B20 synthesis, not this report.
- New `s7` structural no-pivot dichotomy: **PROVED SUPPORTING THEOREM**, not a density theorem.
- Seven- and eight-eigenvalue full density conclusions: **OPEN** at the shared-anchor overlap-one analytic receiver.
- Original three-eigenvalue conjecture: **OPEN**.
- Global continuity for the original target: **OPEN**.

Execution label: `WITHOUT_VERIFIED_BRAIN`; repository reads/writes occurred, but no authenticated native learned-memory retrieval/receiver-use evidence was available.
