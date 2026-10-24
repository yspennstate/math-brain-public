SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-24T10:18:17.466006Z.
attacking: the small-weight region in the sum-difference mixed-Lp identity via signed scalar-cell aggregation before inversion.

# account01/B01 r19 — signed scalar-cell recovery at the punctured row

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T101817Z-account01-B01-qform-auto11-r19`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING SIGNED AVERAGED-FREQUENCY THEOREMS / FULL QFORM OPEN**

## 1. Scope and correction boundary

All random inputs below are ORIGINAL independent coordinates with probability densities bounded by one. No Gaussianity, moments, log-concavity, compact or connected support, smoothness, or independence after a rotation is assumed.

The phase-aligned fragmented-support obstruction is preserved. For every prescribed nonzero frequency `tau` and every `eta>0`, one can take a finite union `E` of intervals of total length one inside

`{x : dist(tau x^2,2 pi Z)<eta}`

and `f=1_E`, obtaining `Re E exp(i tau X^2)>=cos eta`. Thus no law-uniform positive-power pointwise decay is used below.

The live programme still records the unrestricted QFORM theorem and the general continuity conclusion as OPEN. In particular, arbitrary-joint coarea, normalized conditional-density caps, naive fiber suprema and absolute cell-by-cell closure remain forbidden proof interfaces.

## 2. Signed integration of one sum/difference cell

Let `X,X'` be iid with density `0<=f<=1`. Set

`U=X-X'`, `V=X+X'`,

`h(u,v)=(1/2)f((v+u)/2)f((v-u)/2)`,

and

`Psi_f(u,s)=int exp(i s v) h(u,v) dv`.

For real `a,z` define the SIGNED pulled-back cell

`K_(a,z)(t)=int_R Psi_f(u,t(a u+z)) du`.                    (2.1)

The preceding B01 run proved that replacing the signed integral in (2.1) by its absolute value before integrating `u` is impossible uniformly: already for `f=1_[0,1]` and `z=0`, `int int |Psi(u,t a u)|^p dt du=infinity` for every `p>0`. The next identity shows exactly what cancellation that absolute-value step destroys.

### Theorem 2.1 — `QFORM-SIGNED-CELL-FACTOR-L32-v1`

For every `a!=0`, every `z in R`, and every cap-one probability density `f`,

`boxed: K_(a,z)(t)=G_(a,z)(t) G_(-a,z)(t),`                   (2.2)

where

`G_(a,z)(t)=int f(x) exp(i t(a x^2+z x)) dx`.                (2.3)

Moreover

`boxed: int_R |K_(a,z)(t)|^(3/2) dt <= 50 pi / |a|.`          (2.4)

Consequently, for every `lambda>0`,

`|{t: |K_(a,z)(t)|>lambda}|
 <= (50 pi/|a|) lambda^(-3/2).`                              (2.5)

#### Proof

Use `u=x-y`, `v=x+y`, for which `du dv=2 dx dy`. The factor `1/2` in `h` cancels this Jacobian. The phase becomes

`(a(x-y)+z)(x+y)=a x^2-a y^2+z x+z y`,

which factorizes and proves (2.2).

For `a!=0`, completing the square in (2.3) reduces it, up to a unimodular constant and a translation of the cap-one density, to the characteristic function of `aY^2`. The density `g` of `Y^2` satisfies `g(w)<=w^(-1/2)` for `w>0`. Hence

`int g(w)^(3/2) dw <= 5`: on `(0,1)` integrate `w^(-3/4)` to obtain `4`, while on `(1,infinity)` use `g^(3/2)<=g`. Scaling by `a` gives

`int g_a^(3/2) <= 5 |a|^(-1/2)`.

Hausdorff--Young with Fourier convention `hat g(t)=int exp(itx)g(x)dx` therefore yields

`int |G_(+/-a,z)(t)|^3 dt <= 2 pi * 25 / |a| = 50 pi/|a|`.  (2.6)

Hölder in `t`, applied to (2.2), gives (2.4). Markov gives (2.5). QED.

This is a signed averaged-frequency replacement for the false pointwise scalar Fresnel bound. The same fragmented `f` may make `|G_(a,z)(tau)|` close to one at a chosen frequency; (2.4) says only that the complete signed frequency occupation remains controlled.

## 3. Exact zero-curvature endpoint: a weighted half-Riesz frequency identity

The nonzero-`a` estimate (2.4) blows up as `a->0`, so the endpoint must be treated separately rather than by perturbatively discarding a small quadratic coefficient.

Let

`hat f(s)=int exp(isx)f(x)dx`,

and let `r(u)=int f(x)f(x-u)dx` be the density of `X-X'`. Then `0<=r<=1` and `int r=1`.

### Theorem 3.1 — `QFORM-SIGNED-CELL-ZEROCURVATURE-HALFRIESZ-v1`

For `z!=0`,

`K_(0,z)(t)=hat f(tz)^2`,                                    (3.1)

and

`boxed:
 int_R |t|^(-1/2)|K_(0,z)(t)| dt
 <= 4 sqrt(pi) |z|^(-1/2).`                                  (3.2)

If `Z` is any independent real random variable with density cap `M`, then

`boxed:
 E_Z int_R |t|^(-1/2)|K_(0,Z)(t)| dt
 <= 8 sqrt(2 pi M).`                                          (3.3)

#### Proof

Equation (3.1) is (2.2) at `a=0`. Since

`|hat f(s)|^2=int exp(isu)r(u)du`,

and

`int_0^infinity s^(-1/2) cos(su) ds=sqrt(pi/2)|u|^(-1/2)`,

