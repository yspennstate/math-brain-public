# fleet01/B02 independent fixed-multiplicity audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Run: `20260924T122547Z-fleet01-B02-fixedmult-audit-r11`.

## Source pin

- Baseline source commit supplied by the owner: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Fresh `master` snapshot checked immediately before publication: `5d3f80eea2180e48192db1c106c3320c4e878219`.
- `manuscript.tex` git blob at that fresh snapshot: `183ccd294763214e6a707e8d4749ff9a8cf7006d`, identical to the canonical baseline blob named in `README.md`/`AUDIT.md`.
- Canonical source SHA-256 reported by the source package: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- The complete 790-line `manuscript.tex`, `README.md`, and `AUDIT.md` were read in this run.

## Overall verdict

**PASS (mathematical manuscript, one independent complete review).** I found no fatal mathematical gap in the written 17-eigenvalue theorem after independently checking every displayed dependency and proof section. This is one worker's complete review, not an independent-validation certificate. The owner requirement of two genuinely separate complete reviews remains in force.

**GAP (repository package/reproducibility only).** At the fresh audited snapshot, `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are referenced by `README.md`/`AUDIT.md` but are not present at the manuscript root. Their claimed finite-test and manifest contents are therefore **UNCHECKED** in this run. This does not by itself invalidate the symbolic proof in `manuscript.tex`, but it is a release/reproducibility defect and the README should not claim those files are stored there until they actually are.

## Line-by-line / dependency audit

The source ranges below are the manuscript line ranges read directly from the pinned blob.

### A01 — lines 1--80: definitions, theorem quantifiers, architecture
**PASS.** Singular values are defined consistently; for symmetric `A` they equal absolute eigenvalues. The theorem keeps arbitrary dimension, signature, remaining spectrum, affine terms, and arbitrary independent densities bounded by `K`. The normalized parameters are `eta=1/100`, `kappa=1/80^2`. No continuity claim is silently added to the full theorem. The stated counts `9=4*3-3`, `17=4*5-3` match the later structural proposition.

### A02 — lines 81--160: Fourier normalization, inversion, negative half moments
**PASS.** With `hat f(t)=int exp(itx)f(x)dx`, Plancherel is `int |hat f|^2 = 2*pi int |f|^2` and inversion carries `1/(2*pi)`. The Gaussian identity
`E exp(-v(Z-a)^2) = (2 sqrt(pi v))^{-1} int exp(-t^2/(4v)) exp(-ita) phi_Z(t) dt`
has the correct normalization. The power-envelope integral is exactly `2ap/(p-1)`, hence density bound `ap/(pi(p-1))`. The Riesz computation is also normalized correctly: after integrating in `v`, the coefficient is `1/sqrt(2*pi)`, and a `3/4` Fourier envelope gives the stated `12 sqrt(u/(2*pi))` bound.

### A03 — lines 161--240: singular-value perturbation, Schur spectral count, diagonal dominance, start of geometric BL
**PASS.** The rank perturbation statement is valid for nonsymmetric matrices and follows from the approximation characterization of singular values. For an invertible principal pivot, `S^{-1}` is the complementary principal compression of `A^{-1}`; applying interlacing separately to positive and negative eigenvalues gives `N_S(t) >= N_A(t)-k`. The singular-`A` limiting argument preserves the non-strict threshold. Strict row diagonal dominance implies invertibility without symmetry. In the heat-flow proof, `partial_t F-Delta F = F(sum c_i v_i^2 - |sum c_i u_i v_i|^2) >= 0`; the sign is the one needed for monotonicity toward the Gaussian large-time limit.

### A04 — lines 241--320: geometric BL completion, projection density, scalar Fourier powers, decoupling statement
**PASS.** The heat-flow large-time normalization uses `sum c_i=d` and gives exactly the product of masses. In the projection lemma, `b_i=1-|U^T e_i|^2`, the remaining normalized rows form the required frame, and
`prod b_i^{-b_i/2} <= exp((1/2)sum(1-b_i)) <= exp(d/2)`.
The scalar consequence is therefore `sqrt(e)/|a|`. For `p>=2`, setting `m=floor(p/2)` is legitimate because `|hat f|<=1`; `|hat f|^{2m}` is integrable since it is bounded by `|hat f|^2`. Fourier inversion at zero plus the scalar projection bound yields
`int |hat f|^p <= 2*pi*sqrt(2e)/sqrt(p)`.
The difference density satisfies `f*tilde f <=1`. The two decoupling powers follow from Cauchy--Schwarz and then Jensen, with all conditioning on original independent coordinates.

### A05 — lines 321--400: regularized crossing determinant and volume envelopes
**PASS.** This was the primary B02 lens and was re-derived independently. Put `a=2t`, `alpha=(2*pi*e)^2`, `H=alpha I+a^2 M^T M`. The graph-frame weights satisfy `sum c_j+sum d_i=d` and `theta=sum d_i=sum(1-c_j)`. After the `H^{-1/2}` change of variables, the BL factors are
`alpha^{c_j/2}c_j^{-c_j/2}||g_j||_{1/c_j}` and `d_i^{-d_i/2}||h_i||_{1/d_i}`.
The scalar Fourier-power lemma gives
`||h_i||_{1/d_i} <= (2*pi*sqrt(e d_i))^{d_i}`;
its `d_i^{d_i/2}` exactly cancels the BL scaling `d_i^{-d_i/2}`. The entropy factor from `c_j` is at most `e^{theta/2}`. Hence the remaining scalar multiplier is `(2*pi*e/sqrt(alpha))^theta=1`, so taking fourth roots gives exactly
`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^{-1/8}`.
No hidden leverage assumption appears. Keeping the `k`th elementary-symmetric term gives `u_k=pi e Z_k^{-1/(2k)}` and Fourier power `k/4`; for `k=5` inversion gives `5e Z_5^{-1/10}`, and for `k=3` the Riesz bound is `12 sqrt((e/2) Z_3^{-1/6})`.

### A06 — lines 401--480: scalar square, definite pair, hyperbolic pair
**PASS.** The translated-square density and inverse-image length have the correct factors of two. The two-dimensional definite Jacobian is `1/(2 sqrt(|det B|))`, hence density bound `pi M/sqrt(|det B|)`. In the indefinite case the hyperbolic coordinates have the same Jacobian. The tail argument chooses an original coordinate, not a rotated independent coordinate. The cutoff `T_1=(3/4)log 2` follows from the worst ratio `|w_i|/|u_i|<=sqrt(2)`. Each tail is controlled by the original one-coordinate density and the decreasing weight `1/|y|`; the two tails plus the middle interval yield the displayed `6+log_+(32/(delta Lambda))`, and `Lambda>=2/sqrt(D)` gives the final `16 sqrt(D)` normalization.

### A07 — lines 481--560: quarter-power concentration, pivot-volume definitions, sampling setup
**PASS.** If a diagonal coefficient is at least `||S||/2`, the scalar inverse-image estimate gives the required quarter-power bound. Otherwise random signs produce a literal physical cross block of norm at least `||S||/4`; using only its top singular value in the determinant theorem gives the `|t|^{-1/4}` envelope. The Gaussian localization calculation has coefficient
`2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)`; the manuscript's elementary estimate `<40/3<16` is valid. Layer cake then yields the logarithmic potential. The no-pivot entry bound follows directly from the principal `2x2` determinant inequality. In the sampling lemma, squaring removes ordering signs, and every disjoint `(r+1)` ordered pair is charged at most `(r+1)^2` times; singular seeds contribute zero weight, so the manuscript correctly uses an inequality rather than equality.

### A08 — lines 561--640: completion, global/restricted ranks, spectral-to-volume conversion, random cut
**PASS.** With `E` equal to the off-diagonal `LxL` residual and `D` the diagonal residual on `L`, one has `R_{L,L}=P_{L,L}` and therefore restricted rank at most `r`. Globally, `R-P` is supported in rows `T` or columns `S`, giving rank at most `2r`; together with `rank P<=r`, this yields `rank R<=3r`. For a bad volume ratio, `||E||_F<=1/16`. From `s_{4k-3}(A)>=1` and global rank `3r`, at least `r+1` diagonal entries of `D` have magnitude at least `1-epsilon`; because `D` vanishes on the seed these entries lie in `L`. The manuscript's row-diagonal-dominance slack is
`371/400 - 23/28 = 297/2800 >0`,
so an `(r+1)x(r+1)` block of `R_{L,L}` would have rank `r+1`, contradicting the restricted rank bound. The random cut factor is exactly `4^{-k}`.

### A09 — lines 641--720: no-pivot consequences, singular kernels, pivot half-potentials
**PASS.** From `Z_k >= 4^{-k}kappa^k` one gets `Z_k^{-1/(2k)}<=160`; hence the order-three full half-potential is `12 sqrt(80e)<200`, and order five gives density `800e<2400`. The kernel `J(d)` is split correctly into a bounded near region and a logarithmic far region. The log-kernel convolution is maximized when the interval superlevel sets are centered together, giving value `8`. The scalar-pivot half-potential uses the Schur survivor and does not assume independence between the square and remainder. Definite and indefinite pair branches use conditional measure domination and Tonelli, not exceptional pointwise slices.

### A10 — lines 721--790: nine-eigenvalue half-potential, main theorem, scaling, limitations
**PASS.** With a pivot, `s_9>=1` is more than enough for the two-eigenvalue hypothesis in the pivot-half-potential proposition; without a pivot the full half-potential is already `<200`. The tail outside `|Q-a|<=1` contributes at most one, giving the stated `601`. In the main scalar-pivot branch, a one-coordinate Schur complement leaves at least 16 eigenvalues of modulus at least one, so the nine-direction bound applies. A two-coordinate pivot leaves at least 15. In the indefinite-pair branch only one surviving eigenvalue is needed for the logarithmic potential. The normalization `Y=KX`, `tilde Q=(K^2/s)Q` is exact and yields the factor `K^2/s` in the final density. The continuity limitation is stated correctly: only the no-pivot Fourier-L1 branch automatically gives a continuous density.

## Package / non-proof items

- `README.md`: **PASS** as a description of the intended theorem and baseline, except for the missing-file issue below.
- `AUDIT.md`: **PASS as a self-audit document**, but its finite-test claims are not independent evidence.
- `SOURCE_MANIFEST.json`: **GAP / missing at audited root**.
- `proof_map.csv`: **GAP / missing at audited root**.
- `verify.py`: **GAP / missing at audited root**.
- `checks.json`: **GAP / missing at audited root**.
- Claims about the absent finite test suite and compiled-PDF hashes: **UNCHECKED** in this run.
- Bibliographic priority/attribution beyond the proof's self-contained mathematics: **UNCHECKED**; these citations are not used as mathematical dependencies.

## Threshold reduction audit

**No rigorous reduction from 17 to 16 was obtained.** The only place where 17 is structurally essential in the present proof is the no-pivot order-five terminal bad-ratio chamber `r=4`. With `s_17>=1`, global rank `rank R<=12` leaves five large diagonal entries of `D`, contradicting `rank R[L,L]<=4` after diagonal dominance. With only `s_16>=1`, the same rank perturbation leaves only four large diagonal entries. A diagonally dominant `4x4` block has rank four, which is compatible with the restricted rank bound. Therefore replacing 17 by 16 in the current proof is invalid; a genuine 16-eigenvalue theorem needs a new terminal-`r=4` ingredient or a stronger analytic endpoint than the order-five route.

I also checked the obvious analytic endpoint replacement: an order-four crossing gives only a `|t|^{-1}` Fourier envelope. Combining that fact merely with the manuscript's one-direction quarter-power concentration cannot imply an `L^infinity` density in general. The model density
`p(x)=(1/2) log(1/|x|) 1_{|x|<1}`
is unbounded, has characteristic function `Si(t)/t=O(1/|t|)`, and satisfies uniform quarter-power small-ball bounds. Thus a 16-direction improvement cannot be justified by simply gluing the existing `k=4` Fourier endpoint to the existing quarter-power concentration lemma; additional product/quadratic structure is required.

## Independent-review status

This file records one complete end-to-end review by fleet01/B02. It does not certify a second independent review and does not mark the manuscript independently validated. The full three-eigenvalue conjecture is not addressed by this fixed-multiplicity theorem.
