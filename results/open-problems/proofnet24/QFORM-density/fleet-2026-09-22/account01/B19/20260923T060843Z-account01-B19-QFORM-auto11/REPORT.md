SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T06:08:43Z.
attacking: punctured near-null rank-two cross branch: combine the partner endpoint with a coefficient-exact product-preserving transducer rather than continuity in the small transverse square.

# account01/B19 auto11 — a uniform punctured near-null rank-two cross transducer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Universal proof assembly / SYNTHESIS  
**Fresh owner control before derivation:** revision `2026-09-22.15`; full QFORM remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (repository retrieval is not native learned-memory ingestion).  
**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN`.

No moment, compact-support, log-concavity, Gaussianity, post-rotation independence, arbitrary-joint coarea estimate, conditional-density-as-independence substitution, coefficient-continuity interpolation, or pointwise oscillatory-decay assertion is used.

## 1. Source-pinned state used

The designated partner is account02/B19, source

`yspennstate/math-open-problems@3c7101e52142bfcd34c20325430867e2972c1202`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T051116Z-account02-B19-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-RANK2-CROSS-NULL-TRANSVERSE-HYPERBOLIC-v1` pays the exact `lambda=0`, `delta>0` endpoint, and its first unpaid implication is the punctured strip `0<|lambda|<eta` with quantitative `delta` and rank-two cross product. It also records the aggregate threshold

`rho0 := s1(C)s2(C) >= sqrt(29/3072)`

in the current compound-energy branch, and uses `delta>=1/64` as the fixed-scale hyperbolic trigger.

The complementary account03/B19 theorem is source-pinned at

`yspennstate/math-open-problems@82773d6d0339c8867b76c777216b6c564939f2ae`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T043056Z-account03-B19-QFORM-r26/REPORT.md`.

It proves `QFORM-RANK2-CROSS-TRANSVERSE-3D-CURVATURE-v1`, namely a continuous-density bound

`||p_Q||_infinity < 12.01 |lambda|^(-1/4)(s1s2)^(-3/8)`

for nonzero transverse square coefficient `lambda`. The present argument fuses the two mechanisms and removes the singular dependence on whether `lambda` vanishes.

The product-marginal input used below is the already-consumed source-valid theorem used in account03/B19: every orthogonal `k`-dimensional projection of an independent cap-one product law has density cap `2^(k/2)`. Thus the relevant caps are

`K3=2sqrt(2)`, `K2=2`, `K1=sqrt(2)`.

## 2. New theorem

### Theorem — `QFORM-RANK2-CROSS-TRANSVERSE-UNIFORM-NEARNULL-v1`

Let `U` and `V` be disjoint banks of original independent real coordinates, every scalar density bounded by one. Consider

`Q = U^T B U + 2 U^T C V + V^T D V + a^T U + b^T V + c`,

where `B,D` are symmetric and `C` has exact rank two with nonzero singular values `s1>=s2>0`.

Assume there is a three-dimensional physical subspace `E` of the `U`-coordinate space such that

1. `range(C) subset E`;
2. `range(B) subset E`;
3. `a in E`.

Let `P=range(C)`, let `r` be a unit vector spanning `E cap P^perp`, and put

`lambda = r^T B r`,
`delta = ||P B r||_2`.

If `(lambda,delta)!=(0,0)`, then `Q` has a continuous density, vanishing at infinity, and

`||p_Q||_infinity <= C_* (lambda^2+delta^2)^(-1/8) (s1 s2)^(-3/8)`,        (2.1)

where

`C_* = 2^(15/4) 3^(-3/8) = 8.9113194670... < 8.912`.                       (2.2)

In particular, if `delta>0`,

`||p_Q||_infinity < 8.912 delta^(-1/4)(s1s2)^(-3/8)`                        (2.3)

uniformly for **all** real `lambda`, including the punctured near-null regime and the exact endpoint `lambda=0`.

All signs and degeneracies allowed by the hypotheses are included. `D` and `b` are arbitrary. No perturbative deletion of `lambda` is used.

## 3. Proof

Take an orthonormal basis `(p1,p2)` of `P`. If `delta>0`, choose `p1` in the direction of `PBr`; if `delta=0`, choose any orthonormal basis of `P`. Write

`z=(x,z2)=(p1^T U,p2^T U)`, `y=r^T U`.

Since `B` is symmetric and `range(B) subset E`, its source polynomial is

`F(z) + 2 delta x y + lambda y^2`                                                        (3.1)

for a quadratic polynomial `F`. The `U`-affine term contributes an additional scalar multiple of `y` and an affine term in `z`.

If `delta>0`, absorb the `y`-linear coefficient into a deterministic shift `x0`, giving

`F1(z) + 2 delta (x-x0)y + lambda y^2`.                                                (3.2)

If `delta=0` then necessarily `lambda!=0`; complete the scalar square in `y`. A deterministic translation of `y` preserves all density caps below. Thus both cases reduce to the phase

`q_z(y)=lambda y^2 + 2 delta (x-x0)y`,                                                   (3.3)

with the convention `x0=0` when `delta=0` after completing the scalar square.

Choose a thin SVD basis on the `V` side. In the chosen `P` basis the cross pairing is

`2 z^T K w`,                                                                            (3.4)

where `K` is an invertible `2x2` matrix and

`|det K|=s1 s2`.                                                                         (3.5)

Let `p(z,y)` be the joint density of the orthogonal three-dimensional projection `(z,y)` of the original product bank `U`. Then

`||p||_infinity <= K3=2sqrt(2)`.                                                         (3.6)

Its two-dimensional marginal

`m(z)=int p(z,y)dy`

is the density of the orthogonal projection onto `P`, hence

`||m||_infinity <= K2=2`.                                                                (3.7)

On the `V` side, disintegrate over `w` and absorb `V^T D V+b^TV` and all orthogonal fibers into a complex amplitude `b_t(w)`. Its absolute value is bounded by the positive two-dimensional projection density, hence

`||b_t||_2 <= sqrt(2)`                                                                    (3.8)

for every real `t`.

Define

`G_t(z)=exp(i t F1(z)) int p(z,y) exp(i t q_z(y))dy`.                                    (3.9)

Then

`phi_Q(t)=int int G_t(z)b_t(w)exp(2it z^T K w) dz dw`.                                  (3.10)

### 3.1 A uniform mixed `L_t^3(L_z^2)` estimate

Fix `z` and set `g(y)=p(z,y)`. For almost every `z`, the pushforward of `g(y)dy` by `q_z` has a density `h_z`. If `lambda!=0`, there are at most two inverse branches; if `lambda=0`, there is one inverse branch except on the null slice `x=x0`, which is irrelevant to the `z` integration.

For a.e. `u`,

`h_z(u)=sum_{q_z(y)=u} g(y)/|q_z'(y)|`.

