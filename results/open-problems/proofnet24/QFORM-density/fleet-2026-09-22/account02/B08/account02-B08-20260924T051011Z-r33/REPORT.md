SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-24T05:10:11.605722Z.
attacking: intersect the newest diffuse-to-localized row router with a literal balanced-cut fifth-volume gate; quantify the unpaid large-but-low-rank complementary crossing and build a target-valid obstruction family.

# account02/B08 r33 — actual rank-seven complementary-crossing tube after the diffuse/localized gate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / complementary constructions and source-valid counterexamples  
Designated partner: `account03/B08`  
Status: **NEW SUPPORTING HYBRID ROUTER + EXACT TARGET-VALID STRESS FAMILY / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains **OPEN**. All statements below retain arbitrary independent one-dimensional input densities bounded by one, arbitrary signs, arbitrary affine terms produced by original-coordinate conditioning, and arbitrary same-bank curvature unless an exact displayed structural hypothesis says otherwise. No moment, compact-support, log-concavity, connected-support, Gaussianity, diagonal-basis, or post-rotation independence assumption is introduced.

## 1. First unpaid implication after this run

The first B08 debt is now

`QFORM-LOCALIZED-ROW-PLUS-RANK4-CROSS-TUBE-COMPILER-v1`:

> Let the leading three absolute-eigenvalue eigenvectors be diffuse at physical row leverage at most `1/48`. In the only branch not already paid below by `<197.779/L`, one has simultaneously:
> 
> 1. an actual fourth spectral value `s_4(A)>0.3198739505 L`;
> 2. an actual high-window physical localization at scale `0.00499803048 L` and hence an ORIGINAL scalar/star row witness `>0.00062475381 L`;
> 3. an ORIGINAL-coordinate balanced cut `S union T` for which the **actual** crossing `A[S,T]` lies within `0.05894596927 L` in operator norm of rank at most four;
> 4. after removing the chosen top-three spectral component and only its physical diagonal remainder, the complementary crossing still has operator norm `>0.3198739505 L` and lies within the same error of rank at most seven.
> 
> Prove `O(L^-1)` in this joint state while retaining arbitrary same-bank curvature and original product provenance. A successful compiler should split the low-rank complementary carrier by physical leverage rather than rotate the independent variables. A diffuse low-rank carrier is not itself an obstruction: Section 7 gives an exact family in this chamber paid by the fixed-source Fresnel theorem with constant `<8.214/L`.

This is strictly narrower than the partner r50 terminal alternative “some physical scalar/star row is large.”

## 2. Fresh sources and corrections


The required fixed source was read exactly at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Two completed fixed-source results are used at actual equations below.

**D5, unrestricted fifth-volume crossing.** For any ORIGINAL-coordinate crossing block `M=A[I,J]`, with

`Z_5=e_5(M^T M)`,

one has

`||p_Q||_infinity <= 5 sqrt(2e) Z_5^(-1/10)`,                    (2.1)

with no volume-marginal hypothesis. The same-bank quadratic blocks and affine terms remain arbitrary.

**F, rank-r Fresnel--Brascamp--Lieb.** If

`A=R Lambda R^T + D`,

`D` is physical diagonal, `R` has orthonormal columns, and every physical row of the rank-r frame has leverage at most `1/2`, then

`|phi_Q(t)| <= (4pi)^(r/2) |t|^(-r/2) prod_j |lambda_j|^(-1/2)`.  (2.2)

The fixed-source proofs retain the original product laws; the spectral frame is used analytically, not as a rotation of the random coordinates.

The newest compatible designated partner found at publication is account03/B08 r50,

`yspennstate/math-open-problems@11f861a6349b8865fcbcf6f1feb5afcccd25531a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T042041Z-account03-B08-qform-diffuse-r50/REPORT.md`.

