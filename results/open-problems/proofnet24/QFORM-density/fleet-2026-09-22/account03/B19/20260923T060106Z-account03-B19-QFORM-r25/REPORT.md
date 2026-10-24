SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T06:01:06Z.
attacking: QFORM-COLLAR-SECOND-GRADIENT-OR-RANKONE-ALIGNMENT-v1 — pay a dominant physical star atom, then convert the diffuse-star survivor into either aggregate two-volume or a quantitatively near-line product bank.

# account03/B19 r25 — dominant-star payment and stable line-bank reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** universal proof assembly / quantitative inequalities  
**Owner control at start:** `yspennstate/math-research-brain@2bf933209ce168f6e792d47f0089f1279f516cae`, OWNER CONTROL revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW TARGET-LEVEL BRANCH + STRUCTURAL REDUCTION / FULL TARGET OPEN`.

The unrestricted conjecture remains OPEN. Global continuity remains OPEN. The arguments below use only ORIGINAL-coordinate independence. They do not use post-rotation independence, arbitrary-joint rank-three coarea, a worst conditional projection cap, pointwise law-uniform van der Corput decay, a local-minor-from-aggregate assertion, or perturbative deletion of a small quadratic matrix.

## 1. Source-pinned state entering this run

The current exact-rank-three small-Pluecker collar is supplied by account03/B10 r23b,

`yspennstate/math-open-problems@91759f77fcdf696a75d8e6c6ef398c03654b025a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T023946Z-account03-B10-QFORM-r23b/REPORT.md`.

Write

`A=R Lambda R^T`, `R^T R=I_3`,                                    (1.1)

with the three eigenvalues of `Lambda` satisfying `|lambda_r|>=1`. In the only unpaid exact-rank-three collar, after the already-paid scalar-pivot exit, there is an ORIGINAL physical hub which we relabel `0` such that, with

`A=[[a,m^T],[m,H]]`,                                               (1.2)

one has

`|a|<1/64`,
`M^2:=||m||_2^2>1023/4096`.                                       (1.3)

The preceding B19 r24 theorem,

`yspennstate/math-open-problems@2c88af5e0ac6a4faf8d923a621c7d7006d544ffe`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T034239Z-account03-B19-QFORM-r24/REPORT.md`,

proved that two ORIGINAL physical gradients with cross matrix `N` and

`Delta_2=sqrt(det(NN^T))>0`

give the `2/3` small-ball estimate

`sup_z P(|Q-z|<=eps)<=12(2 Delta_2)^(-1/3) eps^(2/3)`.            (1.4)

The failed r25 checkpoint already observed that if every two-gradient area vanishes then the residual off diagonal is exactly rank one. This report strengthens that calculation quantitatively, pays the large-single-star-atom branch completely, improves the exact endpoint from seven line directions to five, and compiles the positive-area branch into the new three-sample two-volume theorem of account03/B04.

The analytic inputs used at actual equations are:

1. `QFORM-RANK3-INDEFINITE-PAIR-PIVOT-v1`, canonical
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`:
   for an invertible indefinite ORIGINAL physical pair `B`, with `D=|det B|`, `kappa=sigma_min(B)`, in an exact-rank-three target with spectral scale at least one,

   `||p_Q||_infinity <=8 sqrt(5) (D kappa)^(-1/4)`.                (1.5)

2. `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`, canonical
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`:
   for a physical coordinate `j`, leverage `c_j=||r_j||^2`, and `A_jj!=0`,

   `||p_Q||_infinity <=128[c_j |A_jj| |det Lambda|]^(-1/4)`.      (1.6)

3. `QFORM-PHYSICAL-TRIPLE-DETERMINANT-v1` through the finite-line report account02/B16:

   `C_3=16 sqrt(30) 2^(1/4)=104.216889989...`,                    (1.7)

   and an invertible ORIGINAL physical `3x3` block `B_3` gives

   `||p_Q||_infinity <=C_3 |det B_3|^(-1/3)`.                     (1.8)

