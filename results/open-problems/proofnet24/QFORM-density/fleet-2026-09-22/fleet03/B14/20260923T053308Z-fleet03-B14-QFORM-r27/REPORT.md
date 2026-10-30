SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-23T05:33:08Z.
attacking: translation/localization for the heavy-row angular-cancellation endpoint, with a product-preserving coloop receiver that keeps arbitrary shifts, fragments and unbounded supports.

# fleet03/B14 r27 — coloop angular-cancellation localization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Translations and localization  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN / CONTINUITY OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full owner target remains open. This report proves a new zero-loss translation/localization lemma and applies it to close the exact-coloop part of the current heavy-row angular-cancellation endpoint. It does not rotate the independent coordinates, invoke pointwise van-der-Corput decay, use the false arbitrary-joint coarea statement, assume moments/support bounds, or normalize individual fragments.

## 1. Fresh source state and premises


Corrections consumed include the law-uniform pointwise quadratic-phase counterexample, the failure of positive moments of worst conditional projection caps, the failure of bounded-diameter/fixed-fragment localization, and the failure of selecting one universally good physical minor. The proof below retains the original product coordinates through every conditioning step.

The immediate analytic frontier used here is fleet03/B03 r27,

`yspennstate/math-open-problems@b580b09027d8c20c3d3bbea0bea6cf8caa04d541`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T045638Z-fleet03-B03-QFORM-r27/REPORT.md`.

Its heavy-right-plane packet has

`Q = a^{-1} H^2 + 2 sigma U V`,                                      (1.1)

with

`H = a X_i + h_L.X_L + h_R.X_R + h_K.X_K`,
`U=u.X_L`, `V=v.X_R`,                                                (1.2)

where `u,v` are unit vectors on disjoint original-coordinate banks and

`h_R = beta v + m q`,                                                (1.3)

with `q` unit, `q perp v`, `m>0`. In the current one-sided endpoint,

`m=rho y`, `y^2>1/2`, `rho^2=a^2+||k||^2`,
`gamma=rho^2/|a|`, `gamma |sigma| >= s_3(A)^2`.                     (1.4)

A heavy physical row `r in R` satisfies

`eta_r=v_r^2+q_r^2>1/2`,                                             (1.5)

and B03 r27 proves, whenever `h_r:=beta v_r+m q_r !=0`,

`||p_Q||_infinity
 <= (16 sqrt(60)/s_3(A)) sqrt(rho/|h_r|).`                           (1.6)

Thus the first unpaid state is angular cancellation `|h_r|/rho ->0`, including `h_r=0`.

Two completed supporting results are used at actual inequalities:

1. fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical
   `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`.
   Its one-dimensional consequence is: if `c` is a coefficient vector and `Y_j` are independent cap-one variables, then the scalar projection `c.Y` has density cap at most

   `sqrt(e)/||c||_2`.                                                 (1.7)

2. **Designated partner fleet04/B14**, affine-mixture localization, canonical
   `yspennstate/math-open-problems@19d9434e07142e6b9fe19b4a88bbd46ccec8eeee`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260923T001323Z-fleet04-B14-affine-mixture-compiler-r5/REPORT.md`.
   For a fixed original-coordinate quadratic core, any interval estimate uniform in all affine parameters transfers with the identical constant from compact finite-fragment cap-one product inputs to arbitrary cap-one product laws and arbitrary outside tails/couplings. Singular cores are allowed; kernel-affine leakage is retained rather than silently translated away.

## 2. A scalar square-linear localization lemma

The following lemma is the new B14 contribution. It is deliberately stated with arbitrary outside state, because that is what makes it useful after physical-coordinate conditioning.

### Theorem 2.1 — `QFORM-SQUARE-LINEAR-COLOOP-LOCALIZATION-v1`

Let

