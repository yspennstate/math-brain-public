SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-23T06:36:28.500738Z.
attacking: finish the disjoint-minor random-cut compiler with corrected constants; combine order-two residual volume with the completed E2 entropy-or-trihub theorem and transfer the paid slab bound through fleet04/B13 purification.

# fleet03/B13 — cut-free disjoint bordered-volume compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Extremal product laws`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED TARGET-RELEVANT ANALYTIC/STRUCTURAL SUPPORTING THEOREMS / FULL QFORM OPEN / FULL CONTINUITY OPEN**

## 1. Scope and source-valid premises

The owner target remains the unrestricted statement for independent ORIGINAL-coordinate real random variables with probability densities bounded by one and a real symmetric matrix having at least three eigenvalues of modulus at least one. No moment, compact-support, connected-support, Gaussian, log-concavity, interval-support, fixed-fragment, or post-rotation-independence assumption is introduced below.


Completed mathematics actually used:

1. **Cross-three-volume L3 theorem.** `yspennstate/math-open-problems@77bd4ea475a11a505c6990630cbdfebdcce0fd8f`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T013555Z-fleet03-B13-qform-r21/REPORT.md`: for an ORIGINAL-coordinate cross block `M` with `Z=e_3(M^T M)>0`, the full quadratic-affine output has

   `||p||_3 < 6.787 Z^(-1/9)`,

   with arbitrary same-side terms and outside couplings.

2. **Sharp one-sided half-Riesz transducer.** `yspennstate/math-open-problems@aa2dca68a08b39fa15e783403a82bd54e711bfb5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T030125Z-fleet03-B13-qform-r22/FINAL_REPORT.md`: if `p` is a probability density with `||p||_3<=M`, then

   `sup_t int_0^infinity p(t-u)u^(-1/2)du <= C_H M^(3/4)`,

   where

   `C_H=2 sqrt(pi/sqrt(3))=2.693547374177197...`.

   Consequently, after completing one ORIGINAL scalar square with coefficient `a!=0`, the residual `L3` norm `M` gives

   `||p_Q||_infinity <= C_H |a|^(-1/2) M^(3/4)`.

3. **Order-two entropy-or-trihub theorem.** `yspennstate/math-open-problems@95ac7bddb7bb865e223a74ad77df639763194056`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T034405Z-fleet03-B13-qform-r23/REPORT.md`: if an ORIGINAL-coordinate cross block has `E=e_2(M^T M)>0`, then at the specialization `h=3/5`, `L=log 4`, either the ambient residual output has

   `||p_R||_3 < 7.681 E^(-1/6)`,

   or, after applying the theorem in both orientations, there is one physical row-column pair whose joint pair-minor mass exceeds `E/18`; if the pair is reindexed first in `M=[[b,p^T],[q,T]]`, that joint mass is exactly `||bT-q p^T||_F^2`.

4. **Designated partner fleet04/B13 no-attainment purification.** `yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260922T231352Z-fleet04-B13-rough-geometric-transfer-r5/REPORT.md`, Corollary 2.2: for every bounded product kernel, the supremum over arbitrary cap-one marginals equals the supremum over product indicators of bounded finite unions of intervals of measure one. This is an equality of suprema, not an attainment, interval-extremality, bounded-diameter, or fixed-fragment theorem.

Fresh corrections consumed include `QFORM-INTERPACKET-LOCAL-CURVATURE-CANCELS-v1` and `QFORM-BALANCED-FIXED-PACKET-EXTRACTION-FALSE-v1`. Therefore the trihub survivor obtained below is **not** declared paid merely because it contains a local pair packet; global third-curvature/bank structure must remain present.

## 2. General cut-elimination identity

Let `S=(S_ij)` be any finite real matrix whose row and column labels are the same physical index set `V`. For `m>=1`, define the complete disjoint order-`m` exterior energy

`D_m^perp(S)
 := sum_{R,C subset V, |R|=|C|=m, R cap C=empty} det(S[R,C])^2`.      (2.1)

### Theorem 2.1 — `QFORM-DISJOINT-MINOR-RANDOM-CUT-v1`

