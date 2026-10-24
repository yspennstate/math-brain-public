# account03/B11 — full fixed-multiplicity audit and threshold descent

Run: `20260924T140428Z-account03-B11-fixedmult-audit-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Lens: Schur-complement spectral counts, including singular ambient matrices; indefinite-signature interfaces.

## Pinned source

Repository: `yspennstate/math-open-problems`  
Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`  
Git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Size: 47,883 bytes / 790 lines.

The full 790-line source was read in this invocation, not just the assigned Schur section. The support package is now present: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`. The repository checker records PASS on 534 exact interpolation seeds, 18 exact volume comparisons, 240 floating Schur threshold cases, and 30 graph-weight cases. Those finite checks are diagnostics only.

## Verdicts

- Baseline `s_17` theorem: **PASS in this independent B11 audit.**
- New `s_9` fixed-multiplicity replacement: **PASS in this independent B11 reconstruction**, with the conservative fully reconstructed constant `<5338 K^2/s`.
- General `s_8` L-infinity theorem: **OPEN**.
- New in this run: **proved** an aggregate two-sided split-row endpoint showing that the only unpaid `s_8` collar lies in every finite `L^r`, with linear-in-`r` norm growth and `epsilon log(1/epsilon)` small balls. See the sibling improvement artifact.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity: **OPEN/not claimed**.

## A. Baseline manuscript audit

### Lines 47–160 — theorem, scaling, Fourier inversion, negative half moments: PASS

The theorem keeps the correct quantifiers: arbitrary independent real coordinate laws with density cap `K`, arbitrary symmetric `A`, arbitrary affine terms, no support/moment/log-concavity assumptions. The Gaussian regularization and inversion formulas match the stated Fourier convention. The half-Riesz representation uses

`|z|^-1/2 = Gamma(1/4)^-1 int_0^infinity v^-3/4 exp(-v z^2) dv`

and the subsequent Gaussian-Fourier integral gives the stated `|t|^-1/2` weight. The final normalization `Y=KX`, `A -> A/s`, `Q=(s/K^2) Qtilde` gives density scale `K^2/s`.

### Lines 169–217 — singular values and Schur complements: PASS

The rank perturbation lemma is stated in singular values and therefore applies to the nonsymmetric interpolation matrices later in the manuscript.

For the Schur lemma, write

`A=[[B,C],[C^T,D]]`, `S=D-C^T B^-1 C`, `dim B=k`.

For invertible `A`, block congruence implies the complementary principal block of `A^-1` is `S^-1`. Interlacing for `A^-1` and `-A^-1` gives

`# {|lambda(S^-1)|>1/t} <= # {|lambda(A^-1)|>1/t}`,

which is exactly

`(n-k)-N_S(t) <= n-N_A(t)`.

Hence `N_S(t)>=N_A(t)-k`.

The singular ambient case is also valid. For `A_e=A+eI`, the selected pivot remains invertible for all sufficiently small `e`, `S_e -> S`, and

`N_(A_e)(t-|e|)>=N_A(t)`.

Applying the invertible statement at threshold `t-|e|` gives, for `q=N_A(t)-k>0`,

`s_q(S_e)>=t-|e|`.

Continuity of ordered singular values under `S_e -> S` yields `s_q(S)>=t`. Thus the moving threshold in the written proof is legitimate; no fixed-threshold gap occurs.

### Lines 221–301 — geometric BL, product projections, scalar Fourier powers: PASS with a wording clarification

The heat-flow proof of geometric BL is closed at the constants used. Product projection is applied only to literal linear images of original product coordinates; no independence after rotation is asserted.

After zero-leverage rows (`b_i=0`) are dropped in the projection proof, the displayed equality involving `sum(1-b_i)=d` should be read with the omitted nonnegative terms restored. On retained rows one only needs

`sum_(b_i>0)(1-b_i) <= d`,

which gives exactly the same `e^(d/2)` bound. This is a local wording clarification, not a theorem defect.

