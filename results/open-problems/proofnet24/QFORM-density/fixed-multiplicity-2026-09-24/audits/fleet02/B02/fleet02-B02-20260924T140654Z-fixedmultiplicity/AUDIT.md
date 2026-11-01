# fleet02/B02 — full fixed-multiplicity audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `fleet02-B02-20260924T140654Z-fixedmultiplicity`  
Lens: scalar Fourier powers, convolution and projection constants; fleet02 counterexample stress.

## Source pin and verdict

Repository `yspennstate/math-open-problems`, master observed during this run at `1021307c73d1f46686db7fbdfef6d30100236918`. The canonical manuscript is unchanged from the owner baseline: git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47,883 bytes, 790 lines. I read `README.md`, `DELIVERY_STATUS.md`, `SOURCE_MANIFEST.json`, `manuscript.tex` in full, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json` before this verdict.

**Mathematical verdict on the canonical 17-eigenvalue manuscript: PASS.** I found no fatal mathematical gap. Every mathematical source range was independently checked in this run. The two bibliography entries are attribution-only and were not independently priority/source-verified under the B02 lens; they are not proof dependencies. No unrestricted three-eigenvalue conclusion is claimed.

The wording concern previously recorded by this slot in `lem:projection` is discharged, not fatal: after the `b_i=0` factors are dropped,

`sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`.

Thus the manuscript's displayed `log p(y)<=d/2` is correct. The missing intermediate inequality can be inserted for clarity, but no theorem or constant changes.

## Line-range ledger

| Lines | Item | Status | Independent check / impact |
|---|---|---|---|
| 1–46 | preamble, abstract, conventions | PASS | Abstract matches the exact 17-direction theorem and does not claim continuity or the unrestricted conjecture. |
| 47–57 | `thm:main` | PASS | Quantifiers, affine terms, arbitrary signs/laws, and `10000 K^2/s` scaling are consistent. |
| 59–61 | `cor:33` | PASS | Immediate from monotonicity of ordered singular values. |
| 62–89 | architecture/parameters | PASS | `eta=1/100`, `kappa=1/80^2`; counts `9=4*3-3`, `17=4*5-3` correctly match later uses. |
| 91–120 | `lem:fourier` | PASS | Fourier convention, Plancherel factor `2pi`, inversion factor `1/(2pi)`, and Gaussian regularization are mutually consistent. |
| 122–130 | power envelope | PASS | Integral of `min(1,(a/|t|)^p)` is `2ap/(p-1)`; density constant follows exactly. |
| 132–160 | half-Riesz | PASS | Gamma/Tonelli normalization gives `1/sqrt(2pi)`; weighted envelope integral is `12 sqrt(u)`. |
| 161–181 | norms/counts; rank perturbation | PASS | Singular-value approximation formula is valid without symmetry; rank shift is used with correct indices. |
| 183–207 | Schur spectral count | PASS | Congruence/inverse-compression argument and singular limiting argument preserve the stated `N_S(t)>=N_A(t)-k`. |
| 209–217 | diagonal dominance | PASS | Standard row-max proof; nonsymmetry allowed as required later. |
| 221–255 | geometric rank-one BL | PASS | Heat-flow sign, frame contraction, large-time Gaussian limit, small-time Fatou, and rough-law truncation all close. |
| 258–282 | product projections | PASS | BL application and scaling are correct. Clarification: after dropping zero `b_i`, use `sum_{b_i>0}(1-b_i)<=d`; hence `e^{d/2}`. Scalar cap is `sqrt(e)/|a|`. |
| 284–301 | scalar Fourier powers | PASS | With `m=floor(p/2)>=p/4`, `|fhat|^p<=|fhat|^{2m}` and inversion of the sum of `m` independent differences give `2pi sqrt(2e)/sqrt(p)`. |
| 302–324 | cross form and decoupling | PASS | Copies and conditioning remain on original independent coordinates; powers two/four and product Fourier factors are correct. |
| 326–373 | regularized determinant | PASS | Frame weights, Jacobians, `alpha=(2pi e)^2`, cancellation of `d_i`, and fourth-root determinant exponent `-1/8` all check. |
| 374–400 | crossing volumes / envelopes | PASS | Cauchy–Binet expansion exact. Order five gives exponent `5/4`; order three gives `3/4` and is used only with the Riesz weight. |
| 404–421 | square profile / conditional domination | PASS | Two inverse branches and interval preimage length are correct; conditional formula is measure domination, not an independence claim. |
| 423–434 | definite pair | PASS | Polar/Jacobian constant `pi/sqrt(|det B|)` is correct and needs no post-rotation independence. |
| 437–482 | hyperbolic pair | PASS | Hyperbolic Jacobian `1/(2 sqrt D)`, original-coordinate tail changes of variables, and logarithmic envelope are valid for rough product densities. |
| 485–525 | quarter-power concentration | PASS | Random cut produces a cross block with norm at least `L/4`; smoothing coefficient and `rho^(1/4)` scaling are correct; layer cake excludes atoms and controls logarithms. |
| 528–543 | pivots / disjoint volumes / small entries | PASS | No-pivot determinant inequality yields `|a_ij|<1/7` at baseline parameters. |
| 545–564 | sampled interpolation | PASS | Bordered determinant identity, ordered-pair multiplicity at most `(r+1)^2`, and nonsymmetric interpolation support are correct. |
| 566–580 | completion | PASS | `D` vanishes on seed, `E` has zero diagonal, global `rank R<=3r`, and restricted `rank R[L,L]<=r` all follow from the stated support. |
| 582–619 | spectral-to-volume | PASS | Telescoping choice, perturbation/rank subtraction, forced `r+1` large diagonal entries, and strict diagonal dominance close for `k<=5`. |
| 621–645 | random cut / no-pivot consequences | PASS | Each ordered disjoint minor survives with probability `4^-k`; constants `160`, `<200`, and `800e<2400` are correct. |
| 646–674 | truncated potential / singular kernels | PASS | Full-vs-truncated distinction is preserved; both kernel integrals are finite with the advertised conservative constants. |
| 676–714 | pivot half-potential | PASS | Scalar, definite, and indefinite pivot branches use the exact surviving spectral hypotheses; `H<=600` is valid. |
| 716–724 | nine-direction half-potential | PASS | Pivot branch gives truncated `600`; no-pivot gives stronger full `<200`; outside distance one contributes at most one. |
| 726–749 | main proof and scaling | PASS | All four branches cover the normalized theorem. `Y=KX`, `A/s`, and `Q=(s/K^2)Qtilde` give the density scale `K^2/s`. |
| 750–780 | threshold accounting, limitations, acknowledgement | PASS | Statements accurately describe the proof and explicitly avoid a three-direction or global-continuity claim. |
| 782–790 | bibliography / document close | UNCHECKED (bibliographic only) | Classical attributions are not used as black-box proof inputs because the needed statements are reproved. No mathematical dependency is unchecked. |

## B02 exact-law and normalization stress tests

1. **Scalar Fourier exponent is sharp.** For the admissible cap-one Gaussian `f(x)=exp(-pi x^2)`,
   `fhat(t)=exp(-t^2/(4pi))` and exactly
   `int |fhat(t)|^p dt = 2pi/sqrt(p)`.
   Thus the manuscript's `p^{-1/2}` dependence cannot be improved under only `f<=1`; only its constant can improve.

2. **Convolution cap is sharp.** For `X~Unif[-1/2,1/2]`, the difference density is `(1-|x|)_+`, with supremum exactly one. The normalized projection `(X_1+X_2)/sqrt(2)` has peak `sqrt(2)`, providing a concrete lower benchmark for the universal scalar projection constant `sqrt(e)`.

3. **Square/definite/hyperbolic endpoints are real.** The same uniform law gives the exact square-root singular coefficient one for `X^2`; two uniforms give density `pi` at the origin for `X^2+Y^2`; and `X^2-Y^2` has a logarithmic singularity with coefficient one. Hence an order-two indefinite endpoint cannot by itself be upgraded to a universal `L^infinity` density theorem.

4. **Bilinear Fourier normalization.** For independent cap-one Gaussians and `Z=2mXY`, direct Gaussian integration gives
   `phi_Z(t)=(1+m^2 t^2/pi^2)^(-1/2)`, confirming the manuscript's cross-term factor `2` and `pi^2` normalization.

5. **Endpoint obstruction.** Under the baseline determinant exponent `-1/8`, an order-`k` crossing term gives `|t|^{-k/4}`. Order four is exactly `|t|^{-1}` and is logarithmically nonintegrable. Because the Gaussian example makes the scalar Fourier `p^{-1/2}` exponent sharp, changing only scalar Fourier/convolution/projection constants cannot make the old `4k-3` architecture close at order four.

## Support-package check

`SOURCE_MANIFEST.json` still identifies the canonical source blob/hash above. The supplied `checks.json` reports PASS with 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict-sampling cases, exact diagonal-dominance slack `297/2800`, 240 Schur threshold diagnostics, and 30 graph-weight diagnostics. I inspected `verify.py`; these are reproducibility checks, not a proof certificate.

## Downstream status and next obligation

The canonical 17-eigenvalue manuscript is mathematically sound in this review. A complete nine-eigenvalue replacement is now present in the repository and is audited separately in this run's improvement artifact. Multiplicity eight remains unproved: current structure reaches an overlap-one/two-sided collar for which no dependence-safe analytic receiver is yet complete. Do not claim the unrestricted three-eigenvalue theorem.
