SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-23T14:30:34Z.
attacking: exact two-hub anchored third-volume identities and a diffuse-or-rank-two-alignment reduction on the partner Schur crosscut.

# account01/B13 auto11 — anchored third-volume and balanced two-hub Schur reduction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: `Extremal product laws`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING TARGET-LEVEL THEOREMS; FULL QFORM OPEN; FULL CONTINUITY OPEN SEPARATELY**

The full target remains: for every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal bound on the essential supremum of the density of `X^T A X`, or give a valid counterexample. Nothing below claims the unrestricted theorem.

This run attacks the current two-hub Schur obstruction. The main new point is an exact identity turning a family of **original-coordinate anchored 3x3 minors** into the transverse Frobenius energy of a Schur cross block. Combined with a sharpened weighted D3 Fourier estimate, this either pays that transverse energy at scale `rho^-3` or forces an anchored physical volume star. A second deterministic lemma chooses the same Schur cut while keeping both halves of the physical two-hub cross bank quantitatively nondegenerate. The designated account02/B13 determinant-star identity is then applied to the actual high-ratio witness.

No small matrix is deleted as a random perturbation. The final Frobenius-small tail is retained explicitly and is an unresolved part of the full problem.

## 1. Fresh scope and source-valid inputs

Fresh owner control was read from `yspennstate/math-research-brain` on `main`; OWNER CONTROL is revision `2026-09-22.15`, QFORM is the sole research target, and `QFORM-FULL` remains `OPEN`. The live correction inbox was refreshed before publication. In particular this report does not use law-uniform pointwise quadratic oscillatory decay, independence after rotation, arbitrary-joint quadratic coarea, conditional projection-density caps, bounded-diameter localization, fixed fragment count, or perturbative deletion of max-norm-small coefficients.

The completed inputs used below are:

1. **Finite-mixture/extremal-product purification.** The B13 reduction proves that every cap-one product law is approximable in total variation by finite convex mixtures of indicators of bounded finite unions of intervals of measure one in each coordinate. Therefore every strict bounded-slab violation transfers with arbitrarily small loss to a product of unit-measure bounded finite-union sets. No attained optimizer, centered interval, bounded diameter, or uniform fragment count is asserted.

2. **Designated partner account02/B13 r25.** Source

   `yspennstate/math-open-problems@04973c0d13c8cbe814f1303b7de8aeffd40791df`

   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T110032Z-account02-B13-extremal-r25/REPORT.md`.

   For a physical two-hub cross bank `B=[b_1,...,b_m]` of rank two, put

   `G=BB^T`, `D=det G`, `beta_j=b_j^T G^-1 b_j`.

   The partner proves the exact determinant-star identity

   `sum_{k!=j} det(b_j,b_k)^2 = beta_j D`,                         (1.1)

   together with its complementary non-star identity. This is applied at equation (6.4) below.

3. **Nystrom rigidity from account01/B13 auto22.** Source

   `yspennstate/math-open-problems@ac5acc0621d0b45e2942a259747399d983e24c14`

   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T113036Z-account01-B13-qform-auto22/REPORT.md`.

   For an invertible physical hub pair

   `H0=A[H,H]=[[a,h],[h,g]]`, `a!=0`,

   with leaf cross bank `B=A[H,L]` and exact leaf Schur remainder

   `S=A[L,L]-B^T H0^-1 B`,                                        (1.2)

   every slab ratio `rho=P(Q in J)/|J|` forces

   `||S||_max <= eta`,
   `eta=C_N/(rho^4 |a det H0|)`,                                  (1.3)

   where

   `C_N=sqrt(128^8+32^8)<2.685e8`.                                (1.4)

4. **Schur large-spectrum retention.** The completed Schur-interlacing lemma in the pinned Fourier package says that if `A` has at least three eigenvalues of modulus at least one and `H0` is an invertible physical `2x2` principal block, then `A/H0` has at least one eigenvalue of modulus at least one. Hence the full `S` in (1.2) satisfies

   `||S||_op >=1`.                                                 (1.5)

5. **Weighted D3 Brascamp--Lieb Fourier mechanism.** Source

   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

   and `FOURIER_ROUTE_REPORT.md`. Its weighted form allows any probability weight on nonzero physical `3x3` cross minors whose row marginals are at most one half; the effective determinant currency is

   `exp(E_w log det^2 + H(w))`,                                    (1.6)

   while column marginals enter only through the entropy factor. This is specialized below to a new anchored family where two column marginals are exactly one.

## 2. Exact two-hub anchored third-volume identity