The scalar Fourier-power bound correctly uses an actual sum of independent signed original coordinates and Fourier inversion of its continuous density.

### Lines 310–400 — decoupling and regularized determinant: PASS

Copies are introduced only in original-coordinate banks. The difference coordinates remain independent with density cap one. The geometric-frame weights satisfy the trace identity; the choice `alpha=(2pi e)^2` cancels the scalar factors. The fourth-root step gives exponent `-1/8` as written. Order five gives an integrable `|t|^-5/4` envelope; order three is used only with the half-Riesz weight in the baseline.

### Lines 404–525 — square, definite pair, indefinite pair, quarter concentration: PASS

All three statements are conditional measure dominations and tolerate arbitrary induced affine terms. The deterministic orthogonal diagonalization in the definite-pair integral is not a rotation of random independent coordinates. The hyperbolic proof keeps the moving critical value and controls both tails using only density cap and mass one. The quarter-power concentration proof uses either a literal scalar square or an original-coordinate bipartition plus the determinant theorem. No pointwise rough-law van-der-Corput claim appears.

### Lines 528–645 — disjoint minors, interpolation, spectral-to-volume: PASS

For a sampled seed `B=A[S,T]`, the bordered determinant identity is exact. Singular seeds may have nonsingular extensions, so the volume comparison is correctly an inequality. In the completion

`A=D+R+E`,

one has `rank R<=3r` globally but the crucial sharper restriction `rank R[L,L]<=r`. `D` vanishes on the seed and `E` has zero diagonal.

In Proposition `prop:volume`, if the ratio `V_(r+1)/V_r` is small, then `||E||<=1/16`. With `m=4k-3` and `r<=k-1`,

`m-3r >= r+1`.

Thus `D` has at least `r+1` heavy diagonal entries in `L`. The manuscript entry bounds make the corresponding `R[H,H]` strictly row-diagonally dominant, hence invertible of rank `r+1`, contradicting `rank R[L,L]<=r`. The proof is valid although `R` can be nonsymmetric.

The fair random cut identity is exact term-by-term, with probability `4^-k` for each ordered disjoint minor.

### Lines 654–790 — singular kernels, pivot half potentials, main theorem: PASS

The kernel integrals are adequate at the constants used. The pivot half-potential argument correctly separates scalar, definite-pair, and indefinite-pair alternatives. Full and truncated half potentials are not confused: outside the unit window the kernel is at most one.

In the main proof, a scalar pivot loses at most one unit-scale spectral direction and therefore leaves at least sixteen under `s_17`; a pair pivot loses at most two. The no-pivot branch uses the actual order-five density receiver. The largest normalized final branch is the scalar-pivot `6010`, below `10000`. The manuscript correctly claims only essential boundedness globally.

**Baseline conclusion: no fatal mathematical gap found.**

## B. Independent reconstruction of the nine-eigenvalue replacement

I did not infer this verdict from another worker's PASS. I read the grouped product-Fourier proof and re-derived its three delicate steps.

### B1. Complex pushforward / Plancherel step: PASS

For a promoted `k`-dimensional product projection `W`, pushing `e^{itF}` to `W` gives a complex density `a_t` with `|a_t|<=p_W`; therefore `||a_t||_2^2<=M_H`. Plancherel after `xi=2t(l+beta)` gives

`int |hat a_t(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k`.

This is an integrated estimate, not forbidden pointwise oscillatory decay.

### B2. Difference bank and weighted subset step: PASS

After regularizing the residual complex pushforward and expanding its squared `L^2` norm, only an independent copy of the literal `J` bank is needed. `D=X_J-X'_J` remains a product vector with coordinate density caps one. Pure same-bank phases cancel or have modulus one. Averaging the original independent `I` coordinates produces scalar characteristic factors.

For subset weights

`w_T=det(C_T C_T^T)/Z_ell`, `alpha_i=P_w{i in T}`,

Holder uses exponent `1/alpha_i` only for `alpha_i>0`; zero-marginal factors are omitted. When `alpha_i<=1/2`, the manuscript scalar Fourier-power estimate applies at power at least two. The Jacobian of

