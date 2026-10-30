SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B19, 2026-09-23T19:27:51Z.
attacking: QFORM-FINITECORE-PHYSICAL-R2-FROBENIUS-COLLAR-PAYMENT-v1 by a tail-retaining two-sided scalar Schur compiler, then the exact-rank-two cross-null curvature endpoint through the completed dependent overlap-square theorem.

# fleet03/B19 r40 — two-sided Schur / overlap-square compiler for the finite-core rank-two collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **NEW SUPPORTING THEOREM + TWO NEW TARGET-LEVEL PAYMENTS / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Full-target continuity: **OPEN**. Continuity is proved only on the overlap-square payment and on the designated-partner branch explicitly identified below.

## 1. Source boundary and corrections


No step below uses post-rotation independence, an arbitrary-joint coarea bound, a conditional projection-density supremum, moment/support assumptions, law-uniform pointwise quadratic-phase decay, or deletion of a small nonzero quadratic/cross term as a random perturbation. Every conditioning operation is on ORIGINAL coordinates. Deterministic rotations are used only to describe a bounded-density joint projection after the product source has already been kept intact.

The current UTC hour already had the canonical fleet03/B19 login `20260923T190035Z-fleet03-B19-QFORM-r39`; it is preserved rather than overwritten. This r40 package has its own immutable mathematical/run records.

## 2. Current first missing branch inherited from fleet03/B19 r38

Source:

`yspennstate/math-open-problems@f09b670173440c4c511985c9a89baf38f97e82c1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T183023Z-fleet03-B19-QFORM-r38/REPORT.md`.

The finite-core compiler supplies disjoint ORIGINAL coordinate banks `H,L=H^c`, with

`|H|<=124`,
`C=A[H,L]`,
`s_3(C)<1/64`,
`s_1(C)s_2(C)>1/480`.                                             (2.1)

The r38 two-row compiler selects a literal pair `T={i_1,i_2} subset H` and writes

`M=A[T,L]`,
`S=sqrt(det(MM^T))`,                                              (2.2)

with

`S>1/(480 sqrt(7626))=2.3856699607287348e-5`.                    (2.3)

Let `Pi` project onto `row(M)` and

`rho=||A[H\T,L](I-Pi)||_F`.                                     (2.4)

If `rho>=1/64`, r38 already proves a continuous `C_0` density with `||p_Q||_infinity<743`. Hence the still-unpaid collar satisfies

`rho<1/64`.                                                       (2.5)

This run attacks (2.5), retaining the complete nonzero cross tail.

Two completed analytic inputs are used at their exact scopes.

1. **Two-sided scalar Schur endpoint.** `QFORM-TWOSIDED-SCHUR-2PLUS1-v1`, contained immutably at
   `yspennstate/math-open-problems@8d0cfcc9b0b1e88eee6fba2e63187d8607ca2d0c`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260922T144010Z-fleet02-B19-qform-r13/REPORT.md`.
   Its proof combines a genuine scalar square with a rank-two mixed residual and arbitrary same-side phases.

2. **Dependent overlap-square endpoint.** `QFORM-CROSS2-OVERLAP-SQUARE-L1-v1`, contained immutably at
   `yspennstate/math-open-problems@8103579cff840cf3e09607ac05841bd156fa8744`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/fleet01-B16-20260923T170732Z-auto11/REPORT.md`.
   For disjoint source banks, a rank-two cross pair plus a square in a third projection of the SAME source bank gives a continuous density; no independence inside that three-dimensional projection is assumed.

The source-valid near-null obstruction in fleet02/B06,
`yspennstate/math-open-problems@0d6e70139fe0f7d8ee22cc5210efb3b8d00a0bda`,
shows explicitly that a nonzero self block cannot be discarded merely because its operator norm is small. The present argument therefore never uses such a perturbative deletion.

## 3. New theorem: two-sided physical scalar pivot with an arbitrary product receiver bank

### Theorem 3.1 — `QFORM-TWOSIDED-SCHUR-2PLUS1-PRODUCTBANK-v1`

Let `X` be a real random variable with density cap `M_X`, let `U in R^2` have joint density cap `M_U`, and let `Y=(Y_j)_{j in J}` be an ORIGINAL-coordinate product bank with one-dimensional density caps one. Assume `X,U,Y` are mutually independent. Let

