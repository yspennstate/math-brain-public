SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-23T15:34:32Z.
attacking: arbitrary same-side curvature in the superdiffuse near-coloop survivor—prove a rank-two cross L^{3/2} compiler that keeps both projected pairs dependent, then identify the exact missing half-power.

# fleet02/B16 — rank-two cross L^{3/2}, fresh-square closure, and overlap-curvature obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREMS + NEW MECHANISM OBSTRUCTION / FULL QFORM OPEN`  
**Regularity:** the fresh-square and transverse-low-rank branches below have continuous densities; the bare L^{3/2} cross theorem is only a characteristic-function estimate.  

## 1. First unpaid implication and source discipline

The full target is unchanged: arbitrary independent original-coordinate inputs with one-dimensional densities at most one, arbitrary dimension, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No support, moment, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumption is introduced. Continuity remains separate from essential boundedness.

The latest **completed** designated partner actually used here is fleet03/B16 r29,

`yspennstate/math-open-problems@4da4d30d980b1eafd4074401ff0e4727abefc524`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260923T132339Z-fleet03-B16-QFORM-r29/REPORT.md`.

After its physical-diagonal and physical-pair exits, the exact-rank-three true-near-coloop survivor has hub leverage `c>63/64`, normalized physical hub-star atoms `<1/251`, and at least 80 disjoint original-coordinate source banks. Its explicit debt is to retain the same-side curvature jointly with those source banks. The preceding fleet02/B16 run paid a rank-two cross cut when the curved side is diagonal in ORIGINAL coordinates. The first question here is what survives when **both same-side blocks are completely arbitrary**.

The required pinned package is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

I use its completed two-dimensional product-marginal input at equations below: if `U` has two orthonormal columns and `X` is an original-coordinate product law with density caps one, then

`||p_(U^T X)||_infinity <=2`.                                      (1.1)

This is a **joint** density bound. It is never upgraded to independence of the two projected coordinates or to a uniform conditional density cap.

## 2. New theorem: arbitrary self-curvature costs exactly a borderline `L^{3/2}`

### `QFORM-CROSS2-ARBITRARY-SELFBLOCK-L32-v1`

Partition the active ORIGINAL coordinates as `I disjoint union J`; arbitrary other original coordinates may first be conditioned. Suppose the physical cross block has exact rank two,

`M=A_IJ=U Sigma V^T`,
`Sigma=diag(s_1,s_2)`, `s_1>=s_2>0`,                              (2.1)

where `U,V` have orthonormal columns. Allow **arbitrary symmetric** same-side blocks `A_II,A_JJ` and arbitrary affine terms. Let `phi(t)` be the conditional characteristic function of the resulting quadratic polynomial. Then

`boxed:
 |phi(t)| <= min(1, 2 pi / (|t| sqrt(s_1 s_2))).`                 (2.2)

Consequently

`boxed:
 integral_R |phi(t)|^(3/2) dt <= 12 pi / sqrt(s_1 s_2).`          (2.3)

No diagonal or low-rank assumption is made on either same-side block.

### Proof

Put

`Z=U^T X_I`, `W=V^T X_J`.                                         (2.4)

The vectors `Z` and `W` are genuinely independent of one another because `I,J` are disjoint original-coordinate source banks. Their **internal** coordinates may be dependent. By (1.1),

`||p_Z||_infinity, ||p_W||_infinity <=2`.                          (2.5)

Write the conditioned form as

`Q=R_I(X_I)+R_J(X_J)+2 Z^T Sigma W`,                               (2.6)

where `R_I,R_J` are arbitrary real quadratic-plus-affine polynomials on their respective source banks. For each `t`, define the complex pushforward densities

`a_t(z)=p_Z(z) E[exp(i t R_I(X_I)) | Z=z]`,
`b_t(w)=p_W(w) E[exp(i t R_J(X_J)) | W=w]`.                        (2.7)

Then

`|a_t|<=p_Z`, `|b_t|<=p_W`,
`||a_t||_1,||b_t||_1<=1`,
`||a_t||_2,||b_t||_2<=sqrt(2)`.                                   (2.8)

The exact product-source factorization is

`phi(t)=int_R2 int_R2 a_t(z)b_t(w)
        exp(2 i t z^T Sigma w) dz dw`.                             (2.9)

With Fourier convention

`hat a(xi)=int exp(i xi.z)a(z) dz`,                               (2.10)

Cauchy-Schwarz in `w`, the change of variables `xi=2t Sigma w`, and two-dimensional Plancherel give

`|phi(t)|
 <= ||b_t||_2 [int |hat a_t(2t Sigma w)|^2 dw]^(1/2)`

` <= sqrt(2)
    [ (4 t^2 s_1s_2)^(-1) (2pi)^2 ||a_t||_2^2 ]^(1/2)`

` <= 2pi / (|t| sqrt(s_1s_2)).`                                  (2.11)

This proves (2.2). If `B=2pi/sqrt(s_1s_2)`, then

`int_R min(1,(B/|t|)^(3/2)) dt=6B`,                               (2.12)

which is exactly (2.3). QED.

### Interpretation

The arbitrary same-side curvature has disappeared into the modulus-one conditional amplitudes (2.7), but the price is exact: a nondegenerate rank-two cross source interaction provides only a `|t|^{-1}` pointwise envelope and an `L^{3/2}` characteristic function. This is not enough for Fourier inversion by itself. The remaining debt is one genuine `L^3` factor, equivalently one additional half-power of time decay supplied without destroying source provenance.

This theorem is complementary to the pinned rank-three volume theorem: it works when the cross block has only rank two, where every 3-volume certificate vanishes, and it does so without diagonalizing the same-side phases.

## 3. New theorem: one genuinely fresh square closes the missing half-power

### `QFORM-CROSS2-PLUS-FRESH-SQUARE-v1`

Keep the hypotheses of Section 2. Suppose in addition there is a disjoint original-coordinate scalar `Y`, independent of both active banks, with density cap `L`, and after conditioning all other original coordinates the form separates as

`Q=Q_0(X_I,X_J)+lambda Y^2+mu Y+constant`,
`lambda !=0`.                                                       (3.1)

Then `Q` has a continuous density and

`boxed:
 ||p_Q||_infinity
 <=900^(1/3) L^(2/3)
   (|lambda| s_1 s_2)^(-1/3).`                                    (3.2)

For a cap-one physical scalar,

`900^(1/3)=9.654893846056...`.                                    (3.3)

### Proof

Scale `Y` to cap one. Completing the square leaves only a translate of a cap-one variable squared. If `g(t)` denotes the characteristic function of `lambda Y^2+mu Y`, the standard square-density/Hausdorff-Young estimate gives

`int_R |g(t)|^3 dt <= 50pi L^2/|lambda|`.                           (3.4)

(The cap-one case is `50pi/|lambda|`; replacing `Y` by `LY` gives the factor `L^2`.) The separated source scalar makes the total characteristic function equal to `phi_0(t)g(t)`. Hölder with exponents `3/2` and `3`, followed by (2.3), yields

`integral |phi_0 g|
 <=(12pi/sqrt(s_1s_2))^(2/3)
    (50pi L^2/|lambda|)^(1/3)`.                                   (3.5)

Dividing by `2pi` gives

`(7200)^(1/3)/2=900^(1/3)`,                                       (3.6)

which proves (3.2). The right side of (3.5) is an `L^1` Fourier majorant, hence the density is continuous. QED.

### Target-valid diffuse application with genuinely dependent projected pairs

Let `C,D` be `m x 2` matrices with orthonormal columns, chosen for example from balanced sign frames, and let `X,Ybank` be two disjoint original-coordinate product banks. Put

`Z=C^T X`, `W=D^T Ybank`.                                          (3.7)

The coordinates inside `Z` and inside `W` need not be independent. Let `B_X,B_Y` be **arbitrary symmetric** matrices on their respective source banks with

`||B_X||_op, ||B_Y||_op <=1/2`,                                   (3.8)

and let `T` be one further independent cap-one coordinate. Consider

`Q=X^T B_X X+Ybank^T B_Y Ybank+4 Z^T W+T^2`.                      (3.9)

Its cross block is `2 C D^T`, hence `s_1=s_2=2`. Before adding the two self blocks the cross part has eigenvalues `{2,2,-2,-2}`; (3.8) moves each of those by at most `1/2`, while the separated `T^2` contributes an exact eigenvalue `1`. Thus this is a strict member of the full target class, with at least three eigenvalues of modulus at least one.

Equation (3.2) gives for **all** independent cap-one source laws

`boxed:
 ||p_Q||_infinity
 <=900^(1/3) 4^(-1/3)
 =6.08220199557... <6.083.`                                       (3.10)

This is an actual higher-rank, non-diagonal, arbitrary-same-side-curvature application of the completed two-dimensional product-marginal result. Nothing in (3.10) treats `Z_1,Z_2` or `W_1,W_2` as independent.

## 4. New theorem: transverse low-rank same-side curvature can itself provide the missing decay

The previous theorem requires a source-separated square. There is another safe branch when part of the same-side curvature lives in directions independent, at the coefficient-frame level, of the rank-two cross plane.

### `QFORM-PROJECTED-2HUB-TRANSVERSE-LOWRANK-SIDE-v1`

Again condition arbitrary outside original coordinates and split the active coordinates as `I disjoint union J`. Assume

`A_IJ=U Sigma V^T`, `Sigma=diag(s_1,s_2)`,                         (4.1)

and on the `J` source bank

`A_JJ=D+R Lambda R^T`,                                             (4.2)

where `D` is diagonal in the ORIGINAL `J` coordinates, `R^T R=I_r`, and

`Lambda=diag(lambda_1,...,lambda_r)`, `lambda_l !=0`.               (4.3)

For `j in J`, set

`rho_j=Sigma V_{j,*}^T in R^2`,
`q_j=(rho_j,R_{j,*}) in R^(2+r)`,
`G=sum_j q_j q_j^T`.                                               (4.4)

Assume `G` is positive definite and every normalized row leverage satisfies

`c_j=q_j^T G^(-1) q_j <=1/2`.                                     (4.5)

Then, with arbitrary `A_II` and arbitrary affine/outside terms, the full conditional law has a continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_r
 [ (prod_l |lambda_l|) det G ]^(-1/(r+4)),`                       (4.6)

