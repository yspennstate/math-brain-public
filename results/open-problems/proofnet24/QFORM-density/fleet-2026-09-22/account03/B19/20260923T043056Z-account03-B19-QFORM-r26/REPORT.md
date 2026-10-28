SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T04:30:56Z.
attacking: QFORM-N3-CURVED-AGGREGATE-THIRD-SOURCE-v1 via an exact rank-two aggregate cross bank plus transverse within-bank curvature, after the universal local-second-gradient extraction was refuted.

# account03/B19 r26 — a rank-two cross bank plus one transverse aggregate curvature has bounded continuous output density

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN`.

The unrestricted owner theorem is **not** claimed. The theorem below proves a continuous density on a concrete aggregate-third-source branch and gives an explicit `L^infinity` constant. It uses no Gaussianity, moments, log-concavity, compact support, connected support, post-rotation independence, arbitrary-joint coarea, pointwise quadratic van der Corput estimate, or fixed-good-minor premise.

## 1. Why the mechanism changed

The preceding B19 r24 route left `QFORM-COLLAR-SECOND-GRADIENT-OR-RANKONE-ALIGNMENT-v1`: try to force one quantitative pair of physical cross gradients. Fresh account02/B19 r26,

`yspennstate/math-open-problems@d294539dec9f048e8da354542b37cc9ac664f020`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T041017Z-account02-B19-QFORM-r26/REPORT.md`,

constructs target matrices whose nonzero spectrum contains `(+1,+1,+1,-1,-1,-1)` while the best physical two-gradient area tends to zero like `m^(-1/2)`. It proves `QFORM-N3-SINGLE-SECOND-GRADIENT-EXTRACTION-FALSE-v1`. The same family is nevertheless paid by an aggregate rank-four light block and, independently, by the pure-bipartite theorem

`||p_Q||_infinity <= e sqrt(pi) < 4.819`.

Therefore a universal proof cannot insist on one physical second gradient. This run switches to the aggregate gate identified by that report: retain a whole rank-two cross bank and fuse it with a third curvature source **before** selecting a local minor.

A second fresh input is account01/B19 r11,

`yspennstate/math-open-problems@d037aee47f5f73abf078021e69478a2ebece1700`,

which proves the heavy-hub compound-energy identity `W_i>=||m||^2` and, in its exact-rank-three small-diagonal co-heavy branch, produces a full original-coordinate partition whose cross block `C` satisfies

`e_2(CC^T) >= 29/3072`.                                           (1.1)

When that captured block has exact rank two, (1.1) means

`s_1(C)s_2(C) >= sqrt(29/3072)`.                                  (1.2)

The problem is then exactly to pay a third source without rotating the input law into independent spectral coordinates.

## 2. Product-marginal input

I use the source-valid Livshyts--Paouris--Pivovarov product-marginal theorem in the form already recorded by account02/B07 (`WALSH_AGGREGATION.md`, source-visible at `yspennstate/math-open-problems@dd04097afb60aca6ff16b7f36d38df1b8b9d2080`): if `X` has independent one-dimensional densities bounded by one and `T` is a rank-`k` real matrix, then the density of `TX` satisfies

`||p_(TX)||_infinity <= 2^(k/2) / sqrt(det(TT^T)).`                (2.1)

In particular an orthogonal two-dimensional projection has density cap `2`, an orthogonal three-dimensional projection has cap `2 sqrt(2)`, and a one-dimensional projection by a row of Euclidean norm at least one has cap at most `sqrt(2)`.

No independence of the projected coordinates is asserted or used.

## 3. The new aggregate third-source theorem

### Theorem 3.1 — `QFORM-RANK2-CROSS-TRANSVERSE-3D-CURVATURE-v1`

Let `U` and `V` be disjoint banks of original independent cap-one coordinates. Consider a homogeneous quadratic form

`Q = U^T B U + 2 U^T C V + V^T D V`,                              (3.1)

where `B,D` are arbitrary real symmetric matrices and `C` has **exact rank two** with nonzero singular values

`s_1 >= s_2 > 0`.

Assume there is a three-dimensional subspace `E` of the physical `U`-coordinate space such that

1. `range(C) subset E`;
2. `range(B) subset E`;
3. if `P` denotes the two-dimensional space `range(C)` and `r` is a unit vector spanning `E intersect P^perp`, then

`lambda := r^T B r != 0`.                                         (3.2)

Then `Q` has a continuous density, vanishing at infinity, and

