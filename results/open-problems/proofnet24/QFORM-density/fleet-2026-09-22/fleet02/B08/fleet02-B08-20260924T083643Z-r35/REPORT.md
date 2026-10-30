SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-24T08:36:43.059355Z.
attacking: the rank-two balanced-crossing cancellation survivor by forcing the actual localized row into the same physical cut, then using the newest fleet03/B08 exterior-algebra star inequality to isolate the remaining aligned/two-mode branches.

# fleet02/B08 r35 — row-aware balanced cut and scalar/aligned/two-mode cancellation router

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / complementary constructions and source-valid counterexamples  
Designated partner: `fleet03/B08`  
Status: **NEW SUPPORTING HYBRID ROUTER + EXACT TARGET-VALID SCALAR/CANCELLATION STRESS FAMILY / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted theorem remains **OPEN**. Every statement below keeps arbitrary independent one-dimensional input densities bounded by one, arbitrary complementary spectrum, arbitrary same-bank curvature, and arbitrary affine terms created by conditioning on ORIGINAL coordinates. No moments, support condition, log-concavity, Gaussianity, connectedness, diagonal-basis independence, post-rotation independence, arbitrary-joint coarea bound, conditional projection-height bound, or small-random-perturbation claim is used. Continuity is asserted only on branches paid by an integrable Fourier estimate.

## 1. First unpaid implication after this run

The B08 debt is now

### `QFORM-ROWAWARE-SCALAR-OR-DOUBLECANCEL-COMPILER-v1`

In the diffuse top-three chamber `max_i ||U_{i,*}||^2<=1/48`, retain the r34 actual spectral/row gates

` s_4(A)>0.3198739505 L`,

`max_i (1_{|A|>=0.00499803048L})_{ii}>1/32`,

and an ORIGINAL physical coordinate `k` with

`max{|A_kk|,||A[k,-k]||_2}>gamma L`,
`gamma=0.0006247538095703261...`.

If the benchmark `197.779/L` is still unpaid, then either the witness is genuinely scalar,

`|A_kk|>gamma L`,

or there is one ORIGINAL-coordinate cut `S union T`, with `k in S`, that simultaneously has a balanced selected top-three frame and a nontrivial physical cross-star,

`U_S^T U_S,U_T^T U_T >= 3I_3/10`,

`||A[k,T]||_2>gamma L/sqrt(6)=0.0002550546747...L`.

For that same cut the literal crossing is in a rank-two tube and complementary curvature cancels a target-scale top-three direction. After deleting `k`, one of two more rigid alternatives holds at the explicit gate

`sigma=sqrt(67/800)L/2=0.1446979612848...L`:

1. **star-aligned branch:** the surviving cross-star lies within `0.008001027956 L` of the top-two right singular plane of the literal deleted crossing; or
2. **two-mode complementary-cancellation branch:** the deleted complementary crossing has second singular value at least `0.1446979612848...L`.

The next compiler must pay the scalar branch or one of these two source-valid branches without replacing the product source by a rotated/joint law. The exact family in Section 7 shows the scalar branch and complete crossing cancellation are real, even though that family itself is easily paid by the fixed-source whole-frame Fresnel theorem.

## 2. Fresh sources and exact scopes


The required fixed source was read exactly at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

The fixed source proves, among other results, the generalized Fresnel--Brascamp--Lieb estimate for

`A=D+R Lambda R^T`,

where `D` is physical diagonal, `R` has orthonormal columns, and every physical leverage of the rank-`r` frame is at most `1/2`:

`||p_Q||_infinity <= [4r/(r-2)] prod_j |lambda_j|^(-1/r)`,        (2.1)

with a `C_0` density for `r>2`. It is applied to an actual target-valid obstruction in Section 7, not merely cited.

The marginal-free physical third-compound receiver is the completed fleet01/B04 theorem

`QFORM-THIRDCOMPOUND-CROSS-PROMOTION-v1`,

canonical source

`yspennstate/math-open-problems@c2ce876df8b5483a00802170001d4144bb4cdbfa`.

For every literal ORIGINAL-coordinate crossing `B=A[I,J]`, arbitrary same-bank phases included,

`||p_Q||_infinity <= C_3 e_3(BB^T)^(-1/6)`,
`C_3=6^(4/3)=10.90272355699...`,                                  (2.2)

