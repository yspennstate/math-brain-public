# fleet03/B10 independent full audit — fixed multiplicity 17

Run: `20260924T121633Z-fleet03-B10-fixedmult-audit-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer lens: constants, exact arithmetic, adversarial finite examples; fleet03 exact identities and alternative derivations.  
Pinned manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Advertised source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh math-open-problems master observed immediately before publication: `1dab25580592c69084c149ebc42e6d9e999acef6`.

## Verdict

**Mathematical verdict: PASS.** I read all 790 source lines of `manuscript.tex` and reconstructed every dependency used in the main theorem. I found no fatal mathematical gap in the claimed 17-eigenvalue theorem:

> If the independent real coordinate densities are bounded by `K`, `A=A^T`, `s_17(A)>=s>0`, and `b,c` are arbitrary, then `X^T A X+b^T X+c` has an essentially bounded density, with the manuscript's stated bound `10000 K^2/s`.

This is one worker's independent review, not a two-review validation certificate. The unrestricted three-eigenvalue conjecture remains open. The manuscript proves an essentially bounded density globally; continuity is proved on the no-pivot Fourier branch but is not established for every pivot branch.

**Packaging/reproducibility verdict: GAP, non-mathematical.** At the root visible in this run, `README.md`, `AUDIT.md`, `manuscript.tex`, `audits/`, and `improvements/` were present, but the advertised `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` were absent. I therefore did not treat the advertised finite-check counts or SHA-256 as independently reproduced evidence. The proof itself is self-contained in the pinned source blob.

## End-to-end audit

| Source range | Claim / dependency | Verdict | Independent check |
|---|---|---|---|
| 41–80 | Theorem, quantifiers, architecture, normalization | PASS | Arbitrary signature, dimension, affine terms, remaining spectrum, and rough product laws are retained. Final scaling with `Y=KX` and `Q=(s/K^2) Qtilde` is correct. |
| 81–160 | Gaussian Fourier identities, inversion, power envelope, negative half moments | PASS | Gaussian normalization, Plancherel convention, `1/(2pi)` inversion constant, Riesz coefficient `1/sqrt(2pi)`, and weighted `3/4`-envelope integral `12 sqrt(u)` check. |
| 161–220 | Singular-value perturbation, Schur spectral count, diagonal dominance | PASS | Approximation formula is valid nonsymmetrically. For invertible `A`, `S^{-1}` is the complementary compression of `A^{-1}`; positive/negative interlacing gives the absolute spectral count. The `epsilon I` singular limiting argument is valid. |
| 221–282 | Geometric rank-one Brascamp–Lieb and product projections | PASS | Heat-flow sign is correct, the frame map is a contraction, the large-time scaling uses `sum c_i=d`, and the rough-input limit is supported by Fatou/monotone approximation. Projection proof never asserts independence after rotation. |
| 283–400 | Integrated scalar Fourier powers, decoupling, determinant theorem, volume envelopes | PASS | `m=floor(p/2)>=p/4`; difference coordinates retain cap one. Both decoupling powers are valid. In the determinant argument the `d_i` powers cancel and `alpha=(2pi e)^2` cancels the residual exponential exactly; fourth roots give exponent `-1/8`. Cauchy–Binet constants lead to the stated `k=5` density and `k=3` half-potential bounds. |
| 401–526 | Square profile, definite pair, hyperbolic pair, quarter-power concentration | PASS | Coarea/Jacobian factors and original-coordinate tail estimates check. The indefinite pair logarithmic envelope uses only the original independent coordinates. The random-sign cross-block construction gives norm at least `L/4`; the Gaussian smoothing exponent is `1/4`. |
| 527–651 | Disjoint volumes, sampled interpolation, nonsymmetric completion, spectral-to-volume conversion, random cut | PASS | The bordered determinant identity is exact. Singular seeds justify an inequality, not equality. Support gives `rank R<=3r`; on the seed complement `R_LL=P_LL` gives `rank<=r`; `D` vanishes on `S union T`. The perturbation count and strict diagonal-dominance contradiction are valid for nonsymmetric `R`. |
| 652–760 | Singular kernels, pivot half potentials, nine-direction theorem, main theorem | PASS | Full versus truncated half potentials are kept separate. Every pivot invocation meets its exact Schur spectral-count requirement. Conditional measure domination is averaged through Tonelli rather than conditional-independence shortcuts. |
| 761–790 | Threshold accounting and limitations | PASS | Order five gives integrable exponent `5/4`; order three only gives the half-potential after the `|t|^-1/2` weight. The source correctly declines to claim the three-eigenvalue theorem or pivot-branch continuity. |

No source segment remains `UNCHECKED` in this review.

## Exact arithmetic checks

The most delicate finite arithmetic in the spectral-to-volume contradiction is exact:

`371/400 - 23/28 = 297/2800 > 0`.

Thus the chosen `(r+1) x (r+1)` block is strictly row diagonally dominant for every terminal `r<=4`. The two no-pivot analytic constants are also safely inside the manuscript's rounded bounds:

`12 sqrt(80 e) = 176.959336187... < 200`,

`800 e = 2174.625462767... < 2400`.

Those decimal evaluations are diagnostics only; the manuscript already supplies elementary rational inequalities sufficient for the displayed rounded bounds.

## New exact constant improvement found in this audit

The quarter-power coefficient in the manuscript is

`Cq = 2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)`.

The source only needs `Cq<16`. A fully elementary chain gives the stronger exact bound

`Cq < 35/8`.

Indeed:

1. `2^(5/8)<31/20`, since
   `31^8 - 32*20^8 = 33,691,037,441 > 0`.
2. `pi^(-1/4)<19/25`: use `pi>3` and
   `3*19^4 - 25^4 = 338 > 0`.
3. `e^(3/8)<22/15`: first
   `e < 8/3 + (1/24) sum_{j>=0} 5^{-j} = 87/32 < 11/4`,
   and then
   `64*22^8 - 1331*15^8 = 100,848,484,429 > 0`,
   which is equivalent to `(11/4)^3 < (22/15)^8`.
4. For the gamma factor, on `[0,1]`, `e^{-x}<=1-x+x^2/2`, while on `[1,infinity)` use `x^{-5/8}<=1`. Hence
   `Gamma(3/8) <= 8/3 - 8/11 + 4/19 + e^{-1}`.
   Since `e>8/3`, `e^{-1}<3/8`, so
   `Gamma(3/8) < 12665/5016 < 81/32`, with exact last margin `127/20064`.

Multiplying the four rational upper bounds,

`Cq < (31/20)(19/25)(22/15)(81/32) = 174933/40000 = 4.373325 < 35/8`,

with final exact margin `67/40000`.

Consequently the quarter-power concentration lemma strengthens to

`P{|R-a|<rho} <= min(1,(35/8)(rho/L)^(1/4))`.

For `L>=1`, layer cake gives

`sup_a E log_+(1/|R-a|) <= 4+4 log(35/8) < 10`.

For the last strict inequality, `e>27/10` from the first six positive exponential-series terms and

`(27/10)^3 - (35/8)^2 = 4339/8000 > 0`,

so `log(35/8)<3/2`.

The scalar-pivot truncated half-potential is therefore below

`10(8+3*10)=380`.

The indefinite-pair pivot becomes the dominant half-potential branch. From the manuscript formula

`H_ind <= 10(32+4 log 16)+4/e`,

one gets the elementary bound `H_ind<434`: `log 2<7/10` because `e>27/10` and

`27^7 - 1024*10^7 = 220,353,203 > 0`,

hence `log16<14/5`; also `4/e<3/2` from `e>8/3`. Therefore

`10(32+4 log16)+4/e < 433.5 < 434`.

The definite-pair branch is `<160` and the no-pivot nine-direction branch is `<200`. Thus Proposition 7.3 may be sharpened to

`H(Q)<434`, and `sup_a E|Q-a|^(-1/2)<435`.

The scalar-pivot branch of the main theorem is then `<4350`. Every other main branch is smaller, so the same hypotheses prove the stronger universal statement

`||p_Q||_infinity < 4350 K^2/s`.

Keeping the logarithm and `e` instead of rounding gives the even sharper valid same-threshold constant

`3210 + 400 log 16 + 40/e = 4333.7506665...`,

but `4350` is a simple completely elementary integer envelope. This improves only the constant; it does not lower multiplicity.

## New no-pivot adversarial finite example: both rank bounds are genuinely sharp

The completion lemma uses two distinct bounds, `rank R<=3r` globally and `rank R_LL<=r` on the seed complement. These cannot be lowered merely from the no-pivot hypothesis.

For `r=1`, take

`A0 = [[0,-1,-1],[-1,0,-1],[-1,-1,0]]`,

and `A=(1/20)A0`. Choose the seed `S={1}`, `T={2}`, `L={3}`. Then `B=-1/20` is invertible. Every diagonal entry is zero, and every principal `2 x 2` determinant equals `-1/400`, whose modulus is `< eta=1/100`; hence `A` has **no eta-pivot**.

The interpolation is exact off the residual diagonal, so `E=0`,

`D=diag(0,0,1/20)`,

and

`R=(1/20)[[0,-1,-1],[-1,0,-1],[-1,-1,-1]]`.

Directly, `rank R=3` while `rank R_LL=1`. Direct sums of `r` copies, with `S,T,L` chosen blockwise, give simultaneously

`rank R=3r`, `rank R_LL=r`,

and remain no-pivot. At `r=4` this gives exact ranks `12` and `4`. The scaled base block has eigenvalues `{-1/10,1/20,1/20}`, so this is deliberately **not** a counterexample to the large-spectrum proposition. It proves only that a reduction from seventeen to sixteen cannot come from replacing the two rank bounds by better universal constants based on no-pivot structure alone.

This complements the terminal-count obstruction: at order five, the bad-ratio case `r=4` plus only `s_16(A)>=1` forces at most four large diagonal entries, which is compatible with `rank R_LL=4`. The existing contradiction needs five. A 16-eigenvalue theorem therefore requires an additional consequence of the **combined** large-spectrum, sampling, and no-pivot hypotheses, or a different analytic receiver. This review does not claim 16 is false.

## Numerical diagnostics performed in this run

These are checks, not proof premises:

- 2000 random symmetric block matrices and thresholds: no violation found of `N_S(t)>=N_A(t)-k` for invertible sampled pivots.
- 1000 random sampled-completion instances: no violation found of the displayed completion identity or global/restricted rank bounds.
- Direct-sum no-pivot sharpness example: exact ranks `12` and `4` at `r=4`.

No Monte Carlo output-density histogram is used as evidence for the theorem.

## Status and next obligation

**Baseline:** PASS for the pinned 17-eigenvalue theorem; one independent review only.  
**Improvement:** PROVED same-threshold constant `4350 K^2/s`; the exact displayed constant `3210+400 log16+40/e` is smaller.  
**Threshold:** 16 remains unpaid. The precise next structural obligation is the terminal sampled `r=4` chamber: exploit information beyond the two raw rank bounds to force a fifth effective direction/crossing contribution from `s_16>=1`, or replace the order-five receiver.  
**Full QFORM:** OPEN.  
**Continuity:** continuous on the no-pivot Fourier branch; not proved globally by the pivot branches.
