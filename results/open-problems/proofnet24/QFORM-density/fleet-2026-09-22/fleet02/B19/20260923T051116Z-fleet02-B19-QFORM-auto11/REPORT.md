SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T05:11:16Z.
attacking: the rank-two aggregate cross-bank near-range endpoint — pay the exact zero transverse-square case when the third source survives as a transverse hyperbolic coupling.

# fleet02/B19 auto11 — exact-null transverse hyperbolic receiver and updated N3 proof graph

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Universal proof assembly / SYNTHESIS / complementary constructions and source-valid counterexamples  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem is not claimed. All input coordinates remain original independent coordinates; no moments, support regularity, log-concavity, Gaussianity, post-rotation independence, arbitrary-joint coarea estimate, law-uniform pointwise stationary phase, or coefficient-perturbation continuity is used.

## 1. Source-pinned proof graph used in this run

The current owner synthesis reduces the global theorem, after completed scalar/pair exits, to a no-pivot class `N3(tau)` with three actual eigenvalues of modulus at least one and uniformly small physical scalar/pair pivots. That statement remains open.

The required newest-Claude package was used at its exact source pin

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its Theorem F gives, for a rank-three source block whose physical leverage scores are at most one half, with arbitrary cross/opposite blocks retained,

`||p_Q||_infinity <= 12 |mu_1 mu_2 mu_3|^(-1/3)`.              (1.1)

Its D/D'/D5 theorems pay quantitative physical cross-volume branches; its Theorem H pays appropriate low-rank-plus-diagonal hub packets. None is an exhaustive N3 theorem.

The current designated partner is `fleet03/B19`, canonical mathematics

