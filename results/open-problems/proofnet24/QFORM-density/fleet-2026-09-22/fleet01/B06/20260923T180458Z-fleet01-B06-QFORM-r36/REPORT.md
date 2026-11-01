SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T18:04:58.766711Z.
attacking: the curved-section replacement behind (CS) — retain the parabola exactly, integrate the singular Fresnel weight against product Fourier volume before any fiber supremum, and splice diffuse-frame and disjoint-bank regimes.

# fleet01/B06 r36 — weighted curved-section integration

Status: `SUPPORTING_ANALYTIC_THEOREMS_PROVED / BETA=0-ENDPOINT-CLOSED / PAIRWISE-COAREA-INTERFACE-LOSS-QUANTIFIED / FULL_TARGET_OPEN`.

Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture is **not** proved here. The results below preserve the original-coordinate product law and use no moment, support, connectedness, log-concavity, iid, Gaussian, or spectral-coordinate-independence assumption. They also avoid the corrected false pointwise quadratic-phase decay and the corrected false arbitrary-joint coarea interface.

## 1. Product Fourier input

For a cap-one probability density `f` on `R`, write

`psi(z)=int_R f(x) exp(i z x) dx`.

Use the already source-validated one-dimensional estimate

`int_R |psi(z)|^p dz <= 4 pi / sqrt(p),     p>=2`.                 (1.1)

If vectors `r_i in R^d` satisfy

`sum_i r_i r_i^T = I_d`,                                           (1.2)

and `ell_i=|r_i|^2<=1/2`, then geometric Brascamp--Lieb plus (1.1) gives, uniformly in arbitrary scalar shifts `c_i`,

`int_{R^d} prod_i |psi_i(<r_i,z>+c_i)| dz <= (4 pi)^d`.             (1.3)

Indeed write `r_i=sqrt(ell_i)e_i`, use BL with weights `ell_i`, and set
`G_i(s)=|psi_i(sqrt(ell_i)s+c_i)|^(1/ell_i)`. Then

`int G_i = ell_i^(-1/2) int |psi_i|^(1/ell_i)
         <= ell_i^(-1/2) 4pi sqrt(ell_i)=4pi`,

since `1/ell_i>=2`. Zero rows are omitted.

We also use the elementary interpolation inequality: if `H>=0`, `||H||_infinity<=M`, and `int H<=N`, then

`int_R |t|^(-1/2) H(t) dt <= 4 sqrt(MN)`.                          (1.4)

Proof: split at `R>0`; the inner part is at most `4M sqrt(R)` and the outer part at most `N/sqrt(R)`, then optimize.

## 2. A one-output parabolic smoothing theorem

### Theorem 2.1 — `QFORM-DIFFUSE-PARABOLIC-P2-v1`

Let `X_1,...,X_n` be independent with densities at most one. Let `u,v in R^n` be orthonormal and assume

`u_i^2+v_i^2 <=1/2` for all `i`.                                   (2.1)

Put `U=<u,X>`, `V=<v,X>`. For every `c!=0` and `v0 in R`,

`F=U+c(V-v0)^2`                                                     (2.2)

has a continuous density vanishing at infinity and

`boxed: ||p_F||_infinity <= 8/sqrt(|c|).`                          (2.3)

**Proof.** Fresnel linearization gives, for `t!=0`,

`|phi_F(t)| <= (4pi |ct|)^(-1/2) H(t)`,                            (2.4)

where

`H(t)=int_R prod_i |psi_i(tu_i+xi v_i)| dxi`.                      (2.5)

The translation `v0` contributes only a unimodular factor. For fixed `t`, (1.3) in the one-dimensional `v` frame gives `H(t)<=4pi`. Integrating over `t` and `xi`, (1.3) in the two-dimensional `(u,v)` frame gives `int H(t)dt<=(4pi)^2`. Hence (1.4) gives

`int |t|^(-1/2)H(t)dt <=32 pi^(3/2)`.                              (2.6)

Thus `int |phi_F(t)|dt <=16pi/sqrt(|c|)`, and Fourier inversion gives (2.3). Since the characteristic function is integrable, the density has a continuous `C_0` representative. QED.

The point is that the curvature singularity is integrated against the **same product Fourier volume before any fiber supremum**.

## 3. Diffuse curved section when the transverse coefficient is nonzero

Let `w,v,b` be orthonormal, with

`w_i^2+v_i^2+b_i^2 <=1/2` for all `i`,                             (3.1)

and write

`L=<w,X>`, `V=<v,X>`, `B=<b,X>`,
`Y=lambda(V-v0)^2+beta B`.                                         (3.2)

### Theorem 3.1 — `QFORM-DIFFUSE-CURVED-SECTION-BL-v1`

If `lambda beta !=0`, then `(L,Y)` has a continuous `C_0` density and

`boxed: ||p_(L,Y)||_infinity <=16/sqrt(|lambda beta|).`             (3.3)

