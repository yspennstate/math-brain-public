SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T12:44:08Z.
attacking: aggregate singleton-augmentation third-volume to a disjoint original-coordinate bilinear cut, preserving arbitrary same-bank curvature and seeking a direct O(interval length) payment.

# Aggregate singleton third-volume -> one fixed physical cut

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: fleet01/B09, Bilinear block mechanism  
Status: **ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL-ANALYTIC COMPILER / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. The new result below is a source-coordinate routing theorem for the rank-two-hub / arbitrary-leaf-curvature frontier. It converts fleet03/B09's aggregate singleton-augmentation third-volume into either a single fixed disjoint physical cut that is paid by the fractional three-volume Fourier theorem, or a literal high-volume physical row lying in a bounded candidate set. No spectral rotation of the random inputs, no pointwise quadratic van-der-Corput envelope, no probability squaring into a square-root small-ball loss, and no small-random-quadratic perturbation argument is used.

## 1. Completed inputs actually used

### 1.1 Fractional three-volume Fourier theorem

From `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`:
for an ORIGINAL-coordinate cross block `M=A[I,J]`, `Z=e_3(M^T M)>0`, and `1<=q<3/2`, if the row three-volume marginals satisfy `alpha_i<=q/2`, then

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`,

with a continuous density and the same coefficient multiplying interval length. All same-bank functions and outside-conditioned affine terms are arbitrary.

The determinant proof uses only a positive weighted family of 3x3 minors. Therefore the same proof applies verbatim to any restricted minor family `Omega`: if

`Z_Omega=sum_((S,T) in Omega) det(M[S,T])^2>0`

and `alpha,beta` are the inclusion marginals of the normalized weights `det^2/Z_Omega`, the diagonal-plus-PSD determinant expansion is simply restricted to `Omega`, and weighted AM-GM gives

`det(D_J+M^T D_I M) >= Z_Omega prod_i d_i^(alpha_i) prod_j e_j^(1-beta_j)`.

The sharp Hausdorff--Young/Jensen part is unchanged. Thus

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z_Omega^(-1/6)`          (1.1)

whenever `max alpha_i<=q/2`. This is an application of the completed theorem's determinant mechanism, not a new law assumption.

### 1.2 Aggregate singleton-augmentation identity

