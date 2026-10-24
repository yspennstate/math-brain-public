# account01/B18 complete fixed-multiplicity audit — r12

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and actual scope

- Baseline mathematical source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Fresh `master` manuscript blob during this run: `183ccd294763214e6a707e8d4749ff9a8cf7006d`, identical to the pinned baseline blob.
- Owner/source-manifest SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`; 47,883 bytes; 790 lines.
- Freshly read end to end in this invocation: `manuscript.tex` lines 1–790, `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`.
- `checks.json` reports the newly supplied finite suite PASS on 534 exact interpolation seeds, 18 exact volume comparisons, 240 floating Schur-threshold diagnostics and 30 graph-weight diagnostics. I inspected the checker source. These computations are diagnostics only, not mathematical proof or a fresh execution by this slot.

## Fatal issues first

**No fatal mathematical defect found.** My fresh reconstruction again supports the exact candidate statement

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
\le 10^4 K^2/s
\]

for arbitrary real symmetric `A`, arbitrary affine `b,c`, and independent arbitrary real coordinate densities bounded by `K`.

Verdict: **PASS mathematically; GAP-PRESENTATION in prior-art/bibliography scope.** This is one B18 review, not a second independent reviewer and not a release certificate. The unrestricted three-eigenvalue conjecture remains open.

## Complete source ledger

Every mathematical source range is reviewed below; there are no `UNCHECKED` manuscript ranges in this run.

| Lines | Status | Reconstruction / exact reason |
|---|---|---|
| 1–46 | PASS | Notation, theorem environments, abstract and metadata agree with the eventual theorem; no hidden distributional assumption is introduced. |
| 47–61 | PASS | Main theorem and 33-eigenvalue corollary have the correct arbitrary-law/matrix/affine quantifiers. For symmetric `A`, singular values are absolute eigenvalues. |
| 62–80 | PASS, with prior-art GAP-PRESENTATION | Proof architecture and normalization are consistent. The attribution sentence is incomplete, not false: directly relevant LPP product-marginal work and Banks–Garza Vargas–Kulkarni–Srivastava quadratic-form anticoncentration should be added. |
| 81–120 | PASS | Fourier convention, Plancherel constant `2pi`, Gaussian regularization, inversion and weak identification of the density all close for rough probability laws. |
| 121–160 | PASS | Power-envelope integral is exact. The Riesz half-potential Gamma representation, Gaussian inversion and two Tonelli steps give the stated `1/sqrt(2pi)` coefficient and the `12 sqrt(u)` weighted integral. |
| 161–181 | PASS | Approximation-number proof gives both singular-value Lipschitz continuity and rank shift for nonsymmetric matrices, exactly what later auxiliaries require. |
| 182–207 | PASS | Schur spectral count is sign-independent. In the singular case, `N_{A+eps I}(t-|eps|)>=N_A(t)` and the invertible result imply `s_m(S_eps)>=t-|eps|` for `m=N_A(t)-k`; `S_eps->S` then gives `s_m(S)>=t`. The moving threshold is valid. |
| 208–217 | PASS | Strict row diagonal dominance proves invertibility without symmetry. |
| 218–255 | PASS | Geometric rank-one Brascamp–Lieb heat-flow proof is self-contained: frame contraction supplies the sign, compact-time Gaussian tails justify differentiation/integration by parts, `sum c_i=d` gives the large-time limit, and Lebesgue points/Fatou plus monotone truncation handle rough inputs. |
| 256–282 | PASS, wording clarification only | Product-projection proof never assumes rotated independence. After dropping `b_i=0` factors, one may extend `-b log b` continuously by zero and sum over all `i`, obtaining `sum(-b_i log b_i)<=sum(1-b_i)=d`. Thus the `e^{d/2}` bound is correct. |
| 283–301 | PASS | For `m=floor(p/2)`, `|fhat|^p<=|fhat|^{2m}` and the even power is integrable by Plancherel. Fourier inversion at zero plus the proved scalar projection cap yields `2pi sqrt(2e)/sqrt p`. |
| 302–324 | PASS | Decoupling conditions only on genuine disjoint original-coordinate product banks. Cauchy–Schwarz, independent copy expansion and Jensen give powers two/four; same-bank phases disappear only inside modulus, not by an independence fiction. |
| 325–373 | PASS | Determinant receiver: the `H`-frame identity, weights `c_j,d_i`, trace relation, Jacobian, BL one-dimensional norms, scalar Fourier powers and entropy cancellation reconstruct exactly. `alpha=(2pi e)^2`, `a=2t`, and fourth root give exponent `-1/8`. |
| 374–400 | PASS | Cauchy–Binet gives crossing volumes. Retaining order `k` produces exponent `k/4`; `k=5` is integrable, while `k=3` is used only with the Riesz `|t|^{-1/2}` weight. Constants check. |
| 401–422 | PASS | Scalar square density/preimage profile is valid as measure domination under conditioning; no independence between the square and Schur remainder is asserted. |
| 423–434 | PASS | Definite two-coordinate coarea uses only a deterministic change of variables and the joint density cap; no post-rotation independence is used. |
| 435–482 | PASS | Hyperbolic parameterization, Jacobian `1/(2sqrt D)`, original-coordinate tail monotonicity, bathtub estimate, middle interval and `Lambda>=2/sqrt D` yield the displayed log envelope. Critical level is handled through test functions/Tonelli. |
| 483–525 | PASS | Quarter-power concentration: diagonal branch, physical random-sign crossing, determinant envelope, Gaussian smoothing/Gamma integral, atom exclusion and log layer cake all check. |
| 526–544 | PASS | Ordered disjoint volume definition is unambiguous. No-pivot condition gives the stated off-diagonal entry control from the principal `2x2` determinant. |
| 545–564 | PASS | Volume-sampled interpolation: bordered determinant identity is exact; sorting signs disappear on squaring; each extension is counted at most `(r+1)^2`; singular seeds correctly turn equality into inequality. |
| 565–580 | PASS | Completion has zero-diagonal `E`, diagonal `D` vanishing on seed, `R_LL=P_LL`, global `rank R<=3r`, and restricted `rank R_LL<=r`. The support decomposition of `R-P` is correct. |
| 581–619 | PASS | Spectral-to-volume proof uses nonsymmetric singular values correctly. Ratio-drop selection is exhaustive. Global rank forces large diagonal entries of `D`; seed vanishing places them in `L`; strict diagonal dominance contradicts restricted rank. |
| 620–645 | PASS | Random cut probability is exactly `4^{-k}` per ordered disjoint minor. Orders three/five yield the stated negative-half-moment and density bounds. |
| 646–674 | PASS | Truncated potential and both singular-kernel estimates are Tonelli-safe. The interval-overlap argument for the log kernel is valid. |
| 675–714 | PASS | Pivot half-potential: scalar branch uses valid Schur survivor + quarter-power log potential; definite and indefinite pair branches preserve literal original-coordinate conditioning; `sup D^{-1/2} log_+D=2/e` is correct. |
| 715–724 | PASS | Nine-eigenvalue statement correctly distinguishes truncated pivot bound from full no-pivot bound and pays the outer kernel tail by `<=1`. |
| 725–749 | PASS | Main proof exhausts no-pivot, scalar, definite-pair and indefinite-pair cases; Schur losses leave 16 or 15 directions as stated; arbitrary induced affine terms remain allowed. Scaling `Y=KX` gives exactly `K^2/s`. |
| 750–779 | PASS | Threshold accounting correctly identifies the current architecture barrier: order four gives the nonintegrable `|t|^{-1}` endpoint; the `r=4` interpolation contradiction needs `m>=17`. It explicitly disclaims `s_3` and optimality. |
| 780–790 | GAP-PRESENTATION, math PASS | Acknowledgment is nonmathematical. Bibliography should use published BCCT/RV data and add LPP plus Banks et al.; no proof imports any of these sources, so theorem validity is unaffected. |

## Fresh primary-source and prior-art scope audit

Search date: 2026-09-24. A search miss is **not** treated as evidence of novelty.

1. **Bennett–Carbery–Christ–Tao.** The cited preprint is genuine; published as *The Brascamp–Lieb inequalities: finiteness, structure and extremals*, GAFA 17 (2008), 1343–1415, DOI `10.1007/s00039-007-0619-6`. Heat-flow monotonicity is explicitly part of their method. Appropriate provenance for lines 218–255; not a dependency because the manuscript proves its needed rank-one statement.

2. **Rudelson–Vershynin.** *Small ball probabilities for linear images of high-dimensional distributions*, IMRN 2015(19), 9594–9617, DOI `10.1093/imrn/rnu243`, arXiv:1402.4492. Their Theorem 1.2 gives the sharp `sqrt(2)K` scalar normalized-sum density cap under independent density caps. This is stronger than the manuscript's self-contained `sqrt(e)K` scalar projection estimate but does not undermine it.

3. **Livshyts–Paouris–Pivovarov.** *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216(2) (2016), 877–889, arXiv:1507.07949. For cap-one product densities, every `d`-dimensional orthogonal marginal is bounded by `2^{d/2}`. This is directly relevant omitted prior art and sharper than the manuscript's `e^{d/2}` self-contained bound.

4. **Banks–Garza Vargas–Kulkarni–Srivastava.** arXiv:2005.08930, Section 2, Theorem 2.1 is explicitly titled “Density of Quadratic Forms.” It handles `X^T ZY+X^T U+V^T Y+W` for independent bounded-density entries; Corollary 2.4 gives, for scalar output, a geometric-mean leading-singular-value refinement. It does **not** subsume the manuscript's physical-cut object `F(X_I)+2X_I^TMX_J+G(X_J)`, because both same-bank phases may be arbitrary quadratic polynomials. Therefore it does not close the order-four endpoint or the fixed-multiplicity theorem by citation alone.

5. **Herry–Malicet–Poly.** arXiv:2303.09488 studies quadratic forms for iid inputs whose common law admits a sufficiently smooth Gaussian-field representation. That is materially narrower than arbitrary non-iid bounded-density coordinates here.

A fresh targeted 2025–2026 search did not locate a theorem matching all present quantifiers. No novelty assertion is made from that fact.

## Current `17 -> 16` reconstruction

I read the strongest current source-pinned endpoint improvements before attempting a new reduction:

- account01/B20: if the no-pivot `s_16` chamber is not already paid by `V_5`, there is a physical cut carrying quantitative `Z_4`, a `1/64`-near-rank-four crossing, and eight near-unit same-bank modes.
- account03/B11: those same-bank modes survive after projection away from the old rank-four crossing carrier; a literal internal physical crossing has quantitative carrier-orthogonal mass.
- account01/B04: mixed four-plus-one exterior energy is uniformly positive; if at least half is physically disjoint, a literal repartition gives order-five volume and a full-law density bound `<1546`. The remaining survivor is an explicit weighted row-leverage or self-coordinate residual trap.
- account03/B05: an independent seed-mass analysis makes the unpaid chamber highly diffuse over many low-residual physical four-seeds, but still lacks a dimension-free weighted-preimage/coarea receiver.

I did not find a valid way to turn either surviving trap into a fifth product-preserving direction while retaining arbitrary same-bank phases. In particular, the Banks scalar bilinear theorem cannot simply replace the manuscript determinant receiver because conditioning away a same-bank phase also destroys the needed two-bank crossing geometry. Thus **no universal `s_16` theorem is claimed in this run**.

## Review status

This r12 report is a fresh same-slot reread. It is not a distinct human/agent identity from r11 and must not be counted as the owner's second genuinely separate full review. No independent-validation status is asserted.
