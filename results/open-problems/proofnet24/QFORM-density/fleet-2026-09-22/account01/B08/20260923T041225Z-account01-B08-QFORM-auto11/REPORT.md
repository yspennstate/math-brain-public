SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T04:12:25Z.
attacking: scale-sensitive near-rank-one recoloring: either genuine third-volume smoothing, localized bicolop currency, or quantitative second-exterior cross currency.

# account01/B08 — robust recoloring: third volume or second exterior cross mass

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T041225Z-account01-B08-QFORM-auto11`  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

The unrestricted target remains OPEN. Nothing below claims that the three-large-eigenvalue hypothesis by itself forces the extra second-stage child-window hypotheses in Section 6. Continuity is proved only on the paid third-volume branch explicitly identified below.


## 1. Sources consumed at equations

1. Latest completed designated partner account02/B08: `QFORM-DIFFUSE-HYBRID-VOLUME-TAIL-LADDER-v1`, canonical mathematics

   `yspennstate/math-open-problems@31212dc0982ef58cdae6fc12c9354599a663fad6`,

   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T020620Z-account02-B08-QFORM-auto11/REPORT.md`.

   In its selected-three leverage `<=1/48` branch, with

   `rho=sqrt(3/5)`, `beta=(3/16)rho L`,

   the k=2 survivor is either already paid, a 3-volume bicolop, a very tight rank-two tube, or a rank-one Frobenius tube

   `dist_F(B,{rank<=1})<beta/8`.

2. Previous B08 bilateral-curvature theorem:

   `yspennstate/math-open-problems@9534b12fbf558d1b6c82db1bc55068afd764fcce`.

   In the partner rank-one tube it supplies two actual child eigenvalues on each physical bank larger than

   `kappa_* L`, `kappa_*=sqrt(3/5)-3/128=0.751159169241483...`.

3. Previous B08 recoloring theorem and its falsifier:

   `yspennstate/math-open-problems@e18687997f34a76c422a1d8c76f2cdeba38faff1`,

   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T033753Z-account01-B08-QFORM-auto11/REPORT.md`.

   Exact rank-one outer coupling plus two rank-two child cross blocks gives a 3-volume exit. But scale-free stability under `dist_F(B,rank<=1)->0` is false: a huge rank-one core can multiply a tiny perturbation and annihilate the recolored third volume. The present theorem identifies exactly what currency is forced when that happens.

4. Fractional second-volume theorem, used only in Section 5 as an additional finite-p receiver:

   `QFORM-FRACTIONAL-E2-BL-L3-v1`, account03/B01,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T223030Z-auto12/REPORT.md`.

## 2. Notation

For a real matrix `T`, write

`E_k(T)=e_k(T^T T)=||wedge^k T||_HS^2`.

Thus `E_2(T)` is the total squared physical 2-minor volume and `E_3(T)` is the total squared physical 3-minor volume.

Take an ORIGINAL-coordinate partition `I=I_+ disjoint_union I_-`, `J=J_+ disjoint_union J_-`. Let

`C=A[I_+,I_-]`, `D=A[J_+,J_-]`, `B=A[I,J]`,

and assume

`s_2(C)>=c`, `s_2(D)>=c`                                      (2.1)

for some `c>0`. Recolor the physical coordinates as

`K=I_+ union J_+`, `L=I_- union J_-`.

The true recolored physical cross block is

`M=A[K,L]
  =[[C,                  B[I_+,J_-]],
    [B[I_-,J_+]^T,       D           ]]`.                      (2.2)

No rank assumption is made on `B` in the theorem below.

## 3. The 4-by-4 cofactor lemma

### Lemma 3.1 — `QFORM-RECOLOR-COFACTOR-DEFECT-v1`

For arbitrary real `2x2` matrices `U,V`, put

`N=[[I_2,U],[V,I_2]]`.

Then

`boxed: E_3(N)>=||I_2-VU||_F^2`,                              (3.1)

and symmetrically

`E_3(N)>=||I_2-UV||_F^2`.                                    (3.2)

#### Proof

For a `4x4` matrix, `E_3(N)` is exactly the squared Frobenius norm of its cofactor matrix, equivalently of `adj(N)`.

Whenever `N` is invertible, the Schur-complement inverse formula gives

`[adj(N)]_(22)
 =det(N)[N^(-1)]_(22)
 =det(I_2-VU)(I_2-VU)^(-1)
 =adj(I_2-VU)`.                                                (3.3)

Both sides are polynomial in the entries, so (3.3) holds for every `U,V`, including singular cases. Hence