`boxed(
 ||p_Q||_infinity
 < 12.01 |lambda|^(-1/4) [s_1 s_2]^(-3/8).
)`                                                                  (3.3)

The same statement holds after adding affine terms that lie in `E` on the `U` side and arbitrary affine terms on the `V` side. Reflection covers `lambda<0`; all signatures and repeated eigenvalues are allowed.

The theorem deliberately does **not** claim stability under an arbitrary affine term in `E^perp` on the `U` bank. Such a term can arise after conditioning an unrelated outside bank and would introduce a time-dependent fiber amplitude into the only Hausdorff--Young step. That extension is a separate debt rather than a silently added premise.

### Matrix interpretation

Since `B` is symmetric and `range(B) subset E`, it annihilates `E^perp`. Thus all `U`-side quadratic curvature is carried by one three-dimensional **linear projection of the original product bank**. The theorem aggregates that bank first. It never treats the three aggregate coordinates as independent.

## 4. Reduction to a three-variable source receiver

Take a thin SVD

`C=P Sigma R^T`, `Sigma=diag(s_1,s_2)`,                            (4.1)

where the two columns of `P` are orthonormal in the physical `U` space and the two columns of `R` are orthonormal in the physical `V` space. Write

`z=P^T U in R^2`, `w=R^T V in R^2`, `y=r^T U`.                    (4.2)

Because `E=span(P,r)`, the `U` quadratic part has the form

`U^TBU = z^T H z + 2 y d^T z + lambda y^2`.                       (4.3)

Complete only this deterministic three-dimensional square:

`y' = y + lambda^(-1)d^Tz`                                       (4.4)

(with the obvious additional constant shift if an allowed affine term is present). Then

`U^TBU = lambda (y')^2 + F(z)`                                   (4.5)

for a real quadratic-plus-affine `F`.

The map from the original `U` coordinates to `(z,y')` has row Gram matrix

`[[I_2,c],[c^T,1+|c|^2]]`, `c=d/lambda`,                          (4.6)

whose determinant is exactly one. Therefore (2.1) gives its joint density `p(z,y')` the uniform cap

`||p||_infinity <= K_3 := 2 sqrt(2)`.                             (4.7)

The one-dimensional marginal of `y'` is itself a linear projection by the physical row `r+Pc`, whose norm is `sqrt(1+|c|^2)>=1`; hence

`||p_(y')||_infinity <= K_1 := sqrt(2)`.                          (4.8)

On the `V` side, integrate every coordinate orthogonal to `range(R)` into a complex amplitude `b_t(w)`. Its absolute value is bounded by the positive two-dimensional marginal of `R^T V`, so

`||b_t||_2 <= sqrt(2)`                                            (4.9)

for every real `t`, regardless of the quadratic form `D` and regardless of its signature.

The characteristic function is consequently

`phi_Q(t)
 = int_R2 int_R2 F_t(z) b_t(w)
     exp(2it z^T Sigma w) dz dw`,                                 (4.10)

where

`F_t(z)=exp(itF(z)) int_R p(z,y) exp(it lambda y^2) dy`.           (4.11)

The crucial point is that the amplitude `p(z,y)` in (4.11) is a genuine, `t`-independent product projection density. This is where the three-dimensional range hypothesis in Theorem 3.1 is spent.

## 5. A Hilbert-valued quadratic Hausdorff--Young estimate

Put, for `q>0`,

`H(q,z)=[p(z,sqrt(q))+p(z,-sqrt(q))]/(2sqrt(q))`.                 (5.1)

Then

`int p(z,y)e^(it lambda y^2)dy
 = int_0^infinity H(q,z)e^(it lambda q)dq`.                       (5.2)

Let `g(y)=int_R2 p(z,y)dz` and `G(y)=g(y)+g(-y)` for `y>0`. From (4.7),

`||H(q,.)||_2^2
 <= K_3 [G(sqrt(q))]/(2q)`.                                      (5.3)

Indeed `|a+b|^2<=2(|a|^2+|b|^2)` and `p^2<=K_3p`.

Therefore

`||H||_(L_q^(3/2)(L_z^2))^(3/2)
 <= 2 (K_3/2)^(3/4)
    int_0^infinity y^(-1/2)G(y)^(3/4)dy`.                        (5.4)

The last integral is dimension-free. Since `G<=2K_1` and `int_0^infinity G=1`, split at one:

`int_0^1 y^(-1/2)G(y)^(3/4)dy
 <=2(2K_1)^(3/4)`,                                                (5.5)

while Holder with exponents `4/3` and `4` gives

`int_1^infinity y^(-1/2)G(y)^(3/4)dy
 <=(int_1^infinity G)^(3/4)(int_1^infinity y^(-2)dy)^(1/4)
 <=1`.                                                            (5.6)

Thus, with

`M_0 := {2(K_3/2)^(3/4)[2(2K_1)^(3/4)+1]}^(2/3)`,                (5.7)

we have

`||H||_(L^(3/2)(L^2)) <= M_0 = 5.7831399996...`.                 (5.8)

For completeness, the Hilbert-valued Hausdorff--Young constant used here follows by interpolation: the unnormalized Fourier transform maps `L^1(R;L^2_z)` to `L^infinity(R;L^2_z)` with norm one and maps `L^2` to `L^2` with norm `sqrt(2pi)`. Riesz--Thorin at exponent `3/2 -> 3` gives norm `(2pi)^(1/3)`. Scaling by `lambda` in (5.2) therefore yields

`boxed(
 || ||F_t||_2 ||_(L_t^3)
 <= (2pi)^(1/3) M_0 |lambda|^(-1/3)
 =10.6714556068... |lambda|^(-1/3).
)`                                                                  (5.9)

The factor `exp(itF(z))` in (4.11) has modulus one and does not affect this norm.

This is an **integrated** quadratic estimate. It makes no forbidden law-uniform pointwise decay claim.

## 6. Bilinear Plancherel and `L^1` Fourier inversion

For `t!=0`, apply two-dimensional Plancherel in the `w` variable to (4.10). With the unnormalized Fourier convention,

`||hat b_t||_2=2pi||b_t||_2`,

and the change `xi=2t Sigma z` has Jacobian `4t^2s_1s_2`. Hence

`|phi_Q(t)|
 <= [pi/(|t|sqrt(s_1s_2))] ||F_t||_2||b_t||_2
 <= [pi sqrt(2)/( |t|sqrt(s_1s_2))] ||F_t||_2`.                  (6.1)

Let `beta=sqrt(s_1s_2)`. For any `T>0`, use `|phi_Q|<=1` on `|t|<=T`, (6.1) on the tail, Holder `(3,3/2)`, and (5.9):

`int_R |phi_Q(t)|dt
 <=2T+A |lambda|^(-1/3) beta^(-1)T^(-1/3)`,                     (6.2)

where

`A=pi sqrt(2)(2pi)^(1/3)M_0 4^(2/3)
 =119.4708242929...`.                                             (6.3)

The optimizer is

`T=[A |lambda|^(-1/3)beta^(-1)/6]^(3/4)`.                        (6.4)

At this value the tail equals `6T`, so (6.2) is `8T`. Fourier inversion gives

`||p_Q||_infinity
 <=(4/pi)(A/6)^(3/4)
   |lambda|^(-1/4)beta^(-3/4)`.                                  (6.5)

Since

`(4/pi)(A/6)^(3/4)=12.0017085448...<12.01`,                      (6.6)

and `beta^(-3/4)=(s_1s_2)^(-3/8)`, this proves (3.3). Moreover `phi_Q in L^1`, so the density has a continuous version vanishing at infinity.

## 7. Exact-rank-three matrix corollary

### Corollary 7.1 — `QFORM-RANK3-RANK2CROSS-TRANSVERSE-PAID-v1`

Suppose the **entire** target matrix has exact rank three,

`A=RMR^T`, `R^TR=I_3`, `M=M^T` invertible,                        (7.1)

and split the original physical coordinates into a genuine partition `I union J`. Put

`B=A_II`, `C=A_IJ`, `D=A_JJ`.

Assume

- `rank(R_I)=3`;
- `rank(C)=2`;
- if `r` spans `range(R_I) intersect range(C)^perp`, then
  `|r^T B r|>=alpha>0`;
- `s_1(C)s_2(C)>=rho>0`.

Then, for arbitrary independent cap-one physical inputs,

`boxed(||p_(X^TAX)||_infinity <12.01 alpha^(-1/4)rho^(-3/8))`,     (7.2)

and the density is continuous.

Proof: since `rank(R_I)=3` and `M` is invertible, `range(B)=range(R_I)`, a three-dimensional space containing `range(C)`. Theorem 3.1 applies with `U=X_I`, `V=X_J`. No spectral rotation of the law is made; `R_I` is used only to identify a physical-bank projection to which (2.1) applies.

