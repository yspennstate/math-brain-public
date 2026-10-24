# account02/B10 r11 — fresh full fixed-multiplicity audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T141506Z-auto11-account02-B10`  
B10 lens: constants, exact arithmetic, adversarial finite examples.

Pinned mathematical baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `manuscript.tex` git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, owner-recorded SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47,883 bytes / 790 lines. Fresh `master` observed during the audit advanced through `6b946fa19d943a8c77e375bfb3e7cc86d098f759`; the baseline manuscript blob remained the pinned byte-identical source.

## Verdict

**PASS** for the complete pinned seventeen-direction theorem. I independently reread all 790 source lines and all required package files. No mathematical source range is left UNCHECKED and I found no FALSE statement or fatal GAP in the pinned theorem. This is one worker audit, not formal verification or an owner-level validation certificate. The unrestricted three-eigenvalue QFORM conjecture remains OPEN.

Nonmathematical `UNCHECKED`: I did not independently reconstruct the conversation-only compiled PDF or reproduce the historical finite-test counts from the authoring self-audit. Neither is a dependency of the written theorem. The current `verify.py/checks.json` suite is internally consistent and explicitly distinguishes itself from the historical suite.

## Package audit

- `README.md`: **PASS**. It identifies the self-contained 790-line source and correctly distinguishes source delivery, PDF delivery, audit status, and the fixed-multiplicity scope.
- `DELIVERY_STATUS.md`: **PASS as delivery metadata**. It records that the source is unchanged and that the current finite checker is a new scoped suite, not a proof certificate.
- `SOURCE_MANIFEST.json`: **PASS**. Source commit/blob/SHA/bytes/lines and support-file hashes are consistent with the package.
- `AUDIT.md`: **PASS as historical self-report only**; it is not treated as independent validation.
- `proof_map.csv`: **PASS**. Its statement/proof ranges agree with the source ranges used below.
- `verify.py`: **PASS as finite diagnostics, not proof**. It pins the source SHA, checks exact interpolation identities and the exact diagonal-dominance slack, and separately labels floating diagnostics.
- `checks.json`: **PASS** against the supplied execution: 534 exact interpolation seeds, 18 exact volume comparisons, 9 strict cases, 240 Schur threshold cases, 30 graph-weight cases, exact slack `297/2800`.

## Complete source audit by contiguous range

### Lines 35–83 — statement, quantifiers, normalization

**PASS.** The theorem keeps arbitrary independent real coordinate densities `<=K`, arbitrary symmetric `A`, arbitrary signature and remaining spectrum, arbitrary affine `b,c`, and only an essential-density conclusion. The singular-value convention is correct for symmetric matrices. The normalization `Y=KX`, `A -> A/s`, and `Q=(s/K^2) Qtilde` gives exactly the final `K^2/s` scale. No moment/support/log-concavity/continuity assumption is hidden.

### Lines 91–160 — Fourier inversion, power envelope, Riesz half potential

**PASS.** With the manuscript Fourier convention, Plancherel has factor `2pi`, inversion `1/(2pi)`, and Gaussian regularization is normalized correctly. The gamma substitution gives

`int_0^infty v^(-5/4) exp(-t^2/(4v)) dv = sqrt(2) Gamma(1/4)|t|^(-1/2)`.

For the `3/4` envelope the weighted integral is exactly `12 sqrt(u)`, hence the displayed negative-half-moment constant follows.

### Lines 169–217 — perturbation, Schur count, diagonal dominance

**PASS.** The singular-value approximation formula proves both nonsymmetric perturbation inequalities. The Schur proof correctly applies principal compression to `A^{-1}` and `-A^{-1}` and the singular case is obtained by `A+epsilon I` with continuity of ordered eigenvalue moduli. Strict row diagonal dominance needs no symmetry.

### Lines 221–301 — geometric BL, projection density, scalar Fourier powers

**PASS.** The heat-flow identity is

`partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`,

with the frame giving the contraction. Large-time Gaussian normalization, small-time Lebesgue-point/Fatou passage, and monotone truncation are valid. The projection proof uses complement-row weights `b_i=1-|U^T e_i|^2`, obtains `e^(d/2)`, and never asserts independence after rotation. For scalar Fourier powers, `m=floor(p/2)>=p/4` and the projection bound at zero gives exactly `2pi sqrt(2e)/sqrt(p)`.

### Lines 310–400 — decoupling, determinant theorem, crossing volumes

**PASS.** Copies are introduced only on literal independent source coordinates. The determinant proof's weights form the exact geometric frame; the `d_i` powers cancel, `alpha=(2pi e)^2` cancels the trace penalty, and fourth-rooting gives exponent `-1/8`. Cauchy–Binet gives the stated `Z_k`. Retaining one order yields `u_k=pi e Z_k^(-1/(2k))`; `k=5` gives `5e Z_5^(-1/10)` and `k=3` gives the stated half-potential estimate.

### Lines 404–482 — scalar square, definite pair, hyperbolic pair

**PASS.** The square map has the correct two inverse branches and interval-preimage length. The definite-pair Jacobian is `1/(2 sqrt(|det B|))`, so the angular integral gives `pi M/sqrt(|det B|)`. The hyperbolic parametrization has Jacobian `1/(2 sqrt D)` per branch. The original-coordinate tail substitution is valid for rough cap-one laws; the baseline tail estimate and `Lambda>=2/sqrt D` give the displayed logarithmic envelope. Exceptional critical levels are handled as measure domination rather than by selecting pointwise conditional densities.