`E_3(N)=||adj(N)||_F^2
       >=||adj(I_2-VU)||_F^2`.                                (3.4)

For every real `2x2` matrix `S`, `||adj S||_F=||S||_F`, proving (3.1). Interchanging the two block sides proves (3.2). QED.

The key point is that a collapse of recolored third volume forces the multiplicative defect `VU-I` to be small. This is the exact scale-sensitive replacement for the false continuity argument in the previous run.

## 4. Main theorem — third volume OR second exterior cross mass

### Theorem 4.1 — `QFORM-RECOLOR-E3-OR-ORIGINAL-E2-v1`

Under (2.1), for every `0<delta<1`, at least one of the following holds:

`(A)  E_3(M)>=delta^2 c^6`,                                   (4.1)

or

`(B)  s_1(B)s_2(B)>=(1-delta)c^2`.                            (4.2)

Consequently branch (B) has the aggregate second-exterior lower bound

`boxed: E_2(B)>=(1-delta)^2 c^4`.                             (4.3)

No dimension, support, moment, sign, or distributional assumption enters this deterministic theorem.

#### Proof

Choose top-two left/right singular subspaces of `C` and of `D`, and compress (2.2) blockwise to a `4x4` matrix

`M_4=[[C_0,U_0],[V_0,D_0]]`,                                  (4.4)

where `C_0,D_0` are invertible `2x2` matrices with every singular value at least `c`. Orthogonal compression contracts exterior Hilbert-Schmidt norm, hence

`E_3(M)>=E_3(M_4)`.                                           (4.5)

Factor

`M_4=diag(C_0,D_0) N`,

`N=[[I_2,U],[V,I_2]]`,

`U=C_0^(-1)U_0`, `V=D_0^(-1)V_0`.                            (4.6)

Every singular value of `diag(C_0,D_0)` is at least `c`, so the least singular value of its third exterior power is at least `c^3`. Thus

`E_3(M)>=c^6 E_3(N)`.                                         (4.7)

Suppose (A) fails. Then `E_3(N)<delta^2`. By Lemma 3.1,

`||I_2-VU||_op<=||I_2-VU||_F<delta`.                          (4.8)

Therefore

`s_min(VU)>1-delta`,

and, since `VU` is `2x2`,

`|det V det U|=|det(VU)|>(1-delta)^2`.                        (4.9)

Undoing the normalization,

`|det U_0 det V_0|
 >(1-delta)^2 |det C_0 det D_0|
 >=(1-delta)^2 c^4`.                                          (4.10)

Each of `U_0` and `V_0` is a `2x2` orthogonal compression of a physical subblock of `B` or `B^T`. Hence

`|det U_0|<=||wedge^2 B||_op=s_1(B)s_2(B)`,
`|det V_0|<=s_1(B)s_2(B)`.                                   (4.11)

Combining (4.10)-(4.11) gives

`[s_1(B)s_2(B)]^2>(1-delta)^2 c^4`,

which proves (4.2). Finally `E_2(B)>=s_1(B)^2s_2(B)^2`, proving (4.3). QED.

### Interpretation

The previous near-rank-one counterexample is now explained rather than merely excluded. A tiny Frobenius tail can destroy the recolored 3-volume only when it is multiplied by enough rank-one scale to create a **fixed second exterior product**. Thus the correct perturbation parameter is not `dist_F(B,rank<=1)` alone; it is the multiplicative two-volume currency `s_1(B)s_2(B)`.

## 5. Concrete `delta=1/4` routing

Take `delta=1/4`. Theorem 4.1 yields

`E_3(M)>=c^6/16`                                               (5.1)

or

`s_1(B)s_2(B)>=3c^2/4`,
`E_2(B)>=9c^4/16`.                                             (5.2)

### 5.1 Third-volume branch

Let `Z=E_3(M)`. If either the row or column third-volume marginals of `M` are all at most `2/3`, apply the completed `q=4/3` fractional three-volume theorem (transposing `M` if necessary). Then the full ambient quadratic form has a continuous `C_0` density and

`||p_Q||_infinity
 <=(9 sqrt(3)e/2) Z^(-1/6)
 <=(9 sqrt(3)e/2) 2^(2/3) c^(-1)
 <33.633/c`.                                                   (5.3)

If both the row and column third-volume gates fail, choose a physical row `i` and column `j` with inclusion marginals greater than `2/3`. Their joint inclusion probability is greater than `1/3`, so the double-incident physical 3-minor bank satisfies

`W_ij^(3)>Z/3>=c^6/48`.                                       (5.4)

