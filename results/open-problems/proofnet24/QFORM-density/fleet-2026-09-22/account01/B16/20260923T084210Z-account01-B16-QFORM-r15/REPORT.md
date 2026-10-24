SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T08:42:10Z.
attacking: rank-two grouped cross-bank density closure with determinant rather than smallest-singular-value payment, then apply it to the latest account02/B16 nonaligned obstruction family.

# account01/B16 r15 — determinant grouped bilinear projection-product closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Projection-product interaction  
Status: `NEW SUPPORTING ANALYTIC THEOREM + DESIGNATED-PARTNER APPLICATION / FULL QFORM OPEN`  
Continuity: not claimed by the theorem below; essential boundedness only.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh scope and source pins

Fresh owner control was re-resolved on `yspennstate/math-research-brain@6e799fa5db4ada5ce47eae56067a881c8c1c2361`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM only. The live QFORM status remains `FULL_CONJECTURE_OPEN`; the arbitrary-joint coarea gate, positive conditional projection-height moment gate, post-rotation independence, and worst-fiber-normalization shortcuts remain forbidden.

The completed source theorem strengthened here is account03/B01 `QFORM-GROUPED-BILINEAR-2D-RECEIVER-v1`, canonical report

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T033250Z-r23/REPORT.md`.

It proves, for two disjoint original-coordinate product banks, a direct density bound after aggregating a two-dimensional bank before inversion. Its stated bound pays a determinant on one side and the smallest singular value on the still-random side.

The designated partner consumed in this run is account02/B16 r27, canonical source

`yspennstate/math-open-problems@60079077a1035516fb0f88477c4eda71fbad8ca1`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T073515Z-account02-B16-QFORM-r27/REPORT.md`,

blob `fee8ac84e4a9b53f2a5bd7aad5a91b2629ba50b6`.

Its theorem `QFORM-RANK1-NONALIGNED-SLICE-WIENER-BARRIER-v1` gives a target-valid family for which a natural slice-Wiener interface is infinite even for arbitrarily weak rank-one nonalignment. The family is not a QFORM counterexample. Section 5 below pays that exact family by a different original-product inequality.

The product-projection inputs used are the source-validated consequences already recorded in the fleet:

1. for any coefficient vector `v`, a normalized one-dimensional projection of independent cap-one coordinates has density at most `sqrt(2)`, i.e.

`||p_(v^T X)||_infinity <= sqrt(2)/||v||_2`;

2. for any rank-two real matrix `M`,

`||p_(M X)||_infinity <= 2/sqrt(det(M M^T))`.

These are applied only to genuine original-coordinate product banks.

## 2. Determinant inverse-radius upgrade

Partition the ORIGINAL independent coordinates into mutually disjoint banks `I,J,D,W`. Let

`U=M X_I+a(X_W) in R^2`,
`V=N X_J+b(X_W) in R^2`,

where `M` and `N` have rank two. Let `H=H(X_I,X_D,X_W)` be any finite measurable real function. Thus the entire `I`-side curvature and all `D,W` dependence may be retained in `H`; the only structural requirement is that the untouched `J` bank enters the active interaction linearly through `V`.

Let `C` be an invertible real `2 x 2` matrix and set

`Q=2 U^T C V+H`.                                                 (2.1)

Write

`Delta_M=det(MM^T)>0`,
`Delta_N=det(NN^T)>0`.                                          (2.2)

### Theorem 2.1 — `QFORM-GROUPED-BILINEAR-DETERMINANT-RECEIVER-v1`

Under (2.1)-(2.2), `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(pi) [Delta_M Delta_N]^(-1/4) |det C|^(-1/2).`        (2.3)

This is determinant/determinant currency. In particular it improves the earlier account03/B01 bound whenever the still-random cross bank is strongly anisotropic: no factor `sigma_min(N)^(-1)` remains.

### Proof

Condition on `(X_I,X_D,X_W)`. Then `U=u`, `H=h`, and `b=b(X_W)` are deterministic, while the untouched `X_J` coordinates retain their original independence and cap-one densities. For `u!=0`,

`2 u^T C V+h
 =2 (N^T C^T u)^T X_J + constant`.

The one-dimensional product-projection theorem therefore gives the conditional density bound

`p_(Q | X_I,X_D,X_W)(q)
 <= sqrt(2)/[2 ||N^T C^T u||]
 =1/[sqrt(2) sqrt(u^T G u)]`,                                   (2.4)

where

`G=C N N^T C^T`                                                  (2.5)

is positive definite. The event `u=0` has probability zero because, conditional on `X_W`, `U` has a two-dimensional density.

Now condition only on `X_W=w`. The two-dimensional product-marginal theorem gives

`||p_(U|X_W=w)||_infinity <= K_M:=2/sqrt(Delta_M)`              (2.6)

uniformly in the translation `a(w)`. Put

`Y=G^(1/2) U`.

Since

`det G=(det C)^2 Delta_N`,                                      (2.7)

the conditional density of `Y` is bounded by

`K_Y <= K_M/sqrt(det G)
     =2/[sqrt(Delta_M Delta_N)|det C|]`.                        (2.8)

For every probability density `rho<=K` on `R^2`, layer cake gives the exact dimension-two inverse-radius estimate

`E |Y|^(-1)
 =int_0^infinity P(|Y|<1/s) ds
 <=int_0^infinity min(1,pi K s^(-2)) ds
 =2 sqrt(pi K).`                                                (2.9)

Apply (2.9) to (2.8):

`E[(u^T G u)^(-1/2) | X_W=w]
 <=2 sqrt(2 pi) [Delta_M Delta_N]^(-1/4)|det C|^(-1/2).`        (2.10)

Average (2.4) and use (2.10). The factor `1/sqrt(2)` cancels, yielding exactly

