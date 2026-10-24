# account01/B10 r14 — full baseline audit, checker-coverage audit, and exact finite diagnostics

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T144911Z-account01-B10-fixedmult-r14`  
Role lens: exact constants, rational slack, computational checker coverage, adversarial small matrices, singular seeds.  
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Baseline source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Declared source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Fresh `master` observed before publication: `2ff6f0d4a534d645f3a806774de6a5c6445c79f8`; the fetched `manuscript.tex` still had the pinned baseline blob above.

## Executive verdict

**PASS for the literal 790-line seventeen-eigenvalue manuscript in this independent B10 audit.** I read `manuscript.tex` in full, together with root `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`. I found no mathematical FALSE statement or fatal GAP in the baseline theorem. No mathematical source range remains UNCHECKED in this review.

This is one worker's mathematical audit, not formal verification, journal peer review, or an owner-level release-gate change. The unrestricted three-eigenvalue conjecture is not proved by the manuscript.

## End-to-end source audit

| Source lines | Status | Check |
|---|---|---|
| 1–46 | PASS | LaTeX/preamble/abstract accurately state the scope; no hidden regularity or sign hypothesis. |
| 47–83 | PASS | Main quantifiers, `K^2/s` scaling target, pivot/no-pivot architecture and counts `9,17` are internally consistent. |
| 84–120 | PASS | Fourier convention, Gaussian transform, Plancherel/inversion and rough-law limiting argument have the correct `2pi` normalization. |
| 121–160 | PASS | Power envelope and half-Riesz formula: gamma exponent and constant `1/sqrt(2pi)` rederive correctly; the `12 sqrt(u/(2pi))` weighted integral is correct. |
| 161–217 | PASS | Singular-value perturbation/rank and Schur spectral count are valid, including singular ambient `A`; the moving-threshold limit is a closed order-statistic inequality. Strict diagonal dominance is used correctly for nonsymmetric matrices. |
| 218–282 | PASS | Heat-flow geometric Brascamp–Lieb sign, Gaussian limit, rough truncation, and product-projection argument are correct. Orthogonal changes occur only inside deterministic integrals; no rotated independence is asserted. |
| 283–301 | PASS | Scalar Fourier powers use genuine independent signed copies; projection scaling by `sqrt(2m)` and Fourier inversion at zero are correct. |
| 302–373 | PASS | Original-coordinate decoupling powers two/four, graph frame, Jacobian/scales, entropy factor, `alpha=(2pi e)^2`, and determinant exponent `-1/8` rederive correctly. |
| 374–400 | PASS | Cauchy–Binet crossing volumes and the order-five density/order-three half-Riesz envelopes have the correct exponents and constants. |
| 401–421 | PASS | Scalar square profile, inverse-image length and conditional domination formula are correct and do not assert independence of the Schur remainder. |
| 422–482 | PASS | Definite-pair Jacobian and indefinite hyperbola coarea/tail proof are correct in original coordinates; exceptional levels are handled through test-function/Tonelli formulations. |
| 483–525 | PASS | Quarter-power concentration: diagonal branch, sign cut, retained singular factor, Gaussian smoothing and logarithmic layer cake all check. |
| 526–580 | PASS | Pivot/volume definitions, no-pivot entry bound, ordered disjoint-minor sampling, nonsymmetric interpolation support, `rank R<=3r`, `rank R[L,L]<=r`, zero seed diagonal of `D`, and zero diagonal of `E` all check. |
| 581–645 | PASS | Spectral-to-volume argument, random-cut factor `4^{-k}`, and no-pivot analytic consequences close with the stated `k<=5` hypotheses. |
| 646–724 | PASS | Both singular-kernel estimates, scalar/definite/indefinite pivot half-potential branches, truncated-versus-full distinction, and nine-direction half-potential proposition are correct. |
| 725–760 | PASS | Main case split: no-pivot density, scalar pivot plus Schur count, both pair pivots, rough conditional averaging, and general `K,s` scaling all close. |
| 761–790 | PASS | Threshold accounting and limitations match the proved claims; continuity is claimed only where Fourier inversion supplies it. |

### Singular Schur paragraph, explicitly

Let `m=N_A(t)-k`. The manuscript gives

`N_{S_eps}(t-|eps|) >= N_{A+eps I}(t-|eps|)-k >= m`.

For `m>0` this is exactly `s_m(S_eps)>=t-|eps|`. Since `S_eps -> S` and singular values are continuous,

`s_m(S)>=t`, hence `N_S(t)>=m`.

Thus no continuity of the integer-valued counting function at a threshold is needed.

## Exact constant audit

With `eta=1/100`, `kappa=1/80^2`:

- no-pivot off diagonal: `eta^2+eta=101/10000 < 2 eta=1/50 <1/49`, hence `|a_ij|<1/7`;
- for `r<=4`, `epsilon<=(r+1)/80<=1/16`;
- forced residual diagonal: `1-1/16-1/100=371/400`;
- residual off diagonal: `<1/7+1/16=23/112`;
- worst four-neighbor row sum: `4*(23/112)=23/28`;
- exact diagonal-dominance margin: `371/400-23/28=297/2800>0`;
- order-three no-pivot half potential: `12 sqrt(80 e)<200` using `e<3`, `sqrt(240)<16`;
- order-five no-pivot density: `800e<2400`;
- baseline scalar-pivot final branch: `10*601=6010<10000`;
- baseline definite pair: `10 pi<40`;
- baseline indefinite main branch: `10(10+5 log16)+1/e<251` from `log16<3`.

I found no arithmetic failure in the baseline constants.

## Root checker coverage audit

Root `verify.py` is correctly labeled a finite reproducibility suite, not a proof certificate. Its recorded `checks.json` says PASS on 534 exact interpolation seeds, 18 exact volume comparisons, 240 floating Schur-threshold cases and 30 floating graph-weight cases. I checked the code against those labels.

### Covered by the root checker

- source SHA/byte/line pinning;
- exact rational diagonal-dominance slack and a few final scalar inequalities;
- finite interpolation/support/rank/bordered-minor checks for `n=4,5,6`, only `r=1,2`;
- aggregate sampling inequality in those cases;
- floating Schur-count diagnostics;
- floating graph-frame weight/trace diagnostics.

### UNCHECKED by the root computational suite (but PASS mathematically in this audit)

The checker does **not** computationally certify the analytic arguments on lines 84–160, 218–525, 621–790; it also does not finite-test interpolation/sampling at the proof-critical higher orders `r=3,4`. In particular, heat-flow Brascamp–Lieb, rough-law limits, projection densities, scalar Fourier powers, decoupling, determinant integration, hyperbolic coarea, Riesz normalization, pivot kernels, and final measure domination are proof-only in the package. This is not a mathematical gap; it is checker coverage that should remain labeled UNCHECKED rather than inferred from `checks.json`.

I extended finite diagnostics in this run to `r=3,4` (still not proof):

- one exact symmetric `8x8`, `r=3` case: `V_3=33892`, `V_4=24552`, weighted bordered residual sum `356740`, while `(r+1)^2 V_4=392832`, exact slack `36092>0`; 498 nonsingular seeds were exercised;
- one exact symmetric `10x10`, `r=4` case: `V_4=982996`, `V_5=838608`, weighted residual sum `20125054`, while `25 V_5=20965200`, exact slack `840146>0`; 2706 nonsingular seeds were exercised.

These extend diagnostics to the actual maximum order used by Proposition 6.4 but remain finite examples only.

## Adversarial exact finite examples

### A. `r=2` completion attains both rank bounds simultaneously in the no-pivot regime

Let

```
A0 = [[ 1, 1,-2, 0, 2, 1],
      [ 1, 1, 0, 1, 0, 2],
      [-2, 0,-1, 2,-1, 0],
      [ 0, 1, 2,-1,-2, 2],
      [ 2, 0,-1,-2, 0, 2],
      [ 1, 2, 0, 2, 2, 2]]