- `Z` be a real random variable with probability density `f_Z<=1`;
- `Y=(Y_1,...,Y_N)` have independent cap-one coordinates and be independent of `Z`;
- `Omega` be an arbitrary random state independent of `(Y,Z)`;
- `U=U(Omega)` have a density bounded by `L<infinity`;
- `S=h.Y`, `h!=0`, have a density bounded by `M<infinity`;
- `xi=xi(Omega)` and `F=F(Omega)` be arbitrary measurable real functions.

For real constants `A,d,alpha,c,b` with `A d !=0`, define

`Delta=b-c alpha`                                                     (2.1)

and assume `Delta!=0`. Put

`T = A(S+alpha Z+xi)^2 + 2d U(cS+bZ) + F`.                           (2.2)

Then `T` has an essentially bounded density and

`boxed:
 ||p_T||_infinity
 <= 4 sqrt(2) M sqrt(L) / sqrt(|A d Delta|).
`                                                                          (2.3)

The same estimate holds as an interval inequality

`P(T in J)<= [4 sqrt(2) M sqrt(L)/sqrt(|A d Delta|)] |J|`             (2.4)

for every interval `J`. No support radius, moment, centering, connectedness, fragment-count, or fragment-separation assumption occurs.

### Proof

Fix an outside state `omega` and abbreviate `u=U(omega)`, `xi=xi(omega)`, `F=F(omega)`. Set

`r=d c u/A`.                                                         (2.5)

A direct completion in the **scalar product coordinate `S`** gives the exact identity

`A(S+alpha Z+xi)^2 +2d u(cS+bZ)+F`
`= A(S+alpha Z+xi+r)^2`
`  +2d u(b-c alpha)Z`
`  +F-2d c u xi-d^2 c^2 u^2/A`.                                     (2.6)

Thus every arbitrary outside shift is retained exactly; the only physical transversality parameter is `Delta=b-c alpha`.

For fixed `omega,z`, the random variable

`A(S+s_0)^2`                                                         (2.7)

has density bounded pointwise on its supported side by

`M/(sqrt(|A|)|w|^(1/2))`.                                            (2.8)

Indeed the two inverse branches of the square each contribute at most `M/(2 sqrt(|A||w|))`.

Consequently, writing all terms in (2.6) not involving `Z` as a shift,

`p_(T|Omega=omega)(t)
 <= M/sqrt(|A|) * E_Z |t-c_0-2d u Delta Z|^(-1/2).`                  (2.9)

For every cap-one probability density and every real center `z_0`, the one-dimensional rearrangement inequality gives

`int f_Z(z)|z-z_0|^(-1/2) dz
 <= int_{-1/2}^{1/2}|z|^(-1/2)dz
 =2 sqrt(2).`                                                        (2.10)

Hence, for `u!=0`,

`p_(T|Omega=omega)(t)
 <= 2 M /[sqrt(|A d Delta|) sqrt(|u|)].`                              (2.11)

The exceptional event `U=0` has probability zero because `U` has a density. Averaging over `Omega` remains legitimate even though `xi,F,U` may be arbitrarily dependent. The same rearrangement argument at density cap `L` yields

`E |U|^(-1/2)
 <= L int_{-1/(2L)}^{1/(2L)} |u|^(-1/2)du
 =2 sqrt(2L).`                                                       (2.12)

Combining (2.11)-(2.12) proves (2.3).

To make the rough-law localization step explicit, first prove (2.9)-(2.11) on compact finite-fragment active inputs `(Y,Z)`. For every fixed outside state `omega`, (2.6) is a fixed original-coordinate quadratic core plus an arbitrary affine term. Applying the completed **fleet04/B14 affine-mixture localization theorem** gives the actual same-constant inequality

`P(T in J | Omega=omega)
 <= [2M/(sqrt(|A d Delta|)sqrt(|u|))] |J|`                            (2.13)

for arbitrary cap-one product laws on `(Y,Z)`, with no tail/fragment tax. Integrating (2.13) and then using (2.12) gives (2.4). This is the designated-partner result applied to an equation, not merely cited as background. `QED`

### Product-law corollary

If both `S=h.Y` and `U=u.X_L` arise from disjoint original-coordinate product banks with `||u||_2=1`, then (1.7) gives