4. `QFORM-FINITE-LINE-BANK-COMPRESSION-v1`, canonical account02/B16 report
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T220011Z-account02-B16-QFORM-auto11/REPORT.md`:
   if all nonzero spectral rows occupy at most `K` line directions, then

   `||p_Q||_infinity <=2 C_3 binom(K,3)^(1/3)`.                   (1.9)

5. Fresh account03/B04 r26, canonical
   `yspennstate/math-open-problems@053c462960cc0c0068d221ffece8029a662a7ab6`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T055256Z-account03-B04-qform-auto11-r26/REPORT.md`:
   for an ORIGINAL-coordinate cross block with squared two-volume `Z_2` and three-sample overlap parameter `delta_3>0`, its full residual quadratic-plus-affine form `R` satisfies

   `sup_s E|R-s|^(-1/2)
    <=6*3^(1/4)*sqrt(e) Z_2^(-1/8) delta_3^(-1/24)`.              (1.10)

   If `delta_3=0` on both orientations, the nonzero two-minor support is an exact row star and an exact column star; deleting the corresponding physical row/column leaves rank at most one.

No input above is promoted beyond its stated source scope.

## 2. First new target-level exit: one star atom carries half the hub energy

### Theorem 2.1 — `QFORM-COLLAR-DOMINANT-STAR-ATOM-v1`

Assume (1.2)-(1.3). If some leaf `j` satisfies

`m_j^2 > M^2/2`,                                                   (2.1)

then the full exact-rank-three quadratic form has an essentially bounded density with

`boxed: ||p_Q||_infinity <104.`                                   (2.2)

No continuity claim is made.

### Proof

Put `h=A_jj`. From (1.3) and (2.1),

`|m_j| > b_0:=sqrt(1023/8192)=0.3533807149...`.                    (2.3)

#### Case A: `|h|>=4`

Let `L=||Lambda||op`. Since

`|h|=|r_j^T Lambda r_j|<=c_j L`,

we have `c_j>=|h|/L`. Because the other two spectral eigenvalue magnitudes are at least one,

`|det Lambda|>=L`.                                                  (2.4)

Therefore

`c_j |h| |det Lambda| >= |h|^2`.                                  (2.5)

The scalar-pivot theorem (1.6) gives

`||p_Q||_infinity <=128 |h|^(-1/2) <=64`.                         (2.6)

#### Case B: `|h|<4`

Use the ORIGINAL physical pair `{0,j}`:

`B=[[a,m_j],[m_j,h]]`.                                             (2.7)

Its determinant is negative because

`m_j^2>|a h|`,

and quantitatively

`D:=|det B|
 >= b_0^2-(1/64)4
 =511/8192
 =:D_0`.                                                           (2.8)

Hence the pair is invertible indefinite. Its operator norm is at most the maximum absolute row sum,

`||B||op <= |m_j|+4`.                                              (2.9)

For a `2x2` invertible matrix, the singular values multiply to `D`, so

`kappa=sigma_min(B)=D/||B||op
 >= (|m_j|^2-1/16)/(|m_j|+4)`.                                    (2.10)

The right side is strictly increasing for positive `|m_j|`, hence

`kappa>=kappa_0:=D_0/(b_0+4)
 =0.01432861809...`.                                               (2.11)

Apply (1.5):

`||p_Q||_infinity
 <=8 sqrt(5)(D_0 kappa_0)^(-1/4)
 =103.4584989...<104`.                                             (2.12)

This proves the theorem. QED.

Thus every still-unpaid hub collar may now be assumed to satisfy the **diffuse-star condition**

`m_j^2 <= M^2/2` for every leaf `j`.                              (2.13)

This is useful because it gives a dimension-free denominator in every deleted-star projection below.

## 3. Quantitative rigidity of failure of every second gradient

For each leaf `j`, delete coordinate `j` from the star and the `j`th residual row and define

`Delta_j^2
 :=||m_{-j}||^2 ||H_{j,-j}||^2
   -<m_{-j},H_{j,-j}>^2`.                                         (3.1)

Equivalently,

`Delta_j^2
 =sum_{k<l; k,l!=j}(m_k H_jl-m_l H_jk)^2`,                       (3.2)

so it is exactly the squared two-row cross area available to the r24 receiver for the active ORIGINAL pair `{0,j}` and receiver bank excluding that pair.

Put

`T:=sum_j Delta_j^2`.                                              (3.3)

### Theorem 3.1 — `QFORM-DIFFUSE-STAR-STABLE-LINEBANK-v1`

Under (2.13), there exists a scalar `theta` such that, with

`E:=Off(H-theta m m^T)`,                                          (3.4)

one has

`boxed: ||E||_F^2 <= (12/M^2) T.`                                 (3.5)

### Proof

Since (2.13) gives

`||m_{-j}||^2=M^2-m_j^2>=M^2/2`,                                 (3.6)

define

`alpha_j=<H_{j,-j},m_{-j}>/||m_{-j}||^2`,
`e_jk=H_jk-alpha_j m_k`, `k!=j`.                                  (3.7)

Orthogonal projection gives the exact identity