Its theorem `QFORM-DIFFUSE-TOP3-THIRDCOMPOUND-RIDGE-ROUTER-v1` gives, under top-three row leverage at most `1/48`, either a continuous density `<197.779/L` or an ORIGINAL physical scalar/star witness `>0.0006247538095703261 L`. Its proof supplies the actual spectral gate used below.

The live correction inbox was reread. In particular this report does **not** use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, independence after spectral rotation, conditional-density suprema, or a guaranteed uniformly conditioned physical minor.

## 3. Partner half-cut and notation

Assume

`s_3(A)>=L>0`.                                                    (3.1)

Choose orthonormal eigenvectors `U in R^(n x 3)` corresponding to the three leading absolute eigenvalues and write

`A=A_3+R`,
`A_3=U Lambda U^T`,
`min_j |lambda_j|>=L`.                                            (3.2)

Let

`mu=max_i ||U_{i,*}||_2^2<=1/48`.                                (3.3)

Account03/B08 r50 proves by a Bernoulli half-cut that there is an ACTUAL partition of the physical coordinates

`[n]=S disjoint_union T`                                          (3.4)

such that

`U_S^T U_S >= (3/8) I_3`,
`U_T^T U_T >= (3/8) I_3`.                                        (3.5)

Therefore the top-three crossing

`B_0=A_3[S,T]=U_S Lambda U_T^T`                                  (3.6)

satisfies

`s_3(B_0)>=3L/8`.                                                  (3.7)

Now split the complementary curvature into its physical diagonal and off-diagonal parts:

`D=diag(R)`,
`C=R-D`.                                                          (3.8)

Since a physical diagonal has zero `S x T` block, the **literal full crossing** is

`B:=A[S,T]=B_0+C[S,T]`.                                           (3.9)

This elementary observation is useful because an arbitrarily large diagonal complementary spectrum costs nothing at the crossing. Thus the relevant perturbation gate is an actual off-diagonal crossing norm, not the global number `s_4(A)`.

## 4. New router: small off-diagonal complement or fifth-volume payment

Put

`C_X=6^(4/3)=10.902723556992836...`,                              (4.1)

`C_R=288 sqrt(3e)/13=63.26405187778285...`.                       (4.2)

Use the partner r50 balanced value

`eta_* = (3/8) C_R/(C_R+C_X)
       = 0.31987395050000694...`,                                 (4.3)

and

`C_*=(C_R+C_X)/(3/8)
    =197.7780678260685...`.                                       (4.4)

### 4.1 Small actual complementary crossing

If

`||C[S,T]||_op <= eta_* L`,                                      (4.5)

then Weyl and (3.7) give

`s_3(B)>=(3/8-eta_*)L`.                                           (4.6)

The reviewed third-compound crossing theorem used by account03/B08 r50 states

`||p_Q||_infinity <= C_X e_3(BB^T)^(-1/6)`.                       (4.7)

Since

`e_3(BB^T)>=s_1(B)^2 s_2(B)^2 s_3(B)^2>=s_3(B)^6`,               (4.8)

(4.6)-(4.8) give

`boxed:
 ||p_Q||_infinity <= C_*/L,
 p_Q in C_0(R).
`                                                                    (4.9)

All same-bank terms are retained by the crossing theorem.

### 4.2 Large complement but enough fifth volume

Suppose (4.5) fails. Apply the required fixed-source theorem D5 directly to the same literal crossing `B`.

Set

`K_5=5 sqrt(2e)=11.658219907985622...`,                           (4.10)

and choose

`tau_*:=K_5/C_*
      =0.05894596926813029...`.                                  (4.11)

If

`s_5(B)>=tau_* L`,                                                (4.12)

then

`Z_5=e_5(B^T B)
    >=prod_{j=1}^5 s_j(B)^2
    >=(tau_* L)^10`.                                              (4.13)

Substitution in the fixed-source inequality (2.1) gives the real target inequality

`boxed:
 ||p_Q||_infinity <= K_5/(tau_* L)=C_*/L,
 p_Q in C_0(R).
`                                                                    (4.14)