`||p_Q||_infinity
 <=2 sqrt(pi)[Delta_M Delta_N]^(-1/4)|det C|^(-1/2).`

The bound is uniform in `q` and in `w`, so averaging the outside conditioning completes the proof. QED.

## 3. Why this is a genuine projection-product result

The argument does not use a bounded joint projection density as a substitute for an indefinite level-set estimate. It uses the product provenance twice and in different dimensions:

- the untouched `J` bank gives the actual one-dimensional linear-projection cap in (2.4);
- the conditioned `I` bank gives the actual two-dimensional product-projection density cap in (2.6), after which the singularity is only `1/|y|`, integrable in dimension two.

The nonlinear remainder `H` may depend arbitrarily on the entire conditioned `I` bank; it is just a target translation after conditioning. Thus one full side of the quadratic form may retain arbitrary same-bank curvature. What is not allowed is arbitrary nonlinear curvature involving the still-random `J` bank.

This also explains why the crude rank-two cross Fourier estimate reaching only a `|t|^{-1}` endpoint is not decisive: direct real-space aggregation pays the inverse-radius singularity before absolute Fourier integration.

## 4. Useful normalized corollaries

If both grouped maps are orthonormal two-dimensional projections,

`MM^T=NN^T=I_2`,

then

`boxed: ||p_Q||_infinity <=2 sqrt(pi)|det C|^(-1/2).`           (4.1)

If `C=I_2`, the universal constant is

`2 sqrt(pi)=3.544907701811...`.

More generally the only geometric cross currency is

`[Delta_M Delta_N det(C)^2]^(1/4)`,                             (4.2)

the geometric mean of the two two-dimensional bank areas and the cross determinant. No individual physical entry, local reciprocal minor, or smallest singular value is paid.

## 5. Designated partner r27 applied to an actual inequality

Account02/B16 r27 defines independent cap-one source variables `X_h,Y_0,Y_1,Y_2,X_1,...,X_4` and the cube-bank projections

`L=(X_1+X_2+X_3+X_4)/2`,
`V_c=(X_1+X_2-X_3-X_4)/2`,
`T=(X_1-X_2)/sqrt(2)`,

with target-valid quadratic family

`Q_epsilon
 =2 X_h(L+Y_0)+2 V_c Y_1+2 epsilon T Y_2`.                    (5.1)

The partner proves that its proposed mixed slice-Wiener quantity is infinite for every `epsilon>0`; this is a mechanism obstruction, not a density blowup.

Apply Theorem 2.1 by taking the conditioned/curved bank

`I={Y_0,X_1,X_2,X_3,X_4}`,

and

`U=(Y_0+L, V_c)=M X_I`.                                         (5.2)

The two coefficient rows are orthogonal with squared norms `2` and `1`, hence

`MM^T=diag(2,1)`,
`Delta_M=2`.                                                     (5.3)

Take the untouched linear bank

`J={X_h,Y_1}`,
`V=(X_h,Y_1)`,
`N=I_2`,
`Delta_N=1`,                                                     (5.4)

and put `D={Y_2}`. The weak nonaligned term

`H=2 epsilon T Y_2`                                              (5.5)

is an arbitrary same-side/D-bank remainder of the exact kind allowed in Theorem 2.1. With `C=I_2`, (2.3) gives

`boxed:
 ||p_(Q_epsilon)||_infinity
 <=2 sqrt(pi) 2^(-1/4)
 =2^(3/4) sqrt(pi)
 =2.980900178858...`                                            (5.6)

for every real `epsilon`, including `epsilon=0`, and for arbitrary independent cap-one source laws, not merely the uniform cubes used by the partner to expose the Wiener barrier.

This is the requested equation-level use of the completed designated-partner result. The exact same family on which the broad slice-Wiener interface is infinite is uniformly paid by aggregate-before-inversion product geometry, with a constant below three.

## 6. Relation to the current near-coloop debt

The partner r27 conclusion remains correct: a generic arbitrary-nonaligned slice-Wiener transducer cannot be the missing near-coloop bridge. Theorem 2.1 identifies a positive structural replacement:

> if the semi-aligned near-coloop geometry can expose two disjoint original-coordinate banks carrying a rank-two cross interaction, with one whole bank entering linearly after conditioning the other side, then the branch is paid by determinant currency and arbitrary same-side leakage may remain in `H`.

The unresolved implication is therefore narrower:

`QFORM-NEAR-COLOOP-TWO-BANK-DETERMINANT-OR-CURVED-BICORE-v1`:
from the strict exact-rank-three near-coloop coefficient identities, either produce such a disjoint rank-two grouped receiver with

`Delta_M Delta_N det(C)^2 >= c_0>0`,

or route the residual to the already-paid two-sided-curved bicore / capped-basis / ridge / physical-pair exits.

A generic near-coloop frame need not visibly provide this partition, and self-curvature on BOTH active grouped banks remains outside Theorem 2.1. Those are real remaining structural debts; no full-QFORM completion is claimed.

## 7. Corrections and status

Preserved corrections include: no law-uniform scalar pointwise Fresnel decay; no independence after spectral rotation; no arbitrary-joint indefinite coarea bound from density cap alone; no positive conditional projection-height moment; no worst-fiber normalization; no deletion of small coefficients for arbitrary unbounded laws. The proof above avoids all of them.

`QFORM-GROUPED-BILINEAR-DETERMINANT-RECEIVER-v1`: PROVED supporting analytic theorem.

Partner family (5.1): uniformly paid by (5.6), despite the partner's slice-Wiener obstruction.

Full QFORM: OPEN / NOT PROVED / NOT DISPROVED.

Continuous density in the full target: OPEN. The theorem establishes an essentially bounded density in its stated branch but does not by itself prove continuity.