`yspennstate/math-open-problems@82773d6d0339c8867b76c777216b6c564939f2ae`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T043056Z-fleet03-B19-QFORM-r26/REPORT.md`.

Its theorem `QFORM-RANK2-CROSS-TRANSVERSE-3D-CURVATURE-v1` says that if two disjoint original product banks have an exact rank-two cross block with nonzero singular values `s1,s2`, all source-bank self curvature lies in one three-dimensional physical projection `E` containing the cross range `P`, and the scalar transverse self curvature

`lambda = r^T B r`, `r in E cap P^perp`, `||r||=1`,

is nonzero, then

`||p_Q||_infinity < 12.01 |lambda|^(-1/4)(s1 s2)^(-3/8)`.       (1.2)

The proof is aggregate and product-safe. Its displayed bound diverges as `lambda -> 0`, and it explicitly leaves a near-range/near-null branch.

The fresh fleet01/B19 compound-energy theorem supplies, in one exact-rank-three co-heavy branch, a full original-coordinate partition with a rank-two cross block satisfying

`e_2(CC^T)>=29/3072`, hence `s1(C)s2(C)>=rho0:=sqrt(29/3072)`.   (1.3)

This run attacks the exact `lambda=0` boundary of (1.2) without treating it as a perturbative limit.

## 2. New theorem: exact-null transverse hyperbolic receiver

### Theorem 2.1 — `QFORM-RANK2-CROSS-NULL-TRANSVERSE-HYPERBOLIC-v1`

Let `U` and `V` be disjoint banks of original independent real coordinates, every scalar density bounded by one. Let

`Q = U^T B U + 2 U^T C V + V^T D V + a^T U + b^T V + c`,       (2.1)

where `B,D` are symmetric and `C` has exact rank two with nonzero singular values `s1>=s2>0`.

Assume there is a three-dimensional physical subspace `E` of the `U`-coordinate space such that

1. `range(C) subset E`;
2. `range(B) subset E`;
3. the `U`-affine vector `a` belongs to `E`.

Let `P=range(C)` and let `r` be a unit vector spanning `E cap P^perp`. Assume

`lambda:=r^T B r=0`,                                             (2.2)

but the transverse-to-cross-plane coupling is nonzero:

`delta:=||P B r||_2>0`.                                          (2.3)

Then `Q` has a continuous density, vanishing at infinity, and

`boxed(
 ||p_Q||_infinity
 <= C_h delta^(-1/4)(s1 s2)^(-3/8),
 C_h=4(4sqrt(3)/3)^(3/4)=7.49349659500199...<7.50.
)`                                                                  (2.4)

No restriction is imposed on the opposite-bank self matrix `D` or on the opposite affine vector `b`.

This theorem is an exact endpoint statement. It does **not** assert that a small nonzero `lambda` may be deleted; the live correction set forbids such a law-uniform coefficient perturbation under arbitrary fragmented/unbounded supports.

### Proof

Take a thin SVD of the cross block. Choose orthonormal coordinates `z=(x,z_2)` on `P` with the first axis parallel to `PBr`, and orthonormal coordinates `w` on `range(C^T)`. In these coordinates the cross pairing is

`2 z^T K w`,                                                     (2.5)

where `K` is invertible and

`|det K|=s1 s2`.                                                  (2.6)

Put `y=r^T U`. Because `B` is symmetric, `range(B) subset E`, and `r^TBr=0`, the source-bank self polynomial is exactly

`F(z)+2 delta x y`                                                (2.7)

for a real quadratic polynomial `F`; the affine term in `E` changes this to

`F_1(z)+2 delta (x-x0)y`                                         (2.8)

for some deterministic `x0`. No random-coordinate shear is made.

Let `p(z,y)` be the joint density of the orthogonal three-dimensional projection `(z,y)` of the original product vector `U`. The source-valid product-marginal theorem used in the designated-partner proof gives

`||p||_infinity <= K3:=2sqrt(2)`.                                (2.9)

Let

`m(z)=int_R p(z,y)dy`.                                           (2.10)

The two-dimensional marginal `m` and the one-dimensional marginal

`h(x)=int_R m(x,z_2)dz_2`                                       (2.11)

satisfy

`||m||_infinity<=K2:=2`, `||h||_infinity<=K1:=sqrt(2)`.          (2.12)

On the `V` side, disintegrate over `w`. Absorb `V^T D V+b^TV` and every orthogonal fiber into the complex amplitude

`b_t(w)=rho_w(w) E[exp(i t(V^TDV+b^TV)) | w]`.                  (2.13)

Then

`|b_t(w)|<=rho_w(w)`, `||b_t||_2<=sqrt(2)`                       (2.14)

for every real `t`, since the orthogonal two-dimensional projection density is at most two.

Define

`F_t(z)=exp(i t F_1(z)) int_R p(z,y) exp(2 i t delta(x-x0)y)dy`. (2.15)

The characteristic function is

`phi_Q(t)=int_R2 int_R2 F_t(z)b_t(w)exp(2it z^T K w) dz dw`.     (2.16)

#### Step 1: an integrated hyperbolic estimate

Fix `z` and set `g_z(y)=p(z,y)`. With the unnormalised Fourier transform `hat g(xi)=int g(y)e^(i xi y)dy`,

`||hat g_z||_infinity<=m(z)`,                                   (2.17)

and Plancherel plus `0<=g_z<=K3` gives

`int |hat g_z(xi)|^2 dxi =2pi int g_z(y)^2dy <=2pi K3 m(z)`.     (2.18)

Therefore

`int |hat g_z(xi)|^3 dxi
 <=||hat g_z||_infinity int|hat g_z|^2
 <=2pi K3 m(z)^2`.                                               (2.19)

After `xi=2delta(x-x0)t`,

`int_R |F_t(z)|^3dt
 <= [2pi K3/(2delta|x-x0|)] m(z)^2`.                             (2.20)

Minkowski in the form `L_t^3(L_z^2)<=L_z^2(L_t^3)` yields

`|| ||F_t||_2 ||_(L_t^3)^2
 <=(2piK3)^(2/3)(2delta)^(-2/3)
   int_R2 |x-x0|^(-2/3)m(z)^(4/3)dz`.                            (2.21)

Using `m<=K2`,

`m^(4/3)<=K2^(1/3)m`,                                            (2.22)

so the remaining integral is at most

`K2^(1/3) int_R |x-x0|^(-2/3)h(x)dx`.                           (2.23)

For every probability density `0<=h<=K1`, layer cake (equivalently the one-dimensional bathtub inequality, with approximation if needed) gives

`int |x-x0|^(-2/3)h(x)dx
 <=6*2^(-1/3)K1^(2/3)=6`.                                       (2.24)

Indeed the right side is the integral against the cap-saturating centred interval of length `1/K1`; no support or moment assumption enters.

Combining (2.21)-(2.24),

`boxed(
 || ||F_t||_2 ||_(L_t^3)
 <= M_h delta^(-1/3),
 M_h=2^(2/3)pi^(1/3)sqrt(6)=5.69480572809660....
)`                                                                  (2.25)

This is an integrated estimate, not a forbidden pointwise stationary-phase envelope.

#### Step 2: rank-two bilinear Plancherel

For each nonzero `t`, apply two-dimensional Plancherel to (2.16). Since the change of variables `xi=2tK^Tz` has Jacobian `4t^2|det K|`,

`|phi_Q(t)|
 <= pi/[|t|sqrt(s1s2)] ||F_t||_2||b_t||_2
 <= pi sqrt(2)/[|t|sqrt(s1s2)] ||F_t||_2`.                      (2.26)

For `T>0`, use `|phi_Q|<=1` on `|t|<=T` and Hölder `(3,3/2)` on the tail. Because

`|| |t|^(-1)1_(|t|>T)||_(3/2)=4^(2/3)T^(-1/3)`,                 (2.27)

(2.25)-(2.26) give

`int_R |phi_Q(t)|dt
 <=2T+A delta^(-1/3)(s1s2)^(-1/2)T^(-1/3)`,                    (2.28)

where the constant simplifies exactly to

`A=pi sqrt(2) M_h 4^(2/3)=8sqrt(3)pi^(4/3)
 =63.7554200285204....`                                         (2.29)

The optimum is

`T=[A delta^(-1/3)(s1s2)^(-1/2)/6]^(3/4)`.                     (2.30)

At this value the tail term equals `6T`, hence the right side of (2.28) is `8T`. Fourier inversion gives

`||p_Q||_infinity
 <=(4/pi)(A/6)^(3/4)delta^(-1/4)(s1s2)^(-3/8)
 =4(4sqrt(3)/3)^(3/4)delta^(-1/4)(s1s2)^(-3/8)`.                (2.31)

The bound also proves `phi_Q in L^1`; therefore the density has a continuous representative vanishing at infinity. QED.

## 3. Equation-level application of the designated partner

In the fresh fleet01/B19 compound-energy branch (1.3), put

`rho0=sqrt(29/3072)=0.09716019847...`.                            (3.1)

If the designated-partner transverse square satisfies

`|lambda|>=1/64`,                                                 (3.2)

then applying (1.2) to the actual cross bank gives

`||p_Q||_infinity
 <12.01*64^(1/4)*rho0^(-3/8)
 =81.4291409999...<81.43`.                                       (3.3)

This is a direct use of the current named partner at a real inequality, not a copied citation.

At the exact boundary `lambda=0`, if the new hyperbolic coupling satisfies

`delta=||PBr||>=1/64`,                                           (3.4)

Theorem 2.1 gives

`||p_Q||_infinity
 <7.50*64^(1/4)*rho0^(-3/8)
 <50.86`.                                                        (3.5)

Thus the exact-null boundary is no longer an unanalysed singular limit when a fixed transverse bilinear source survives.

## 4. Equation-level application of newest-Claude Theorem F

Still in the same two-bank geometry, suppose instead that the source self matrix `B|_E` has rank three and physical leverage at most one half in its three-dimensional range. Embed its three eigenvectors in the full two-bank coordinate space and place every cross term and the arbitrary opposite self block in the residual matrix. On the source bank the residual principal block is zero, hence diagonal, so newest-Claude Theorem F applies exactly and gives

`||p_Q||_infinity <=12 |det(B|_E)|^(-1/3)`.                     (4.1)

Consequently a surviving rank-two-cross near-range state which escapes both Theorem 2.1 and the partner theorem must also evade this diffuse rank-three self-curvature exit: either its source leverage is high or its three-dimensional self determinant is quantitatively small (or rank deficient). This is an actual use of the required `e5f71d...` package, with the arbitrary opposite-bank curvature retained.

## 5. Updated conditional proof graph

A correction-safe source-pinned route to the full theorem now has the following paid nodes.

1. Scalar and physical-pair completion branches: paid at their source scopes; they reduce the hard structural problem to `N3(tau)`.
2. Diffuse/ridge/volume branches: newest-Claude F/H/D/D'/D5 and the current volume-stability theorem pay quantitative low-leverage and high-cross-volume packets while retaining arbitrary same-bank curvature according to their exact hypotheses.
3. Pure bipartite targets: fleet02/B19 r26 pays every target matrix `[[0,C],[C^T,0]]` by `||p||inf<=e sqrt(pi)`; the same run refutes any universal fixed-scale single-second-gradient extraction.
4. Co-heavy aggregate currency: fleet01/B19 forces either an overlap packet or a full-partition aggregate rank-two cross currency `e2(CC^T)>=29/3072` in its stated exact-rank-three branch.
5. Quantitative transverse square: designated partner fleet03/B19 r26 pays the rank-two-cross branch by (1.2), and gives the concrete `<81.43` bound at (3.2).
6. **Exact-null but hyperbolically transverse source:** Theorem 2.1 above pays `lambda=0`, `delta>0`; at the fixed scale (3.4) it gives `<50.86`.
7. Diffuse full three-dimensional source self-curvature: newest-Claude F pays it by (4.1).

These nodes do not yet exhaust N3 and do not handle arbitrary extra spectrum automatically.

## 6. First unpaid implication after this run

The first local gap is now the punctured near-null alignment problem:

### `QFORM-RANK2-CROSS-PUNCTURED-NEARNULL-TRANSVERSE-v1`

Find universal constants `eta,c,C>0`, or a scale-free repartition theorem, such that whenever a source-valid full original-coordinate partition has

- exact rank-two cross block `C` with `s1(C)s2(C)>=c`;
- three-dimensional source self range `E` containing `range(C)`;
- `r` spanning `E cap range(C)^perp`;
- `0<|lambda|=|r^TBr|<eta`;
- `delta=||PBr||>=c`;

and none of the already-paid F/H/D/D'/D5, ridge/volume-stability, physical pivot/pair, pure-bipartite, or grouped-coordinate exits applies, prove a universal density bound **uniform as `lambda ->0`**, or prove a product-preserving structural descent to an already-paid branch.

The endpoint `lambda=0` with `delta>=c` is now paid by Theorem 2.1, while every fixed `|lambda|>=eta` is paid by the designated partner. A coefficient-continuity interpolation between those endpoints is not valid under the owner hypotheses: the laws may have arbitrary unbounded fragmented support. A legitimate proof must therefore keep the mixed quadratic/hyperbolic phase jointly, or extract another original-coordinate aggregate packet.

The additional endpoint `lambda=0`, `delta=0` is also structurally unpaid unless another source supplies the third direction; in that case the source self matrix is entirely aligned with the rank-two cross range.

Beyond exact-rank-three/full-partition descendants, arbitrary additional spectrum remains a separate global synthesis debt. There are not two independent end-to-end reviews. Full QFORM and full-target continuity therefore remain OPEN.

## 7. Numerical/exact constant check

With `K3=2sqrt(2)`, `K2=2`, `K1=sqrt(2)`, the weighted marginal constant in (2.24) is exactly `6`; the derived constants are

`M_h=5.694805728096604`,
`A=63.755420028520426`,
`C_h=7.493496595001987`.

For `rho0=sqrt(29/3072)`, the designated-partner fixed-scale bound at `|lambda|=1/64` is `81.42914099990658`, while the new endpoint bound using the rounded coefficient `7.50` at `delta=1/64` is `50.850837427085715`.
