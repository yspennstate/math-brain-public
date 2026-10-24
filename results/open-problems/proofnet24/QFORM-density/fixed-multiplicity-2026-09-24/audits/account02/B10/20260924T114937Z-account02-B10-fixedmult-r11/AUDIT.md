# account02/B10 independent end-to-end audit — fixed multiplicity 17

Run: `20260924T114937Z-account02-B10-fixedmult-r11`

Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Review basis: current master was first read at `406c30abfcdb1a0c77ffb2071341cca90ffad76d` and re-resolved before writing at `40707d098ab29d59b647bcbd47e5448dec66e7d0`. The manuscript blob was unchanged: `183ccd294763214e6a707e8d4749ff9a8cf7006d`. The same blob is present at the advertised initial source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`. The advertised SHA-256 is `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`; I pinned the git blob but did not independently recompute that SHA-256 because the advertised checker/manifest files are absent from the repository tree available in this run.

## Verdict

**Mathematical verdict: PASS, one independent full end-to-end review.** I read all 790 source lines and independently reconstructed each specialized step used by the theorem. I found no fatal gap in the candidate theorem:

> If the independent real coordinate densities are bounded by `K`, `A=A^T`, and `s_17(A)>=s>0`, then every affine quadratic polynomial `X^T A X+b^T X+c` has an essentially bounded density.

The manuscript's stated constant `10000 K^2/s` is valid. This review is one independent end-to-end PASS, not the two-review validation required by the current objective.

**Packaging/reproducibility verdict: GAP, non-mathematical.** At the latest root listing available before this write, `README.md`, `AUDIT.md`, `manuscript.tex`, and the newly populated `audits/` directory were present. The advertised `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` were not present. Therefore I could not inspect or rerun those advertised finite checks. This does not alter the self-contained proof text, but the README/AUDIT reproducibility claims presently exceed the delivered tree.

## Line-by-line proof audit

### Lines 41–80: statement, normalization, architecture — PASS

The theorem is stated with the correct quantifiers, arbitrary signature and affine terms, and no regularity/support/moment assumptions. The normalization to `K=s=1` and the final scaling are algebraically correct. The proof architecture separates scalar/pair pivots from the no-pivot crossing-volume branch without assuming independence after a spectral rotation.

### Lines 81–160: Fourier inversion, power envelope, half-Riesz potential — PASS

The Gaussian regularization proof of Plancherel/inversion is valid for the stated rough laws. The power-envelope integration gives `ap/[pi(p-1)]`. The negative-half-moment representation has the correct gamma normalization; after the change of variables in the Gaussian integral the coefficient is `1/sqrt(2 pi)`. The weighted integral under a `3/4` envelope is exactly `12 sqrt(u)`, yielding the displayed half-potential constant.

### Lines 161–220: singular-value perturbation, Schur spectral count, diagonal dominance — PASS

The singular-value distance formula is used correctly for nonsymmetric auxiliaries. The Schur-complement count is valid: for invertible `A`, `S^{-1}` is the complementary principal compression of `A^{-1}` and positive/negative interlacing controls the number of eigenvalues with modulus above the reciprocal threshold; the singular case follows by the stated `epsilon I` perturbation. Strict row diagonal dominance is applied in its correct nonsymmetric form.

### Lines 221–282: geometric Brascamp–Lieb and product projections — PASS

The heat-flow calculation has the correct sign:

`partial_t F - Delta F = F( sum c_i v_i^2 - |sum c_i u_i v_i|^2 ) >= 0`.

The frame identity makes the map with columns `sqrt(c_i)u_i` a contraction. The large-time Gaussian limit has the correct scaling `sum c_i=d`; the `t downarrow 0` step is justified by Lebesgue points and Fatou. In the projection lemma, rows with `b_i=0` are legitimately dropped and `-b log b<=1-b` gives the claimed `e^{d/2}` cap without probabilistic rotation.

### Lines 283–400: scalar Fourier powers, decoupling, regularized crossing determinant, volume envelopes — PASS

For `p>=2`, `m=floor(p/2)>=p/4` and `|hat f|<=1` reduce to an even power; the density-at-zero estimate for the sum of `m` independent differences gives the displayed `2 pi sqrt(2e)/sqrt(p)` bound.

The two decoupling inequalities are correct and preserve original-coordinate product provenance. In the determinant proof, the Gaussian regularizer and the frame exponents are consistent. The potentially delicate constants cancel exactly: the `d_i^{-d_i/2}` terms cancel the `sqrt(d_i)` Fourier factors, while `prod c_j^{-c_j/2}<=e^{theta/2}` combines with `(2 pi sqrt(e))^theta` to give `(2 pi e)^theta`; since `alpha=(2 pi e)^2`, no residual exponential factor remains. Taking fourth roots yields

`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^{-1/8}`.

Cauchy–Binet then gives the stated order-`k` envelopes. For `k=5`, the inversion constant is `5e Z_5^{-1/10}`; for `k=3`, the half-potential constant is `12 sqrt((e/2) Z_3^{-1/6})`.

### Lines 401–526: square/pair kernels and quarter-power concentration — PASS

The scalar square profile and interval-preimage bound are correct. The definite-pair area computation uses only a deterministic orthogonal parametrization of the integral, not rotated-coordinate independence.

For the indefinite pair, the hyperbolic parametrization has Jacobian `1/(2 sqrt(D))`. On each tail one original coordinate is monotone once `t >= (3/4)log 2`; the cap-one/mass-one bathtub estimate gives the logarithmic tail. The two branches and `Lambda>=2/sqrt(D)` yield exactly

`D^{-1/2}(6+log_+(16 sqrt(D)/|z-v|))`.

The quarter-power argument is also valid. The random-sign split gives a cross block of norm at least `||S||/4`; retaining one singular factor in the determinant theorem and Gaussian smoothing gives the coefficient

`2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8) = 3.995259... < 16`.

Layer cake then gives `L0=4+4 log 16`.

### Lines 527–651: sampled interpolation, completion, spectral-to-volume implication — PASS

The bordered determinant identity and weighted sampling count are correct; singular seeds can only remove representations, hence the manuscript correctly uses an inequality rather than equality. The completion has

`rank R <= 3r`, `R[L,L]=P[L,L]`, and `rank R[L,L]<=r`.

The support proof of the global `3r` rank and the restricted `r` rank is valid even though `P,R,E` need not be symmetric.

For the bad-ratio case, `epsilon<=(r+1)/80<=1/16`. With `m=4k-3`, singular-value perturbation and `rank R<=3r` force at least `r+1` entries of the diagonal `D` to have modulus at least `1-epsilon`, all in `L`. On the resulting `(r+1)`-set,

`|R_ii| >= 371/400`,

and each row has off-diagonal sum strictly below

`4(1/7+1/16)=23/28`.

The exact diagonal-dominance slack is

`371/400 - 23/28 = 297/2800 > 0`.

This contradicts `rank R[L,L]<=r`. The `r=0` branch is also correct. The fair-cut expectation is exactly `4^{-k}V_k`; hence `Z_k^{-1/(2k)}<=160`. The resulting constants are

`12 sqrt(80 e) = 176.959336... < 200`,

and

`800 e = 2174.625463... < 2400`.

### Lines 652–760: singular kernels, pivot half-potentials, nine-direction bound, main proof — PASS

The two kernel estimates are valid; the near-singularity beta/hyperbolic integral in `J(d)` is bounded uniformly and the far part contributes at most the logarithm stated. The log-kernel rearrangement is legitimate because both superlevel sets are intervals and their overlap is maximized by aligning centers.

For a scalar pivot, Schur leaves one large direction and the quarter-power logarithmic bound gives

`H(Q) <= 200+120 log 16 = 532.710647...`.

The definite pair is below `40 pi`, and the indefinite-pair truncated half-potential is below

`10(32+4 log 16)+4/e = 432.375067...`.

Thus the manuscript's rounded universal pivot bound `600` is safe. Combining with the no-pivot nine-direction bound gives the stated full half-potential `<=601`.

The final four branches are consistent: no-pivot `<2400`; scalar pivot `<=6010`; definite pair `<40`; indefinite pair is in fact

`<=10(10+5 log 16)+1/e = 238.997316... <251`.

The general `K,s` rescaling is exactly correct.

### Lines 761–790: threshold accounting and limitations — PASS

The text correctly distinguishes order five, whose determinant envelope exponent `5/4` is integrable, from order three, whose exponent `3/4` is only sufficient after the half-Riesz weight. The manuscript does not overclaim the three-eigenvalue conjecture or continuity in the pivot branches.

## New quantitative improvement: the same proof gives a smaller final constant

Status: **PROVED improvement, same multiplicity 17.** No new lemma is needed.

The scalar-pivot truncated half-potential estimate is not merely `<600`; the displayed proof gives

`H_* := 200 + 120 log 16`.

This dominates all other pivot-H bounds and the no-pivot nine-direction bound. Hence every nine-direction remainder used by the main scalar-pivot branch satisfies

`sup_a E|R-a|^{-1/2} <= 1 + H_* = 201 + 120 log 16`.

Since `|a_ii|^{-1/2}<=10`, the scalar branch is bounded by

`C_* := 2010 + 1200 log 16`.

All other main branches are smaller. Therefore the theorem can be strengthened, with no change of hypotheses, to

`||p_Q||_infinity <= (2010 + 1200 log 16) K^2/s < 5610 K^2/s`,

where the final integer inequality uses the manuscript's own `log 16<3` estimate. This is recorded separately under the improvement path.

## Multiplicity reduction attempt: exact terminal obstruction of the present rank-count proof

Status: **GAP for 16; obstruction to a naive one-index reduction, not a counterexample to a 16-eigenvalue theorem.**

The only place where `17` is essential is the no-pivot order-five volume step. In the terminal bad-ratio case `r=4`, the manuscript uses

`s_17(D+R)>=1-epsilon`, `rank R<=12`

to force five large diagonal entries of `D`; these create a `5 x 5` invertible block inside `R[L,L]`, contradicting `rank R[L,L]<=4`.

With only `s_16`, the same inequality forces only four large entries. An invertible `4 x 4` block is compatible with restricted rank four, so the contradiction disappears exactly at this terminal case. The global/support rank constants themselves are not artifacts of a trivial estimate: already at `r=1` the symmetric exact matrix

```
A0 = [[ 2, 1, 0, 0],
      [ 1, 0, 1,-1],
      [ 0, 1, 2, 0],
      [ 0,-1, 0, 0]]