### Lines 485–525 — quarter-power concentration

**PASS.** A large diagonal gives the stated conditional square small-ball estimate. Otherwise the random sign cut gives a literal crossing block of norm at least `L/4`, and the determinant theorem yields the `|t|^(-1/4)` envelope. The Gaussian-smoothed coefficient and layer-cake calculation give the printed safe constant `16` and `L_0=4+4 log16`. A sharper Fejer replacement is recorded separately in this run's improvement artifact; it is not needed for baseline correctness.

### Lines 528–645 — pivots, sampled interpolation, both rank bounds, spectral-to-volume conversion

**PASS.** No-pivot implies `|a_ij|^2<eta^2+eta<1/49`. The determinant-squared seed sampling uses the exact bordered identity on nonsingular seeds; singular seeds can have nonsingular extensions, so the manuscript correctly states an inequality rather than a false equality. The completion satisfies

`rank P<=r`, `rank R<=3r`, `R_LL=P_LL`, `rank R_LL<=r`, `D=0` on the seed, `diag E=0`.

The support proof for the global `3r` bound is valid. In the bad-ratio branch, `epsilon<=(r+1)/80<=1/16` and `m=4k-3>=4r+1`. The exact diagonal-dominance margin is

`371/400 - 4(1/7+1/16) = 371/400-23/28 = 297/2800 >0`.

Thus an `(r+1)x(r+1)` invertible restricted block contradicts `rank R_LL<=r`. The fair physical cut contributes exactly `4^(-k)` to each ordered disjoint minor. The resulting no-pivot constants are `12 sqrt(80e)<200` at order three and `800e<2400` at order five.

### Exact finite rank stress test

**PASS / route-sharpness witness.** I recomputed in exact rational arithmetic the symmetric integer matrix

```
A =
[-1 -1 -1 -1  0 -1]
[-1 -1  1 -1  1  0]
[-1  1  1  1 -1  1]
[-1 -1  1  0  0  1]
[ 0  1 -1  0  0 -1]
[-1  0  1  1 -1 -1]
```

with `S={1,2}`, `T={3,4}` and `L={5,6}` in one-based notation. Here

`B=[[-1,-1],[1,-1]]`, `det B=2`,

and the manuscript completion gives exactly

`rank P=2`, `rank R=6=3r`, `rank R_LL=2=r`,

`D_55=1/2`, `D_66=-2`,

`R_LL=[[-1/2,-1/2],[0,1]]`.

So both rank bounds can be simultaneously sharp. This is a proof-interface stress test, not a counterexample to the theorem.

### Lines 654–724 — singular kernels, pivot half potentials

**PASS.** The two singular-kernel estimates are correctly normalized. The scalar pivot calculation actually yields the sharper baseline value

`H <= 10(20+12 log16)=200+120 log16 = 532.7106466687...`.

The baseline definite and indefinite pair bounds are safely below `600`, so Proposition 6.3 is valid. The full half potential adds at most one outside distance one.

### Lines 726–790 — main theorem, scaling, limitations

**PASS.** The no-pivot branch is `<2400`; scalar pivot leaves sixteen Schur directions and gives the printed `6010`, definite pair gives `10pi`, and indefinite pair is `<251`. The exact baseline scalar arithmetic already improves the same proof to

`2010+1200 log16 = 5337.106466687737... <5338`,

without changing a hypothesis. Scaling is exact. The limitations correctly say the proof does not settle the unrestricted three-eigenvalue problem and does not assert global continuity.

## Current lower-threshold state checked after the baseline

The already written account02/B10 nine-direction replacement was reread and its grouped product-Fourier compiler, rough-law mollification/Fatou step, determinant-weighted entropy inequality, `E_3` density promotion tree and `E_2` half-potential tree were rederived. I found no defect. Thus the currently closed fixed-multiplicity candidate remains

`s_9(A)>=s  =>  ||p_Q||_infinity <= C K^2/s`

under the full original hypotheses. A sharper constant is proved separately in this run.

I also checked the fresh account03/B10 invertible-seed overlap-one identity. For determinant-squared sampling of nonsingular order-two seeds,

`W^x_{2,1}/V_2 = E sum_h D_h^2`,

and rank subtraction plus Jensen gives, under `s_7(A)>=s`,

`W^x_{2,1} >= V_2 (s-3 sqrt(V_3/V_2))_+^2`.

In the normalized no-pivot chamber this means seven directions already force either `V_3>=kappa^3` or a dimension-free overlap-one packet. This is a **PASS structural theorem**, not a seven-direction density theorem. The missing implication is still a product-preserving overlap-one analytic receiver with the common physical anchor retained.

## Status ledger

- Pinned 17-eigenvalue manuscript: **PASS**.
- Required package/source consistency: **PASS**, with PDF/history items noted nonmathematical UNCHECKED above.
- Complete 9-eigenvalue replacement encountered and rederived: **PASS mathematical candidate**; no owner-level release status self-awarded.
- Structural no-pivot boundary `s_7 -> (V_3 large) OR (overlap-one packet large)`: **PASS supporting theorem**.
- Product-preserving overlap-one density receiver: **GAP / next obligation**.
- Multiplicity 8 and 7 bounded-density theorems: **UNPROVED**, not false.
- Unrestricted three-eigenvalue QFORM: **OPEN**.