This is the required fixed-source result applied to an actual full-ambient branch, not merely cited.

### 4.3 What remains if neither payment occurs

If neither (4.5) nor (4.12) holds, then

`||C[S,T]||_op>eta_*L`,                                          (4.15)

`s_5(B)<tau_*L`.                                                  (4.16)

By the operator-norm Eckart--Young theorem there exists `B_4` of rank at most four with

`||B-B_4||_op=s_5(B)<tau_*L`.                                    (4.17)

As `rank(B_0)<=3`,

`C[S,T]
 =(B_4-B_0)+(B-B_4)`.                                             (4.18)

The first term has rank at most seven, so

`boxed:
 dist_op(C[S,T], {rank<=7})<tau_*L.
`                                                                    (4.19)

Thus a genuinely unpaid complementary crossing is not arbitrary high rank: it is **large** at scale `0.31987L` but trapped inside a `0.05895L` operator tube around rank seven. Simultaneously the actual full crossing itself lies in a rank-four tube by (4.17).

This is theorem

### `QFORM-DIFFUSE-TOP3-OFFDIAG-RANK7-ROUTER-v1`

Under (3.1)-(3.3), there is an ORIGINAL-coordinate partition `S union T` such that either

`boxed: ||p_Q||_infinity <=197.779/L, p_Q in C_0(R),`             (4.20)

or simultaneously

`boxed:
 ||C[S,T]||_op>0.3198739505 L,
 dist_op(A[S,T],{rank<=4})<0.05894596927 L,
 dist_op(C[S,T],{rank<=7})<0.05894596927 L.
`                                                                    (4.21)

No claim is made that the low-rank approximants are aligned with spectral coordinates or preserve product independence after rotation; they are deterministic matrix certificates only.

## 5. Intersect with the newest localized/diffuse spectral gate

The preceding theorem and account03/B08 r50 are both exhaustive under the same diffuse top-three assumption (3.3). Hence if the density is not already paid by `C_*/L`, **both** terminal certificates must hold.

The partner proof shows that its unpaid branch can occur only after

`boxed: s_4(A)>eta_* L=0.3198739505... L.`                        (5.1)

Define the actual spectral-window projection

`P_* = 1_{|A|>=eta_*L/64}`.                                      (5.2)

The window scale is

`eta_*L/64=0.0049980304765626085... L`.                           (5.3)

If `max_i(P_*)_ii<=1/32`, the reviewed ridge-window theorem pays the form by `C_R/(eta_*L)=C_*/L`. Therefore any unpaid branch has

`boxed: max_i(P_*)_ii>1/32.`                                     (5.4)

For a coordinate `k` with (5.4), the partner spectral-energy estimate gives

`||Ae_k||_2>eta_*L/(256 sqrt2)`                                  (5.5)

and hence

`boxed:
 max{|A_kk|, ||A[k,-k]||_2}>eta_*L/512
 =0.0006247538095703261... L.
`                                                                    (5.6)

Combining (4.21), (5.1), (5.4), and (5.6) gives the quantified remaining hybrid promised in Section 1.

### Corollary `QFORM-DIFFUSE-UNPAID-INTERSECTION-v1`

If `s_3(A)>=L`, the leading-three physical leverage is at most `1/48`, and the form is not already controlled by `197.779/L`, then there exist an ORIGINAL coordinate `k` and an ORIGINAL partition `S union T` such that

`boxed:
 s_4(A)>0.3198739505 L,
 max_i(1_{|A|>=0.00499803048L})_ii>1/32,
 max{|A_kk|,||A[k,-k]||_2}>0.00062475381 L,
 ||C[S,T]||_op>0.3198739505 L,
 dist_op(A[S,T],rank<=4)<0.05894596927 L,
 dist_op(C[S,T],rank<=7)<0.05894596927 L.
`                                                                    (5.7)