Tonelli after a standard exponential cutoff and monotone/dominated passage gives

`int_R |s|^(-1/2)|hat f(s)|^2 ds
 =sqrt(2 pi) int_R |u|^(-1/2)r(u)du`.                         (3.4)

Among probability densities bounded by one, the symmetric decreasing kernel `|u|^(-1/2)` is maximized by the centered interval density of mass one, so

`int |u|^(-1/2)r(u)du <= int_(-1/2)^(1/2)|u|^(-1/2)du=2sqrt(2)`. (3.5)

Thus the right side of (3.4) is at most `4sqrt(pi)`. The substitution `s=tz` proves (3.2). Likewise, for a density cap `M`, the bathtub principle gives

`E|Z|^(-1/2)<=2sqrt(2M)`,                                    (3.6)

which combined with (3.2) proves (3.3). QED.

The endpoint estimate is weaker numerically than the newest partner's direct physical-space zero-diagonal theorem, but it is important analytically: the exact `a=0` state has a finite signed half-Riesz frequency budget even though the unweighted absolute pullback from the previous run diverges logarithmically.

## 4. What this says about the punctured diffuse-row gap

The newest completed account02/B01 report isolates a finite-leak survivor with a certified ORIGINAL row satisfying

`0<|S_ii|<1/64`,
`r_i=(sum_(l!=i)S_il^2)^(1/2)>=31/64`,
`max_(l!=i)|S_il|<1/8`,                                      (4.1)

and proves the raw cubic row budget

`R_i(T)<=min{2T,18.344807[1+log_+(T/9.172404)]}.`             (4.2)

It also proves the exact zero-diagonal endpoint uniformly. Theorem 2.1 gives a complementary SIGNED resource for every nonzero scalar curvature, while Theorem 3.1 gives a signed half-Riesz resource at exactly zero curvature. Hence the obstruction is now sharper than simply "small pivot": one must synthesize these two signed regimes while retaining the other cells' dependence on the same difference variable. In particular, integrating the scalar cell in `u_i` first is not automatically legal for the full product in the exact decoupling identity, because the other factors contain `(Au)_k` and therefore also depend on `u_i`.

This prevents an overclaim. The missing implication is a multilinear signed interpolation/aggregation theorem, not another scalar estimate.

## 5. Designated partner applied to an actual target inequality

The freshest completed designated-partner result used here is account02/B01

`QFORM-ZERODIAG-ROW-HALFRIESZ-v1`,

from

`yspennstate/math-open-problems@f2bb4e5d3f65c19715e6cbad2e79d7c071d6b174`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T091804Z-account02-B01-qform-auto11/REPORT.md`.

It states that if an ORIGINAL-coordinate quadratic-plus-affine form has `S_ii=0` and off-diagonal row norm `c_i>0`, then, with arbitrary remaining quadratic curvature,

`H_(1/2)(R)<=2^(11/4)c_i^(-1/2)`.                             (5.1)

Apply it to, for every `m>=1`,

`Q_m^+ = X_0^2 + Z^2 + 2 H m^(-1/2) sum_(j=1)^m Y_j`,         (5.2)

with all displayed coordinates independent and cap one. The residual after peeling the literal outer square `X_0^2` has zero physical diagonal at `H` and row norm exactly one; the extra `Z^2` is allowed arbitrary remaining curvature. Therefore (5.1) and the scalar-square peel give

`boxed: ||p_(Q_m^+)||_infinity <= 2^(11/4)
       = 6.727171322029716...`                                (5.3)

uniformly in `m` and in all admissible input laws.

The coefficient spectrum of (5.2) is

`{1,1,1,-1,0,...,0}`,                                        (5.4)

so (5.3) is a strict full-target application of the designated partner theorem. It also illustrates why aggregate row energy, rather than a largest individual edge, is the correct currency: every star edge has size `m^(-1/2)` while the uniform bound stays constant.

## 6. Remaining implication

The first unpaid implication is now

`QFORM-SIGNED-PUNCTURE-INTERPOLATION-v1`:

in the full decoupled product, prove a multilinear signed aggregation estimate that is uniform as a certified diffuse-row diagonal coefficient `a=S_ii` passes through zero, combining the finite `L^(3/2)_t` signed-cell budget for `a!=0`, the weighted half-Riesz endpoint for `a=0`, and the target's inherited second spectral direction, without taking absolute values before the cancellation and without dividing by conditional difference densities.

A successful version for the partner's state (4.1) would close its punctured diffuse-row branch. A full theorem would still require structural routing showing that every remaining target matrix reaches a paid branch.

Full QFORM status: **OPEN**.  
Full continuity status: **OPEN**.

## 7. Source pins

Fresh control before publication: `yspennstate/math-research-brain`, OWNER CONTROL revision `2026-09-22.15`; current README blob `14046b5138615be52bb1c49a998122a7c84e200e`; live correction-inbox blob `ba7aeac3d879f59da5ec8a12daad74ea85714465`.

Previous B01 sum/difference theorem and absolute-pullback obstruction:
`yspennstate/math-open-problems@9f02f516e97372b852fe88a9d4a6138adee74a41`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260924T091018Z-account01-B01-qform-auto11-r18/REPORT.md`.

Newest designated partner theorem actually applied:
`yspennstate/math-open-problems@f2bb4e5d3f65c19715e6cbad2e79d7c071d6b174`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T091804Z-account02-B01-qform-auto11/REPORT.md`.

A bounded literature search found no published theorem matching the full arbitrary-product, arbitrary-sign, three-large-eigenvalue scope; this is not a novelty claim.
