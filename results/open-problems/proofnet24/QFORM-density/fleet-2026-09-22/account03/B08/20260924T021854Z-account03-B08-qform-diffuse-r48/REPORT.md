SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T02:18:54Z.
attacking: the near-rank-one aligned carrier by a product-safe tangent shear that converts every indefinite rank-two carrier/twist triple into an exact one-hub/one-child mixed-Fresnel configuration without dividing by the physical pivot.

# account03/B08 r48 — tangent-shear receiver for indefinite rank-two aligned carriers

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / quantitative inequalities and rigorous computations  
Run: `20260924T021854Z-account03-B08-qform-diffuse-r48`  
Status: **NEW SUPPORTING THEOREM / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains OPEN. The new point is an exact algebraic reduction for the aligned two-arm state that remains useful when `det R` is very small but nonzero: a large physical diagonal twist can compensate a near-rank-one carrier. No scalar Schur division by the possibly cancelled physical diagonal `a_j` is used.

## 1. Source-valid inputs

Fresh startup control was `yspennstate/math-research-brain@d54104c32ea9811a4910dbe56cf452a3b435093c`, OWNER CONTROL revision `2026-09-22.15`, QFORM only. The live correction boundary was reread. In particular this report does not use law-uniform pointwise quadratic-phase decay, rotated independence, arbitrary-joint coarea, worst-fiber sup integration, or deletion of a small quadratic coefficient error.

The immediate predecessor is account03/B08 r47,
`yspennstate/math-open-problems@8e77db5a814feaec39c26d72782c66de6ee1d721`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T012032Z-account03-B08-qform-diffuse-r47/`.
It established the product-safe triangular-shear interface and the exact rank-one carrier receiver.

The analytic receiver used below is account03/B08 r37,
`yspennstate/math-open-problems@58b2a0752f409dd48ae5e39851ac84f13be4470b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T122051Z-account03-B08-qform-diffuse-r37/REPORT.md`.
Its one-hub/one-child specialization states that for a physical light block `D+lambda ss^T`, a retained physical hub-light vector `g`, transverse component `h=(I-ss^T)g`, and augmented physical row leverage

`max_k (s_k^2+h_k^2/||h||^2) <= 1/2`,

the full conditional form has a continuous `C_0` density satisfying

`||p||_infinity <= 3*4^(2/3) |lambda|^(-1/3) ||h||^(-2/3)`.   (1.1)

As in r47, a triangular translation of the hub density by a measurable linear function of the light variables is admissible: after the Jacobian-one change the hub factor remains pointwise at most one, and the source proof uses only that cap in the hub integration while the light variables retain their original product density.

The designated partner theorem actually applied below is account04/B08 r2,
`yspennstate/math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T212412Z-account04-B08-QFORM-r2/REPORT.md`.
For an ORIGINAL-coordinate deletion child `C`, if `s_3(C)>=m` and the physical spectral projection onto `|lambda(C)|>=m/64` has maximum diagonal at most `1/32`, then the parent output is continuous `C_0` and

`||p_Q||_infinity < 64/m`.                                      (1.2)

## 2. Aligned rank-two carrier normal form

Work in the exact original-coordinate aligned state

`A = [[B,M],[M^T,M^T R M + D]]`,                               (2.1)

where `B` is arbitrary symmetric `2x2`, `M in R^(2xm)` has row rank two, `R` is invertible symmetric `2x2`, and `D=diag(d_1,...,d_m)` is an arbitrary physical diagonal matrix. Put

`G=MM^T`, `ell_j=m_j^T G^(-1)m_j`, `mu=max_j ell_j`,             (2.2)

where `m_j` is the `j`th column of `M`.

Fix a physical light coordinate `j` with `d:=d_j != 0`. Write `z=X_j`, `y=X_{-j}`, `m=m_j`, and `N=M_{-j}`. Condition on the two ORIGINAL hub coordinates. Their entire contribution becomes affine/constant in `(z,y)` and is harmless for the source theorem.

The non-diagonal part of the remaining light polynomial is

`d z^2 + (m z + N y)^T R (m z + N y)`.                          (2.3)

Define

`a=d+m^T R m`, `r=R m`,
`K=[[a,r^T],[r,R]]`.                                             (2.4)

The elementary congruence

`d z^2 + (u+m z)^T R (u+m z)`

shows that `K` is congruent to `diag(d,R)`. Hence

`det K = d det R`                                                (2.5)

and `K` is indefinite exactly when the three-dimensional parameter form `diag(d,R)` is indefinite.

## 3. Tangent-shear lemma

### Lemma 3.1 — an indefinite nondegenerate 3D form has a product-safe tangent graph

Assume `K` from (2.4) is indefinite. Since `d det R != 0`, it is nondegenerate. There exists an isotropic vector `w=(w_0,w_u) in R x R^2` such that

`w^T K w=0`, `h_0 != 0`, where `h:=K w=(h_0,h_u)`.               (3.1)

Indeed the null cone of a nondegenerate indefinite real three-dimensional quadratic form spans all of `R^3`: after a real congruence to signature `(2,1)` or `(1,2)`, four elementary null vectors already span. If the functional `v -> e_0^T K v` vanished on every null vector, it would vanish on all of `R^3`, contradicting invertibility of `K`.

Set

`c=h_u/h_0`.                                                     (3.2)

Then the tangent plane `w^{perp_K}` is exactly the graph

`W_c={(-c^T u,u):u in R^2}`.                                    (3.3)

Make the triangular physical change

`z=z' - c^T N y`.                                                (3.4)