```

with `S={1}`, `T={2}` (1-based), `L={3,4}`, has `B=1`; the manuscript completion has `E=0`,

```
D = diag(0,0,2,0),
R = [[ 2, 1, 0, 0],
     [ 1, 0, 1,-1],
     [ 0, 1, 0, 0],
     [ 0,-1, 0, 0]],
```

so `rank R=3` and `rank R[L,L]=1` simultaneously. Direct sums give algebraic saturation `3r` and `r`. This example has a pivot and therefore is **not** a counterexample to the no-pivot proposition; it shows only that a 16-direction proof needs extra no-pivot/sampling structure or a different analytic receiver, not a cosmetic improvement of the two rank bounds.

The first unpaid implication is therefore:

`QFORM-FIXEDMULT-R4-TERMINAL-STRUCTURE-v1` — in the no-pivot order-five bad-ratio chamber with `r=4`, use the exact sampled identities and no-pivot inequalities to force either an additional effective direction/crossing volume or a different density receiver from only `s_16>=1`; alternatively produce a source-valid family showing this terminal implication is false.

## Required legacy source result: actual receiver use

The older pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` proves the ruled one-sheet estimate for signature `(2,1)`. Applying it to a genuinely rotated exact-rank-three target, let

`r1=(1,1,1,1)/2`, `r2=(1,-1,1,-1)/2`, `r3=(1,1,-1,-1)/2`,

`A=r1 r1^T+r2 r2^T-r3 r3^T`.

Then `A` has nonzero spectrum `{1,1,-1}` and, for arbitrary independent original-coordinate cap-one laws,

`p_{X^T A X}(s) <= pi sqrt(2)` for every `s>=0`.

This is a real non-diagonal product-source inequality; no post-rotation independence is asserted. It is not used as a premise in the 17-eigenvalue audit.

## Final scope

Result status: **one independent full PASS of the self-contained 17-eigenvalue theorem; same-threshold constant improved; 16 remains unpaid.** The missing supplementary files are a reproducibility/package gap, not a mathematical gap in the source blob reviewed here. Full three-eigenvalue QFORM remains open.