### Application to the fresh compound-energy packet

In the account01/B19 r11 disjoint branch, the partition is of **all** residual physical indices, so `U={i} union J` and `V=K` form a genuine full partition. If its captured cross block has exact rank two, then from (1.1)

`rho=s_1(C)s_2(C)>=sqrt(29/3072)=0.09716019847...`.               (7.3)

If additionally `rank(R_U)=3` and the transverse scalar curvature obeys

`|r^T A_UU r|>=1/64`,                                             (7.4)

Corollary 7.1 gives the concrete target-level branch

`boxed(||p_Q||_infinity <81.373<82)`,                             (7.5)

with a continuous density.

Thus a fixed aggregate `E_2` cross packet plus a genuine transverse bank curvature is now paid without choosing one physical second-gradient row. This is precisely the mechanism that survives the fresh account02/B19 local-gradient no-go.

## 8. Designated partner account04/B19 applied to an actual branch

The completed designated-partner theorem is account04/B19 r2,

`yspennstate/math-open-problems@1e7af7988c38150c1591910270c44f4f219164b3`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`,

`QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`.

In its proved residual-diffuse exact-rank-three null-coloop scope it gives, for `0<D_res<=1`,

`||p_Q||_infinity <34 sqrt(log(e/D_res))`.                         (8.1)

Therefore the actual proof-tree interval

`e^(-8) <= D_res <=1`                                             (8.2)

is paid by

`boxed(||p_Q||_infinity <102)`,                                   (8.3)

because `log(e/D_res)<=9`. The same partner source separately gives `<11.748` for `D_res>=1` and `<5.844` at the exact endpoint `D_res=0`. I do not extend (8.1) to near-coloops, non-diffuse residual laws, or the punctured interval `0<D_res<e^(-8)`.

This is an equation-level application of the designated partner result, not a citation-only acknowledgement.

## 9. Compact correction-safe proof map after this run

The present synthesis is now:

1. scalar/pair, diagonal, diffuse-ridge, regularized-determinant, exact-null-coloop, grouped-square, rank-two affine half-Riesz and several heavy-coordinate branches are already paid at their source-pinned hypotheses;
2. account02/B19 r26 closes every pure bipartite target and refutes a universal fixed second-gradient extraction, so the r24 local-gradient proposal is retired as a global mechanism;
3. account01/B19 r11 forces a constant **aggregate** second-compound packet from a small-diagonal co-heavy hub;
4. Theorem 3.1 above pays an exact-rank-two aggregate cross bank whenever its third curvature lives transversely inside the same three-dimensional product projection; in the concrete r11 packet, the thresholds `(1.1),(7.4)` give the continuous bound `<82`;
5. account04/B19 pays its residual-diffuse null-coloop branch by the explicit inequalities in Section 8.

The first unpaid implication on this route is therefore narrower than either the old local-gradient extraction or a generic arbitrary-joint trace bound:

### `QFORM-RANK2-CROSS-NEAR-RANGE-SELF-CURVATURE-v1`

In the exact-rank-three aggregate-cross survivor, assume a full physical partition has a quantitatively nontrivial exact-rank-two cross block, but every three-dimensional source bank available to it has transverse scalar curvature below the chosen fixed threshold (e.g. `1/64`) on both sides, while the already-paid pure-bipartite, ridge, volume, null-coloop and grouped-square exits fail. Prove that this forces a product-preserving ridge/Theorem-H/grouped-coordinate exit, or pay the remaining near-null transverse curvature directly.

Equivalently: after aggregation, the hard case is no longer “find one second gradient.” It is “understand an exact rank-two cross interaction whose same-bank quadratic curvature is almost confined to the two cross ranges.” That is a finite-rank geometric alignment problem and preserves the full fragmented-support product law.

For arbitrary **extra spectrum** beyond exact rank three, a separate descent/conditioning splice remains unpaid; Theorem 3.1 does not hide that issue.

## 10. Continuity and full-target status

- New Theorem 3.1 and Corollary 7.1: **bounded continuous density** in their stated scope, because their characteristic functions are proved `L^1`.
- Partner branch Section 8: continuous density in the partner theorem's scope.
- Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuous representative: **OPEN**.

No end-to-end full candidate exists from this run, so the owner's requirement for two independent full-proof reviews is not triggered.
