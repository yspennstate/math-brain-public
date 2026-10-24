# account03/B13 independent audit — fixed-multiplicity 17 candidate

Run: `20260924T120229Z-account03-B13-fixedmult-audit-r1`
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`
Source commit pinned by owner: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
Source blob audited: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
Source SHA-256 supplied by owner: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
Lens: B13 definite pairs and the full hyperbolic envelope, with account03 emphasis on exact identities and alternative derivations. I nevertheless read the complete 790-line manuscript end-to-end and rechecked the dependency chain independently.

## Verdict

**PASS for the mathematical 17-eigenvalue baseline in this independent worker audit.** I found no fatal mathematical defect in the theorem as written. The full three-eigenvalue conjecture remains open. This report is an independent scheduled-worker review, not formal verification or peer review, and I do not self-award the repository's release status.

I found two nonfatal presentation/package issues:

1. In the projection lemma, after zero-`b_i` rows are omitted, the bound should use `sum_{b_i>0}(1-b_i) <= d`; writing equality at that point is stronger than justified but unnecessary. The theorem and constant remain valid with `<= d`.
2. The repository root currently exposes `README.md`, `AUDIT.md`, `manuscript.tex`, and `audits/`; the README names `proof_map.csv`, `verify.py`, `checks.json`, and `SOURCE_MANIFEST.json`, but those files were absent from the root listing I inspected. This is a reproducibility/package mismatch, not a mathematical gap in `manuscript.tex`.

A small B13-specific editorial clarification is also advisable in the hyperbolic proof: the coordinate chosen for the negative tail may differ from the coordinate chosen for the positive tail. The proof only needs a coordinate with `|w_j| >= rho_0/sqrt(2)` for the negative tail, and such a coordinate always exists. No constant changes.

## End-to-end audit ledger

### Lines 1–80: theorem, quantifiers, architecture — PASS

The statement preserves arbitrary dimension, arbitrary real symmetric `A`, arbitrary affine `b,c`, arbitrary signs and remaining spectrum, and independent coordinate densities bounded only by `K`. The normalized target is `K=s=1`; the final scaling `Y=KX`, `A -> A/s`, `Q=(s/K^2) Q_tilde` correctly yields `10000 K^2/s`.

The architecture correctly distinguishes the no-pivot Fourier branch from scalar and two-coordinate pivots. The manuscript makes only an essential-boundedness claim globally and does not silently claim continuity in the pivot branches.

### Lines 81–160: Fourier normalization and negative half potential — PASS

With `fhat(t)=int e^{itx}f(x) dx`, the Plancherel constant `2*pi`, inversion factor `1/(2*pi)`, and Gaussian identity are consistent. For the Riesz bound,

`|z|^{-1/2} = Gamma(1/4)^{-1} int_0^infty v^{-3/4} e^{-v z^2} dv`

and

`int_0^infty v^{-5/4} exp(-t^2/(4v)) dv = sqrt(2) Gamma(1/4)|t|^{-1/2}`

give exactly `(2*pi)^(-1/2)` in the Fourier half-potential estimate. The `3/4` characteristic-function power is used only with the `|t|^{-1/2}` weight, where the tail exponent is `5/4`; it is never misused as an absolutely integrable characteristic function.

### Lines 161–240: singular values, Schur count, geometric BL setup — PASS

The singular-value perturbation/rank statements are valid for nonsymmetric auxiliaries. For a nonsingular principal pivot, the Schur-count lemma is correctly derived by applying Cauchy interlacing separately to `A^{-1}` and `-A^{-1}`: the complementary principal block is `S^{-1}`, and counting `|lambda| > 1/t` in the inverse is equivalent to counting original eigenvalues with modulus `<t`. The singular case is correctly obtained by an `A+epsilon I` limit while the pivot remains invertible.

Strict diagonal dominance is used only for invertibility of a possibly nonsymmetric restricted matrix, where the row argument is valid.

### Lines 241–320: geometric Brascamp–Lieb, projections, scalar Fourier powers — PASS WITH LOCAL WORDING REPAIR

The heat-flow identity is correct:

`partial_t F - Delta F = F( sum c_i v_i^2 - |sum c_i u_i v_i|^2 ) >= 0`,

because the weighted frame map is a contraction. The large-time Gaussian limit and monotone approximation close the proof.

For product projections, the one-dimensional rescalings and BL exponents give `prod b_i^{-b_i/2}`. After rows with `b_i=0` are dropped, one only needs

`sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`.

Thus `||p||_infty <= e^{d/2}` remains correct. This is a wording repair, not a mathematical failure.

The scalar Fourier-power proof is correct: `2m <= p`, `|fhat|<=1`, and `|fhat|^{2m}` is integrable because it is bounded by `|fhat|^2`; inversion at zero plus the scalar projection estimate gives the stated `p^{-1/2}` bound.

### Lines 321–400: decoupling, regularized determinant, crossing volumes — PASS

The two-copy decoupling keeps original-coordinate independence and all self/affine terms inside modulus-one factors. Jensen produces the fourth-power version without any conditional-density-cap assumption.

In the determinant theorem, with `H=alpha I+a^2 M^TM`, the frame weights

`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`

have outer products summing to identity. The BL rescalings are exact. The `d_i` powers cancel against the scalar Fourier-power estimate; `prod c_j^{-c_j/2} <= e^{theta/2}`; choosing `alpha=(2*pi*e)^2`, `a=2t` removes the remaining entropy factor. Taking the fourth root gives exponent `-1/8` and denominator `pi^2 e^2` exactly.

Cauchy–Binet gives the coefficient `Z_k`. Retaining the order-`k` term yields the `k/4` envelope. The order-five density constant and order-three half-potential constant are consistent.

### Lines 401–425: scalar square and definite pair — PASS

The scalar square profile is the sum of the two monotone inverse branches and has density at most `1/sqrt(|a||z-v|)`. Its interval-preimage length bound is correct after completing the square.

For the definite two-coordinate lemma, completing the square and using the deterministic eigenbasis gives Jacobian

`|d(w_1,w_2)/d(delta,theta)| = 1/(2 sqrt(det B))`.

A joint density bounded by `M` remains bounded by `M` under the orthogonal deterministic coordinate change, whether or not the rotated variables are independent. Integrating over `theta in [0,2*pi)` therefore gives `pi M/sqrt(|det B|)` exactly.

### Lines 426–485: full hyperbolic envelope — PASS, independently rederived

Let the eigenvalues be `mu_+>0>-nu` with `nu=|mu_-|`, `D=mu_+ nu`, and `delta=z-v>0`. Each branch is

`w_epsilon(t)=epsilon sqrt(delta/mu_+) cosh(t)e_+ + sqrt(delta/nu) sinh(t)e_-`.

Direct differentiation gives the exact Jacobian

`|d(w_1,w_2)/d(delta,t)|=1/(2 sqrt(D))`.

Writing one branch as `u e^t + w e^{-t}` gives

`|u|=|w|=rho_0=(sqrt(delta Lambda))/2`, `Lambda=mu_+^{-1}+nu^{-1}`.

For the positive tail choose an original coordinate `i` with `|u_i|>=rho_0/sqrt(2)`. Since `|w_i|<=rho_0`, the choice

`T_1=(3/4)log 2`

ensures `|w_i|e^{-t} <= |u_i|e^t/2` for `t>=T_1`. Hence the coordinate map is monotone, has one sign, and

`|w_i'(t)| >= |w_i(t)|/3`.