Since `(A+B)^(3/2)<=sqrt(2)(A^(3/2)+B^(3/2))`, change of variables on the monotonic branches gives

`int h_z(u)^(3/2) du
 <= sqrt(2) int g(y)^(3/2)|q_z'(y)|^(-1/2)dy
 <= sqrt(2) K3^(1/2) I(z)`,                                                             (3.11)

where

`I(z)=int g(y)|2lambda y+2delta(x-x0)|^(-1/2)dy`.                                       (3.12)

By Hausdorff--Young for the unnormalised Fourier transform,

`||G_.(z)||_3 <= (2pi)^(1/3)||h_z||_(3/2)`.                                             (3.13)

Hence

`||G_.(z)||_3^2 <= (2pi)^(2/3) 2^(2/3) K3^(2/3) I(z)^(4/3)`.                            (3.14)

Now write

`L(x,y)=lambda y+delta(x-x0)`.

Because `I=2^(-1/2) int g |L|^(-1/2)`, weighted Jensen at exponent `4/3` gives

`I(z)^(4/3)
 <= 2^(-2/3) m(z)^(1/3) int g(y)|L(x,y)|^(-2/3)dy`.                                    (3.15)

Using (3.7) and integrating in `z`,

`int I(z)^(4/3)dz
 <= 2^(-2/3)K2^(1/3) E|lambda y+delta(x-x0)|^(-2/3)`.                                  (3.16)

The scalar linear form

`W=(lambda y+delta x)/R`, `R=sqrt(lambda^2+delta^2)`,                                   (3.17)

is a unit one-dimensional projection of the original product bank `U`, so its density is bounded by `K1=sqrt(2)`. For any probability density bounded by `sqrt(2)`, the bathtub principle gives

`sup_c E|W-c|^(-2/3) <= 6`.                                                              (3.18)

Therefore

`E|lambda y+delta(x-x0)|^(-2/3) <= 6 R^(-2/3)`,                                         (3.19)

and consequently

`int I(z)^(4/3)dz <= 6*2^(-2/3)K2^(1/3)R^(-2/3)`.                                     (3.20)

Since `3>=2`, Minkowski yields

`|| ||G_t||_(L_z^2) ||_(L_t^3)^2 <= int ||G_.(z)||_3^2 dz`.                             (3.21)

Combining (3.14) and (3.20),

`|| ||G_t||_2 ||_(L_t^3)
 <= (2pi)^(1/3)sqrt(6)K3^(1/3)K2^(1/6)R^(-1/3)
 = 2sqrt(6) pi^(1/3) R^(-1/3)`.                                                         (3.22)

This is the key estimate. It is uniform through `lambda=0`; no coefficient continuity argument appears.

### 3.2 Rank-two bilinear Plancherel and Fourier inversion

