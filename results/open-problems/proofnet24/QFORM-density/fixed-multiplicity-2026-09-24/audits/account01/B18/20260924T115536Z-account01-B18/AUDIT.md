# account01/B18 end-to-end audit — QFORM-FIXED-MULTIPLICITY-AUDIT-20260924

## Source pin and scope

- Baseline source commit requested by owner: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Fresh `master` read of `manuscript.tex` has Git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, exactly the blob named by the owner objective and baseline materials.
- Recorded SHA-256 in the owner objective/self-audit: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`. I pinned this value but did not independently recompute SHA-256 from a local byte-for-byte checkout; the Git blob itself was independently fetched and read in full.
- `manuscript.tex` was read in full, lines 1–790. `README.md` and `AUDIT.md` were read in full.
- The files `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` return 404 at the specified root on fresh `master`. Therefore their claimed contents/tests are **UNCHECKED / MISSING FROM CURRENT ROOT** in this review. The finite-check claims in `AUDIT.md` are not treated as evidence here.

## Overall verdict

**GAP (repairable), not FALSE.** I found one genuine proof gap in the written baseline: the singular-matrix limiting paragraph of Lemma `lem:schur` does not justify passage at the moving threshold `t-|epsilon|`. The lemma itself is true and the gap has a short rigorous repair, supplied separately in this run under `improvements/account01/B18/.../SCHUR_REPAIR.md`. Every downstream use is repaired by that replacement proof.

Apart from that written gap, my independent reconstruction found no second mathematical defect in the 17-eigenvalue argument. In particular, I checked the nonsymmetric interpolation support, both rank bounds, seed vanishing of `D`, the spectral-to-volume count, Fourier normalization and powers, heat-flow limits, rough-law/Tonelli formulations, and full-versus-truncated half potentials. This is **one** account01/B18 review and does not by itself satisfy the owner's two-genuinely-separate-review validation gate.

## Fatal issues first

### GAP-1 — singular Schur spectral-count limit

**Range:** manuscript lines 183–207, specifically the singular case at lines 205–207 (`lem:schur`).

**Written step:** for singular `A`, the manuscript regularizes by `A+epsilon I`, invokes the invertible case at threshold `t-|epsilon|`, then says continuity of ordered eigenvalue moduli yields `N_S(t) >= N_A(t)-k`.

**Why this is a gap:** although `S_epsilon -> S`, an eigenvalue of `S` equal to or just below `t` may approach at speed `C|epsilon|` with `C>1`; continuity alone does not allow a count at the moving threshold `t-|epsilon|` to pass directly to the count at `t`.

**Repair:** fix an arbitrary `delta in (0,t)`, choose invertible regularizations with `|epsilon|<delta/2`, apply the invertible case at the fixed threshold `t-delta`, pass `epsilon->0`, and only then let `delta downarrow 0`. Full proof is in `SCHUR_REPAIR.md`.

**Downstream impact:** scalar-pivot truncated half potential, scalar-pivot branch of the main theorem, and indefinite-pair main branch cite `lem:schur`; all are restored by the replacement proof. No change of constants or hypotheses is needed.

### GAP-2 — reproducibility bundle is incomplete at the stated root

**Range:** repository packaging, not a mathematical line of `manuscript.tex`.

`README.md`/owner instructions name `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`, but all four are absent (404) from the specified root on fresh `master`. Thus the advertised finite diagnostics cannot be independently rerun from this package. This does **not** refute the theorem because the proof is self-contained in `manuscript.tex`; it does prevent this run from validating the computational/reproducibility claims.

## Complete line coverage

Every source line 1–790 is covered below. `PASS` means I reconstructed the mathematical step without relying on the self-audit. `GAP` is the issue above. No range is silently omitted.

| Lines | Status | Independent reconstruction / reason |
|---|---|---|
| 1–35 | PASS | LaTeX definitions/macros and metadata only; no mathematical dependency hidden in macros. |
| 36–80 | PASS | Abstract and theorem quantifiers agree: arbitrary dimension, independent real coordinate densities `<=K`, symmetric `A`, arbitrary affine `b,c`, `s_17(A)>=s`; no continuity claim in the theorem. Normalized architecture correctly separates pivot/no-pivot branches. |
| 81–120 | PASS | Fourier convention is internally consistent. Gaussian kernel has transform `e^{-epsilon t^2}`. Plancherel normalization is `2pi`; inversion is `(2pi)^{-1}`. Gaussian inversion coefficient `1/(2 sqrt(pi v))` is correct. Approximate-identity and weak-limit argument is valid for rough laws. |
| 121–180 | PASS | Power-envelope integral is exact. Riesz/negative-half-moment representation has correct Gamma exponent and coefficient `1/sqrt(2pi)`; weighted `3/4` envelope integrates to `12 sqrt(u)`. Singular-value perturbation/rank approximation is valid for nonsymmetric matrices. |
| 181–204 | PASS | `lem:schur` invertible case is valid: `S^{-1}` is the complementary principal compression of `A^{-1}`; Cauchy interlacing/min-max separately for positive and negative tails controls the absolute-value count. |
| 205–207 | **GAP** | Singular regularization uses a moving threshold and continuity without a fixed-threshold buffer. Repair supplied separately. |
| 208–260 | PASS | Strict diagonal dominance proof is standard and does not use symmetry. Heat-flow geometric Brascamp–Lieb: derivative identity, frame contraction, integration by parts, large-time Gaussian normalization, a.e. Lebesgue-point limit, truncation/monotone convergence all close. |
| 261–285 | PASS | Product-projection density proof is valid and never asserts rotated independence. For `b_i=0`, the factor is dropped; extending `-b log b` by `0` at zero and retaining RHS `1-b` gives the displayed `<=d/2` bound. Full-dimensional case is handled separately. |
| 286–319 | PASS | Integrated scalar Fourier power: difference density is `<=1`, inversion at zero uses an integrable even power, and the projection coefficient norm `sqrt(2m)` produces the stated `2pi sqrt(2e)/sqrt(p)` bound. |
| 320–373 | PASS | Decoupling powers 2 and 4 are correct: only original independent coordinates are used, `G(Y)-G(Y')` is discarded after modulus, and the difference coordinates remain independent with densities `<=1`. No moment assumption enters. |
| 374–420 | PASS | Regularized determinant proof: frame weights `c_j,d_i`, Jacobian `det(H)^(-1/2)`, one-dimensional scaling, Fourier-power exponents, cancellation at `alpha=(2pi e)^2`, and fourth-root exponent `-1/8` all check. Cauchy–Binet expansion of `Z_k` is correct. The `k=5` and `k=3` exponents/constants follow with the stated Fourier and Riesz lemmas. |
| 421–455 | PASS | Scalar square profile and inverse-image length are correct. Conditional domination formula is a measure inequality, not an independence claim. Definite two-dimensional quadratic pushforward has Jacobian `1/(2 sqrt(det B))`, giving `pi M/sqrt(det B)`. |
| 456–516 | PASS | Hyperbolic pair: level-set parametrization, two branches, Jacobian `1/(2 sqrt D)`, original-coordinate monotone tail selection, bathtub bound, middle-length estimate, and `Lambda>=2/sqrt D` all close. Exceptional critical level is correctly handled through nonnegative test functions. |
| 517–552 | PASS | Quarter-power concentration: random sign cut gives a cross block of operator norm at least `L/4`; determinant theorem gives the `|t|^{-1/4}` envelope; Gaussian smoothing and Gamma integral have the correct powers; layer cake yields `L0=4+4 log 16`. No atoms follow. |
| 553–580 | PASS | Pivot-volume definition and no-pivot entry bound are correct. Volume-sampled interpolation uses the bordered determinant correctly. Ordered disjoint extensions are counted at most `(r+1)^2`; singular seeds are correctly treated as an inequality, not equality. |
| 581–605 | PASS | Completion `A=D+R+E`: `E` has zero diagonal; `D` vanishes on `S union T`; `R_LL=P_LL`; global support decomposition gives `rank R<=3r`; restricted rank is `<=r`. Nonsymmetry of `P,R,E` is harmless because subsequent estimates use singular values/rank. |
| 606–644 | PASS | No-pivot spectral-to-volume conversion: telescoping ratio selection is exhaustive; `r=0` contradicts `||A||<1`; for `1<=r<=4`, `||E||<=1/16`, global rank creates at least `r+1` large diagonal entries because `m=4k-3>=4r+1`; seed vanishing puts them in `L`; strict diagonal dominance of the `(r+1)` block contradicts `rank R_LL<=r`. Constants `371/400` and `23/28` have positive slack. |
| 645–670 | PASS | Random coordinate cut probability is exactly `4^{-k}` for each ordered disjoint minor. For `k=3,5`, `Z_k^{-1/(2k)}<=160`; the resulting full half-potential `<200` and density `800e<2400` are correct. |
| 671–703 | PASS | Kernel integrals: near singularities are integrable, far part yields the logarithm, and centered interval overlap proves the `<=8` log-kernel bound by Tonelli. |
| 704–737 | PASS subject to GAP-1 repair | Pivot truncated-half-potential proof is otherwise correct. Scalar pivot uses the Schur spectral survivor and logarithmic potential. Definite pair is uniformly bounded. Indefinite pair integrates the logarithmic envelope; `sup D^{-1/2} log_+ D=2/e` is correct. Constants are conservative. |
| 738–751 | PASS subject to GAP-1 repair | Nine-eigenvalue proposition correctly combines pivot `H<=600` with no-pivot full half potential `<200`, then adds at most `1` for the tail `|Q-a|>1`. |
| 752–773 | PASS subject to GAP-1 repair | Main normalized proof is exhaustive: no pivot `<2400`; scalar pivot uses at least 16 surviving spectral directions and the nine-direction half potential; definite pair `<40`; indefinite pair keeps at least 15 directions, so one survives for the log bound. All conditioning is on original coordinates. |
| 774–790 | PASS | Scaling `Y=KX` gives coordinate caps `<=1`; `tilde Q=(K^2/s)Q` with quadratic matrix `A/s`; scalar density scaling yields `K^2/s`. The 33-direction corollary is immediate. The limitations correctly do not claim the 3-eigenvalue theorem or global continuity. |

## Sensitive points requested by owner

- **Nonsymmetric interpolation support:** PASS. `R-P` is supported in rows `T` or columns `S` outside the zero `LxL` residual, yielding two rank-`r` pieces in addition to rank-`r` `P`.
- **Global rank `<=3r` vs restricted rank `<=r`:** PASS and both are used distinctly. Collapsing them would lose the 17 threshold.
- **`D` vanishes on seed:** PASS by definition; this is essential to place all forced large diagonal entries inside `L`.
- **Spectral-to-volume:** PASS. For the worst `r=k-1`, `m=4k-3=4r+1` is exactly what forces `r+1` large diagonal entries.
- **Fourier normalization:** PASS (`2pi` convention consistent everywhere).
- **Heat-flow / rough-law limits:** PASS; truncation, Fatou, Tonelli and dominated convergence are used in valid directions.
- **Schur counts:** GAP only in the singular regularization paragraph; fixed proof supplied.
- **Full vs truncated half potentials:** PASS. `prop:pivot-H` is truncated; `prop:nine` adds at most `1` outside the unit window; no-pivot `k=3` estimate is already full.

## Prior-art / primary-source scope audit

1. **Bennett–Carbery–Christ–Tao**, *The Brascamp–Lieb inequalities: finiteness, structure, and extremals* (arXiv:math/0505065; later GAFA): appropriate antecedent for geometric Brascamp–Lieb and heat-flow monotonicity. The manuscript proves the exact rank-one inequality it uses, so correctness does not depend on importing BCCT.
2. **Rudelson–Vershynin**, *Small ball probabilities for linear images of high dimensional distributions* (arXiv:1402.4492): exact primary source for bounded-density projection/sum anticoncentration. Their Theorem 1.2 gives the sharp scalar `sqrt(2) K` bound for normalized sums. The manuscript's `sqrt(e)` scalar bound is weaker and self-proved.
3. **Livshyts–Paouris–Pivovarov**, *On sharp bounds for marginal densities of product measures* (arXiv:1507.07949): directly relevant omitted prior art. It gives the sharp product-marginal bound `2^{d/2}` in the cap-one setting (in the relevant proper-marginal range), improving the manuscript's self-contained `e^{d/2}` estimate. This omission does not affect validity but should be cited in a publication version.
4. **Banks–Garza Vargas–Kulkarni–Srivastava**, *Overlaps, Eigenvalue Gaps, and Pseudospectrum under real Ginibre and Absolutely Continuous Perturbations* (arXiv:2005.08930; Ann. IHP 2024), Theorem 2.1 “Density of Quadratic Forms” and Corollary 2.4: direct prior art for bilinear-affine forms `X^T ZY + X^T U + V^T Y + W` under independent bounded-density entries, with singular-value anticoncentration. It is not an exact prior solution of the manuscript theorem because the manuscript determinant theorem permits arbitrary same-bank measurable phases `F(X_I)+G(X_J)` generated by unrestricted within-bank quadratic terms.
5. **Herry–Malicet–Poly**, arXiv:2303.09488 / PTRF, studies regularity of quadratic forms for iid variables whose common law admits a sufficiently smooth Gaussian-field representation. Its hypotheses are substantially narrower than arbitrary non-iid cap-one coordinate densities, so it does not subsume this theorem.

A targeted current search did **not** locate a published theorem matching all of the manuscript's arbitrary-law/arbitrary-sign fixed-multiplicity hypotheses. This is only a scope report; a search miss is **not** a novelty or priority claim.

## Threshold reduction audit

I found no rigorous reduction below 17 that preserves the full hypotheses in this run. The obstruction is explicit inside the current architecture:

- bounded density from the determinant envelope requires crossing order `k>=5`, since the Fourier exponent is `k/4`; `k=4` is the non-integrable endpoint `|t|^{-1}`;
- the interpolation argument for order `k=5` needs `m>=4r+1` for every possible bad ratio index `r<=4`; at the worst `r=4` this is `m>=17`;
- with only `m=16`, the same argument forces only four large diagonal entries after the global rank-12 correction, while the restricted correction may have rank four, so the diagonal-dominance contradiction does not fire.

Thus 17 is the lowest threshold justified by **this exact proof mechanism**. Lowering it needs a new endpoint analytic argument for order four, an improved rank/support decomposition, or a new alternative branch. I do not claim impossibility of a lower theorem.

## Immediate rigorous constant improvement

The displayed proof already supports a stronger constant than `10000` once GAP-1 is repaired. The largest branch is the scalar pivot. Keeping the exact bound instead of rounding `H` to `600`,

`H <= 10(20+12 log 16)`

(the definite and indefinite pair bounds and no-pivot `<200` are smaller), hence

`sup_a E|Q-a|^{-1/2} <= 10(20+12 log 16)+1`.

The main scalar-pivot density is therefore at most

`2010 + 1200 log 16 = 5337.106466...`,

while every other branch is below 2400. Consequently the same argument proves

`||p_Q||_infty <= (2010+1200 log 16) K^2/s`.

This is recorded separately as an improvement; it does not lower the spectral multiplicity.

## Validation gate

Baseline status after this review: **GAP, repair supplied; not independently validated**. This B18 report counts as one complete end-to-end review only. A second genuinely separate complete review of the repaired source is still required before any validation label. Missing reproducibility files should also be restored or README/AUDIT claims corrected before a reproducible release.