With `T=max(T_1,log(2/|u_i|))`, the reached absolute coordinate value is at least one. Because the other one-dimensional density is at most one and the selected density has total mass at most one on either half-line,

`int_T^infty f_1(w_1(t))f_2(w_2(t))dt <= 3 log 2`.

For the negative tail, choose (possibly another) coordinate `j` with `|w_j|>=rho_0/sqrt(2)` and apply the same argument to `t -> -infinity`. Both cutoffs satisfy

`T,T' <= (3/4)log2 + (1/2)log_+(32/(delta Lambda))`.

The middle interval contributes only its length, so each branch is bounded by

`(15/2)log2 + log_+(32/(delta Lambda))`

and `(15/2)log2 = 5.198603854... < 6`. Finally `Lambda>=2/sqrt(D)` gives the manuscript envelope

`D^{-1/2}(6+log_+(16 sqrt(D)/|z-v|))`.

The negative-`delta` case is obtained by negating the form. The exceptional critical level is null and all later uses can be formulated as domination against nonnegative test functions, so rough densities do not create an exceptional-slice gap.

This derivation also gives a harmless constant sharpening: the leading `6` may be replaced by `(15/2)log2`, but this does not change the multiplicity threshold.

### Lines 486–540: quarter-power concentration — PASS

If a diagonal coefficient is large, the scalar-square small-ball estimate suffices. Otherwise the sign partition applied to the zero-diagonal part produces an original-coordinate cross block of operator norm at least `L/4`. One singular factor in the regularized determinant theorem gives the `|t|^{-1/4}` envelope. Gaussian smoothing and the displayed gamma integral then yield the `rho^{1/4}` concentration bound. The layer-cake logarithmic potential is finite and uniform for `L>=1`. No forbidden law-uniform pointwise van-der-Corput estimate is used.

### Lines 541–640: sampled interpolation, support/ranks, spectral-to-volume — PASS

For a nonsingular disjoint seed `B=A_{S,T}`, the nonsymmetric interpolant

`P=A_{.,T} B^{-1} A_{S,.}`