`sum_{k!=j}e_jk^2=Delta_j^2/||m_{-j}||^2`.                        (3.8)

Let

`E_0=sum_j sum_{k!=j}e_jk^2`.                                    (3.9)

By (3.6),

`E_0 <= 2T/M^2`.                                                   (3.10)

Symmetry of `H` gives, for `j!=k`,

`alpha_j m_k-alpha_k m_j=e_kj-e_jk`.                              (3.11)

Choose

`theta=<alpha,m>/M^2`.                                             (3.12)

The standard wedge/variance identity gives

`M^2 ||alpha-theta m||^2
 =sum_{j<k}(alpha_jm_k-alpha_km_j)^2
 <=2E_0`.                                                          (3.13)

For `j!=k`,

`H_jk-theta m_jm_k
 =(alpha_j-theta m_j)m_k+e_jk`.                                   (3.14)

Therefore, summing over ordered off-diagonal pairs and using `(x+y)^2<=2x^2+2y^2`,

`||E||_F^2
 <=2M^2||alpha-theta m||^2+2E_0
 <=6E_0
 <=12T/M^2`.                                                       (3.15)

QED.

This proof avoids division by individual `m_j`; zeros of the star cause no singularity.

## 4. Small aggregate area localizes two spectral directions onto five physical coordinates

Write

`H=D+theta m m^T+E`,                                               (4.1)

where `D=diag(d_j)` and `E` is the zero-diagonal matrix from (3.4). Put

`eps=||E||_F`.                                                      (4.2)

The exact-rank-three hypothesis implies `rank(H)<=3`. Hence `B:=D+theta mm^T=H-E` lies within Frobenius distance `eps` of a rank-three matrix. By Eckart--Young,

`sum_{k>=4}s_k(B)^2 <=eps^2`.                                     (4.3)

Since `B-D` has rank one, singular-value interlacing gives

`s_{k+1}(D)<=s_k(B)`.                                              (4.4)

Thus, if `E_*` is the set of four largest diagonal residuals `|d_j|` and `O` its complement,

`boxed: sum_{j in O}d_j^2 <=eps^2.`                               (4.5)

Now let `U_O` be the matrix of spectral rows `r_j^T`, `j in O`. Every leaf row of the physical coefficient matrix is

`A_{j,*}=m_j q^T+d_j e_j^T+E_{j,*}`,

where

`q^T=[1,theta m^T]`.                                               (4.6)

Hence

`sum_{j in O}||A_{j,*}-m_jq^T||^2<=4eps^2`.                       (4.7)

Project `q` orthogonally onto the row space of `A`; this can only decrease the left side because every `A_{j,*}` already belongs to that row space. The map

`z^T -> z^T Lambda R^T`                                           (4.8)

from spectral space onto the row space of `A` has all singular values at least one. Therefore there exists a spectral vector `w` such that

`||U_O-m_O w^T||_F <=2eps`.                                      (4.9)

Let the eigenvalues of the outside spectral Gram

`G_O=U_O^T U_O`                                                    (4.10)

be `mu_1>=mu_2>=mu_3>=0`. The best rank-one approximation inequality applied to (4.9) gives

`boxed: mu_2+mu_3 <=4eps^2.`                                      (4.11)

Let

`C={0} union E_*`,                                                 (4.12)

so `|C|<=5`, and let `G_C` be the Gram of the spectral rows in this physical core. Parseval gives

`G_C=I_3-G_O`.                                                      (4.13)

### Corollary 4.1 — small-T dichotomy

If

`T<=M^2/192`,                                                       (4.14)

then by (3.5)

`eps^2<=1/16`,                                                     (4.15)

and hence

`mu_2+mu_3<=1/4`.                                                  (4.16)

There are two possibilities.

#### (i) `mu_1<=1/2`: a physical triple pays the full density

The three eigenvalues of `G_C=I-G_O` are `1-mu_3,1-mu_2,1-mu_1`. Equations (4.15)-(4.16) imply

`det G_C >= (3/4)^2(1/2)=9/32`.                                  (4.17)

Cauchy--Binet over at most five physical rows yields a triple `S subset C` with

`det(R_S)^2 >= (9/32)/binom(5,3)=9/320`.                          (4.18)

Since

`det A_[S,S]=det Lambda det(R_S)^2`                               (4.19)

and `|det Lambda|>=1`, the physical-triple theorem (1.8) gives

`boxed: ||p_Q||_infinity
 <=C_3(320/9)^(1/3)
 =342.694603...<343.`                                              (4.20)

