SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T09:20:51Z.
attacking: near-null nonzero coloop interpolation; retain an unnormalised dependent square fiber instead of a false conditional-density cap, and separate finite-ray bank geometry from the genuinely non-collinear survivor.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T092051Z-account01-B10-QFORM-auto11`.
Status at checkpoint: supporting analytic lemma + product-bank reduction; full target OPEN.
Execution label: `WITHOUT_VERIFIED_BRAIN`.

Fresh owner control was read on `yspennstate/math-research-brain` main, OWNER CONTROL revision `2026-09-22.15`; the full QFORM target remains sole. The live corrections against post-rotation independence, arbitrary-joint coarea, conditional-cap substitution, pointwise law-uniform quadratic-phase decay, and local-minor selection are retained.

Required current sources actually used:

* designated partner `account02/B10`, run `20260923T064541Z-account02-B10-QFORM-auto11`, canonical mathematics `yspennstate/math-open-problems@16ecbcc3f6d34d4195ff6e29066216df155d9530`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260923T064541Z-account02-B10-QFORM-auto11/REPORT.md`;
* newest-Claude package `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, especially the ruled one-sheet estimate and mixed-Fresnel mechanism.

The partner reduces the genuinely unpaid exact-rank-three indefinite near-coloop state to

`1-eta < 2(1-rho_M)|alpha| <= 2|alpha|`,

with `c=||r_h||^2>63/64`, `rho_M<1/64`, `alpha=e^T Lambda e`, `eta=||H_M||op`; the newest-Claude ruled estimate already pays the one-sheet side by `pi sqrt(2)` at unit spectral scale. Thus the remaining issue is the minority/two-sheet side with a constant hub-incident Pluecker packet spread through non-collinear ORIGINAL-coordinate banks.

## 1. New unnormalised dependent-square L3 theorem

### Theorem (`QFORM-FIBER-SQUARE-L3-MASS-v1`)

Let `(Omega,nu)` be sigma-finite. Let `h(z,w)>=0` on `R x Omega` satisfy

`h(z,w)<=H`,  `M:=int_Omega int_R h(z,w) dz dnu(w)<infinity`.

Let `theta:Omega->R` be measurable and `b!=0`. Define the *unnormalised* fiber transform

`F(t,w)=int_R exp(i t b (z+theta(w))^2) h(z,w) dz`.

Then

`boxed: int_Omega int_R |F(t,w)|^3 dt dnu(w) <= 32 pi H^2 M / |b|.`

No conditional density is formed. In particular tiny fiber masses do not get divided out, so the theorem is compatible with the live counterexample showing that conditional density caps can blow up.

### Proof

Fix `w` and abbreviate `k(z)=h(z,w)`, `m=int k`. Translation lets us replace `z+theta(w)` by `z`. Push `k(z)dz` forward under `u=z^2`; for `u>0`,

`q(u)=[k(sqrt u)+k(-sqrt u)]/(2 sqrt u)`.

Thus `F(t,w)=hat q(bt)` under the convention `hat q(s)=int exp(is u)q(u)du`. First,

`I:=int_0^infinity q(u)^(3/2)du`
` =2^(-1/2) int_0^infinity [k(r)+k(-r)]^(3/2) r^(-1/2)dr`
` <=int_R k(z)^(3/2)|z|^(-1/2)dz`,

using `(a+b)^(3/2)<=sqrt(2)(a^(3/2)+b^(3/2))`.

For any `R>0`, since `0<=k<=H`,

`I <= 4 H^(3/2) sqrt(R) + H^(1/2)m/sqrt(R)`.

Choose `R=m/(4H)` (the zero-mass case is trivial). This gives

`I<=4H sqrt(m)`.

Hence

`||q||_(3/2)^3 = I^2 <=16H^2 m`.

Hausdorff-Young for the above Fourier convention gives

`||hat q||_3 <=(2pi)^(1/3)||q||_(3/2)`.

After the scaling `s=bt`,

`int_R |F(t,w)|^3dt <= (2pi/|b|)||q||_(3/2)^3 <=32pi H^2 m/|b|`.

Integrating in `w` and using `int m(w)dnu=M` proves the theorem. QED.

### Product-projection corollary actually relevant to B10

If `(Y,Z)` is any two-dimensional projection of an ORIGINAL cap-one product law for which the established projection theorem gives joint density `rho(y,z)<=2`, then for every measurable shift `theta(y)` and `b!=0`,

`boxed: int_R int_R | int_R exp(it b(z+theta(y))^2) rho(y,z)dz |^3 dt dy <=128 pi/|b|.`

This allows arbitrary dependence between `Y` and `Z`; it is precisely an unnormalised substitute for the forbidden operation `sup_y ||p_(Z|Y=y)||_infinity`.

## 2. Exact endpoint of this mechanism: it still does not alone give L1 in time

Consider the model retained by the near-null Witt reduction,

`T=2a S Y+F_0(Y)+b(Z+theta(Y))^2`,

where `S` is a genuine independent ORIGINAL scalar with density cap one and `(Y,Z)` has joint density at most `H`. Set

`G_t(y)=int exp(it b(z+theta(y))^2)rho(y,z)dz`.

Then

`phi_T(t)=int hat f_S(2at y) exp(itF_0(y))G_t(y)dy`.

For every `p>=2`, Holder in `y`, the standard cap-one Fourier `L^p` estimate, and interpolation between `||G_t||_1<=1` and `||G_t||_3` give

`|phi_T(t)| <= C_p |a t|^(-1/p) B(t)^(3/(2p))`,

where `B(t)=||G_t||_3` and the theorem above gives `B in L^3(dt)`. Consequently the second factor belongs to `L^(2p)(dt)`. Holder in time would need

`|t|^(-1/p) in L^(2p/(2p-1))(1,infinity)`,

but its power is `2/(2p-1)<=2/3<1`. Thus this natural fiber-L3 + scalar-Fourier synthesis is genuinely short of `L^1_t`. The new lemma is valid and translation-uniform, but a second smoothing feature (or phase-sensitive coupling of the two existing features) is still required. This records the first essential missing implication rather than hiding it behind a conditional supremum.

## 3. Actual designated-partner application: bounded projective-ray complexity is paid

The partner proves `QFORM-COLLINEAR-PRODUCT-BANK-COMPRESSION-v1`: three disjoint collinear ORIGINAL-coordinate banks with aggregate squared spectral determinant `w` in an exact-rank-three form satisfy

`||p_Q||_infinity <=2 C_3 (D w)^(-1/3)`,

where `D=|det Lambda|` and `C_3=16 sqrt(30)2^(1/4)`.

Here is a direct structural application. Let the non-hub spectral rows be partitioned into `N` collinear ray classes `B_1,...,B_N`. Put the aggregate row of class `a` equal to

`r~_a=(sum_(i in B_a)||r_i||^2)^(1/2) v_a`,

with `v_a` its unit ray direction. For a Parseval exact-rank-three frame and hub row `r_h=sqrt(c)e`, Cauchy-Binet in the transverse plane gives the exact hub packet identity

`sum_(j<k;j,k!=h) det(r_h,r_j,r_k)^2=c`.

Collinearity gives the exact class decomposition

`c=sum_(a<b) det(r_h,r~_a,r~_b)^2`.

Therefore some class pair satisfies

`w_ab:=det(r_h,r~_a,r~_b)^2 >= c / binom(N,2)`.

Applying the completed partner theorem to the three genuinely disjoint ORIGINAL-coordinate banks `{h},B_a,B_b` yields

`boxed: ||p_Q||_infinity <=2 C_3 [D c/binom(N,2)]^(-1/3).`

In the true near-coloop collar `D>=1` and `c>63/64`, hence for every fixed `N>=2`,

`||p_Q||_infinity < 2 C_3 [64 binom(N,2)/63]^(1/3)`.

Thus any unresolved sequence in this collar must have genuinely unbounded projective directional complexity; it cannot be a bounded union of exact product-preserving rays. This uses the partner result at an actual density inequality, not merely as a citation.

## 4. Current first unpaid implication

The surviving task is now sharper:

`QFORM-TRUECOLLAR-HIGH-PROJECTIVE-COMPLEXITY-PHASE-SYNTHESIS-v1`.

One must combine the constant hub Pluecker packet with the unnormalised fiber-square smoothing above when that packet is dispersed among increasingly many non-collinear original-coordinate directions. A proof must gain the missing time exponent without normalising thin fibers, selecting a single reciprocal minor, or treating a small coefficient matrix as a small random perturbation. The likely next interface is a two-feature/vector-valued Fresnel-Brascamp-Lieb inequality that keeps the hub translation phase and the curved fiber simultaneously.