`Q = a X^2 + 2X(beta+r^T U+s^T Y)
     + F(U) + 2 U^T B Y + G(Y) + c`,                              (3.1)

where `a!=0`, `r in R^2`, `s in R^J`, `B` is a `2 x |J|` real matrix, and `F,G` are arbitrary measurable real functions for which (3.1) is defined. Put

`C = B-a^(-1) r s^T`.                                             (3.2)

Assume `rank(C)=2`, and let

`Delta=s_1(C)s_2(C)>0`.                                           (3.3)

Then the law of `Q` is absolutely continuous and

`boxed:
 ||p_Q||_infinity
 <= C_0 M_X (2 M_U)^(1/4) |a|^(-1/2) Delta^(-1/4),`               (3.4)

where

`C_0=3*2^(1/3)*sqrt(6)=9.258491065302312...`.                     (3.5)

No sign condition is imposed. Every additional singular direction/coupling on the product bank is retained inside `G`; only the two-dimensional row space of the Schur-corrected cross map is projected.

### Proof

Complete the square only in the genuinely independent scalar `X`:

`aX^2+2X(beta+r^T U+s^T Y)
 =a(X+a^(-1)(beta+r^TU+s^TY))^2
  -a^(-1)(beta+r^TU+s^TY)^2`.                                    (3.6)

The residual has the form

`S(U,Y)=F_1(U)+2U^T C Y+G_1(Y)`,                                  (3.7)

with arbitrary same-bank real functions `F_1,G_1`. Take an SVD

`C=P diag(s_1,s_2) V^T`,                                         (3.8)

where `P` is `2 x 2` orthogonal and `V` has two orthonormal columns in `R^J`. Put `U'=P^TU` and `W=V^T Y`. Orthogonal change in `U` preserves its joint density cap. The genuine product-projection theorem gives

`||p_W||_infinity<=2`.                                            (3.9)

Push the complex measure `exp(itG_1(Y))dP_Y` onto `W`; its complex density has modulus at most `p_W`. Likewise the `U'` amplitude has modulus at most `p_U`. Thus the two-dimensional mixed Plancherel calculation used in the source theorem applies verbatim and gives

`|psi_S(t)|
 <=min(1, pi |t|^(-1) Delta^(-1/2)(2M_U)^(1/2)).`                 (3.10)

The source proof converts (3.10) by inverse Hausdorff--Young to

`||p_S||_4
 <=2^(3/2)(2M_U)^(3/8) Delta^(-3/8).`                            (3.11)

For fixed `(u,y)`, the shifted scalar in (3.6) still has density cap `M_X`, so its square density is bounded by

`M_X |a|^(-1/2)|v|^(-1/2)`.                                      (3.12)

Averaging the conditional density and splitting the half-Riesz integral exactly as in the source theorem gives

`||p_Q||_infinity
 <=3*2^(1/3)*sqrt(6)
    M_X(2M_U)^(1/4)|a|^(-1/2)Delta^(-1/4)`,                       (3.13)

which is (3.4). This argument uses only the genuine independence of the three ORIGINAL source banks before completion. QED.

**Regularity note.** This theorem proves essential boundedness. I do not upgrade the source proof to a continuous representative here.

## 4. Application to the live finite-core collar: noncancelled physical pivots are paid

Keep the selected literal pair `T` and `M=A[T,L]` from Section 2. For every literal `k in H\T`, set

`a_k=A_kk`,
`r_k=A[T,k] in R^2`,
`s_k=A[k,L] in R^L`,                                              (4.1)

and for `a_k!=0` define the full, tail-retaining Schur-corrected cross matrix

`C_k^Sch=M-a_k^(-1) r_k s_k`,                                    (4.2)

with two-volume

`Delta_k=s_1(C_k^Sch)s_2(C_k^Sch)`                               (4.3)

when it has rank two.

Condition on every ORIGINAL coordinate in `H\(T union {k})`. Then `X_k`, the physical pair `X_T`, and the product bank `X_L` are mutually independent. The pair has joint density cap one, so Theorem 3.1 gives the actual full-law bound

`boxed:
 ||p_Q||_infinity
 <= C_0 2^(1/4)|a_k|^(-1/2)Delta_k^(-1/4).}`                      (4.4)

All conditioned values enter only affine/same-bank terms, so the bound is uniform and averages back to the full law.

At the live r38 scale, if for some `k`

`|a_k|>=1/64`,
`Delta_k>=S/2`,                                                   (4.5)