where

`C_r=4 (r+4)/(r+2) 2^(-2/(r+4)).`                                 (4.7)

In particular

`C_0=4sqrt(2)=5.656854...`,
`C_1=5.052388555...`,
`C_2=4.762203156...`.                                             (4.8)

For `r=0`, (4.6) is exactly the preceding fleet02/B16 diagonal-side theorem because `det G=(s_1s_2)^2`.

### Proof

As in Section 2, disintegrate the `I` source bank over the dependent projected pair `Z=U^T X_I`, using only `p_Z<=2`. For fixed `z`, Fresnel-linearize the `r` squares in (4.2); keep the original-coordinate diagonal twist `D` inside

`g_j(x)=exp(i t d_j x^2) f_j(x)`.                                 (4.9)

The pinned one-dimensional twisted Fourier estimate from the required package is

`int |hat g_j|^p <=4pi/sqrt(p)`, `p>=2`.                           (4.10)

After the substitution `y=2tz`, the `z`-Jacobian contributes `(2|t|)^(-2)`. The Fresnel prefactor contributes

`(4pi|t|)^(-r/2) prod_l |lambda_l|^(-1/2)`.                        (4.11)

The remaining integral is over `R^(2+r)` and has original-coordinate product factors

`prod_j |hat g_j(<q_j,(y,u)>+t b_j)|`.                             (4.12)