with `p_Q in C_0`.

The newest completed designated partner available in the fresh handoff tree is fleet03/B08 `20260924T061920Z-fleet03-B08-qform-diffuse-r51`, canonical mathematics

`yspennstate/math-open-problems@19c12072f7e67266ce894042034bcabb9c376bea`.

Its deterministic exterior-algebra lemma says that for any matrix `D` and row `z`, with `R_2(D)` the top-two right singular subspace,

`e_3([z^T;D][z^T;D]^T)
 >= s_1(D)^2 s_2(D)^2 dist(z,R_2(D))^2`.                         (2.3)

This exact lemma is used in Section 6.

The fixed-source counterexample search reports no counterexample and specifically leaves diffuse/high-dimensional configurations as a plausible hiding place; no numerical observation from that report is used as proof here.

## 3. New lemma: a balanced diffuse cut can be forced to see a chosen off-diagonal row

Let `U in R^(n x 3)` have orthonormal columns and

`mu=max_i ||U_{i,*}||_2^2<=1/48`.                               (3.1)

Fix an ORIGINAL physical coordinate `k`. Put

`R_k^2=sum_(j!=k) A_kj^2=||A[k,-k]||_2^2`.                      (3.2)

Choose independent Bernoulli variables `delta_i in {0,1}` of mean `1/2`, with

`S={i:delta_i=1}`, `T=S^c`,
`G_S=U_S^T U_S`.                                                  (3.3)

Writing `u_i=U_{i,*}^T`, independence and centering give the exact second-moment identity

`E ||G_S-I_3/2||_F^2
 = (1/4) sum_i ||u_i u_i^T||_F^2
 = (1/4) sum_i ||u_i||_2^4
 <= (mu/4) sum_i ||u_i||_2^2
 = 3mu/4
 <=1/64.`                                                        (3.4)

Hence

`P(||G_S-I_3/2||_op>1/5)
 <=P(||G_S-I_3/2||_F>1/5)
 <=25/64`.                                                       (3.5)

On the complementary event,

`G_S,G_T=I_3-G_S >=3I_3/10`.                                    (3.6)

Now define the actual cross-row energy

`Z_k=sum_(j!=k) A_kj^2 1_{delta_j!=delta_k}`.                    (3.7)

Conditioning on `delta_k` shows

`E Z_k=R_k^2/2`, `0<=Z_k<=R_k^2`.                               (3.8)

If `p=P(Z_k>=R_k^2/6)`, then

`R_k^2/2=E Z_k
 <=pR_k^2+(1-p)R_k^2/6`,                                        (3.9)

so

`p>=2/5`.                                                        (3.10)

Therefore

`P( (3.6) and Z_k>=R_k^2/6 )
 >=39/64+2/5-1
 =3/320>0`.                                                      (3.11)

This proves:

### Lemma `QFORM-ROW-AWARE-THREEFRAME-CUT-v1`

Under (3.1), for every fixed ORIGINAL coordinate `k`, there is an ORIGINAL partition `S union T`, with side labels swapped if needed so `k in S`, such that

`boxed: U_S^T U_S,U_T^T U_T >=3I_3/10`,                         (3.12)

and

`boxed: ||A[k,T]||_2 >= ||A[k,-k]||_2/sqrt(6).`                 (3.13)

No matrix term is deleted, and the random variables are never rotated. This is the first new implication: the old diffuse cut and the actual localized off-diagonal row can be made simultaneous. The only witness not forced into the crossing is a genuinely physical scalar `A_kk`.

## 4. Row-aware rank-two cancellation packet

Let

`A_3=U Lambda U^T`, `min_j |lambda_j|>=L`,                       (4.1)

and take the cut from Lemma 3. The selected top-three crossing is

`B_0=A_3[S,T]=U_S Lambda U_T^T`.                                 (4.2)

From (3.12),

`boxed: s_3(B_0)>=3L/10.`                                       (4.3)

Let

`B=A[S,T]`, `C_x=(A-A_3)[S,T]=B-B_0`.                           (4.4)

Retain the r34 benchmark

`C_*=197.7780678260685`,
`theta=C_3/C_*=0.05512604949999305...`.                          (4.5)

If

`e_3(BB^T)^(1/6)>=theta L`,                                     (4.6)