then using (2.3),

`||p_Q||_infinity
 < C_0 2^(1/4)*8*(2/S)^(1/4)
 =1498.7962785392776...<1499.`                                   (4.6)

This payment retains the entire nonzero `rho<1/64` cross tail. It therefore closes a genuine part of the first missing r38 collar which cannot be reached by pretending that the tail is zero.

Hence every still-unpaid collar state satisfies the explicit simultaneous Schur-cancellation condition

`boxed:
 for every k in H\T with |A_kk|>=1/64,
 rank(C_k^Sch)<2 or Delta_k<S/2.}`                                (4.7)

## 5. Exact rank-two endpoint: cross-null self curvature supplies the missing half-power

Now impose the exact endpoint

`rho=0`.                                                          (5.1)

Then every row of `A[H,L]` lies in `row(M)`, so for any `k in H\T`, the literal three-row cross block

`D_k=A[T union {k},L]`                                            (5.2)

has exact rank two. Let `u_k in R^3` be a unit vector spanning

`ker(D_k^T)`,                                                      (5.3)

and define its physical cross-null self curvature

`lambda_k=u_k^T A[T union {k},T union {k}]u_k`.                   (5.4)

Let `sigma_1(k),sigma_2(k)` be the two nonzero singular values of `D_k`. Since the base pair `T` is one of its row pairs, Cauchy--Binet gives

`[sigma_1(k)sigma_2(k)]^2
 =e_2(D_kD_k^T)
 >=det(MM^T)=S^2`,                                                (5.5)

hence

`sigma_1(k)sigma_2(k)>=S`.                                       (5.6)

Condition on all ORIGINAL `H` coordinates outside `T union {k}`. The remaining three physical variables have a joint density bounded by one. Rotate only this **three-dimensional joint density** so that the third deterministic axis is `u_k`; the joint density cap stays one, but no independence among the rotated coordinates is asserted. Rotate the first two coefficient axes and the two-dimensional row space in `L` by the SVD of `D_k`. The product `L`-bank projection has joint density cap at most two.

If `lambda_k!=0`, the three-variable self quadratic-plus-affine phase can be written exactly as

`lambda_k (T_0+h^T Z+u_0)^2+r(Z)`,                               (5.7)

where `Z in R^2`, and every term on the `L` bank remains inside an arbitrary measurable function. The completed theorem `QFORM-CROSS2-OVERLAP-SQUARE-L1-v1` therefore applies with source cap `M=1`, receiver cap `N<=2`, cross product at least `S`, and gives

`boxed:
 ||p_Q||_infinity
 <= C_* 2^(2/5) S^(-2/5)|lambda_k|^(-1/5),}`                      (5.8)

where

`C_*=5(675/256)^(1/5)=6.069917185377548...`,
`C_*2^(2/5)=8.009303743842015...`.                               (5.9)

The theorem supplies an `L^1` characteristic-function majorant uniformly in the conditioned values, so after averaging the **full law has a continuous `C_0` density** on this branch.

At the live thresholds, if some exact-cross-null direction obeys

`|lambda_k|>=1/64`,                                               (5.10)

then

`||p_Q||_infinity
 <8.009303743842015
   [1/(480sqrt(7626))]^(-2/5) 64^(1/5)
 =1299.5309104972737...<1300.`                                   (5.11)

Thus the exact `rho=0` endpoint is paid unless every literal three-coordinate cross-null circuit has self curvature below `1/64` in absolute value.

## 6. Exact Schur-area identity at rho=0

The exact endpoint also admits a useful deterministic identity for the remaining survivor. Since `M` has row rank two, write uniquely

`s_k=alpha_k^T M`, `alpha_k in R^2`.                              (6.1)

For `a_k!=0`, (4.2) becomes

`C_k^Sch=(I_2-a_k^(-1)r_k alpha_k^T)M`.                           (6.2)

Taking Gram determinants and using the matrix determinant lemma,

`boxed:
 Delta_k
 =S |det(I_2-a_k^(-1)r_k alpha_k^T)|
 =S |1-a_k^(-1)alpha_k^T r_k|.}`                                 (6.3)

Consequently failure of the paid gate `Delta_k>=S/2` forces

`boxed:
 |a_k-alpha_k^T r_k|<|a_k|/2}`                                   (6.4)

for every `k` with `|a_k|>=1/64`.