Geometric Brascamp-Lieb with the leverage exponents `c_j` and (4.10) gives

`int_(R^(2+r)) (4.12)
 <=(4pi)^(2+r) det(G)^(-1/2)`.                                    (4.13)

Therefore

`|phi(t)|
 <=(1/2)(4pi)^(2+r/2)
   [ (prod |lambda_l|) det G ]^(-1/2)
   |t|^(-(2+r/2)).`                                                (4.14)

If `p=2+r/2` and the coefficient in (4.14) is `B`, then

`int min(1,B|t|^-p)dt=2p/(p-1) B^(1/p)`.                           (4.15)

Fourier inversion simplifies (4.15) exactly to (4.6)-(4.7). QED.

### Direct partner-r29 consequence

This pays a genuinely new subbranch of the r29 superdiffuse debt: whenever a useful rank-two original-coordinate cross cut has its same-side curvature equal to `diagonal + rank one`, and the **augmented three-dimensional coefficient frame** (two cross directions plus that curvature direction) satisfies (4.5) with quantitative

`|lambda_1| det G >= eta>0`,                                      (4.16)

then

`boxed: ||p_Q||_infinity <=5.053 eta^(-1/5).`                      (4.17)

Thus non-diagonal same-side curvature is not automatically an obstruction; a transverse rank-one piece is actually useful. What remains difficult is curvature that is coefficient-wise **overlapping** with the cross plane, for which the absolute Fresnel augmentation becomes linearly redundant and `G` is singular.