From fleet03/B09 `QFORM-RANK2-NOAUGMENT-AGGREGATE-STABILITY-v1`, canonical source
`yspennstate/math-open-problems@e8b97d9dcd8dd85cacc8fc73c2be4e86fde4b27a`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T114612Z-fleet03-B09-QFORM-r31/REPORT.md`:
for a full-rank two-column hub cross `C`, `G=C^T C`, `Delta=sqrt(det G)`, leaf block `D`, row leverages `ell_k`, `q_C=max ell_k<1`, and singleton-augmentation three-volume `Gamma_k`,

`Gamma_k^2 = Delta^2 (1-ell_k) delta_k^2`,

and with `S=sum_k Gamma_k^2`,

`S^(1/2)/Delta <= inf_(R=R^T,Lambda diagonal) ||D-C R C^T-Lambda||_F
 <= sqrt(2)/sqrt(1-q_C) * S^(1/2)/Delta`.                  (1.2)

The aggregate `S`, not `max Gamma_k`, is the dimension-free defect; the Walsh counterexample in that report rules out replacing `S` by the largest singleton volume.

## 2. New theorem: aggregate singleton volume compiles to one disjoint cut

### Theorem `QFORM-AGGREGATE-SINGLETON-VOLUME-TO-CUT-v1`

Let `H={h_1,h_2}` be two literal original coordinates and `L` a disjoint leaf bank. Condition any further outside coordinates; their effect is only to add arbitrary same-bank/affine terms. Write

`C=A[L,H] in R^(L x 2)`, `D=A[L,L]`.

For each `k in L`, form the three-column singleton-augmented physical cross matrix

`M^(k) = [ C_(L\{k}), D_(L\{k},k) ]`,

and set

`Gamma_k^2 = det((M^(k))^T M^(k)) >=0`,

with the determinant equal to zero when `rank M^(k)<3`. Put

`S=sum_(k in L) Gamma_k^2`.

Assume `S>0`. Then there is a literal physical bipartition

`L=I disjoint_union K`

such that, for the actual cross block

`B=A[I,H union K]=[C_I,D_(I,K)]`,

the restricted anchored three-volume

`Z= sum_(k in K) sum_(T subset I, |T|=3)
       det B[T,{h_1,h_2,k}]^2`                              (2.1)

satisfies

`boxed: Z >= S/16.`                                         (2.2)

Fix any `h` with `1/2<=h<3/4`, and let `alpha_i` be the row inclusion marginals of the normalized squared minors in (2.1). Then one of the following holds.

**(A) Diffuse-cut payment.** `max_(i in I) alpha_i<=h`, in which case the full quadratic form has a continuous density and

`boxed: ||p_Q||_infinity <= C_h S^(-1/6),`                  (2.3)

`boxed: P{Q in J0} <= C_h S^(-1/6)|J0|`                    (2.4)

for every interval `J0`, where with the sharp fractional-volume constant

`C_h = [3e/((3-4h)sqrt(2h))] 16^(1/6).`                     (2.5)

**(B) Literal aggregate-heavy row.** Some original physical leaf `i` has global singleton-volume row participation

`R_i := sum_k sum_(T subset L\{k}, |T|=3, i in T)
             det [C_T,D_(T,k)]^2`

satisfying

`boxed: R_i > (h/16) S.`                                    (2.6)

Since

`sum_i R_i=3S`,                                               (2.7)

the entire candidate set

`H_h={i:R_i>(h/16)S}`

has cardinality

`boxed: |H_h| < 48/h.`                                      (2.8)

In particular, at `h=2/3`, either

`boxed: ||p_Q||_infinity < 33.633 S^(-1/6)}`                (2.9)

with a continuous density and the identical linear interval bound, or a literal physical row belongs to a set of fewer than `72` candidates and carries more than `S/24` of the aggregate row participation.

### Proof of (2.2)

Choose a random physical coloring of every `k in L`, independently putting it in `I` or `K` with probability `1/2`. By Cauchy--Binet,

`Gamma_k^2 = sum_(T subset L\{k}, |T|=3)
               det [C_T,D_(T,k)]^2`.                         (2.10)

A term indexed by `(k,T)` appears in (2.1) exactly when `k in K` and all three elements of `T` lie in `I`. The four coordinates are distinct, so this event has probability `2^-4=1/16`. Therefore

`E Z = (1/16) sum_k Gamma_k^2 = S/16`.                       (2.11)

A deterministic physical partition with `Z>=S/16` follows.

### Proof of the dichotomy

For the partition chosen above, normalize the terms of (2.1) by `Z`. If every row marginal is at most `h`, apply (1.1) with `q=2h` and use `Z>=S/16`. This gives (2.3)--(2.5), continuity, and the direct `O(|J0|)` estimate.

Otherwise some `i in I` has `alpha_i>h`. Let `N_i` be the unnormalized restricted volume in (2.1) whose row triple contains `i`. Then

`N_i=alpha_i Z > h Z >= (h/16)S`.                            (2.12)

Every term counted by `N_i` is also counted by the global `R_i`, so `R_i>=N_i`, proving (2.6). Each global determinant term has exactly three row leaves, hence summing row participations counts every term three times and gives (2.7). Equation (2.8) follows immediately. QED.

The theorem is purely original-coordinate. The random coloring occurs only in the deterministic proof of existence of one fixed physical partition; no random rotation or randomization of the input law is introduced.

## 3. Consequence for genuinely arbitrary within-leaf curvature

Combine (2.9) with fleet03/B09's exact aggregate stability estimate (1.2). Let

`E_curv = inf_(R=R^T,Lambda diagonal) ||D-C R C^T-Lambda||_F`.

From the upper bound in (1.2),

`S >= (1/2)(1-q_C) Delta^2 E_curv^2`.                         (3.1)

Therefore, on the diffuse-cut branch at `h=2/3`,

`boxed: ||p_Q||_infinity
 <= 33.633 [ (1/2)(1-q_C) Delta^2 E_curv^2 ]^(-1/6)
 < 37.751 [Delta E_curv sqrt(1-q_C)]^(-1/3).`                (3.2)

The same coefficient multiplies interval length and the density is continuous. Thus an arbitrary same-bank leaf operator that is quantitatively far from `C Sym_2 C^T + diagonal` is paid unless its aggregate third-volume is forced through one of fewer than `72` literal high-volume rows. No residual quadratic operator is discarded as a small random error.

This is the new B09 structural bridge: the prior `sum Gamma_k^2` defect is now converted into an actual disjoint bilinear cut or a bounded physical-row collar.

## 4. Exact full-target stress family for the new compiler

Let `m>=4` be even. Take two physical hubs `x_1,x_2` and three disjoint leaf groups `G_1,G_2,G_3`, each of size `m`. Let

`c_1=m^(-1/2) 1_(G_1)`, `c_2=m^(-1/2)1_(G_2)`, `u=m^(-1/2)1_(G_3)`,

and

`Q_m = 2 X_(h1)<c_1,X> + 2 X_(h2)<c_2,X> + <u,X>^2`.        (4.1)

On the deterministic coefficient subspace `{e_h1,c_1,e_h2,c_2,u}`, the matrix is the direct sum of two hyperbolic blocks and one positive square, so

`spec_nonzero(Q_m)={1,-1,1,-1,1}`.                            (4.2)

Hence this is a literal full-target family for every admissible product law.

For `k in G_3`,

`Gamma_k^2 = u_k^2 ||u_(G_3\{k})||^2
           = (1/m)(1-1/m)`,

and all other `Gamma_k` vanish. Thus

`S=1-1/m`.                                                     (4.3)

Now split `G_3` into equal halves `I_3,K_3`, put `K=K_3`, and put `I=G_1 union G_2 union I_3`. The actual cross `A[I,H union K]` has singular values

`1,1,1/2`,                                                     (4.4)

because its third block is exactly `u_(I_3) u_(K_3)^T`. Therefore the anchored restricted volume is

`Z=(1*1*1/2)^2=1/4`.                                          (4.5)

Its row marginals are `1/m` on `G_1`, `1/m` on `G_2`, and `2/m` on `I_3`, so the q=1 gate already holds. The sharp fractional-volume theorem gives

`boxed: ||p_(Q_m)||_infinity <= 3e (1/4)^(-1/6)
 =3e 2^(1/3) <10.275,`                                       (4.6)

and

`boxed: P{Q_m in J0}<10.275 |J0|`.                           (4.7)

The physical hub couplings are `m^(-1/2)` and the dense leaf-square coefficients are `m^(-1)`, so every displayed physical coefficient diffuses to zero while the estimate stays dimension-free.

## 5. Designated partner fleet02/B09 applied to an actual inequality

The newest completed fleet02/B09 theorem consumed here is
`QFORM-GROUPED-ONEHUB-DENSE-HUB-CURVATURE-v1`, canonical source
`yspennstate/math-open-problems@46f88948cb35d25a7b146a31c223ec83ca23d65a`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T103752Z-fleet02-B09-QFORM-auto11/REPORT.md`.
It states