For `t!=0`, two-dimensional Plancherel in `w`, followed by the change `xi=2tK^Tz`, gives

`|phi_Q(t)|
 <= [pi/(|t|sqrt(s1s2))] ||G_t||_2 ||b_t||_2
 <= [pi sqrt(2)/( |t|sqrt(s1s2))] ||G_t||_2`.                                          (3.23)

Let `beta=sqrt(s1s2)`. For `T>0`, use `|phi_Q|<=1` on `|t|<=T`, Holder `(3,3/2)` on the tail, and

`|| |t|^(-1)1_(|t|>T)||_(3/2)=4^(2/3)T^(-1/3)`.

By (3.22),

`int |phi_Q(t)|dt
 <= 2T + A R^(-1/3) beta^(-1) T^(-1/3)`,                                             (3.24)

with

`A = 2^(10/3)sqrt(3) pi^(4/3)`.                                                         (3.25)

The optimizer satisfies

`T=[A R^(-1/3)beta^(-1)/6]^(3/4)`.                                                      (3.26)

At this value the tail term equals `6T`, so the integral is at most `8T`. Fourier inversion gives

`||p_Q||_infinity
 <= (4/pi)(A/6)^(3/4) R^(-1/4) beta^(-3/4)
 = 2^(15/4)3^(-3/8) (lambda^2+delta^2)^(-1/8)(s1s2)^(-3/8)`.                          (3.27)

This proves (2.1). The same estimate shows `phi_Q in L^1`, hence the density has a continuous representative vanishing at infinity.

## 4. Direct application to the designated partner's first unpaid inequality

The partner's current unresolved strip is `0<|lambda|<eta` with quantitative `delta` and rank-two cross product. The theorem above removes the strip entirely whenever `delta>0`: the bound does not worsen as `lambda ->0`.

At the current compound-energy thresholds

`delta>=1/64`,
`s1s2>=rho0=sqrt(29/3072)=0.097160198469675...`,

(2.3) gives

`||p_Q||_infinity
 < 8.912 * 64^(1/4) * rho0^(-3/8)
 < 60.42`.                                                                              (4.1)

Thus the partner's `QFORM-RANK2-CROSS-PUNCTURED-NEARNULL-TRANSVERSE-v1` is **paid in the stated fixed-delta/fixed-cross-product scope**, including every sign of `lambda`, all repeated/degenerate eigenvalues consistent with the hypotheses, arbitrary cap-one product laws, and arbitrary opposite-bank self curvature.

This is an actual equation-level application of account02/B19, not a status-only citation.

## 5. Compact conditional end-to-end argument and the first remaining implication

The current source-pinned proof graph can be stated compactly as follows.

1. Existing scalar/pair, ridge/diffuse, cross-volume, hub, exact-cross-rank-two, and grouped-coordinate branches pay their stated quantitative scopes; the unrestricted theorem is reduced to the current `N3(tau)` structural residue.
2. In the rank-two aggregate cross geometry, account03/B19 pays every `lambda!=0` transverse-square state; account02/B19 paid `lambda=0, delta>0` by a separate hyperbolic endpoint theorem.
3. Theorem 2 above unifies these regimes: whenever `(lambda,delta)!=(0,0)`, the same branch has a continuous bounded density with the explicit bound (2.1). In the live fixed-scale aggregate packet, (4.1) gives `<60.42`.
4. Therefore the first essential unproved corner of this route is the **double-null transverse state**

`lambda=0`, `delta=0`.                                                                  (5.1)

Here `r^TBr=0` and `PBr=0`. Because `B` is symmetric with `range(B) subset E=P direct_sum span(r)`, (5.1) implies

`Br=0`.                                                                                 (5.2)

Also `r perp range(C)`, so

`C^T r=0`.                                                                              (5.3)

Thus the transverse source direction `r` is an exact kernel direction of the entire two-bank quadratic matrix restricted to the source/cross geometry. No reciprocal minor should be selected from it. The correct next implication is therefore

`QFORM-RANK2-CROSS-DOUBLE-NULL-TRANSVERSE-DESCENT-v1`:

> product-preservingly descend the exact kernel state (5.2)-(5.3) to a paid two-dimensional source / opposite-bank third-curvature branch, or show that the missing third large spectral direction forces one of the already-paid ridge, hub, physical-pair, rank-three-self, or additional-cross-volume exits.

If that descent is established exhaustively inside the current N3 structural reduction, the rank-two-cross terminal branch closes. The full theorem still requires the rest of the N3 proof graph to be exhaustively assembled and independently reviewed twice; it is therefore **not** claimed solved here.

## 6. Continuity

Unlike the previous exact-null endpoint, the present proof itself gives `phi_Q in L^1`. Hence continuity is proved in the scope of Theorem 2. Continuity for the full QFORM target remains open and is tracked separately.