## 5. Exact true-near-coloop stress: every useful physical bank is non-diagonal and has macroscopic aggregate curvature

Return to the fully shared Walsh family previously paid by fleet02/B16. Fix

`0<a<1/64`, `c=1-a`, and m>=512 divisible by four.                 (5.1)

Choose all four sign pairs `(epsilon_j,tau_j) in {+1,-1}^2` equally often and take the Parseval rows

`r_0=(sqrt(c),0,0)`,
`r_j=m^(-1/2)(sqrt(a),epsilon_j,tau_j)`.                           (5.2)

With

`Lambda=[[0,1,0],[1,0,0],[0,0,1]]`,                              (5.3)

we have `R^T R=I_3` and the nonzero spectrum is exactly `{1,-1,1}`. The physical entries are

`A_00=0`,
`A_0j=sqrt(c) epsilon_j/sqrt(m)`,
`A_jk=[sqrt(a)(epsilon_j+epsilon_k)+tau_j tau_k]/m`.                (5.4)

Hence

`R_*^2=sum_j A_0j^2=c`,
`p_j=A_0j^2/R_*^2=1/m<1/251`,                                    (5.5)

and for `m>=512`,

`|A_0j|<1/16`,
`|A_jj|=(1+2sqrt(a)epsilon_j)/m<1/64`.                             (5.6)

Thus the family sits inside the quantitative r29 superdiffuse-star gate, rather than being excluded by the physical pivot/pair exits.

### 5.1 No diagonal-side rank-two cut exists

For two distinct leaves:

- if `epsilon_j=-epsilon_k`, then `A_jk=tau_j tau_k/m`, so `|A_jk|=1/m`;
- if `epsilon_j=epsilon_k`, then

`|A_jk|>= (1-2sqrt(a))/m >3/(4m)`.                                (5.7)

Every leaf-leaf off-diagonal entry is therefore nonzero. Every hub-leaf entry is also nonzero. Consequently **every original-coordinate principal block of size at least two is non-diagonal**. A one-coordinate `J` has cross rank at most one. Thus the previous diagonal-side rank-two compiler cannot apply to any physical cut of this family.

### 5.2 The partner-sized banks carry non-negligible aggregate same-side curvature

Let `B` be any leaf bank of size `N` with partner star mass

`N/m=sum_(j in B) p_j >=1/120`.                                   (5.8)

On this bank

`A_BB=(1/m)[ sqrt(a)(1 epsilon^T+epsilon 1^T)+tau tau^T ]`.         (5.9)

Testing the Rayleigh quotient on the sign vector `tau` gives

`tau^T A_BB tau / ||tau||^2
 =N/m +(2sqrt(a)/(mN))
   (sum_B tau_j)(sum_B epsilon_j tau_j)`

` >=(1-2sqrt(a))N/m
 >1/160.`                                                          (5.10)

The diagonal part has operator norm