For every `m`, there is a deterministic partition `V=L disjoint_union Rside` such that

`boxed: e_m(S[L,Rside]^T S[L,Rside]) >= 4^(-m) D_m^perp(S).`       (2.2)

More generally, if each physical coordinate is independently put in `L` with probability `theta` and in `Rside` otherwise, then

`E e_m(S[L,Rside]^T S[L,Rside])
 = theta^m(1-theta)^m D_m^perp(S)`,                                (2.3)

whose maximum over `theta` is `4^(-m)D_m^perp(S)` at `theta=1/2`.

#### Proof

For a fixed cut, Cauchy--Binet gives

`e_m(S[L,Rside]^T S[L,Rside])
 = sum_{R subset L, C subset Rside, |R|=|C|=m} det(S[R,C])^2`.     (2.4)

A fixed disjoint ordered pair `(R,C)` is admitted by the random cut exactly when every coordinate of `R` lands in `L` and every coordinate of `C` lands in `Rside`, an event of probability `theta^m(1-theta)^m`. Summing (2.4) and using linearity of expectation gives (2.3). Some realization is at least the mean. The scalar function `theta(1-theta)` is maximal at `theta=1/2`, proving (2.2). QED.

No random variable is rotated here: the random cut is only a proof device selecting two disjoint sets of ORIGINAL coordinates.

## 3. Exact bordered-minor identity after an original scalar pivot

Fix an ORIGINAL coordinate `k` with

`a=A_kk !=0`.                                                       (3.1)

Write, with `k` first,

`A=[[a,c^T],[c,B]]`,
`S=B-a^(-1)c c^T`.                                                  (3.2)

Completing only the original scalar square gives

`Q=a(X_k+a^(-1)c^T Z)^2+Z^T S Z`.                                  (3.3)

The residual coordinates `Z` are still the original independent coordinates.

For `m>=1`, define the complete disjoint bordered energy

`B_{m+1,k}^perp(A)
 := sum_{R,C subset V, |R|=|C|=m, R cap C=empty}
       det A[{k} union R,{k} union C]^2`.                           (3.4)

### Lemma 3.1 — `QFORM-BORDERED-DISJOINT-ENERGY-IDENTITY-v1`

`boxed: B_{m+1,k}^perp(A)=a^2 D_m^perp(S).`                        (3.5)

#### Proof

For every disjoint residual pair `(R,C)`, put `k` first in both the row and column ordering. The scalar Schur determinant identity gives

`det A[{k} union R,{k} union C]
 = a det(B[R,C]-a^(-1)c_R c_C^T)
 = a det S[R,C]`.                                                  (3.6)

Square and sum. QED.

This is the exact algebraic reason the random cut can be eliminated before any reciprocal local-minor payment.

## 4. Order three: corrected cut-free scalar-Schur L-infinity theorem

Take `m=3` in Theorem 2.1. If

`D_3^perp(S)>0`,                                                     (4.1)

there is an original-coordinate cut with cross block `M=S[L,Rside]` and

`Z=e_3(M^T M)>=D_3^perp(S)/64`.                                   (4.2)

The completed cross-three theorem gives

`||p_R||_3 <6.787 Z^(-1/9)`.                                      (4.3)

Apply the half-Riesz transducer from (3.3):

`||p_Q||_infinity
 < C_H 6.787^(3/4) |a|^(-1/2) Z^(-1/12)
 =11.326168157432749... |a|^(-1/2) Z^(-1/12)`.                    (4.4)

Using (4.2), `64^(1/12)=sqrt(2)`, so

`||p_Q||_infinity
 <16.017620617959683... |a|^(-1/2) D_3^perp(S)^(-1/12)`.          (4.5)

Finally (3.5), with `m=3`, gives the matrix-only form.

### Theorem 4.1 — `QFORM-DISJOINT-BORDER4-LINF-v1`

If `a=A_kk!=0` and `B_{4,k}^perp(A)>0`, then for arbitrary independent cap-one inputs