#### (ii) `mu_1>1/2`: the only small-T survivor is a near-rank-one original-product bank

The outside ORIGINAL coordinate bank `O` has

`boxed:
 mu_1>1/2,
 mu_2+mu_3<=4eps^2<=1/4,
 |C|<=5.
}`                                                                  (4.21)

Thus two transverse spectral directions are concentrated on at most five ORIGINAL physical coordinates, while the complementary product bank has more than one half unit of longitudinal spectral energy and at most `4eps^2` total transverse Gram energy. No independence between longitudinal and transverse projections of the same bank is asserted.

This is a strict quantitative reduction of the former vague “near line bank” obstruction.

## 5. The exact all-areas-zero endpoint improves from seven lines to five

The previous checkpoint used only `rank(A-L)<=5`, giving at most five diagonal exceptions and seven line directions. Exact rank three gives two additional units of rigidity.

Assume

`T=0`.                                                             (5.1)

Then `E=0` in (4.1):

`H=D+theta mm^T`.                                                   (5.2)

### Lemma 5.1 — at most three nonzero diagonal residuals

Let `F` be any four indices for which `d_j!=0`. The diagonal matrix `D_F` is invertible. The leaf principal block is

`H_F=D_F+theta m_Fm_F^T`.                                         (5.3)

Because `rank(H_F)<=rank(A)=3`, it cannot be invertible. If `theta=0`, (5.3) is invertible, contradiction. Thus `theta!=0`. The matrix determinant lemma gives

`1+theta u=0`,
`u=m_F^T D_F^(-1)m_F=-1/theta !=0`.                               (5.4)

A rank-one update of an invertible `4x4` matrix has rank at least three, so `rank(H_F)=3`, with kernel generated by `D_F^(-1)m_F`. Since

`m_F^T D_F^(-1)m_F=u!=0`,                                        (5.5)

we have `m_F` not in `Range(H_F)`.

But the full principal block on the hub together with `F` is

`[[a,m_F^T],[m_F,H_F]]`.                                          (5.6)

A symmetric rank-three lower-right block gains rank when its coupling vector is outside its range, so (5.5) forces the block (5.6) to have rank at least four, contradicting `rank(A)=3`. Therefore no such four indices exist:

`boxed: #{j:d_j!=0}<=3.`                                          (5.7)

For every nonexceptional leaf `j`,

`A_{j,*}=m_j[1,theta m^T]`.                                       (5.8)

If `m_j=0`, this row is zero; otherwise all such rows are proportional. Because the map (4.8) is injective, proportional nonzero physical matrix rows correspond to proportional spectral rows. Hence all nonzero spectral rows lie on at most

- one common leaf line,
- the hub line,
- at most three exceptional singleton lines.

Thus `K<=5`. Apply the finite-line theorem (1.9):

`boxed:
 ||p_Q||_infinity
 <=2C_3 binom(5,3)^(1/3)
 =449.056966...<450.
}`                                                                  (5.9)

This is a strict improvement over the `<681.801` seven-line checkpoint. It proves essential boundedness for the exact endpoint; continuity is not asserted.

## 6. Large aggregate second-gradient area produces a genuine physical two-volume cross block

Suppose instead that the small-T condition fails:

`T>M^2/192`.                                                       (6.1)

Randomly color every leaf coordinate left/right with probability `1/2`, keep the hub `0` on the left, and let `M_cut=A[L,R]` be the resulting ORIGINAL-coordinate cross block. For every term in (3.2), the squared minor

`(m_kH_jl-m_lH_jk)^2`

appears among the physical `2x2` minors of `M_cut` whenever `j` is colored left and `k,l` are colored right, an event of probability `1/8`. Every other squared cross minor is nonnegative. Therefore, if

`Z_2(M_cut)=sum_{|S|=|T|=2}det(M_cut[S,T])^2`,                    (6.2)

then

`E Z_2(M_cut) >=T/8`.                                             (6.3)

Hence some actual original-coordinate cut obeys

`boxed:
 Z_2 >=T/8>M^2/1536.
}`                                                                  (6.4)

Apply the fresh account03/B04 three-sample theorem to this actual cross block. Let

`delta_3=max(delta_3^r,delta_3^c)`.                               (6.5)

If `delta_3>0`, then in the precise residual scope of that theorem,

`sup_s E|R-s|^(-1/2)
 <=6*3^(1/4)*sqrt(e) Z_2^(-1/8)delta_3^(-1/24)`
` <32.575 M^(-1/4) delta_3^(-1/24).`                              (6.6)