Fix an invertible physical hub pair `H={h_1,h_2}` and disjoint physical leaf sets `I,J`. Write

`H0=A[H,H]`,
`B_I=A[H,I]`, `B_J=A[H,J]`,
`M=A[I,J]`,
`T=(A/H0)[I,J]=M-B_I^T H0^-1 B_J`.                               (2.1)

Assume `rank B_I=2`, and put

`U=B_I^T`,
`G_I=B_I B_I^T=U^T U`,
`P_I=I-U(U^TU)^-1U^T`.                                            (2.2)

Thus `P_I` is the orthogonal projection in `R^I` onto the complement of the two physical hub rows.

Define the anchored disjoint third-volume

`Z_I = sum_{S subset I, |S|=3} sum_{j in J}
       det A[S, H union {j}]^2`.                                  (2.3)

### Theorem 2.1 — `QFORM-TWOHUB-ANCHORED-D3-IDENTITY-v1`

One has the exact identity

`boxed: Z_I = det(G_I) ||P_I T||_F^2.`                            (2.4)

Similarly, if `rank B_J=2`, with

`G_J=B_J B_J^T`,
`P_J=I-B_J^T(G_J)^-1B_J`,                                         (2.5)

and

`Z_J = sum_{R subset J, |R|=3} sum_{i in I}
       det A[R,H union {i}]^2`,                                   (2.6)

then

`boxed: Z_J = det(G_J) ||T P_J||_F^2.`                            (2.7)

### Proof

For every `S subset I`, `|S|=3`, and `j in J`, the selected `3x3` matrix has columns

`A[S,H union {j}] = [ U_S , M_{S,j} ]`.                           (2.8)

By (2.1),

`M_{S,j}=T_{S,j}+U_S H0^-1 b_j`,                                  (2.9)

where `b_j=A[H,{j}]`. The correction in (2.9) lies in the span of the first two columns, so multilinearity of the determinant gives the exact Schur invariance

`det[U_S,M_{S,j}] = det[U_S,T_{S,j}]`.                            (2.10)

For a fixed `j`, Cauchy--Binet gives

`sum_{|S|=3} det[U_S,T_{S,j}]^2
 =det( [U,T_j]^T [U,T_j] )`.                                      (2.11)

Taking the Schur complement of `U^TU` in this `3x3` Gram determinant yields

`det( [U,T_j]^T [U,T_j] )
 =det(U^TU) T_j^T P_I T_j`.                                       (2.12)

Summing over `j` proves (2.4). The right-hand identity is the same argument applied to the transpose cross block, using symmetry of `A`. QED.

The identity is representation-free and uses only original-coordinate minors and an exact physical Schur complement. No random-variable rotation is made.

## 3. A sharpened anchored D3 density theorem

The weighted D3 theorem is especially efficient for the minors in (2.3). Suppose `Z_I>0` and put the probability weight

`w_{S,j}=det A[S,H union {j}]^2/Z_I`.                              (3.1)

Let

`alpha_i=P_w(i in S)`, `i in I`,
`gamma_j=P_w(the third column is j)`, `j in J`.                    (3.2)

Then

`sum_i alpha_i=3`, `sum_j gamma_j=1`.                             (3.3)

Viewed as a weight on `3x3` minors of the physical cross matrix `A[I,H union J]`, both hub columns have marginal exactly one, while the remaining column marginals are `gamma_j`.

### Theorem 3.1 — `QFORM-TWOHUB-ANCHORED-D3-DENSITY-v1`

If

`max_{i in I} alpha_i <=1/2`,                                     (3.4)

then the full ambient quadratic form has a continuous density and

`boxed:
 ||p_Q||_inf <= C_A Z_I^(-1/6),
 C_A=6 e^(1/6)=7.08816247719... .
`                                                                    (3.5)

All same-side curvature, outside curvature/couplings and affine terms are retained.

### Proof

Run the weighted D3 proof with the weight (3.1). Its determinant/entropy currency (1.6) is exactly `Z_I`, because `w` is proportional to the selected squared minors.

The two hub columns have column marginal one. In the Brascamp--Lieb determinant proof their coordinate-density factors can be dropped using `g<=1`; they contribute no entropy loss. For the remaining columns, the standard entropy factor is

`prod_{j in J}(1-gamma_j)^(-(1-gamma_j)/2)`.                       (3.6)

Since `-x log x<=1-x` on `[0,1]`, and `sum gamma_j=1`,

`prod_j(1-gamma_j)^(-(1-gamma_j)/2) <= e^(1/2).`                  (3.7)