Consequently, for the subprobability law restricted to `|V-v0|>r`, if

`|beta| >= |lambda| r^2`,                                          (3.4)

then

`boxed: ||p_(L,Y; |V-v0|>r)||_infinity <=16/(|lambda|r).`           (3.5)

**Proof.** With `Phi(s,t)=E exp(i[sL+tY])`, Fresnel linearization gives

`|Phi(s,t)| <= (4pi |lambda t|)^(-1/2)
               int_R prod_i |psi_i(sw_i+xi v_i+t beta b_i)| dxi`.  (3.6)

Put `tau=beta t` and

`H(tau)=int_{R^2} prod_i |psi_i(sw_i+xi v_i+tau b_i)| ds dxi`.      (3.7)

For fixed `tau`, (1.3) in the `(w,v)` frame yields `H(tau)<=(4pi)^2`; integrating over `tau`, (1.3) in the `(w,v,b)` frame yields `int H<=(4pi)^3`. Hence

`int |tau|^(-1/2)H(tau)dtau <=128 pi^(5/2)`.                       (3.8)

The change `tau=beta t` then gives

`int_{R^2}|Phi(s,t)| dsdt <=64pi^2/sqrt(|lambda beta|)`.            (3.9)

Two-dimensional Fourier inversion proves (3.3). Restricting a measure only decreases it; under (3.4), `sqrt(|lambda beta|)>=|lambda|r`, proving (3.5). QED.

## 4. New endpoint: beta=0 is also paid in the same diffuse frame

The previous estimate becomes singular as `beta ->0`, but the geometry at `beta=0` is actually easier once one keeps the two-dimensional product projection rather than the one-dimensional curved fibers.

### Theorem 4.1 — `QFORM-DIFFUSE-CURVED-SECTION-BETA0-v1`

Under (3.1), set

`Y_0=lambda(V-v0)^2`, `lambda!=0`.                                  (4.1)

Then the subprobability pushforward of `(L,Y_0)` from the off-fold region `|V-v0|>r` has a density satisfying

`boxed: ||p_(L,Y_0; |V-v0|>r)||_infinity <=4/(|lambda|r).`          (4.2)

**Proof.** The characteristic function of `(L,V)` is

`prod_i psi_i(sw_i+tv_i)`.

Because `w_i^2+v_i^2<=1/2`, (1.3) in dimension two gives

`int_{R^2}|phi_(L,V)(s,t)| dsdt <=(4pi)^2`.                         (4.3)

Thus `(L,V)` has a continuous `C_0` density `g` with

`||g||_infinity <= (4pi)^2/(2pi)^2 =4`.                            (4.4)

For fixed `l,y`, the equation `y=lambda(v-v0)^2` has at most two inverse branches. On `|v-v0|>r`, each branch has Jacobian

`|d/dv [lambda(v-v0)^2]| =2|lambda||v-v0| >=2|lambda|r`.            (4.5)

Therefore the density of the restricted pushforward is bounded by

`2 * 4 /(2|lambda|r)=4/(|lambda|r)`.                               (4.6)

QED.

This is a genuine improvement over the early checkpoint: in the diffuse three-frame regime, both `beta=0` and `|beta|>=|lambda|r^2` are now closed. The remaining analytic discontinuity is only

`0<|beta|<|lambda|r^2`.                                             (4.7)

No perturbative deletion of `beta B` is allowed here because the input laws can have unbounded support.

## 5. Designated partner fleet02/B06 applied at an actual inequality