`||p_Q||_infinity <=3e [rho |lambda| Delta]^(-1/3)`           (5.1)

for a grouped rank-one hub/leaf cross with one exact leaf square, while retaining arbitrary dense hub-bank curvature.

Apply it to a nonuniform mixed frame. On one 16-coordinate physical hub bank take two overlapping Walsh-flat orthonormal vectors `p,w`. On the leaf side take `v` uniform on a 16-coordinate group, and take `c` on a disjoint 17-coordinate group with squared coefficients

`(1/2,1/32,...,1/32)`

(the value `1/32` occurring 16 times). Then `p,w,c,v` are orthonormal in the deterministic coefficient geometry except for the intentional same-bank overlap of `p,w`, and

`F=2<p,X_H><c,X_I> + <v,X_I>^2 + <w,X_H>^2`.                 (5.2)

Its nonzero spectrum is exactly

`{1,-1,1,1}`,                                                  (5.3)

so it satisfies the original target hypothesis. Here `lambda=Delta=1`. The whitened two-frame basis law chooses one coordinate from the `v` support and one from the `c` support. Hence

`rho=(1-sum v_i^4)(1-sum c_i^4)
    =(15/16)(1-(1/4+1/64))
    =(15/16)(47/64)=705/1024`.                               (5.4)

At the actual inequality (5.1),

`boxed: ||p_F||_infinity <=3e (705/1024)^(-1/3)
 =9.2353356301... <9.236,`                                    (5.5)

and `P{F in J0}<9.236|J0|`. The density is continuous. The two projected hub variables are not declared independent; the theorem retains the dense same-bank hub square inside its complex conditional amplitude.

## 6. Scope, correction safety, and next unpaid implication

This run does **not** claim that `S` is universally bounded below by `s_3(A)>=1`, and it does not claim that a high-volume row automatically yields a good scalar pivot. The source correction `max Gamma_k ->0` does not imply low-rank closeness is respected: the compiler uses the full aggregate `S=sum Gamma_k^2`.

The first unpaid B09 implication is now

`QFORM-AGGREGATE-HEAVYROW-COLLAR-ELEVATION-v1`:

starting from the branch in which the aggregate singleton volume is routed through one of fewer than `72` literal rows, use that bounded candidate set without conditioning away the third spectral resource. Either elevate a candidate row into an already-paid physical-pivot/grouped-hub packet, or prove that after removing/elevating the collar a residual determinant family still has a diffuse fixed-cut certificate. The arbitrary complementary quadratic phase must remain exact.

Full QFORM essential boundedness and full-target continuity remain OPEN. The new theorem has not received the two independent end-to-end reviews required for a full candidate.