`||diag(A_BB)||_op <=(1+2sqrt(a))/m <5/(4m)<=1/320`.               (5.11)

Therefore

`boxed:
 ||A_BB-diag(A_BB)||_op >1/320`                                   (5.12)

for every partner-sized bank. Thus the same-side curvature is **aggregate-macroscopic** on every bank even though every individual physical coefficient is `O(1/m)`.

This explicitly rules out a compiler that first partitions into r29 banks and then treats their off-diagonal same-side curvature as uniformly negligible merely because all physical entries are tiny. For unbounded input laws there was already no legitimate small-random-perturbation principle; (5.12) shows here that even the deterministic bank operator norm is bounded away from zero.

### 5.3 No fresh physical square is available either

Because all hub-leaf and all leaf-leaf off-diagonal entries in (5.4) are nonzero, no physical source coordinate is quadratically separated from a nontrivial rank-two cross subsystem. Therefore the fresh-square theorem of Section 3 cannot close this exact family by selecting one physical coordinate. A successful use of Section 3 in the true near-coloop survivor would have to manufacture the `L^3` factor by a **source-bank aggregate**, not by a lone coordinate.

This is a mechanism obstruction, not a QFORM counterexample. The same Walsh family was already controlled globally by the preceding fleet02/B16 source-plane/source-line compiler,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260923T123056Z-fleet02-B16-QFORM-7d2c4a91/REPORT.md`,

which gives

`boxed: ||p_Q||_infinity <27.015`                                 (5.13)

uniformly in `a,m` and all independent cap-one source laws by grouping the four original sign classes before curvature payment.

The required pinned ruled theorem C also gives, at its exact one-sheet scope,

`boxed: p_Q(s)<=pi sqrt(2) for a.e. s>=0`,                        (5.14)

using a two-dimensional product marginal along the ruling lines and never projected independence. Thus both (5.13) and (5.14) confirm that the overlap geometry is a proof-interface obstruction rather than a true density blow-up.

## 6. What changed in the proof map

The r29 same-side-curvature debt now has a quantitative three-level classification.

1. **Arbitrary curvature + rank-two cross:** Section 2 gives a uniform `L^{3/2}` characteristic-function estimate. No diagonalization is needed.
2. **Any genuine extra `L^3` source factor:** a source-separated square closes the branch with the explicit continuous-density bound (3.2).
3. **Transverse rank-one same-side curvature:** Section 4 converts it directly into extra Fresnel dimension and closes the branch with (4.17).

Therefore the genuinely unpaid mechanism is narrower than “non-diagonal curvature.” It is **overlapping curvature**: the same original source banks carry the cross two-plane and the extra curvature in a way that supplies no source-separated square and no coefficient-frame transverse Fresnel direction.

The Walsh calculation shows this obstruction can persist simultaneously on every superdiffuse bank while the actual density remains uniformly bounded. The missing theorem must retain the relative phase between the rank-two cross oscillation and this overlapping curvature long enough to recover one additional half-power; taking absolute values before resolving the overlap loses exactly the resource that Section 2 lacks.

## 7. Next unpaid implication

I record the next B16 target as

**`QFORM-SUPERDIFFUSE-OVERLAP-HALFPOWER-TRANSDUCER-v1`.**

Starting from the fleet03/B16 r29 eighty-bank survivor, find either

- a rank-two original-coordinate cross cut plus a genuinely source-separated bank aggregate whose quadratic contribution has an `L^3` characteristic function at universal scale; or
- an overlap-sensitive analogue of Section 4 that uses same-bank curvature sharing the cross two-plane and upgrades the Section-2 `L^{3/2}` estimate to `L^1` without normalizing conditional projection densities or inferring projected independence.

A proof may use two-dimensional product marginals as joint densities in locally integrable/Fourier kernels, but may not replace them by independent projected coordinates. Arbitrary additional spectrum remains a separate global interface after the exact-rank-three near-coloop step.

## 8. Status

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The results above are supporting theorems and a source-valid mechanism obstruction. Continuity is proved on Sections 3 and 4 only; no global continuity claim is made.