The row `L^p` factors are exactly those of D3 because (3.4) gives `1/alpha_i>=2`. Hence the decoupled characteristic function obeys

`|phi_Q(t)|^2
 <= e^(1/2) (2 pi)^3 |t|^-3 Z_I^-1/2`.                           (3.8)

Therefore

`|phi_Q(t)|
 <= min(1, e^(1/4)(2pi)^(3/2)|t|^-3/2 Z_I^-1/4)`.                 (3.9)

For `B>0`,

`int_R min(1,B|t|^-3/2) dt =6 B^(2/3)`.                           (3.10)

Fourier inversion now gives (3.5). Absolute integrability also gives continuity in this branch. QED.

The same theorem applies with `I,J` interchanged and `Z_J` from (2.6).

### Corollary 3.2 — anchored volume is small or physically starred

For any actual interval with slab ratio `rho`, on the left anchored family either

`boxed: Z_I <= (C_A/rho)^6`,                                      (3.11)

or there exists a physical `i_* in I` for which

`boxed:
 sum_{S contains i_*, j in J}
 det A[S,H union {j}]^2 > Z_I/2.
`                                                                    (3.12)

The same dichotomy holds on the right.

This is an aggregate-before-inversion statement. It does not choose a single good minor, and the star may have arbitrarily many fragmented spokes.

By the finite-mixture purification, (3.5) is equivalently the geometric product-set slab inequality

`|{x in prod E_l : x^T A x in K}|
 <= C_A Z_I^-1/6 |K|`                                             (3.13)

for arbitrary measurable `|E_l|=1`, under (3.4). No interval or centering assumption on any `E_l` is made.

## 4. A cut that is simultaneously Schur-strong and hub-balanced

The partner's previous random-cut lemma extracts a strong physical Schur cross direction from a max-norm-small Schur matrix. Here the cut is strengthened so that both sides retain quantitative two-hub Gram determinant, provided the hub bank itself has no heavy leverage coordinate.

### Lemma 4.1 — `QFORM-JOINT-BALANCED-SCHUR-CUT-v1`

Let `T` be a real symmetric `m x m` matrix with

`L=||T||_op`, `max_i |T_ii|<=eta<=L/2`.                            (4.1)

Let `b_i in R^2` span `R^2`, put

`G=sum_i b_i b_i^T`,
`beta_i=b_i^T G^-1 b_i`,
`max_i beta_i<=delta`.                                             (4.2)

Then there is a partition `[m]=I disjoint-union J` such that

`boxed: s_1(T[I,J]) >= (L-eta)/4`,                                (4.3)

and, for `theta=4 sqrt(delta)`,

`boxed:
 det(sum_{i in I} b_i b_i^T),
 det(sum_{j in J} b_j b_j^T)
 >= ((1-theta)/2)^2 det G,
`                                                                    (4.4)

provided `theta<1`.

In particular, if `delta<=1/256`, `L>=1`, and `eta<=1/2`, then

`boxed: s_1(T[I,J])>=1/8`,                                        (4.5)

and

`boxed: D_I,D_J >=(9/64)D`,                                       (4.6)

where `D=det G`.

### Proof

Let `v` be a unit eigenvector associated with an eigenvalue of modulus `L`; multiply `T` by `-1` inside this deterministic argument if necessary, so `Tv=Lv`.

Choose independent Rademacher signs `xi_i` and let `I={i:xi_i=1}`, `J={i:xi_i=-1}`. Put `w=xi o v` and

`Z=v_I^T T[I,J]v_J`.                                               (4.7)

By symmetry of `T`, the cross terms cancel in the mask expansion and

`Z=(L-w^T T w)/4`.                                                 (4.8)

Thus

`E Z=(L-sum_i T_ii v_i^2)/4 >=(L-eta)/4`.                         (4.9)

Also `|Z|<=L||v_I||||v_J||<=L/2`. With

`a_0=(L-eta)/8`,                                                   (4.10)

we therefore have

`P(Z>=a_0)
 >= (E Z-a_0)/(L/2-a_0)
 >= (L-eta)/(3L+eta)
 >=1/7`.                                                           (4.11)

Now normalize the hub vectors:

`r_i=G^-1/2 b_i`, `sum_i r_i r_i^T=I_2`, `||r_i||^2=beta_i`.       (4.12)

Let

`R=sum_i xi_i r_i r_i^T`.                                         (4.13)

Independence and centering of the signs give

`E||R||_F^2=sum_i ||r_i r_i^T||_F^2
             =sum_i beta_i^2
             <=delta sum_i beta_i=2delta`.                        (4.14)