then (2.2) pays

`||p_Q||_infinity<=C_*/L`,                                      (4.7)

continuously. Thus on an unpaid branch,

`e_3(BB^T)^(1/6)<theta L`.                                      (4.8)

Since `e_3(BB^T)>=s_3(B)^6`,

`boxed: s_3(B)<theta L`,                                        (4.9)

and hence

`boxed: dist_op(B,{rank<=2})<theta L.`                           (4.10)

Weyl and (4.3) give

`boxed: ||C_x||_op>(3/10-theta)L
 =0.24487395050000694...L.`                                     (4.11)

Exactly as in r34, if `B_2` is a best rank-two approximation to `B`, then

`C_x=(B_2-B_0)+(B-B_2)`,                                       (4.12)

with `rank(B_2-B_0)<=5`, so

`boxed: dist_op(C_x,{rank<=5})<theta L.`                         (4.13)

There is also a signed cancellation direction. Let `V_2(B)` be a top-two right singular subspace of `B`. Since `range(U_T)` has dimension three, choose unit

`x in range(U_T) intersect V_2(B)^perp`.                         (4.14)

Then `||Bx||<theta L`, while (4.3) gives `||B_0x||>=3L/10`. With

`y=B_0x/||B_0x||`,                                               (4.15)

one obtains

`boxed:
 y^T C_x x <-(3/10-theta)L
 =-0.24487395050000694...L.`                                    (4.16)

Thus sacrificing some cut balance from `3/8` to `3/10` buys simultaneous access to the actual localized off-diagonal row.

## 5. Insert the inherited actual spectral localization gate

The r34 intersection, inherited from the completed fleet03/B08 spectral router, says that if the same benchmark `C_*/L` has not already paid the diffuse-top-three state, then

`boxed: s_4(A)>0.31987395050000694L`,                            (5.1)

and for

`P_*=1_{|A|>=0.0049980304765626085L}`,                           (5.2)

one has

`boxed: max_i(P_*)_ii>1/32`.                                    (5.3)

Spectral energy therefore supplies an ORIGINAL coordinate `k` satisfying

`boxed:
 max{|A_kk|,||A[k,-k]||_2}>
 gamma L,
 gamma=0.0006247538095703261... .`                               (5.4)

Use this `k` in Lemma 3.

If `|A_kk|>gamma L`, retain it as the explicit **scalar branch**. Otherwise (5.4) forces

`R_k=||A[k,-k]||_2>gamma L`,                                    (5.5)

and the same physical cut from Sections 3--4 satisfies

`boxed:
 ||z||_2:=||A[k,T]||_2>
 gamma L/sqrt(6)
 =0.0002550546747178715...L.`                                   (5.6)

This removes the r34 defect that the localized off-diagonal row might live entirely away from the chosen rank-two crossing. A disconnected witness can now survive only by being scalar at this stage.

## 6. Delete that row and apply the newest fleet03/B08 exterior lemma

Assume the nonscalar branch and relabel so `k in S`. Delete the row `k` from the literal crossing:

`D=A[S\{k},T]`, `z=A[k,T]`, so `B=[z^T;D]`.                     (6.1)

The selected top-three Gram on the deleted side still obeys

`U_(S\{k})^T U_(S\{k})
 =U_S^T U_S-u_k u_k^T
 >=(3/10-1/48)I_3
 =(67/240)I_3`.                                                  (6.2)

Hence the deleted selected top-three crossing

`B_0^-=A_3[S\{k},T]`                                            (6.3)

has

`boxed:
 s_3(B_0^-)
 >=c_0 L,
 c_0=sqrt((67/240)(3/10))
 =sqrt(67/800)
 =0.28939592256975566... .`                                     (6.4)

Set

`sigma=c_0/2=0.14469796128487783... .`                           (6.5)

### Branch 6A: two-mode complementary cancellation

Suppose

`s_2(D)<sigma L`.                                                (6.6)

Let `v_1` be a top right singular vector of `D`. Since `range(U_T)` is three-dimensional, the subspace

`E=range(U_T) intersect v_1^perp`                                (6.7)

has dimension at least two. For every `x in E`,

`||Dx||<=s_2(D)||x||<sigma L||x||`,                             (6.8)

whereas (6.4) gives

`||B_0^-x||>=c_0L||x||`.                                        (6.9)