It has Jacobian one. The original factor `f_j(z)` becomes `f_j(z'-c^TNy)<=1`; the other light factors remain their original independent product law.

Under (3.4), (2.3) becomes

`a z'^2 + 2 z' g^T N y + y^T N^T R_c N y + y^T D_{-j} y`,       (3.5)

where

`g=r-a c`,
`R_c=R-r c^T-c r^T+a c c^T`.                                   (3.6)

Because `W_c=w^{perp_K}` and `w` is isotropic, the restriction of `K` to `W_c` has radical `span(w)`. Therefore

`rank R_c = 1`.                                                  (3.7)

This is the key reduction: one physical coordinate becomes the single hub and the residual non-diagonal light curvature becomes exactly one child direction.

## 4. Exact determinant-to-Fresnel currency identity

Choose a Euclidean orthonormal basis `(v,k)` of the two-dimensional carrier parameter space so that

`R_c=lambda v v^T`, `k in ker R_c`, `lambda != 0`.               (4.1)

In coordinates `(z',v,k)`, the parameter matrix is

`[[a,g_v,g_k],[g_v,lambda,0],[g_k,0,0]]`.

Consequently

`|lambda| |g_k|^2 = |det K| = |d det R|`.                        (4.2)

Now pass back to the actual physical light bank. Put

`s_raw=N^T v`, `s=s_raw/||s_raw||`,
`lambda_phys=lambda ||s_raw||^2`,
`g_phys=N^T g`,
`h_phys=(I-ss^T)g_phys`.                                        (4.3)

Because `N` has row rank two, the Gram-determinant identity gives

`||s_raw||^2 ||h_phys||^2
 = det(NN^T) det[v,g]^2
 = det(NN^T) |g_k|^2`.                                          (4.4)

Combining (4.2)-(4.4),

`boxed: |lambda_phys| ||h_phys||^2
       = |d det R| det(NN^T).`                                  (4.5)

This identity is exact. It contains no reciprocal physical pivot and no approximation in the near-rank-one limit.

## 5. Diffuse leverage is inherited exactly after deleting the twist coordinate

The two physical vectors `s` and `h_phys/||h_phys||` span `row(N)`. Hence their augmented physical row leverage is exactly the row leverage of the deleted arm `N`.

The matrix determinant lemma and Sherman-Morrison give

`det(NN^T)=det(G)(1-ell_j)`,                                    (5.1)

and for every `k != j`,

`ell_k^(-j) <= ell_k/(1-ell_j) <= mu/(1-mu)`.                   (5.2)

Therefore `mu<=1/3` implies every augmented row leverage is at most `1/2`, exactly the r37 gate.

## 6. Main theorem

### `QFORM-RANK2-INDEFINITE-TANGENT-SHEAR-v1`

Assume (2.1), `rank M=2`, `R` invertible, `mu<=1/3`, and choose a physical light coordinate `j` with `d_j!=0` such that `diag(d_j,R)` is indefinite. Then for every independent cap-one product input the full quadratic form has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= 3*4^(2/3)
    [ |d_j det R| det(M_{-j}M_{-j}^T) ]^(-1/3).
`                                                                   (6.1)

Using (5.1),

`boxed:
 ||p_Q||_infinity
 <= 3*4^(2/3)
    [ (1-ell_j)|d_j| |det R| det(MM^T) ]^(-1/3).