`M<=sqrt(e)/||h||_2`, `L<=sqrt(e)`.                                  (2.14)

Therefore

`boxed:
 ||p_T||_infinity
 <= 4 sqrt(2) e^(3/4)
    /[ ||h||_2 sqrt(|A d Delta|) ].
}`                                                                          (2.15)

This form is entirely translation invariant and uniform over arbitrary fragmented or unbounded input supports.

## 3. Exact-coloop geometry

Return to the B03 r27 right-plane packet. Remove the heavy physical row `r` and write

`h_R=(h_r,h_-)`, `v=(v_r,v_-)`.                                      (3.1)

Assume the exact **coloop condition**

`rank [h_-,v_-] <=1`.                                                (3.2)

In the angular-cancellation branch below, `h_-!=0`, so there is a scalar `c` with

`v_-=c h_-`.                                                         (3.3)

Let

`H=||h_-||_2`.                                                        (3.4)

Because `h_R=beta v+m q` with `v,q` orthonormal,

`||h_R wedge v||_2=m`.                                               (3.5)

Under (3.3) the two vectors live in the physical two-plane generated by row `r` and `h_-/H`; therefore

`boxed: H |v_r-c h_r| = m.`                                         (3.6)

This is exactly the transversality quantity occurring in Theorem 2.1:

`Delta=v_r-c h_r`, so `H|Delta|=m`.                                  (3.7)

No reciprocal individual cross minor appears.

A second elementary consequence is

`m=|H v_r-h_r ||v_-||_2 * sign|`
` <= H+|h_r|`,                                                       (3.8)

because `|v_r|<=1` and `||v_-||<=1`. Hence

`boxed: H>=m-|h_r|.`                                                 (3.9)

## 4. Application to the heavy angular-cancellation endpoint

Rewrite (1.1) by taking

`Z=X_r`,
`S=h_-.X_{R\{r}}`,
`Omega=(X_i,X_L,X_K)`,
`U=u.X_L`,
`A=1/a`, `d=sigma`,
`alpha=h_r`, `b=v_r`.                                                (4.1)

All remaining pieces of `H` become the arbitrary outside shift `xi(Omega)`, and any scalar outside term is absorbed into `F(Omega)`. Under the coloop condition (3.3), the residual bilinear projection is exactly `cS`, so Theorem 2.1 applies.

By (2.15) and (3.7),

`||p_Q||_infinity
 <= 4 sqrt(2)e^(3/4)
    /sqrt( |sigma/a| H m ).`                                        (4.2)

Now fix any `theta` with `0<theta<1/sqrt(2)` and consider the angular-cancellation subbranch

`|h_r|<theta rho`.                                                    (4.3)

Since `m=rho y`, `y>1/sqrt(2)`, (3.9) gives

`H>=rho(y-theta)`.                                                   (4.4)

Therefore

`H m >=rho^2 y(y-theta)`.                                           (4.5)

The exact spectral identity from B03 r27 gives

`|sigma/a| rho^2 = gamma |sigma| >=s_3(A)^2`.                        (4.6)

Substituting (4.5)-(4.6) into (4.2),

`boxed:
 ||p_Q||_infinity
 <= [4 sqrt(2)e^(3/4)]
    /[s_3(A) sqrt(y(y-theta))].
}`                                                                          (4.7)

This is stable as `h_r->0`; it explicitly closes the endpoint at which the B03 reciprocal-`sqrt(|h_r|)` estimate diverges.

### A universal exact-coloop constant

Take

`theta=2/3 <1/sqrt(2)`.                                              (4.8)

On the cancellation side, using `y>=1/sqrt(2)`,

`||p_Q||_infinity
 <= 4 sqrt(2)e^(3/4)
    /sqrt[(1/sqrt(2))(1/sqrt(2)-2/3)]
 =70.8185713165... /s_3(A).`                                        (4.9)

On the complementary side `|h_r|>= (2/3)rho`, B03 r27 (1.6) gives

