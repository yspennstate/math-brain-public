# fleet01/B10 full audit — fixed multiplicity, auto11

Run: `20260924T132203Z-fleet01-B10-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Current `master` observed immediately before publication: `4cff3d69361219127ce00e43434fa1b50e6bfd3d`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Advertised manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Immediate verdict

**Fatal mathematical gaps found: NONE.** I reread all 790 source lines and independently rechecked every definition, displayed identity, lemma hypothesis, proof transition and the final scaling argument. My verdict on the pinned candidate is **PASS** for

`||p_(X^T A X+b^T X+c)||_infinity <= 10000 K^2/s`

under arbitrary real symmetric `A`, `s_17(A)>=s>0`, arbitrary affine `b,c`, and independent arbitrary real coordinate densities bounded by `K`.

This is one end-to-end worker review, not formal verification or journal peer review, and it does not solve the unrestricted three-eigenvalue conjecture.

A package issue flagged in my preceding B10 run is now **RESOLVED on current master**: `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` are present and were read in full. The newly supplied checker reports PASS on its stated finite suite. Its finite diagnostics remain evidence only, not proof.

## Complete source classification

| Lines | Labels/content | Status | Reason |
|---|---|---|---|
| 1–90 | preamble, theorem/corollary, architecture, normalization | PASS | Quantifiers retain arbitrary dimension/signature/laws and affine terms. `s_j` is correctly singular-value notation; for symmetric `A` this is absolute eigenvalue. The proof explicitly claims essential boundedness, not continuity. |
| 91–160 | `lem:fourier`, `lem:envelope`, `lem:riesz` | PASS | Fourier convention, Plancherel factor `2 pi`, Gaussian regularization, inversion and the Riesz/Gamma constants are consistent. The weighted `3/4` envelope integrates to exactly `12 sqrt(u)`. Rough-law statements are obtained through positive regularization/Tonelli, not pointwise smoothness. |
| 161–217 | `lem:rank`, `lem:schur`, `lem:dd` | PASS | Approximation-number proofs work for nonsymmetric auxiliaries. The Schur count is valid for invertible `A` by inverse-compression/interlacing and for singular `A` by the stated `A+epsilon I` limit. Row diagonal dominance requires no symmetry. |
| 218–301 | geometric BL, product projection, scalar Fourier powers | PASS | Heat-flow sign is the Parseval-frame contraction. Large-time normalization uses `sum c_i=d`. Projection is a deterministic integral change and never asserts independence after rotation. Even Fourier powers are integrable because `|hat f|<=1` and `hat f in L2`. |
| 302–400 | decoupling, regularized determinant, crossing volumes | PASS | Cauchy–Schwarz/Jensen copy structure is correct. In graph BL, the `d_i` powers cancel, `prod c_j^{-c_j/2}<=e^(theta/2)`, and `alpha=(2 pi e)^2` cancels the remaining multiplier. Fourth roots give determinant exponent `-1/8`. Cauchy–Binet and order-3/order-5 uses are correct. |
| 401–482 | square, definite pair, hyperbolic pair | PASS | Square inverse branches, definite polar Jacobian, hyperbolic Jacobian and tail cutoffs have correct factors. Conditioning is always on original coordinates; no rotated-coordinate independence is used. Exceptional critical levels are handled as measure domination. |
| 483–525 | `lem:quarter` | PASS | The sign-cut extracts a physical cross block of norm at least `L/4`. The Gaussian smoothing computation yields the displayed quarter-power coefficient. Layer cake gives the stated logarithmic potential. A sharper rigorous constant is proved separately in this run's improvement note. |
| 526–580 | pivot/volume definition, no-pivot entry bound, `lem:sampling`, `lem:completion` | PASS | `a_ij^2<eta^2+eta`; bordered determinant identity is exact after squaring. Singular deleted seeds justify an inequality, not equality. `P` interpolates rows `S` and columns `T`; `D` vanishes on the seed; `E` has zero diagonal; global `rank R<=3r` and restricted `rank R[L,L]<=r` are both correctly proved. |
| 581–619 | `prop:volume` | PASS | Telescoping bad-ratio selection includes vanishing volumes. For `r>=1`, `epsilon<=(r+1)/80<=1/16`; `m=4k-3>=4r+1`; global rank loss leaves `r+1` large entries of `D` in `L`. Exact manuscript slack is `371/400-23/28=297/2800>0`, contradicting restricted rank. `r=0` is separately valid. |
| 620–645 | random cut, no-pivot analytic consequences | PASS | Each ordered disjoint minor survives with probability `4^{-k}`. The resulting `Z_k^{-1/(2k)}<=160`, `12 sqrt(80e)<200`, and `800e<2400` are correct. |
| 646–724 | singular kernels, `prop:pivot-H`, `prop:nine` | PASS | Kernel integrals, scalar/definite/indefinite conditional domination, Schur hypotheses, and full-versus-truncated half potentials are used correctly. The constant `600` is conservative; it can be reduced rigorously. |
| 725–790 | main theorem, scaling, threshold accounting, limitations, bibliography | PASS mathematically; external priority attribution UNCHECKED | Case split is exhaustive. Scalar pivot leaves >=16 Schur directions and needs nine; indefinite pair leaves >=15 but uses only one. `Y=KX` has cap one and `Q=(s/K^2) Qtilde`, giving exactly `K^2/s`. The final remarks accurately distinguish continuity branches. Classical citation/priority history was not independently re-searched because it is not a proof dependency. |

No mathematical source line remains UNCHECKED in this review. The only UNCHECKED item is external bibliographic/priority history, which has no downstream role because all specialized ingredients used by the theorem are proved in the manuscript.

## Supplementary-file audit

### `proof_map.csv` — PASS
The statement/proof ranges agree with the actual source. It covers every named theorem/lemma/proposition and the main proof. Non-labelled architecture/transition text is not represented as a proof-map row, but was read and checked above.

### `SOURCE_MANIFEST.json` — PASS as metadata
It identifies the baseline source blob, byte/line count, source SHA-256, support-file hashes, build metadata, and correctly states that the compiled PDF is not stored in this GitHub root. I did not independently rebuild the PDF in this connector-only run; that build claim is therefore metadata evidence, not mathematical evidence.

### `verify.py` / `checks.json` — PASS for stated finite scope; universal coverage explicitly NOT claimed
The current suite checks the pinned source hash, exact rational diagonal-dominance arithmetic, exact interpolation identities on random symmetric integer matrices of sizes 4–6 for seed orders 1–2, exact sampled-volume inequalities, and floating diagnostics for Schur counts and graph weights. Reported executed counts are 534 exact interpolation seeds, 18 exact volume cases, 9 strict sampling cases, 240 floating Schur threshold cases, and 30 graph-weight cases.

The checker **does not** computationally cover the terminal `r=3,4` interpolation geometry, all dimensions, hyperbolic/quarter-power integral inequalities, rough-law limiting arguments, or the theorem's final scaling. Those are analytically checked in the manuscript audit above. This is a coverage limitation, not a theorem gap.

The historical self-audit's older/larger diagnostic counts are a different suite. The current `checks.json` correctly does not pretend to reproduce them.

## Exact constants and adversarial diagnostics

The manuscript's core rational slack checks exactly:

- `eta^2+eta=101/10000<1/49`, hence `|a_ij|<1/7` in the no-pivot chamber;
- terminal sampling error `5 sqrt(kappa)=1/16`;
- large residual diagonal `1-1/16-1/100=371/400`;
- rounded off-diagonal bound `1/7+1/16=23/112`;
- original five-coordinate row sum `4(23/112)=23/28`;
- strict dominance slack `371/400-23/28=297/2800>0`.

Three adversarial diagnostics from the previous B10 reconstruction remain valid and were rechecked conceptually here:

1. A nonsingular 2-by-2 extension can have singular deleted 1-by-1 seeds (`[[0,1],[1,0]]`), so the sampling count must be an inequality.
2. The interpolation rank bounds can be simultaneously sharp; direct sums of the explicit `r=1` saturation block realize `(rank R,rank R[L,L])=(3r,r)`. Thus `17 -> 16` cannot come from mere arithmetic tightening of those rank inequalities.
3. At a singular Schur boundary, `A=diag(1,-1,0)` with a one-coordinate pivot gives equality in the spectral-count loss, confirming that the singular limiting argument cannot be strengthened by simply deleting the loss.

These are finite diagnostics only; none is used as a proof premise.

## Review state

- Pinned 17-eigenvalue candidate: **PASS in this complete B10 audit**.
- Mathematical FALSE: none found.
- Mathematical GAP: none found.
- Mathematical UNCHECKED: none in source lines 1–790.
- External priority/bibliographic verification: UNCHECKED, nonessential to proof.
- Current root reproducibility package: present; finite checker PASS on stated scope.
- Full three-eigenvalue conjecture: OPEN.
- Independent-validation label: not self-awarded; separate-review gate still applies.
- Execution state: `WITHOUT_VERIFIED_BRAIN`.

No task/schedule/cadence, enabled/paused state, email/push, authentication, permission, visibility, public-release or paid-call setting was changed.