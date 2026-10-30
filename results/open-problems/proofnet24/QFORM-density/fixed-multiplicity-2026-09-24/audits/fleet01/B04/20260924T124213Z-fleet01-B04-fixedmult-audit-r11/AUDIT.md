# fleet01/B04 independent audit — fixed-multiplicity candidate

Run: `20260924T124213Z-fleet01-B04-fixedmult-audit-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Starting lens: geometric Brascamp--Lieb heat flow, derivative sign, integrations by parts, Gaussian domination, and limiting/approximation steps.

## Source pin

Repository: `yspennstate/math-open-problems`, branch `master`.  
Canonical manuscript: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.  
Owner baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Fresh repository head observed while reading: `bed04b22efb76e596e7ffdd5f454c5a7f830b754`.  
Manuscript git blob on fresh master: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Pinned manuscript SHA-256 from the owner manifest: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
The fresh blob is the same blob specified for the baseline candidate, so this audit is of the intended 790-line source.

## Verdict

**Mathematical verdict: PASS for the complete written 17-eigenvalue argument in this B04 review.** I found no false statement and no mathematical gap after an end-to-end source audit. This is one independent worker review only; it is not a self-awarded independent-validation certificate and does not alter the owner's requirement of two genuinely separate complete reviews before validation. It does not solve the unrestricted three-eigenvalue conjecture.

**Repository-package verdict: GAP / supplementary materials UNCHECKED.** `README.md` and `AUDIT.md` advertise `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` at the manuscript root. Fresh direct fetches of all four paths returned 404. Therefore the advertised finite checker and its recorded outputs were not reproducible from the current package in this run. I did not use those advertised finite checks as proof. The self-contained `manuscript.tex` itself was read in full and audited directly.

No mathematical line of `manuscript.tex` remains UNCHECKED in this review. The absent four supplementary files are UNCHECKED.

## Complete source audit

### Lines 1--74 — definitions, theorem, normalization, proof architecture: PASS

The theorem has the intended full quantifiers: arbitrary dimension; independent real coordinate laws with density caps `K`; arbitrary real symmetric `A`; arbitrary affine `b,c`; no moment, support, log-concavity or identical-law assumption. For symmetric `A`, the singular values are exactly the absolute eigenvalues. The target scale `K^2/s` is correct. The pivot/no-pivot case split is exhaustive under the manuscript definition. The statements `9=4*3-3` and `17=4*5-3` match the later structural proposition.

### Lines 75--129 — Fourier conventions, Gaussian regularization, inversion, power envelope: PASS

For `g_epsilon(x)=(4*pi*epsilon)^(-1/2)exp(-x^2/(4epsilon))`, the stated transform `exp(-epsilon t^2)` matches the Fourier convention. The Plancherel proof uses an `L^2` approximate identity legitimately; monotone convergence applies to the nonnegative regularized Fourier integral. When `phi_Z` is integrable, Gaussian-smoothed laws converge uniformly to the inverse transform and weak convergence identifies that function with the law. The power-envelope integral is exactly `2ap/(p-1)`, giving `ap/[pi(p-1)]` after inversion.

### Lines 130--169 — negative half moments: PASS

The gamma representation is used only under Tonelli on nonnegative quantities. The inner Gaussian integral is

`int_0^infinity v^(-5/4) exp(-t^2/(4v)) dv = sqrt(2) Gamma(1/4)|t|^(-1/2)`,

which produces the displayed factor `(2*pi)^(-1/2)`. For the `3/4` Fourier envelope, the weighted integral is exactly `12 sqrt(u)`, hence the stated `12 sqrt(u/(2*pi))` bound.

### Lines 170--218 — singular values, Schur spectral counts, diagonal dominance: PASS

The approximation formula for singular values proves both the Lipschitz perturbation estimate and the rank-shift inequality without symmetry. For invertible `A`, the complementary principal block of `A^{-1}` is `S^{-1}`. Positive and negative eigenvalue interlacing for principal compressions, applied separately, gives `N_S(t)>=N_A(t)-k`. The singular case is reached safely by `A+epsilon I` with threshold relaxed to `t-|epsilon|`. Strict diagonal dominance is correctly applied to a possibly nonsymmetric matrix.

### Lines 219--255 — geometric Brascamp--Lieb heat-flow proof: PASS

This was the primary B04 lens and was independently re-derived.

For `f_i(t)=g_t*h_i`, the chosen heat kernel satisfies `partial_t f_i=partial_s^2 f_i`. With `v_i=partial_s log f_i` and `F=prod_i f_i(t,u_i.x)^{c_i}`, direct differentiation gives exactly

`(partial_t-Delta)F = F[sum_i c_i v_i^2 - |sum_i c_i u_i v_i|^2]`.

The frame map whose columns are `sqrt(c_i)u_i` has `WW^T=I`, hence operator norm one, so the bracket is nonnegative. Thus the derivative sign is correct.

For bounded compactly supported positive-mass data and time in a compact subinterval of `(0,infinity)`, each heat convolution is strictly positive, has Gaussian tails, and its logarithmic derivatives grow at most polynomially. The frame identity converts the product Gaussian decay into a genuine `exp(-c|x|^2)` majorant. This justifies differentiation under the integral, integration by parts, and vanishing boundary terms, so `int F(t,x)dx` is nondecreasing.

Taking traces gives `sum c_i=d`. After `x=sqrt(t)z`, each factor satisfies

`sqrt(t) f_i(t,sqrt(t)u_i.z) -> (4*pi)^(-1/2) M_i exp(-(u_i.z)^2/4)`.

The frame identity gives the combined exponent `-|z|^2/4`; compact support supplies a uniform Gaussian majorant such as `C exp(-|z|^2/8)` for `t>=1`. Dominated convergence therefore gives the exact large-time limit `prod_i M_i^{c_i}`.

At `t downarrow 0`, the inverse image of a one-dimensional null set of non-Lebesgue points under each nonzero linear functional is null by rotation and Fubini. Fatou then gives the correct inequality direction. Finally `min(h_i,m)1_{[-m,m]}` increases to a general nonnegative integrable `h_i`, and monotone convergence closes the rough-data limit. I found no missing boundary term, sign error, normalization error, or hidden smoothness assumption.

### Lines 256--309 — projection densities and scalar Fourier powers: PASS

The orthogonal completion `(U,W)` is only a deterministic change of variables in an integral; no independence of rotated coordinates is asserted. With `b_i=|w_i|^2`, the normalized nonzero rows form the exact geometric frame. Since `0<=f_i<=1` and `1/b_i>=1`, the one-dimensional integrals are at most `b_i^(-1/2)`. The entropy inequality `-b log b<=1-b` and `sum_i(1-b_i)=d` yield `e^{d/2}`. The phrase summing over `i` is harmless even for dropped `b_i=0`, because the limiting left contribution is zero and the right contribution is nonnegative.

For scalar Fourier powers, `m=floor(p/2)>=p/4`; `|hat f|<=1` reduces to the even power, and that even-power integral is finite because it is dominated by `|hat f|^2`. Fourier inversion of the `m`-fold difference law and the scalar projection bound give exactly the stated constant.

### Lines 311--421 — decoupling, graph BL determinant, crossing volumes: PASS

Cauchy--Schwarz is applied in an original-coordinate product law; the copied `J` bank creates independent differences with density cap one. The fourth-power inequality is a valid Jensen consequence of the second-power inequality.

In the determinant theorem, with `a=2t`, `alpha=(2*pi*e)^2`, and `H=alpha I+a^2M^TM`, the coordinate weights `c_j` and row weights `d_i` form an exact geometric rank-one frame, and `theta=sum d_i=sum(1-c_j)`. The change-of-variable scales in the BL inequality are correct. Difference densities have all required `L^{1/c_j}` norms at most one. The scalar Fourier-power lemma at exponent `2/d_i` gives `(2*pi*sqrt(e d_i))^{d_i}`; the `d_i` powers cancel, while the `c_j` entropy tax contributes `e^{theta/2}`. Together with `sqrt(alpha)=2*pi*e`, all scalar constants cancel exactly. Factoring `alpha^d` from `det H` and taking fourth roots gives

`|phi_Z(t)| <= det(I+t^2M^TM/(pi^2 e^2))^(-1/8)`.

Cauchy--Binet gives the `Z_k` coefficient identity. Keeping one determinant coefficient produces exponent `k/4`; `k=5` is integrable for bounded density and `k=3` is exactly strong enough after the Riesz `|t|^(-1/2)` weight. Constants check.

### Lines 422--519 — scalar square, definite/indefinite pair, quarter concentration: PASS

The scalar square Jacobian and inverse-image interval bound are correct and are used as conditional measure domination, not as an independence assertion. The definite two-coordinate change of variables has Jacobian `1/(2sqrt(det B))`, yielding `pi M/sqrt(|det B|)`.

For the hyperbolic pair, the two branches have absolute `(delta,t)` Jacobian `1/(2sqrt(D))`. The decomposition `ue^t+we^{-t}` has `|u|=|w|=sqrt(delta Lambda)/2`. On each tail one original coordinate has a monotone parametrization with derivative comparable to its magnitude; using only that coordinate's cap-one density and mass-one constraint gives the logarithmic tail bound. The middle interval is bounded by length. `Lambda>=2/sqrt(D)` has the correct direction. The negative-sign level is handled by swapping the positive and negative eigendirections. The exceptional critical level is correctly avoided by the test-function/Tonelli formulation.

For quarter-power concentration, either a diagonal entry is large or a random-sign physical cut has crossing operator norm at least `L/4`. Retaining one singular factor in the determinant theorem gives the `|t|^{-1/4}` envelope. Gaussian smoothing yields the claimed small-ball exponent and the displayed coefficient; the elementary Gamma bound is conservative. Layer cake then yields the logarithmic potential bound and atomlessness in the stated order.

### Lines 520--679 — disjoint minors, nonsymmetric interpolation, spectral-to-volume conversion: PASS

The no-pivot entry bound is valid (and conservative). In the sampling lemma the bordered determinant identity is correct; singular seeds are omitted from the sampling law, so the manuscript correctly uses an upper multiplicity inequality rather than asserting equality. `P=A_{.,T}B^{-1}A_{S,.}` may be nonsymmetric but has rank at most `r` and interpolates rows `S` and columns `T` exactly.

In the completion, `E` is the off-diagonal `L x L` residual, `D` is the remaining diagonal and vanishes on the seed, and `R_{L,L}=P_{L,L}` has rank at most `r`. The support of `R-P` is confined to rows `T` or columns `S`, giving global `rank R<=3r`.

For a small volume ratio, `||E||<=||E||_F<=1/16`. The nonsymmetric singular-value rank shift is valid. With `m=4k-3>=4r+1`, at least `r+1` diagonal entries of `D` are large and, because `D` vanishes on the seed, lie in `L`. On their `(r+1)`-set the diagonal of `R` is at least `371/400` while every row's off-diagonal sum is below `23/28`; strict diagonal dominance forces rank `r+1`, contradicting `rank R_{L,L}<=r`. The random-cut expectation is exactly `4^{-k}` for ordered disjoint pairs.

### Lines 680--770 — singular kernels, pivot half-potentials, nine-direction receiver, main proof: PASS

The two kernel integrals are bounded correctly. The scalar-pivot truncated half-potential is obtained by integrating the conditional square profile; the quarter-power lemma first removes the possible atom and then controls the logarithm. The definite and indefinite pair alternatives have the displayed constants, including `sup D^(-1/2) log_+ D=2/e`. The truncated/full distinction in the nine-eigenvalue proposition is correct: outside `|Q-a|<=1`, the half kernel is at most one.

In the main proof, no pivot plus `s_17>=1` invokes the order-five receiver. A scalar pivot removes at most one spectral direction; sixteen remain, more than the nine needed for the full half-potential bound. A two-coordinate pivot removes at most two; the definite branch is direct, and the indefinite branch needs only one surviving spectral direction for the logarithmic critical-value average. Affine terms are retained throughout. The nonnegative test-function formulation correctly handles rough conditional laws and moving critical values.

The general scaling is exact: for `Y=KX`, the coordinate density caps become one; the manuscript's `tilde Q` equals `(K^2/s)Q`; the density rescaling therefore gives `10000 K^2/s`.

### Lines 771--790 — threshold ledger and limitations: PASS

The manuscript accurately distinguishes the `k=3` half-potential use from the `k=5` bounded-density use. It does not claim continuity for the pivot branches and does not claim the unrestricted three-eigenvalue conjecture. The bibliography is attribution only; the specialized inequalities used by the proof are reproduced in the source.

## Missing package files — GAP / UNCHECKED

Fresh master direct fetches returned 404 for each of:

- `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/proof_map.csv`;
- `.../SOURCE_MANIFEST.json`;
- `.../verify.py`;
- `.../checks.json`.

Because README/AUDIT explicitly advertise them, this is a reproducibility/package GAP. It does not invalidate the mathematical argument above. The numerical/finite-check claims attributed to those absent files remain UNCHECKED in this review.

## Lower-threshold conclusion from this audit

I do not certify any unconditional multiplicity below 17. The present interpolation/rank mechanism has a genuine worst-case `4r+1` bookkeeping barrier, and the order-four (`s_13`) determinant endpoint is only `O(1/|t|)`, which by itself does not imply an `L^infinity` density.

I did, however, derive a new rigorous leverage-sensitive interpolation of the determinant argument. It gives direct bounded density from order four whenever the physical crossing has any fixed uniform row-leverage gap below one, and direct bounded density from order three whenever that gap is below `3/4`. The complete proof and constants are saved separately in this run's improvement artifact. This strictly enlarges the known conditional lower-multiplicity regime but does not remove the high-leverage structural obstruction, so the unconditional theorem remains at 17 in this run.

## Review status

- Complete 790-line mathematical manuscript: **PASS in this independent B04 review**.
- Geometric BL heat flow, derivative sign, integrations by parts, Gaussian domination, `t->0` and `t->infinity` limits: **PASS**.
- Advertised finite-check package: **GAP / UNCHECKED because files are absent**.
- Candidate 17-eigenvalue theorem: **survives this review; not self-certified as independently validated**.
- Full three-eigenvalue conjecture: **OPEN**.
- Unconditional multiplicity below 17: **not proved in this run**.