`boxed:
 ||p_Q||_infinity
 <16.018 ( |A_kk|^4 B_{4,k}^perp(A) )^(-1/12).
`                                                                      (4.6)

The law is absolutely continuous with an essentially bounded density. Continuity is **not** proved by this transducer.

### Correction to the unfinished 04:33 UTC checkpoint

The earlier checkpoint `20260923T043329Z-fleet03-B13-qform-r22/CHECKPOINT.md` displayed the weaker numerical constant `22.653`. That number inserted an extra factor `sqrt(2)`: it began from `16.018`, which was already the post-random-cut constant, and multiplied by the random-cut loss a second time. The direct chain is (4.4) -> (4.2), hence exactly one factor `64^(1/12)=sqrt(2)`, producing `16.0176206179...`. The structural identity and theorem were not invalidated; this run corrects the constant and records the correction separately.

Two other exact cut-free consequences, useful even before scalar smoothing, are

`||p_R||_3 < 10.77369093970817 D_3^perp(S)^(-1/9)`,               (4.7)

and, from the completed three-quarter slab estimate,

`P(R in J)<24.361105339814102 D_3^perp(S)^(-1/8)|J|^(3/4)`.       (4.8)

## 5. Order two: L-infinity payment or one cut-free trihub

Now take `m=2`. Theorem 2.1 supplies a cut with

`E=e_2(S[L,Rside]^T S[L,Rside]) >= D_2^perp(S)/16`.              (5.1)

Apply the completed order-two entropy-or-trihub theorem to this actual residual cross block.

### Paid branch

If either orientation pays, then

`||p_R||_3 <7.681 E^(-1/6)
 <=7.681*16^(1/6) D_2^perp(S)^(-1/6)`.                            (5.2)

The scalar half-Riesz theorem gives

`||p_Q||_infinity
 < C_H [7.681*16^(1/6)]^(3/4)
   |a|^(-1/2) D_2^perp(S)^(-1/8)
 <17.57530781411503
   |a|^(-1/2) D_2^perp(S)^(-1/8)`.                                (5.3)

Since `B_{3,k}^perp=a^2D_2^perp`, this is

`boxed:
 ||p_Q||_infinity
 <17.576 ( |A_kk|^2 B_{3,k}^perp(A) )^(-1/8).
`                                                                      (5.4)

Again this proves essential boundedness, not continuity.

### Unpaid branch

If neither orientation pays, the order-two theorem gives a physical row `i in L` and column `j in Rside` such that the joint pair-minor energy obeys

`E_ij > E/18 >= D_2^perp(S)/288`.                                 (5.5)

For the chosen cross block, reindex `i,j` first and write

`S[L,Rside]=[[b,p^T],[q,T]]`.                                      (5.6)

Then exactly

`E_ij=||bT-q p^T||_F^2`.                                          (5.7)

Bordering every contributing `2x2` minor by the scalar pivot `k` and using (3.6) gives

`a^2E_ij
 = sum_{r in L\{i}, c in Rside\{j}}
   det A[{k,i,r},{k,j,c}]^2`.                                     (5.8)

Define the **complete disjoint trihub energy**

`J_{k;i,j}^perp(A)
 := sum det A[{k,i,r},{k,j,c}]^2`,                                 (5.9)

where the sum runs over all residual `r,c` for which the two three-element row/column sets meet only at `k`. The selected-cut sum (5.8) is a sub-sum of (5.9), hence (5.5) and `B_{3,k}^perp=a^2D_2^perp` imply

`boxed:
 J_{k;i,j}^perp(A) > B_{3,k}^perp(A)/288.
`                                                                     (5.10)

### Theorem 5.1 — `QFORM-DISJOINT-BORDER3-LINF-OR-TRIHUB-v1`

For every original scalar pivot `k` with `A_kk!=0` and `B_{3,k}^perp(A)>0`, at least one of the following holds:

1. **analytic payment:** the full quadratic-form output satisfies (5.4); or
2. **structural trihub:** there are distinct physical coordinates `i,j !=k` satisfying (5.10), and on the witnessing cut the normalized packet has the exact Frobenius form (5.7).