`||p_Q||_infinity
 <=16 sqrt(60/(2/3))/s_3(A)
 =48 sqrt(10)/s_3(A)
 =151.7893276881.../s_3(A).`                                        (4.10)

Combining the two sides proves:

### Theorem 4.1 — `QFORM-HEAVY-RIGHT-PLANE-COLOOP-CLOSURE-v1`

In the fleet03/B03 r27 one-sided exact-rank-three heavy-right-plane packet, if deleting the heavy row `r` leaves the two right-plane coefficient vectors collinear, then

`boxed:
 ||p_Q||_infinity <= 48 sqrt(10)/s_3(A).
}`                                                                          (4.11)

Under the owner normalization `s_3(A)>=1`, this is the universal bound

`||p_Q||_infinity <=48 sqrt(10)<151.790`.                            (4.12)

The estimate holds for arbitrary cap-one product laws, arbitrary translations, unbounded supports, arbitrarily distant fragments, and no moment assumptions. Essential boundedness is proved; continuity is **not** claimed by this argument.

## 5. Why this is not a disguised easy subclass

The B03 heavy-row theorem already paid every state with a non-cancelled physical square coefficient but diverged as `h_r->0`. The new theorem attacks exactly that first missing implication in a structural endpoint of the same branch. The important algebra is that the vanishing square coefficient does not destroy all transversality: under the coloop geometry, completing the residual `cS` term converts the surviving transversality into

`H|Delta|=m`,                                                        (5.1)

and the physical scalar `Z` then supplies a translation-uniform `|U|^{-1/2}` smoothing factor. Both singular kernels are integrable because the source variables retain genuine density caps. No post-rotation independence is invented.

The result also shows why fragment geometry is irrelevant at this endpoint: every use of a density cap is rearrangement/mixture stable and depends only on total probability mass, not support diameter or connectedness.

## 6. Remaining full-target debt

The unrestricted three-large-eigenvalue conjecture remains OPEN. This report closes only the **exact-coloop** part of the heavy-row angular-cancellation branch.

The next B14 target is the quantitative **near-coloop/non-coloop angular-cancellation** state. Writing

`v_-=c h_-+w`, `w perp h_-`,                                        (6.1)

completion leaves the additional coupled term `2 sigma U(w.X_{R\{r}})`. The present scalar argument cannot simply condition on that projection because it is dependent on `S=h_-.X`; doing so would reintroduce precisely the conditional-cap failure prohibited by the live corrections. A valid continuation must aggregate the two-dimensional residual product bank before taking any fiber supremum, likely by splicing the grouped-hub Fourier-Brascamp--Lieb theorem with the physical-row receiver.

Thus the exact new frontier is:

`QFORM-HEAVY-ROW-NEAR-COLOOP-AGGREGATE-v1`:

> obtain a bound stable jointly in `h_r->0` and in the residual transverse area `||h_- wedge v_-||`, using the original product bank before conditioning; combine it with the exact-coloop estimate (4.11) and the diffuse-plane estimate to remove the remaining heavy-row angular-cancellation obstruction.

## 7. Quantitative checks

The constants were checked independently from the symbolic inequalities:

- `1/sqrt(2)=0.7071067811865475`;
- `theta=2/3=0.6666666666666666`;
- cancellation constant in (4.9): `70.81857131649502`;
- complementary B03 constant: `16 sqrt(90)=48 sqrt(10)=151.7893276880822`.

These numerical values are diagnostics only; the proof is the exact chain (2.6)-(4.11).

## 8. Claim status

- `QFORM-SQUARE-LINEAR-COLOOP-LOCALIZATION-v1`: **PROVED in stated scope**.
- `QFORM-HEAVY-RIGHT-PLANE-COLOOP-CLOSURE-v1`: **PROVED in stated scope**, conditional on the source-pinned B03 r27 packet and source-pinned scalar projection theorem.
- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuous density: **OPEN**.
- Execution: **WITHOUT_VERIFIED_BRAIN**; repository retrieval/writeback is not native learned-memory ingestion.