`                                                                   (6.2)

In particular, under `mu<=1/3`,

`boxed:
 ||p_Q||_infinity
 <= 8.653498
    [ |d_j| |det R| det(MM^T) ]^(-1/3).
`                                                                   (6.3)

**Proof.** Sections 3-5 produce, by a triangular translation of the single original physical coordinate `j`, an exact one-hub/one-child instance of the r37 mixed-Fresnel theorem. The augmented row leverage is at most `1/2`; equation (4.5) is precisely its product currency `|lambda_phys| ||h_phys||^2`. Substitution into (1.1) gives (6.1). Equations (5.1) and `1-ell_j>=2/3` give (6.2)-(6.3). The source characteristic-function majorant is integrable, hence the density is continuous and vanishes at infinity. QED.

## 7. Scale form: a large twist can compensate an arbitrarily small nonzero carrier determinant

Define the rank-two carrier area currency

`P_2 := |det R| det(MM^T)`.                                     (7.1)

If at target scale `L>0`

`|d_j| P_2 >= xi L^3`                                          (7.2)

and the hypotheses of Theorem 6 hold, then

`boxed: ||p_Q||_infinity <= 8.653498 xi^(-1/3) L^(-1),
       p_Q in C_0(R).`                                          (7.3)

This is useful specifically in the near-rank-one chamber. The completed account02/B08 r30 Strichartz receiver has a fixed lower gate on `P_2` itself. By contrast, (7.3) allows `P_2/L^2 -> 0` provided a physical twist grows so that `|d_j|P_2` remains of order `L^3`. Thus a small nonzero second carrier eigenvalue is not by itself an obstruction in the indefinite twist geometry.

The exact `det R=0` endpoint is not obtained by taking a limit in (6.1); it is covered separately by r47's exact rank-one theorems. No continuity-in-coefficients argument is used.

## 8. Designated account04/B08 result applied to the same physical coordinate

Delete the same ORIGINAL coordinate `j` from the parent matrix and denote the child by `C_j`. Apply account04/B08 r2 with `m=L/64`. If

`s_3(C_j)>=L/64`                                                (8.1)

and the physical spectral projection of `C_j` onto

`|lambda(C_j)|>=L/4096`

has maximum diagonal at most `1/32`, then the partner theorem gives the actual inequality

`boxed: ||p_Q||_infinity < 4096/L, p_Q in C_0(R).`              (8.2)

Therefore for any fixed `xi>0`, an unpaid diffuse indefinite aligned-carrier state at this coordinate must satisfy BOTH

`|d_j| |det R| det(MM^T) < xi L^3`                              (8.3)

and partner failure:

`s_3(C_j)<L/64`,                                                (8.4)

or an actual original child coordinate has high-window leverage

`max_k (P_{C_j}(|lambda|>=L/4096))_{kk}>1/32`.                  (8.5)

Compared with r47, the new residual now includes the entire nonzero near-rank-one side: if the determinant is small, its product with every usable indefinite physical twist must also be small before child loss/localization can survive.

## 9. Deterministic checks

The companion `CHECKS.py` generates nondegenerate indefinite random `K`, constructs an isotropic tangent graph exactly as in Section 3, and verifies:

1. `w^T K w=0`;
2. `det R_c=0`;
3. `|lambda| |g_k|^2=|d det R|`;
4. after a random full-row-rank physical map `N`,
   `|lambda_phys| ||h_phys||^2=|d det R| det(NN^T)`.

Over 1000 parameter tests and 1999 physical-map tests the observed maximum floating residuals were respectively `3.55e-14`, `5.97e-15`, `2.85e-14`, and relative physical-currency error `3.00e-14`. These are regression checks only; the proof above is analytic.

## 10. Remaining implication

The full conjecture and global continuity remain OPEN. The next B08 debt is now

`QFORM-WEAK-CARRIER-PRODUCT-PLUS-CHILDLOSS-LOCALIZED-COMPILER-v2`:

consume the state where both the exact-rank-one currency from r47 (when `det R=0`) or the new nonzero-determinant product currency (8.3) are weak, while the same original-coordinate deletion child either loses its third target-scale singular value or exhibits the explicit high-window localized coordinate. The same-sign definite parameter chamber is separately covered when the completed rank-two carrier/diagonal Strichartz gate applies; no claim is made here that the bare three-eigenvalue hypothesis forces that gate.

No counterexample is claimed.