This is not silently promoted to an `L^infinity` density bound in the collar because no untouched nonzero scalar square is guaranteed.

If `delta_3=0`, account03/B04 gives an exact structural alternative: the supported two-minor row family is a physical star and the supported column family is a physical star; deleting those two distinguished physical indices leaves cross rank at most one. Thus the large-aggregate branch is no longer an unstructured cloud of second gradients: it is either paid up to a half-Riesz receiver with only a `delta_3^(-1/24)` penalty, or it is an exact double-star/low-cross-rank hub geometry.                                      (6.7)

## 7. Designated partner account04/B19 applied at an actual inequality

The completed designated-partner theorem is account04/B19
`QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`, canonical

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`.

In its proved residual-diffuse exact-null-coloop scope,

`||p_Q||_infinity <34 sqrt(log(e/D_res))`, `0<D_res<=1`,           (7.1)

with a continuous density. On the concrete range

`e^(-8)<=D_res<=1`,                                                (7.2)

one has `log(e/D_res)<=9`; therefore the actual target inequality is

`boxed: ||p_Q||_infinity<102.`                                    (7.3)

The same source separately pays `D_res=0` by `<5.844` and `D_res>=1` by `<11.748`. I do not extend it to near-coloops or non-diffuse residuals.

## 8. Compact conditional end-to-end assembly after this run

The present source-valid proof graph can be stated compactly as follows.

1. Existing diagonal, physical-pair, scalar-pivot, grouped `2+1`, exact-cross-rank, cross-volume/Fresnel, and finite-line-bank theorems pay their explicit branches for arbitrary cap-one product laws, with signs and zero pivots handled only where the source theorems say so.
2. In exact rank three, the Pluecker-disjointness split pays `d>=1/64` and `d=0`. In `0<d<1/64`, a scalar pivot pays or B10 yields the near-null physical hub (1.2)-(1.3).
3. This run pays every such hub for which one physical star coefficient carries more than half of the star energy, by `<104`.
4. In the remaining diffuse-star hub, define the complete second-gradient aggregate `T` by (3.1)-(3.3).
   - `T=0` is fully paid by the sharpened five-line theorem `<450`.
   - `0<T<=M^2/192` either has a physical triple and is paid by `<343`, or is reduced to the explicit near-rank-one product-bank state (4.21).
   - `T>M^2/192` produces an actual physical cross block with `Z_2>M^2/1536`; the fresh B04 theorem turns this into either the quantitative half-Riesz currency (6.6) or an exact double-star/low-cross-rank state.
5. Arbitrary-extra-spectrum branches already covered by the pair-plus-two-gradient and cross-energy theorems remain paid in their source scopes. A general descent from the three-large-eigenvalue hypothesis to the exact-rank-three proof graph is still not complete.

Therefore the first exact-rank-three missing implication is now the following **two-headed but quantitative** receiver, rather than the former generic second-gradient request:

`QFORM-COLLAR-PUNCTURED-LINEBANK-OR-DOUBLESTAR-PAYMENT-v1`:

- pay the small positive transverse-tail state (4.21), uniformly as `mu_2+mu_3 ->0`, while retaining the original-product dependence inside the near-line bank; and
- in the large-T branch, turn either (6.6) or the exact B04 double-star residue into a linear small-ball/density estimate without assuming an untouched nonzero scalar pivot.

The exact endpoint is already paid and must not be re-audited as if it were still open.

A separate global debt remains: an exhaustive arbitrary-extra-spectrum splice which preserves all additional quadratic couplings rather than deleting or conditioning on overlapping spectral projections.

## 9. Status and regularity

`QFORM-COLLAR-DOMINANT-STAR-ATOM-v1`: **PROVED TARGET-LEVEL BRANCH**, essential density `<104`; continuity not claimed.  
`QFORM-DIFFUSE-STAR-STABLE-LINEBANK-v1`: **PROVED SUPPORTING STRUCTURAL THEOREM**.  
`QFORM-COLLAR-EXACT-LINEBANK-ENDPOINT-v2`: **PROVED TARGET-LEVEL BRANCH**, essential density `<450`; continuity not claimed.  
`QFORM-COLLAR-SMALL-T-PHYSICAL-TRIPLE-v1`: **PROVED TARGET-LEVEL BRANCH**, essential density `<343`.  
`QFORM-COLLAR-LARGE-T-CROSS-E2-v1`: **PROVED STRUCTURAL/ANALYTIC COMPILER**, not by itself a full density theorem.  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Global continuous-density conclusion: **OPEN**.