This is an actual spectral gate plus an actual physical localized certificate plus an actual low-rank crossing tube. It retains arbitrary product sources; no stochastic rotation is performed.

## 6. Why the diagonal complementary spectrum should be removed before the gate

The use of `C=R-diag(R)` is not cosmetic. A large fourth eigenvalue can be entirely physical-diagonal and therefore irrelevant to the cross-block perturbation.

If `R` itself is diagonal, then `C=0`, so (4.5) holds regardless of `s_4(A)`. Thus the entire diffuse top-three form is paid by (4.9) even if the complementary diagonal eigenvalues are huge.

The fixed-source Theorem F gives the even sharper direct statement: for

`A=U Lambda U^T + D`,                                             (6.1)

with `D` arbitrary physical diagonal, `min_j|lambda_j|>=L`, and top-three leverage at most `1/2`,

`||p_Q||_infinity<=12/L`.                                        (6.2)

Therefore a large `s_4(A)` is not itself the genuine obstruction. The unpaid branch must carry **non-diagonal** complementary geometry on the actual balanced cut.

## 7. Exact target-valid stress family inside the new hybrid

The low-rank-tube alternative (5.7) is not vacuous, and neither it nor the localized row forces a good physical pair.

Let `m=2^q>=512`, with `q>=9`. On the group `(Z/2Z)^q`, choose five independent Walsh characters `chi_1,...,chi_5`; set

`u_j(x)=chi_j(x)/sqrt(m)`.                                        (7.1)

Add one extra physical coordinate `z`, disjoint from the Walsh block. Define

`A_m=L( u_1u_1^T + u_2u_2^T - u_3u_3^T +(9/10)u_4u_4^T )
      +(L/2)e_z e_z^T`.                                           (7.2)

The nonzero spectrum is exactly

`boxed: {L,L,-L,0.9L,0.5L}.`                                     (7.3)

Hence the exact QFORM target is satisfied and **exactly three** eigenvalues have modulus at least `L`.

The leading-three frame `[u_1,u_2,u_3]` has physical row leverage

`3/m<=3/512<1/48`                                                 (7.4)

on every Walsh coordinate and zero at `z`.

### 7.1 Exact balanced crossing

Let

`S_0={x: chi_5(x)=+1}`,
`T_0={x: chi_5(x)=-1}`.                                           (7.5)

Put the extra coordinate `z` on the `S` side. Independence of the character labels gives, for `1<=i,j<=4`,

`u_i[S_0]^T u_j[S_0]=(1/2) delta_ij`,
`u_i[T_0]^T u_j[T_0]=(1/2) delta_ij`.                              (7.6)

Thus the actual crossing of the Walsh block has singular values

`boxed: L/2,L/2,L/2,0.45L`,                                      (7.7)

and no fifth singular value. In particular

`s_5(A_m[S,T])=0`.                                                (7.8)

Relative to the leading-three component, the complementary off-diagonal crossing is exactly the `u_4` rank-one term, so

`boxed:
 ||C[S,T]||_op=0.45L>eta_*L,
 rank(C[S,T])=1.
`                                                                    (7.9)

This lies at the exact centre of the new rank-seven tube rather than merely close to it.

### 7.2 It also triggers the newest localized spectral alternative

Here

`s_4(A_m)=0.9L>eta_*L`.                                          (7.10)

The physical coordinate `z` is itself an eigenvector with eigenvalue `L/2`, which is far above the window threshold (5.3). Therefore

`(P_*)_zz=1>1/32`,                                                (7.11)

and the explicit localized row witness is

`|A_zz|=L/2`.                                                     (7.12)

So this is a literal realization of the intersection between the account03/B08 r50 localized branch and the new low-rank complementary-crossing branch.

### 7.3 Yet no uniformly conditioned physical pair exists

For two coordinates inside the Walsh block, each diagonal entry has magnitude `1.9L/m`, while every off-diagonal entry has magnitude at most `3.9L/m`. Hence every such physical `2 x 2` block has

