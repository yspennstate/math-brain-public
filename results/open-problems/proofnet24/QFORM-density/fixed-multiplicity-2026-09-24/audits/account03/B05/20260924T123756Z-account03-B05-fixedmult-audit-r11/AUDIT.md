# account03/B05 audit — product projections, exceptional slices, and dependency interfaces

Run: `20260924T123756Z-account03-B05-fixedmult-audit-r11`  
Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline manuscript commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256 (owner manifest): `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh math-open-problems master observed before publication: `abbed9eac2ca191022c2e67ac0fb35998fcd06ae`; the manuscript blob was unchanged in the fresh tree observed earlier in this run.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## Scope and verdict

The later owner objective supersedes this slot's older free-form three-eigenvalue coarea assignment. I therefore audited the current self-contained fixed-multiplicity manuscript, beginning with B05's assigned lens (product-projection densities and exceptional slices) and tracing every dependency used by those interfaces into the main theorem.

**Mathematical verdict for the audited interfaces: PASS.** I found no fatal mathematical defect in the product-projection lemma, its use in the scalar Fourier-power lemma, the rough-law limiting step in the geometric Brascamp--Lieb input, the hyperbolic exceptional-level treatment, or the Tonelli/conditioning passages that feed the pivot and main-theorem branches. I also spot-checked the surrounding determinant, interpolation, Schur-count, half-potential, scaling, and final-assembly chain and found no contradiction to their stated hypotheses.

This is **not** a self-awarded independent end-to-end validation of the entire 790-line manuscript. The complete source was read through its proof architecture and all major proof blocks, but I did not produce a line-by-line proof-map certification for every source line in this invocation. In addition, four supplementary files named by README/AUDIT were absent at the fresh repository tree (`SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`). That is a reproducibility/package GAP, not a mathematical counterexample, because `manuscript.tex` contains the specialized proofs used by the theorem.

## Audit records

### 1. `lem:projection` — product-projection density

**Status: PASS.**

Statement audited: for independent coordinates with densities bounded by one and `U^T U = I_d`, the marginal `U^T X` has a density bounded by `e^{d/2}`; in particular a scalar form `a·X` has density at most `sqrt(e)/|a|`.

The proof keeps the original product density. Completing `U` to `(U,W)` is only a deterministic orthogonal change of integration coordinates. For row vectors `w_i`, set `b_i=|w_i|^2=1-|U^T e_i|^2`. For `b_i>0`, the unit vectors `v_i=w_i/sqrt(b_i)` satisfy

`sum_i b_i v_i v_i^T = I_(n-d)`.

Applying the proved geometric rank-one Brascamp--Lieb inequality to

`h_i(t)=f_i((Uy)_i+sqrt(b_i)t)^(1/b_i)`

is legitimate because `0<=f_i<=1`, hence `f_i^(1/b_i)<=f_i`, and

`int h_i <= b_i^(-1/2)`.

Therefore

`p(y) <= prod_(b_i>0) b_i^(-b_i/2)`.

The logarithm obeys

`log p(y) <= (1/2) sum_(b_i>0)(-b_i log b_i)
          <= (1/2) sum_(b_i>0)(1-b_i)
          <= (1/2) sum_i(1-b_i) = d/2`,

because `sum_i b_i = tr(WW^T)=n-d`. This establishes the displayed constant. No independence of `U^T X` coordinates is asserted or used.

**Editorial clarification only:** the manuscript jumps directly from the positive-`b_i` product to `sum_i(1-b_i)=d`; inserting the middle inequality `sum_(b_i>0)(1-b_i) <= sum_i(1-b_i)` would remove a possible ambiguity when some `b_i=0`. The existing bound is nevertheless correct.

### 2. Rough-law passage in geometric Brascamp--Lieb

**Status: PASS on the stated rank-one geometric theorem.**

For bounded compactly supported positive-mass inputs, the heat-flow computation gives `partial_t F - Delta F >=0` from the frame identity. The large-time Gaussian asymptotics and compact-support Gaussian majorant justify the terminal limit. At small time, almost every pullback point is a Lebesgue point because inverse images of one-dimensional null sets under nonzero linear functionals are null by rotation/Fubini. Fatou gives the required inequality. General nonnegative integrable factors are obtained from monotone truncations `min(h_i,m) 1_[-m,m]`; both sides pass by monotone convergence. I found no hidden smoothness or bounded-support assumption left in the final theorem.

### 3. `lem:scalar-fourier` — use of product projection at the origin

**Status: PASS.**

For `p>=2`, putting `m=floor(p/2)` gives `2m<=p`, so `|hat f|^p <= |hat f|^(2m)` since characteristic functions have modulus at most one. The latter power is the characteristic function of a sum of `m` independent differences and is integrable because `|hat f|^(2m) <= |hat f|^2` and Plancherel applies to a cap-one probability density. Fourier inversion therefore supplies a continuous density version at zero, so applying the essential projection-density bound at that point is justified. The signed coefficient vector has norm `sqrt(2m)`, yielding

`int |hat f|^(2m) <= 2 pi sqrt(e)/sqrt(2m) <= 2 pi sqrt(2e)/sqrt(p)`.

No exceptional-version issue remains at zero because inversion produces a continuous representative.

### 4. `lem:hyperbola` — exceptional critical level and rough densities

**Status: PASS.**

For an indefinite physical pair, the hyperbolic parametrization has Jacobian `1/(2 sqrt(D))`. The tail truncation uses one original coordinate with a sufficiently large exponential coefficient, converts the tail integral by a monotone one-dimensional change of variables, and pays only the cap-one/mass-one bound against `1/|y|`. The resulting logarithmic envelope is asserted only for a.e. noncritical output level. This is sufficient because the proof explicitly formulates the conditional change of variables against nonnegative output test functions; the critical level is a Lebesgue-null output set for each fixed conditioning value and no pointwise selection of a rough conditional density is required.

### 5. Exceptional slices after conditioning in `prop:pivot-H`

**Status: PASS.**

For a definite pair the conditional density bound is uniform in the induced affine translation, so averaging over the complementary original coordinates is immediate. For an indefinite pair the hyperbolic envelope is integrated against the truncated kernel by Tonelli; the bound is uniform in the moving critical value. Thus no conditional density cap is inferred from an unconditional projection and none of the live correction events about conditional caps is invoked.

For the scalar-pivot branch, the manuscript uses the square profile as a conditional measure-domination formula and then Tonelli. The Schur remainder is a genuine quadratic polynomial in untouched original independent coordinates. The quarter-power small-ball lemma rules out atoms at the center needed for the logarithmic singular integral. I found no exceptional-slice leak.

### 6. Exceptional slices in the main indefinite-pair branch

**Status: PASS.**

After conditioning on the two original pivot coordinates' complement and completing the square, the critical value is the Schur-remainder quadratic polynomial `R`. The Schur spectral-count lemma leaves at least one nonzero spectral direction, so `lem:quarter` supplies a uniform logarithmic potential and in particular no atom. Averaging the hyperbolic a.e. envelope through its nonnegative-test-function formulation is therefore legitimate. The proof never conditions on rotated spectral coordinates.

### 7. `thm:determinant` / crossing-volume interface used downstream

**Status: PASS on the B05-relevant interface.**

The decoupling variables are differences of disjoint original coordinate blocks and retain independent cap-one coordinates. The geometric BL frame weights are built from `H=alpha I+a^2 M^T M`; the trace identity `sum d_i=sum(1-c_j)` is exact. With `alpha=(2 pi e)^2`, the scalar Fourier-power factors cancel the entropy factor and yield the stated determinant exponent `-1/8`. Retaining the `k`th Cauchy--Binet term gives exponent `k/4`; hence order five is integrable, while order three is used only with the half-Riesz weight. This matches the final theorem's two analytic uses.

### 8. Surrounding structural/main-theorem dependency spot checks

**Status: PASS on checked claims; complete line-by-line certification remains UNCHECKED.**

I independently rechecked the following high-risk interfaces while tracing the B05 branches:

- Schur complement spectral count: the invertible case follows from inverse compression/interlacing separately for positive and negative eigenvalues, and the singular case is reached by a valid `A+epsilon I` limiting argument.
- Sampled interpolation: the bordered-minor identity correctly gives the residual entry after subtracting the seed rows; singular seeds contribute zero weight, so the `(r+1)^2` multiplicity gives an inequality as stated.
- Completion ranks: `R-P` is supported in rows `T` or columns `S`; hence the global rank is at most `3r`, whereas `R[L,L]=P[L,L]` has rank at most `r`; `D` vanishes on the seed.
- Spectral-to-volume contradiction: the proof uses singular-value perturbation for nonsymmetric auxiliaries, forces `r+1` large diagonal entries in `L`, and the displayed diagonal-dominance constants are strict for `r<=4`.
- Full/truncated half potentials: the pivot proposition controls only `H`; `prop:nine` adds at most one from the region `|Q-a|>1` before the main scalar-pivot density estimate. No full-potential conclusion is silently substituted earlier.
- Scaling: with `Y=KX`, `tilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c`, one has `Q=(s/K^2) tilde Q`, so the normalized density bound scales as `K^2/s`.

I did not mark the complete manuscript independently validated because this run did not attach a per-line PASS/GAP record for all source lines and the promised `proof_map.csv` is absent from the repository tree.

## Package/reproducibility gaps

**Status: GAP (non-mathematical packaging).**

At the fresh repository state inspected during this run, `README.md` and `AUDIT.md` name `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`, but direct repository fetches for each of those four files returned `404 Not Found`. The manuscript itself is present and self-contained, so this does not invalidate the written proof. It does mean the advertised finite-check and proof-map package is not currently reproducible from the repository alone. Repair: commit the exact supplementary files claimed by README/AUDIT or edit those metadata files to say they are not repository-resident.

## Independent constant sharpening check

**Status: PASS for the arithmetic sharpening; threshold unchanged.**

I checked the fresh account01/B14 improvement against the manuscript formulas. With

`L0=4+4 log 16`,

the scalar-pivot truncated half-potential is

`10(8+3L0)=200+120 log 16`.

Adding the at-most-one outer contribution gives the full nine-direction half-potential

`201+120 log 16`,

and the main scalar pivot multiplies this by ten, yielding

`2010+1200 log 16 = 5337.106466... < 5340`.

The other branches are smaller, so the same proof supports the sharper constant `<5340 K^2/s` under `s_17(A)>=s`, assuming the audited baseline. This does not lower the multiplicity.

The same peer improvement correctly identifies the current `17 -> 16` obstruction: order four gives only a `|t|^{-1}` determinant envelope, while the terminal structural argument at `r=4` under `s_16` forces only four, not five, large complement diagonals. Its positive-mass heavier-neighbor argument does not propagate the residual-ratio hypothesis to the neighbor, so it is not a proof of the 16-direction theorem. **Multiplicity 16 remains GAP.**

## Current status and next obligation

No fatal defect was found in B05's assigned projection/exceptional-slice interfaces. The candidate 17-eigenvalue theorem remains a plausible complete written proof but is not independently validated by this run alone. The most useful next mathematical obligation is either (i) a truly complete second end-to-end review of all 790 source lines, or (ii) a new order-four endpoint receiver / exchange identity that closes the terminal `s_16` no-pivot chamber without assuming smooth laws or pointwise Fourier decay.

No current fixed-multiplicity `account04/B05` audit artifact was present at the pinned repository state I checked, so I did not fabricate a partner application. The later fixed-multiplicity owner objective supersedes the older partner-specific coarea instruction for this run.