Writing

`C^-=(A-A_3)[S\{k},T]=D-B_0^-`,                                (6.10)

we get uniformly on the two-dimensional `E`

`||C^-x||>(c_0-sigma)L||x||=sigma L||x||`.                      (6.11)

By the min-max characterization of singular values,

`boxed:
 s_2(C^-)>sigma L
 =0.14469796128487783...L.`                                     (6.12)

Thus a literal deleted crossing that loses its second direction forces **two independent target-scale complementary cancellation directions**. This is stronger than the single signed direction in (4.16).

### Branch 6B: absolute star alignment with the literal rank-two carrier

Suppose instead

`s_2(D)>=sigma L`.                                               (6.13)

Apply the newest partner inequality (2.3) to the literal physical matrix `B=[z^T;D]`. From (4.8),

`e_3(BB^T)<theta^6L^6`,                                        (6.14)

while `s_1(D)>=s_2(D)>=sigma L`. Therefore

`dist(z,R_2(D))
 < theta^3 sigma^(-2)L`.                                        (6.15)

Numerically,

`theta^3 sigma^(-2)
 =(3200/67)theta^3
 =0.008001027955285274...`.                                     (6.16)

Hence

`boxed:
 dist(A[k,T],R_2(D))<0.008001027956L.`                           (6.17)

This is an absolute, product-safe alignment certificate. It is deliberately **not** mislabeled as a relative-angle bound: the inherited row gate (5.6) is much smaller than the tolerance in (6.17). The still-unpaid analysis must therefore either amplify the star scale, exploit the scalar branch, or aggregate the two-mode complementary curvature in (6.12), rather than infer a small angle that the constants do not provide.

Combining Sections 3--6 proves the main new structural result.

### Theorem `QFORM-ROWAWARE-RANK2-CANCELLATION-ROUTER-v1`

Assume `s_3(A)>=L`, choose three actual eigenvectors of modulus at least `L` with physical leverage at most `1/48`, and suppose the inherited `197.779/L` payment has not occurred. Then the actual spectral gates (5.1)--(5.4) hold, and either

**(i)** `|A_kk|>0.0006247538095L` for an ORIGINAL coordinate `k`; or

**(ii)** there is an ORIGINAL partition `S union T`, `k in S`, satisfying all of

`U_S^T U_S,U_T^T U_T>=3I_3/10`,

`||A[k,T]||>0.0002550546747L`,

`dist_op(A[S,T],rank<=2)<0.05512604950L`,

`||(A-A_3)[S,T]||_op>0.2448739505L`,

`dist_op((A-A_3)[S,T],rank<=5)<0.05512604950L`,                  (6.18)

plus the signed cancellation (4.16), and after deleting `k` either

`dist(A[k,T],R_2(A[S\{k},T]))<0.008001027956L`,                  (6.19)

or

`s_2((A-A_3)[S\{k},T])>0.1446979612848L`.                       (6.20)

Every object in this theorem lives in the original physical coordinates. Arbitrary product sources and all same-bank terms remain untouched.

## 7. Exact target-valid stress family: complete cut cancellation plus a disconnected scalar witness

The new scalar branch is real, and one cannot strengthen the theorem by asserting that the localized spectral witness must have a nontrivial off-diagonal star.

Let `m=2^q>=1024`. Choose normalized Walsh characters `u_1,u_2,u_3` and an unnormalised sign character

`chi in {+1,-1}^m`                                               (7.1)

so that the six normalized Walsh characters

`u_1,u_2,u_3,
 v_1=chi .* u_1,
 v_2=chi .* u_2,
 v_3=chi .* u_3`                                                  (7.2)

are pairwise distinct, hence orthonormal. Add a separate physical coordinate `z`, and define

`A_m
 =L sum_(j=1)^3 (u_j u_j^T+v_j v_j^T)
 +(L/2)e_z e_z^T`.                                               (7.3)

Its nonzero spectrum is exactly

`boxed: {L,L,L,L,L,L,L/2}.`                                    (7.4)

Thus it is target-valid, with six rather than merely three target-scale eigenvalues. The total spectral projector onto the six `L`-eigenvectors has light-coordinate leverage `6/m`, so in particular every choice of a three-dimensional subspace inside this six-frame has leverage at most `6/m<=1/48` for `m>=288`; the displayed top-three frame `[u_1,u_2,u_3]` has leverage exactly `3/m`.