Hence

`P(||R||_F^2>16delta)<=1/8`.                                      (4.15)

Because `1/7>1/8`, the events in (4.11) and the complement of (4.15) intersect. Fix such a partition. Then

`Z>=a_0`, and

`Z<=s_1(T[I,J])||v_I||||v_J||<=s_1(T[I,J])/2`,                    (4.16)

which proves (4.3).

Moreover `||R||_op<=4sqrt(delta)=theta` and

`sum_{i in I}b_i b_i^T
 =G^(1/2)(I_2+R)G^(1/2)/2`,
`sum_{j in J}b_j b_j^T
 =G^(1/2)(I_2-R)G^(1/2)/2`.                                      (4.17)

Every eigenvalue of `(I_2 +/- R)/2` is at least `(1-theta)/2`, yielding (4.4). The numerical specialization gives (4.5)-(4.6). QED.

The random signs are only an existence proof for a deterministic **original-coordinate** partition. No random-variable rotation or independence claim is involved.

## 5. Diffuse two-hub bank forces a hub-aligned rank-two Schur tube

Return to the physical hub setting (1.2). Assume

`rank B=2`, `D=det(BB^T)>0`,                                      (5.1)

and define the partner leverage numbers

`beta_j=b_j^T(BB^T)^-1 b_j`.                                      (5.2)

Suppose first that

`max_j beta_j <=1/256`.                                            (5.3)

If

`rho^4 |a det H0| >2C_N`,                                         (5.4)

then Nystrom rigidity gives `eta<1/2`, while Schur spectral retention gives `||S||op>=1`. Lemma 4.1 therefore supplies a partition `L=I disjoint-union J` such that

`s_1(S[I,J])>=1/8`,                                                (5.5)

and

`D_I=det(B_I B_I^T)>=9D/64`,
`D_J=det(B_J B_J^T)>=9D/64`.                                      (5.6)

Let

`T=S[I,J]`,                                                        (5.7)

and let `P_I,P_J` be the orthogonal complements of the two hub row spaces on the two sides as in Section 2.

Apply Corollary 3.2 on each side. If neither side has an anchored physical row star, then

`Z_I,Z_J <=(C_A/rho)^6`.                                          (5.8)

Using the exact identities (2.4),(2.7) and (5.6),

`||P_I T||_F
 <= (8/3) C_A^3 /(rho^3 sqrt(D))`,                                (5.9)

`||T P_J||_F
 <= (8/3) C_A^3 /(rho^3 sqrt(D))`.                                (5.10)

Write `Q_I=I-P_I`, `Q_J=I-P_J`. The exact decomposition

`T-Q_I T Q_J=P_I T+Q_I T P_J`                                    (5.11)

has orthogonal summands in Frobenius inner product, and `||Q_I T P_J||F<=||T P_J||F`. Therefore

`boxed:
 dist_F(T,{rank<=2 hub-aligned matrices})
 <= 576 sqrt(2e)/(rho^3 sqrt D)
 =1343.0269334.../(rho^3 sqrt D).
`                                                                    (5.12)

More explicitly, there exists a real `2x2` matrix `K` such that

`boxed:
 T=B_I^T K B_J+E,
 ||E||_F <=576 sqrt(2e)/(rho^3 sqrt D).
`                                                                    (5.13)

Indeed `Q_I T Q_J=B_I^T K B_J` because `Q_I,Q_J` project onto the physical hub row spaces.

Combining with the exact Nystrom part gives the corresponding original cross block

`boxed:
 A[I,J]
 =B_I^T(H0^-1+K)B_J+E,
 ||E||_F <=576 sqrt(2e)/(rho^3 sqrt D).
`                                                                    (5.14)

This is stronger than mere cutwise `s_7=O(rho^-1)` information in this diffuse-hub subbranch: **every component transverse to the two physical hub rows on either side is collectively `O(rho^-3)` in Frobenius norm.**

If additionally

`rho^3 sqrt D >=9216 sqrt(2e)=21488.4309344...`,                   (5.15)

then `||E||op<=||E||F<=1/16`, and (5.5) implies

`s_1(B_I^T K B_J)>=1/16`.                                         (5.16)

Thus the hub-aligned rank-two core is genuinely nonzero; nevertheless the tail `E` remains part of the quadratic form and is not discarded.

### Theorem 5.1 — `QFORM-DIFFUSE-HUB-ALIGNED-RANK2-TUBE-v1`

For any high-ratio witness in an invertible physical two-hub chamber with `rank B=2`, one of the following occurs:

1. **hub determinant degeneracy:**

   `rho^4 |a det H0| <=2C_N`;                                     (5.17)

2. **heavy hub leverage:** `max_j beta_j>1/256`; this is converted in Section 6 into an actual physical determinant star by the designated partner result;

3. **anchored-volume star:** on the balanced cut supplied by Lemma 4.1, one side has a physical coordinate carrying more than half of its anchored squared `3x3` volume as in (3.12);

4. **hub-aligned rank-two tube:** the same balanced cut satisfies (5.5)-(5.6) and the exact decomposition (5.14).

This theorem does not cover rank-one hub banks or the singular/zero-diagonal hub chambers; those require their already separate product-preserving mechanisms.

## 6. Direct application of the designated account02/B13 result

The heavy-leverage branch of Theorem 5.1 is not left as an abstract leverage statement. Apply the partner's exact identity (1.1) to the **same actual physical hub bank** `B=A[H,L]`.

If

`max_j beta_j>1/256`,                                              (6.1)

choose `j_*` attaining the maximum. Then the completed partner identity gives the concrete inequality

`boxed:
 sum_{k!=j_*} det(b_j*,b_k)^2
 =beta_j* D
 >D/256.
`                                                                    (6.2)

Thus the only obstruction to the balanced diffuse-hub cut is a genuine original-coordinate determinant star carrying more than `1/256` of the full two-hub squared area.

This is the required equation-level use of the designated account02/B13 result. It does not rely on an interval optimizer or any rotation of the independent variables.

If the original law is arbitrary cap-one rather than a product indicator, finite-mixture purification first transfers any strict slab ratio to a bounded finite-union product indicator with arbitrarily small loss. Equations (5.17), (6.2), and the anchored-volume alternatives are matrix statements independent of that approximation, while the slab ratio may be taken to the original value in the limit.

## 7. Numerical/algebraic diagnostics

The proof is analytic. As a diagnostic only, the identity (2.4) was checked on 150 random finite matrices with leaf dimensions `(5,4)`, `(6,7)`, and `(10,8)`. The maximum floating-point discrepancy between the two sides was `3.64e-11`.

The constants used above are

`C_A=6e^(1/6)=7.088162477193875`,
`C_A^3=216sqrt(e)=356.1237944712276`,
`576sqrt(2e)=1343.0269333999436`,
`9216sqrt(2e)=21488.430934399097`.                                (7.1)

These numerical checks are not used as proof.

## 8. What remains and exact OPEN status

The new structural reduction is useful but does not close the conjecture. In the most diffuse invertible-hub branch, a hypothetical high-density witness is now forced into the exact original-coordinate form

`A[I,J]=B_I^T L B_J+E`,
`rank(B_I^T L B_J)<=2`,
`||E||F=O(rho^-3 D^-1/2)`,                                       (8.1)

on a cut where both hub-bank Gram determinants are a fixed fraction of the full determinant and the Schur cross block has `s_1>=1/8`, unless a physical determinant star or anchored third-volume star occurs.

The tail `E` cannot simply be removed: the allowed product sets may be arbitrarily translated and fragmented, and even small coefficient matrices can have nonperturbative effects without additional structure. The localized star branches also still require a product-preserving third-smoother argument.

The first unpaid implication is therefore

`QFORM-HUBALIGNED-RANK2-TAIL-OR-ANCHORED-STAR-CLOSURE-v1`:

> Starting from Theorem 5.1, prove a uniform slab estimate for the hub-aligned rank-two tube while retaining the explicit Frobenius tail inside the analysis, or use the determinant/anchored-volume star as a genuine next physical pivot and force one of the already-paid square, pair, grouped-bank, or low-rank Fresnel--Brascamp--Lieb mechanisms. Do not delete the tail perturbatively and do not reduce fragmented product sets to intervals.

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The stronger continuity conclusion remains **OPEN**. The supporting theorems in this report have not yet received an independent end-to-end review.

## 9. Correction compliance

This report preserves the live correction ledger:

- no law-uniform pointwise quadratic oscillatory decay is used;
- no rotated coordinates are declared independent;
- no projection-density bound alone is used to control an indefinite quadratic pushforward;
- no arbitrary-joint coarea theorem is used;
- no conditional projection-density cap is assumed;
- no bounded support, bounded diameter, single interval, centered uniform, or fixed fragment count is assumed;
- no max-norm-small or Frobenius-small matrix is discarded as a random perturbation;
- continuity is claimed only in the scoped Fourier branch Theorem 3.1, not for full QFORM.

The full target remains open pending the closure implication in Section 8 and the other singular hub chambers.