Thus branch (5.1) is either fully paid with continuity or converted into a localized bicolop certificate.

### 5.2 Second-exterior branch

In branch (5.2), if either the row or column order-two volume marginals of `B` are all at most `2/3`, apply account03/B01 `QFORM-FRACTIONAL-E2-BL-L3-v1` at `theta=3/4`. It gives the full ambient law an `L^3` density satisfying

`boxed: ||p_Q||_3 <8.186 c^(-2/3).`                           (5.5)

This is finite-p smoothing, not yet an `L^infinity` conclusion.

If both order-two marginal gates fail, choose a heavy physical row and column. Their joint order-two-volume inclusion probability exceeds `1/3`, hence

`W_ij^(2)>E_2(B)/3>=3c^4/16`.                                 (5.6)

So the second-exterior branch is itself either diffuse `L^3` smoothing or a localized order-two bicolop.

## 6. Actual application of designated partner account02/B08

Now enter the partner's selected-three `<=1/48` k=2 rank-one-tube branch. From the partner theorem,

`dist_F(B,{rank<=1})<epsilon_*`,

`epsilon_*=(beta/8)
 =(3/128)sqrt(3/5)L
 =0.0181546094353473... L`.                                   (6.1)

The preceding B08 bilateral-curvature theorem gives two actual child eigenvalues on each side larger than

`kappa_*L=(sqrt(3/5)-3/128)L`.                                (6.2)

As in the previous run, impose the explicit second-stage diffuse child-window condition on each child:

- the two-eigenvector child window has row leverage `<=1/32`;
- the remaining child spectral operator norm is `<=L/64`.

The rank-two frame splitter then produces internal physical cuts with

`c>=c_* L`,

`c_*=(3/8)(sqrt(3/5)-3/128)-1/64
    =0.266059688465556...`.                                   (6.3)

Apply Theorem 4.1 at `delta=1/4`. There are three source-valid outcomes:

**(P) paid continuous density**

`boxed: ||p_Q||_infinity<126.409/L`,                           (6.4)

with a continuous `C_0` density;

**(V3) localized third-volume bicolop**

`boxed: W_ij^(3)>7.3898093e-6 L^6`;                           (6.5)

or

**(E2) robust outer second-exterior mass**

`boxed: s_1(B)s_2(B)>0.05309081836 L^2`,

`boxed: E_2(B)>0.002818634995 L^4`.                            (6.6)

Because the partner tube (6.1) implies by Eckart--Young that `s_2(B)<epsilon_*`, outcome (E2) sharpens further to

`boxed: s_1(B)>2.9243712765 L`,                               (6.7)

and therefore

`s_1(B)/s_2(B)>161.08`.                                       (6.8)

This is the requested actual use of the designated partner theorem: the genuine near-rank-one tube is no longer left as an uncontrolled perturbative remainder. Either it is paid, converted to a 3-volume bicolop, or forced into a quantitatively huge anisotropic rank-one core carrying fixed second-exterior currency.

Inside outcome (E2), the order-two refinement of Section 5.2 gives either

`||p_Q||_3<19.789 L^(-2/3)`                                  (6.9)

or a localized physical order-two bicolop

`W_ij^(2)>9.39544e-4 L^4`.                                   (6.10)

Again, (6.9) is an `L^3` statement, not a full target bound.

## 7. What changed relative to the previous run

The previous run proved exact-rank-one recoloring but produced a counterexample to naive near-rank-one continuity. The new cofactor-defect lemma repairs that exact gap with an exhaustive, scale-sensitive statement valid for arbitrary outer cross rank. It shows that the obstruction family necessarily pays in second exterior volume: the `R*epsilon=1` cancellation is not an accident but precisely the mechanism captured by (4.2).

No coefficient-small tail is dropped probabilistically. The only smallness-to-structure step is deterministic matrix algebra.

## 8. First unpaid implication

`QFORM-HUGE-RANK1-CORE-E2-RECEIVER-v1`:

In the partner near-rank-one tube after the new routing, pay the remaining branch where

`dist_F(B,rank<=1)<0.018155L`,
`s_1(B)>2.924L`,
`E_2(B)>0.002818L^4`,

and where third-volume recoloring did not already pay. The next mechanism should combine the enormous rank-one channel with either the diffuse order-two `L^3` resource or the localized order-two bicolop, while retaining both child curvatures and the true nonzero tail. A scale-free perturbation argument is now unnecessary and remains forbidden by the previous counterexample.

Full QFORM remains OPEN; no global continuity claim is made.