This is a cut-free, matrix-only descent from the complete disjoint bordered three-volume to either a linear slab estimate or one pivot-row-column hub carrying a fixed `1/288` fraction of that entire currency. No individual determinant is inverted.

The fresh `QFORM-INTERPACKET-LOCAL-CURVATURE-CANCELS-v1` correction is important here: (5.10) is only a structural survivor. Arbitrary interpacket couplings can cancel local pair curvature, so the trihub cannot be declared paid by iterating a two-coordinate theorem. A valid successor must retain a global third-curvature or disjoint-bank resource jointly with (5.10).

## 6. Actual application of the designated fleet04/B13 extremal-product theorem

The matrix alternatives above are independent of the input laws. In either paid branch, first restrict to arbitrary product indicators `prod_l 1_{E_l}`, where every `E_l` is a bounded finite union of intervals of total measure one. Equations (4.6) and (5.4) give, for every interval `J`, respectively,

`|{x in prod E_l:Q(x) in J}|
 <16.018 (|A_kk|^4B_{4,k}^perp)^(-1/12)|J|`,                      (6.1)

and

`|{x in prod E_l:Q(x) in J}|
 <17.576 (|A_kk|^2B_{3,k}^perp)^(-1/8)|J|`.                       (6.2)

Apply fleet04/B13 Corollary 2.2 to the actual bounded kernel

`K(x)=1_{Q(x) in J}`.                                              (6.3)

The same inequalities transfer with **zero constant loss** to every arbitrary independent cap-one product law. No optimizer, single interval, centered uniform law, support-radius bound, or fragment-count bound enters.

There is also a strict-witness consequence. If an arbitrary cap-one product law strictly violates one of the paid slab inequalities, choose the partner finite-mixture approximation sufficiently close in total variation; at least one bounded finite-union unit-product component still violates it. The matrix is unchanged. Therefore every strict violation can be witnessed by an extreme product law while retaining exactly the same bordered energies and the same trihub alternative.

This is the required concrete application of the designated partner result to the new inequalities, rather than a citation-only use.

## 7. Consequence for a hypothetical diverging no-pivot sequence

Let

`Rslab=P(Q in J)/|J|`.                                             (7.1)

The order-three theorem implies, for every nonzero original pivot `k`,

`Rslab <16.018 (|A_kk|^4B_{4,k}^perp)^(-1/12)`.                   (7.2)

Hence along any putative counterexample sequence with `Rslab -> infinity`, necessarily

`boxed:
 |A_kk|^4 B_{4,k}^perp(A)
 < (16.018/Rslab)^12
 ->0
`                                                                     (7.3)

for every nonzero physical pivot.

Likewise, Theorem 5.1 says that for each nonzero pivot either

`|A_kk|^2 B_{3,k}^perp(A) < (17.576/Rslab)^8`,                    (7.4)

or a single physical trihub satisfies (5.10). By fleet04/B13 purification the entire diverging sequence may be taken to have bounded finite-union unit-indicator marginals; the growing support separation and fragment count must still be allowed.

Thus rough marginal densities cannot hide the remaining obstruction. A counterexample sequence must simultaneously collapse every cut-free bordered-four currency and, at order three, either collapse the bordered-three currency or repeatedly concentrate a fixed fraction onto a physical trihub.

## 8. What remains unpaid

Full QFORM is still **OPEN / NOT PROVED / NOT DISPROVED**. Full continuity is also **OPEN**.

The first B13-relevant successor is now:

`QFORM-TRIHUB-PLUS-GLOBAL-THIRD-CURVATURE-v1`.

Starting from the structural alternative (5.10), retain a source-valid global third-curvature or escaped-bank certificate and prove a linear slab bound without conditioning away the coordinates that carry that curvature. The fresh interpacket-cancellation correction rules out treating the trihub as an isolated fixed-dimensional curved packet. In parallel, (7.3) says the exact-null/near-null pivot machinery only needs to confront matrices in which every complete disjoint bordered-four energy has collapsed.

This run does not switch to an easy subclass and does not claim a full solution.