Use completed partner theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical source

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`.

If `w,v,b` are supported on three pairwise disjoint original-coordinate banks, then `L,V,B` are independent, and the partner theorem gives the actual inequalities

`boxed: ||p_L||_infinity<=sqrt(e),  ||p_V||_infinity<=sqrt(e),  ||p_B||_infinity<=sqrt(e).` (5.1)

On `|V-v0|>r`, the subprobability density of `Z=lambda(V-v0)^2` has at most two branches and therefore

`||p_(Z;off)||_infinity <=sqrt(e)/(|lambda|r)`.                    (5.2)

Convolution with independent `beta B` cannot increase this supremum, and independence of `L` gives

`boxed: ||p_(L,Y; |V-v0|>r)||_infinity <= e/(|lambda|r)`           (5.3)

for **every** `beta`, including zero. Thus the entire small-beta problem is already paid at the exact disjoint-bank endpoint.

The newer fleet02/B06 fused-concentration handoff `math-open-problems@e06fb19a6918caacb1b9848ed248f43a9886526b` is compatible with the same splice: if a fused packet concentrates on at most two original coordinates it forces either localized square mass or a quantitative transverse residual hub. I do not promote that structural statement to a complete receiver here; its own handoff records the remaining transverse-chain-hub step.

## 6. New exact obstruction: physical-pair coarea summation loses linearly even in a perfectly diffuse frame

A tempting way to attack (4.7) is to use the coarea Jacobian of the map `(L,Y)`, decompose its unit two-form into physical coordinate pairs, apply a two-coordinate area formula pair by pair, and sum the resulting bounds. The following exact Walsh-frame computation shows that this interface loses a factor of order `n` before any input law is used.

### Proposition 6.1 — `QFORM-PAIRWISE-COAREA-L1-LOSS-v1`

Let `n` be divisible by four, `n>=8`. Partition the coordinates into four equal sign classes indexed by `(s_i,t_i) in {(+,+),(+,-),(-,+),(-,-)}`. Define

`w_i=1/sqrt(n)`, `v_i=s_i/sqrt(n)`, `b_i=t_i/sqrt(n)`.              (6.1)

Then `w,v,b` are orthonormal and

`w_i^2+v_i^2+b_i^2=3/n<=1/2`.                                      (6.2)

For every angle `theta`, put

`n_theta=cos(theta)v+sin(theta)b`                                  (6.3)

and denote the physical `2x2` minors of the orthonormal two-frame `(w,n_theta)` by

`d_ij(theta)=w_i(n_theta)_j-w_j(n_theta)_i`.                       (6.4)

Then

`sum_{i<j} d_ij(theta)^2 =1`,                                      (6.5)

but uniformly in `theta`,

`boxed: sum_{i<j}|d_ij(theta)| >= n/2.`                             (6.6)

In fact, with `a=|cos theta|`, `c=|sin theta|`,

`sum_{i<j}|d_ij(theta)|
 = n/8 [2a+2c+|cos theta+sin theta|+|cos theta-sin theta|]
 = n/4 [a+c+max(a,c)]`.                                            (6.7)

The last expression is at least `n/2`.

**Proof.** Orthogonality follows from the equal occupancy of the four sign classes. Equation (6.5) is Cauchy--Binet for an orthonormal two-frame. Also

`d_ij(theta)=[cos(theta)(s_j-s_i)+sin(theta)(t_j-t_i)]/n`.          (6.8)

Pairs inside one sign class contribute zero. Each unordered pair of distinct sign classes contributes `(n/4)^2` coordinate pairs. Four adjacent class-pairs change one sign and two opposite class-pairs change both. Summing their absolute contributions gives the first expression in (6.7). The identity

`|x+y|+|x-y|=2 max(|x|,|y|)`                                       (6.9)

proves the second. By symmetry reduce to `0<=theta<=pi/4`; then the bracket is `2cos(theta)+sin(theta)`, a concave function whose minimum on that interval is its endpoint value `2`. Hence (6.6). QED.

### Consequence for the proof interface

For a two-output coarea map whose normalized gradient two-frame is `(w,n_theta)`, a physical-pair change of variables along pair `{i,j}` pays a reciprocal Jacobian `1/|d_ij|`. If one inserts the exact Cauchy--Binet partition of unity `1=sum d_ij^2` and then bounds each pair separately, the canonical majorant contains

`sum d_ij^2/|d_ij| = sum |d_ij|`,                                  (6.10)

which is at least `n/2` in this diffuse Walsh frame. Thus **Cauchy--Binet plus separate physical-pair coarea payment is not a dimension-free replacement for the curved fiber supremum**. A successful proof has to aggregate the product law before reciprocal-minor payment, as in Sections 2--5, or introduce a genuinely coupled bank/ridge receiver.

This proposition is a proof-interface obstruction, not a QFORM counterexample and not a statement that every pair-based argument must fail.

## 7. Current first unpaid implication

The curved-section debt is now sharply isolated as

`QFORM-CURVED-SECTION-SMALL-NONZERO-BETA-OVERLAPPING-v1`:

> Under the diffuse leverage gate `w_i^2+v_i^2+b_i^2<=1/2`, prove
> `||p_(L,lambda(V-v0)^2+beta B; |V-v0|>r)||_infinity <= C/(|lambda|r)`
> uniformly in the genuinely overlapping regime `0<|beta|<|lambda|r^2`, while retaining product structure before any fiber maximum or reciprocal physical-minor sum; or prove a structural splice routing that regime to the completed grouped-bank/fused-volume/hub receivers.

The endpoint `beta=0` is now closed by Theorem 4.1, the large-transverse regime by Theorem 3.1, and the exact disjoint-bank geometry by (5.3). Proposition 6.1 rules out the most direct missing interpolation through separately paid physical pairs.

The full arbitrary-dimensional QFORM conjecture remains **OPEN**. No target counterexample is produced. Theorems 2.1 and 3.1 give continuous `C_0` densities in their stated full-pushforward scopes. Theorem 4.1 is a bounded-density statement for the off-fold restricted pushforward; no global continuity claim follows from that restriction. Full-target continuity remains **OPEN**.

Independent end-to-end review of the new r36 statements is still pending.