`D -> (M_JD,(<c_i,D>)_(i in T))`

has Gram determinant `S^2 det(C_T C_T^T)`. These facts yield the stated geometric mean bound without a dimension factor.

### B3. Entropy step and promotion tree: PASS

Uniformly ordering the random `ell`-subset gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

This is exactly the entropy inequality needed to cancel the determinant geometric mean. The heavy-marginal promotion identities are Gram--Schmidt identities; at order three all terminal branches yield

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`,

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`,

while order two yields only

`sup_a E|Q-a|^-1/2 <= C_2 E_2(M)^(-1/8)`.

The order-two statement is not mislabeled as a density theorem.

### B4. Spectral count compilation to nine: PASS

Normalize `K=s=1`.

- No pivot: `s_9(A)>=1` and the audited baseline proposition with `k=3` give `V_3>=kappa^3`; a fair cut gives `E_3>=4^-3 kappa^3`; hence `E_3^-1/6<=160` and the new receiver gives density `<2371`.
- Scalar pivot: the Schur child retains at least eight unit-scale directions. If it has a pivot, the baseline pivot half-potential theorem already needs only two. If it has no pivot, it still has `s_5>=1`, so the baseline `k=2` volume theorem plus the new E2 receiver supplies the required full half potential. Using only baseline constants gives the safe outer density bound `<5338`.
- Definite pair: direct conditional density `<32`.
- Indefinite pair: the Schur child retains at least seven directions, far more than the single nonzero direction needed for the logarithmic potential argument; the branch is `<251` with the baseline constants.

Scaling restores `K^2/s`.

Therefore this audit independently validates the theorem

`boxed: s_9(A)>=s>0 => ||p_Q||_infinity <5338 K^2/s.`

Other workers have sharper constants; this report deliberately uses only constants re-derived here.

## C. Threshold eight — new progress in this B11 run

The B04 terminal theorem shows that every normalized no-pivot `s_8` state either already has a paid third disjoint volume or carries a quantitative two-sided collar `Xi_2`. The sibling improvement in this run combines that collar with the B03 split-row shared-environment theorem before any local reciprocal is taken.

It proves that in the only unpaid `s_8` chamber there is a literal three-bank partition for which

`|phi_Q(t)| <= min(1,197.494/|t|)`.

Consequently, for every finite `r>=2`,

`||p_Q||_r <= (62.865 r)^(1-1/r)`,

and sufficiently small intervals satisfy an `epsilon log(1/epsilon)` bound. After scaling, the factor is `K^2/s` inside the bracket. This is the exact same endpoint growth class as the density of `2XY` for centered unit uniforms, whose `L^r` norm is `Gamma(r+1)^(1/r)~r/e`.

Thus the `9 -> 8` debt is now a logarithm-removal problem, not an absolute-continuity problem and not a missing aggregate-volume problem. The extra overlap-one/rank-saturation structure has not yet been converted into the integrable gain required for `L^infinity`.

## D. Partner application

The designated account04/B11 theorem `QFORM-LDL-SOURCE-DISJOINT-THIRD-CURVATURE-v1`, pinned at commit `494e4a18bff08cc3fbc9ba668ba14a3983e51da6`, is applied in the sibling improvement to

`Q_0=2X_1X_2+X_3^2`.

Its effective matrix has eigenvalues `{1,-1,1}` and the theorem gives

`||p_(Q_0)||_infinity<=128`, `p_(Q_0) in C_0`.

For centered unit uniforms, the rank-two part alone has density `log(1/(2|t|))`, so this is a strict target-level demonstration of a third disjoint curvature direction removing the logarithmic singularity.

## Final status

Baseline 17: **PASS**.  
Nine-eigenvalue replacement: **PASS in this independent review**.  
Eight-eigenvalue bounded-density theorem: **OPEN**; new finite-`L^r`/log-endpoint theorem proved.  
Three-eigenvalue conjecture: **OPEN**.  
Global continuity: **OPEN/not claimed**.