A=A0/1000,
S={1,2}, T={3,4}, L={5,6}      (one-based indices).
```

Then `det A[S,T]=-1/500000 !=0`, every diagonal has modulus at most `1/500<eta`, and every principal two-coordinate determinant has modulus at most `3/500000<eta`; hence this finite matrix is genuinely in the no-pivot regime. The completion has

`rank R=6=3r`, `rank R[L,L]=2=r`,

with

`R[L,L]=[[1/1000,-7/2000],[0,1/250]]`.

Thus neither universal rank constant can be lowered merely by symmetric/no-pivot bookkeeping at the terminal `r=2` order relevant to the eight-direction frontier. This is a local sharpness diagnostic, **not** a counterexample to an `s_8` density theorem (the matrix is only `6x6`).

### B. Singular seed can have a nonsingular one-step extension

For

```
A = [[-1, 2,-2, 0,-2, 1],
     [ 2, 1, 1, 1,-1,-2],
     [-2, 1, 1,-2, 1, 1],
     [ 0, 1,-2, 2,-2, 1],
     [-2,-1, 1,-2, 0,-1],
     [ 1,-2, 1, 1,-1, 2]],
```

take `S={1,4}`, `T={3,5}` (one-based). The seed block is `[[-2,-2],[-2,-2]]`, so its determinant is zero. Adding row `6` and column `2` produces a `3x3` extension of determinant `4`. This explicitly confirms why Lemma 6.2's aggregate counting is an inequality rather than an equality.

## Downstream status

- Baseline `s_17` theorem: **PASS in this full B10 audit**.
- Root finite checker: PASS for its stated scope; analytic and higher-order coverage limitations above remain explicit.
- No baseline source line remains mathematically UNCHECKED by this run.
- This report does not change release-gate status or claim formal verification.
- A separate improvement report from this same run sharpens the already-established nine-direction candidate constant and records the `s_8` obstruction; that new constant requires independent review before any validation label.