has rank at most `r`, equals `A` on rows `S` and columns `T`, and the bordered determinant identity gives the exact squared residual on `L x L`. In the expectation, an extended ordered minor can be produced by at most `(r+1)^2` row/column deletions; singular seeds contribute no sampled weight, so the manuscript correctly claims an inequality, not equality.

In `A=D+R+E`, `D` vanishes on the seed, `E` is zero-diagonal and supported on `L x L`, `R_{L,L}=P_{L,L}` has rank at most `r`, while globally `R-P` is supported in rows `T` or columns `S`, yielding `rank R<=3r`.

For the spectral-to-volume proposition, `m=4k-3` and `r<=k-1` imply `m>=4r+1`, so after the global rank-`3r` perturbation there are at least `r+1` large diagonal entries of `D`. They lie in `L`. The lower diagonal bound `371/400` exceeds the worst row-sum bound `4(1/7+1/16)=23/28`, so the `(r+1)` principal restriction of `R_{L,L}` is strictly row-diagonally dominant and invertible, contradicting restricted rank at most `r`. The `r=0` case is separately correct.

### Lines 641–720: random cut, kernels, pivot half-potential — PASS

A fair cut retains each ordered disjoint `k`-minor with probability `4^{-k}`. Combining this with the volume lower bound gives `Z_k^{-1/(2k)}<=160` for `k=3,5`, hence the manuscript's `<200` full half-potential and `<2400` no-pivot density bounds.

For the kernel estimate `J(d)`, the near region is uniformly finite and the far region contributes a logarithm. The shifted logarithmic kernel is maximized at coincident interval centers by the superlevel-overlap argument and equals `8` at the stated majorant.

In the pivot half-potential proposition:

- scalar pivot: Schur leaves one spectral direction, the quarter-power lemma rules out the singular center atom, and `10(8+3L_0)=532.7106...<600`;
- definite pair: `4*pi*eta^{-1/2}=40*pi=125.6638...<160`;
- indefinite pair: the hyperbolic envelope plus the logarithmic kernel gives `D^{-1/2}(32+4log_+(16 sqrt D))`; with `D>=eta`, this is at most `432.3751...<444`.

All three are uniform in conditioning variables.

### Lines 721–790: nine-direction bound, main theorem, scaling — PASS

The nine-eigenvalue proposition correctly splices the pivot and no-pivot branches; outside the truncation window the half-kernel is at most one, giving the full `<=601` bound.

In the main theorem:

- no pivot: order-five crossing gives density `<2400`;
- scalar pivot: Schur removes one direction, leaving at least sixteen and hence at least nine, so the profile gives `10*601=6010`;
- definite pair: the conditional bound is `10*pi`;
- indefinite pair: Schur removes two directions, leaving at least fifteen and hence operator norm at least one. The hyperbolic envelope averaged against the critical-value polynomial uses the quarter-power logarithmic potential and gives `238.9974...<251`.

The final scaling in `K,s` is algebraically correct. No step rotates the independent random coordinates and then treats the rotated coordinates as independent.

## Threshold reduction attempt

I do **not** claim a lower multiplicity theorem in this run. The present algebraic mechanism has a genuine next endpoint at `k=4`: the same interpolation proof would require `4k-3=13` large singular values, but the determinant theorem then gives only the borderline envelope `|phi(t)| <= O(|t|^{-1})`. Absolute Fourier inversion diverges logarithmically, so a 17->13 reduction is not obtained merely by reusing the current argument.

The B13 pair analysis does not remove that endpoint obstruction. In the no-pivot branch every principal two-coordinate determinant is `<eta`, and no uniform definite/hyperbolic pair constant survives as the determinant tends to zero. A genuine 13-eigenvalue theorem therefore needs a new order-four endpoint estimate or a different structural reduction, not a constant optimization of the pair lemmas.

## Release/status consequences

- 17-eigenvalue mathematical baseline: **PASS in this independent audit**.
- Fatal defect found: **none**.
- Local mathematical wording repair: projection proof should use `<= d` after zero-`b_i` rows are omitted.
- Hyperbolic proof: **PASS**, with the negative-tail coordinate made explicit and a sharpened branch constant `(15/2)log2` available.
- Package reproducibility mismatch: **GAP**, because four files named by README were absent from the root listing inspected.
- Lower threshold proved here: **none**.
- Full three-large-eigenvalue conjecture: **OPEN**.
- Global continuity: **not claimed**; no-pivot Fourier branch is continuous, pivot branches are proved only as essential density bounds.

## Next proof obligation

Attack the order-four endpoint directly. A result of the form “crossing volume `Z_4(M)>=z_0` plus arbitrary self/affine terms and arbitrary cap-one product laws implies a dimension-free `L^infty` density bound” would combine with the already checked interpolation argument to give a 13-eigenvalue theorem. The proof must do more than integrate the crude `|t|^{-1}` envelope absolutely; likely useful routes are a product-preserving physical small-ball argument or an integrated cancellation estimate that retains the full cross-block structure.