The unnormalized physical cross-null vector is

`q_k=(-alpha_k,1)`                                                (6.5)

in the coordinates `(T,k)`. If `B_0=A[T,T]`, then its normalized curvature is exactly

`lambda_k
 =[a_k-2alpha_k^T r_k+alpha_k^T B_0 alpha_k]
  /(1+||alpha_k||^2).`                                           (6.6)

Therefore every exact-rank-two state still unpaid after Sections 4-5 satisfies the simultaneous deterministic system

`|a_k-alpha_k^T r_k|<|a_k|/2` whenever `|a_k|>=1/64`,             (6.7)

and

`|a_k-2alpha_k^T r_k+alpha_k^T B_0 alpha_k|
 <(1+||alpha_k||^2)/64`                                          (6.8)

for every `k in H\T` (otherwise the continuous `<1300` exit applies).

Equation (6.3) was independently checked on 1000 noncommuting random `2 x 7` matrices/rank-one updates; the maximum normalized residual was `2.15e-14`.

## 7. Designated partner fleet04/B19 applied at an actual inequality

The designated partner theorem is

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T222052Z-fleet04-B19-QFORM-r2/REPORT.md`.

In its **residual-diffuse exact-null-coloop** normal form, for `0<D_res<=1` and `|det M|>=1`, it proves a continuous density with

`||p_Q||_infinity<34 sqrt(log(e/D_res))`.                         (7.1)

Applying it at the concrete threshold

`1/64<=D_res<=1`,                                                  (7.2)

gives

`boxed:
 ||p_Q||_infinity
 <34 sqrt(log(64e))
 =77.22479423322396...<78.}`                                      (7.3)

This is a real target-level inequality in the partner's exact scope. I do **not** infer (7.1) for the near-rank-two collar or for a merely near-null row.

## 8. Compact conditional proof assembly after this run

The compatible proof graph now contains the following collar exits.

1. The finite-core physical third-volume branch is already paid when `s_3(A[H,L])>=1/64`.
2. The strong rank-two packet `s_1s_2>1/480` is reduced by r38 to a literal two-row base of area `S>1/(480sqrt(7626))`.
3. If the transverse projected Frobenius residual is at least `1/64`, r38 pays continuously below `743`.
4. **New:** in the remaining `rho<1/64` collar, any physical scalar pivot `|A_kk|>=1/64` whose complete Schur-corrected two-row cross area is at least `S/2` is paid below `1499`, with the small nonzero tail retained.
5. **New:** at the exact rank-two endpoint `rho=0`, any literal cross-null circuit with normalized self curvature at least `1/64` is paid continuously below `1300` by the dependent overlap-square theorem.
6. The designated partner exact-null-coloop residual-diffuse branch is continuously paid below `78` when `D_res>=1/64`.

These exits are not yet exhaustive, so no full theorem is declared.

## 9. First essential missing implication

The first missing inequality is sharpened to

`QFORM-R2-COLLAR-REGULARIZED-OVERLAP-OR-SCHUR-CANCELLATION-v1`:

> In the live finite-core collar (2.3)-(2.5), prove a uniform product-safe receiver that combines the two-row area `S`, cross-null self curvature, and the **nonzero** transverse cross tail as that tail tends to zero; or prove that simultaneous failure of every physical-pivot Schur gate (4.7) forces an already-paid strong-rank-one/two-source/grouped branch. At the exact endpoint, it is enough to pay the explicit simultaneous algebraic survivor (6.7)-(6.8).

This is narrower than the previous generic Frobenius-collar debt. The fleet02/B06 near-null counterexample explains why the required receiver must consume the third large direction rather than perturbatively discard the small self/cross block.

## 10. Status

- Full unrestricted QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- `QFORM-TWOSIDED-SCHUR-2PLUS1-PRODUCTBANK-v1`: **PROVED** above.
- Live noncancelled-pivot collar payment: **essential density `<1499`**.
- Exact-rank-two cross-null-curvature payment: **continuous `C_0` density `<1300`**.
- Designated partner application: **continuous density `<78`** on (7.2) in its exact null-coloop scope.
- Remaining collar debt: `QFORM-R2-COLLAR-REGULARIZED-OVERLAP-OR-SCHUR-CANCELLATION-v1`.
- Full-target continuity: **OPEN**.
- No two independent end-to-end reviews are requested because no full candidate proof exists.