`||B_ij||_op<=5.8L/m`.                                            (7.13)

A pair containing `z` is diagonal with the other diagonal entry of magnitude `1.9L/m`, so its least singular value is at most `1.9L/m`.

Therefore, for `m>=512`, every physical pair satisfies

`boxed:
 sigma_min(A_m[{i,j},{i,j}]) <=5.8L/m
 <=0.011328125L < L/64.
`                                                                    (7.14)

Thus a localized spectral row plus a low-rank complementary crossing does **not** force the already-solved `L/64` physical-pair gate.

### 7.4 The family is not a QFORM counterexample: fixed-source Theorem F pays it

Apply the required fixed-source rank-r Fresnel theorem (2.2) to the rank-four diffuse frame

`R_4=[u_1,u_2,u_3,u_4]`,                                         (7.15)

with spectral coefficients

`L,L,-L,0.9L`,                                                    (7.16)

and diagonal remainder `(L/2)e_z e_z^T`.

Every physical row leverage of `R_4` is `4/m<=1/2`. Therefore

`|phi_Q(t)|
 <=(4pi)^2 |t|^-2 (0.9L^4)^(-1/2)
 =16pi^2/(sqrt(0.9)L^2 t^2)`.                                    (7.17)

Integrating `min(1,K/t^2)` exactly gives

`||p_Q||_infinity
 <=8(0.9)^(-1/4)L^-1
 =8.213520768642727.../L`,                                       (7.18)

and the fixed-source Fourier proof supplies a continuous `C_0` density.

So (7.2) is a **mechanism obstruction, not a conjecture counterexample**. It shows why the next compiler must recursively exploit the physical leverage of the low-rank complementary carrier: if that carrier is itself diffuse, whole-frame Fresnel aggregation can beat every local-pair route.

## 8. Consequence for the remaining proof design

The newest diffuse/localized split no longer leaves an amorphous “large physical row” state. After the present intersection, an unpaid state has two simultaneous resources:

- a localized physical scalar/star row at scale `6.25e-4 L`;
- a large complementary crossing concentrated in at most seven directions up to `5.90e-2 L`, while the total crossing is concentrated in at most four directions at the same tolerance.

The next leverage split should therefore be performed on a rank-at-most-seven approximant to `C[S,T]` **in the original physical rows/columns**:

1. if that low-rank carrier is diffuse on both banks, use a rank-r Fresnel/projected-crossing compiler before choosing a scalar pivot;
2. if it has a heavy physical row or column, merge that ORIGINAL coordinate with the r50 localized row and attempt a two-hub/mixed-star receiver;
3. keep the `0.05895L` residual inside the analytic receiver rather than calling it a small random quadratic perturbation, which is invalid without moments.

The exact family (7.2) verifies that item 1 is necessary. A bounded-cardinality pivot-only strategy cannot be the universal endpoint.

Full unrestricted QFORM and the global continuity conclusion remain **OPEN**.

## 9. Deterministic checks

The constants used above are

`C_R=63.26405187778285`,
`C_X=10.902723556992836`,
`eta_*=0.31987395050000694`,
`C_*=197.7780678260685`,
`K_5=11.658219907985622`,
`tau_*=0.05894596926813029`,
`eta_*/512=0.0006247538095703261`,
`eta_*/64=0.0049980304765626085`.

For `m=512`, direct Walsh arithmetic gives the side Gram matrices `(1/2)I_4` to machine precision and crossing singular values `0.5,0.5,0.5,0.45` at `L=1`. The exact analytic identities (7.6)-(7.9) do not depend on floating-point computation.

The changed-file scope of this run is restricted to the worker-owned account02/B08 mathematical path and the corresponding account02/B08 brain login/run/handoff/memory paths. A manual content review found no credentials, signed URLs, scheduler identifiers, machine paths, unrelated private data, or public-release material.