Take the physical half-cut

`S_0={i:chi_i=+1}`, `T_0={i:chi_i=-1}`                           (7.5)

on the light coordinates, with `z` placed on either side. Orthogonality of `u_i` against every `v_j` gives

`U_(S_0)^T U_(S_0)=U_(T_0)^T U_(T_0)=I_3/2`.                    (7.6)

The selected top-three crossing has singular values exactly

`L/2,L/2,L/2`.                                                   (7.7)

But across this cut `chi` changes sign, so pointwise

`(v_j)_s(v_j)_t=-(u_j)_s(u_j)_t`

for `s in S_0,t in T_0`. Hence

`(v_jv_j^T)[S_0,T_0]=-(u_ju_j^T)[S_0,T_0]`,                     (7.8)

and therefore the **literal full crossing vanishes exactly**:

`boxed: A_m[S_0,T_0]=0.`                                        (7.9)

The complementary crossing is exactly `-B_0`, of rank three and norm `L/2`, so all three selected spectral crossing directions are cancelled, not merely one. Meanwhile the separate coordinate `z` is maximally localized in the high spectral window and has

`A_zz=L/2`, `A[z,-z]=0`.                                        (7.10)

Thus the localized spectral witness can be completely disconnected from the cancellation carrier precisely through the scalar branch isolated in Section 5.

There is still no uniformly conditioned physical pair. For two light coordinates, every matrix entry has modulus at most `6L/m`, so every light-light physical `2x2` block has operator norm at most

`12L/m`.                                                        (7.11)

A `z`--light block is diagonal with smaller entry `6L/m`. Hence for `m>=1024`, every physical `2x2` principal block has

`boxed: sigma_min<L/64.`                                        (7.12)

This is a mechanism obstruction, **not** a counterexample to QFORM.

## 8. Required fixed-source theorem applied to the obstruction

The family (7.3) is exactly in the scope of the fixed `e5f71d79...` generalized Theorem F. Its six-frame has physical leverage

`6/m<=1/2`,                                                     (8.1)

and the only remaining term is the physical diagonal twist `(L/2)e_ze_z^T`. Apply (2.1) with `r=6` and all six `|lambda_j|=L`:

`||p_(X^T A_m X)||_infinity
 <=[4*6/(6-2)] (L^6)^(-1/6)
 =6/L.`                                                         (8.2)

Moreover

`boxed: p_(X^T A_m X) in C_0(R).`                               (8.3)

Equivalently, the fixed-source Fourier envelope is

`|phi(t)|<=min{1,(4pi)^3 L^(-3)|t|^(-3)}`,                      (8.4)

whose exact integral gives the same `6/L` density bound.

This is the required completed fixed-source result applied to a genuine target-valid obstruction. It shows why the next proof should aggregate the full diffuse cancellation carrier before selecting reciprocal local minors: here the physical crossing has rank zero and every physical pair is weak, yet the original-coordinate product Fourier mechanism pays immediately.

## 9. What remains and what does not

The new theorem eliminates one structural ambiguity in r34: an off-diagonal localized row can no longer be disjoint from the balanced spectral cut. The live branch is now explicitly split into a real scalar pivot or an off-diagonal cross-star that is either absolutely aligned with the literal rank-two crossing, or accompanied by two target-scale complementary crossing directions after row deletion.

No claim is made that the `0.008001L` alignment is a small **relative** angle at the minimal star scale. No small operator tail is discarded probabilistically. No selected singular vector is treated as an independent random coordinate. The fixed-source Fresnel payment in Section 8 uses the special exact low-rank-plus-diagonal structure of the stress family and is not transferred to an arbitrary complementary spectrum.

The exact next implication is therefore `QFORM-ROWAWARE-SCALAR-OR-DOUBLECANCEL-COMPILER-v1`: combine a target-scale physical scalar, or the row-aware star-aligned/two-mode-cancellation packet, with the existing pair-log, projected-crossing, hub, and same-bank receivers while retaining all arbitrary product-source provenance. The global theorem and global continuity remain OPEN.

Deterministic arithmetic and exact stress-family identities are recorded in `CHECKS.md`; the marker is `QFORM_B08_R35_CHECK_PASS`.
