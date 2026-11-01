SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-23T16:51:54Z.
attacking: the completed fleet02/B20 in-plane rank-at-most-five carrier; enlarge the product-coordinate paving threshold from 1/320 to 1/25, then use both orientations of D' to turn every diffuse survivor into either a full density payment or a quantitative physical double-anchor packet.

# fleet01/B20 auto11 — rank-five 1/25 paving and two-sided third-volume anchoring

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T165154Z-fleet01-B20-QFORM-auto11`  
Status: **ESSENTIAL_STEP_APPLIED / IN-PLANE R5 BRANCH SHARPLY REDUCED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: continuous `C_0` density on the paid branch below; full-target continuity remains OPEN.

The target remains exactly the owner target: arbitrary independent real coordinates with densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No iid, Gaussian, moment, support, log-concavity, smoothness or rotated-independence assumption is introduced.

## 1. Source-pinned inputs and correction boundaries

The designated completed partner actually consumed is fleet02/B20 auto11c:

`yspennstate/math-open-problems@20ec5f8f3ed2028edf27894cd3956d13e4662a9a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260923T155833Z-fleet02-B20-QFORM-auto11c/REPORT.md`.

Its first current full-target obligation retains the aligned in-plane packet inherited through the current compiler. In that packet there is a real symmetric `S_0` on the ORIGINAL coordinate space such that

`rank(S_0)<=5`,

`s_3(S_0)>0.7985866375852596`,

`||A-S_0||_op<0.20141336241474038`.

The same completed partner run explicitly keeps the full target OPEN and also shows that bare physical `E_2` / half-Riesz credit does not by itself imply `L^infinity`; a third target resource must be spent jointly.

The analytic receiver used below is the reviewed physical cross-block theorem D' from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

For a literal original-coordinate cross block `M=A[I,J]`, let

`Z=e_3(M^T M)=sum_{|R|=|C|=3} det(M[R,C])^2`,

and let `alpha_i` be the row marginal of the natural squared-minor law

`w_{R,C}=det(M[R,C])^2/Z`.

For any `h<3/4`, if `max_i alpha_i<=h`, theorem D' gives, for the FULL ambient quadratic form with arbitrary same-side blocks, outside couplings and affine terms,

`||p_Q||_infinity <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) Z^(-1/6)`,

with an integrable characteristic-function envelope and hence a continuous `C_0` density.

All live corrections are respected. In particular this report does not use law-uniform pointwise one-dimensional quadratic oscillatory decay, post-rotation independence, arbitrary-joint three-dimensional coarea, a worst-fiber conditional cap, deletion of a small nonzero random quadratic tail, or an inference from aggregate volume to one universally large minor.

## 2. Immediate global spectral compression from the partner inequality

### Lemma 2.1 — `QFORM-INPLANE-R5-SIXTH-SINGULAR-COMPRESSION-v1`

In the partner in-plane packet,

`boxed: s_6(A)<403/2000=0.2015.`

Equivalently, because `A` is symmetric, at most five eigenvalues of `A` have modulus at least `403/2000`.

### Proof

The partner gives a rank-at-most-five matrix `S_0` with

`||A-S_0||_op<0.20141336241474038<403/2000`.

By Eckart--Young (or the singular-value min-max principle),

`s_6(A)<=||A-S_0||_op<403/2000`.

No random variables enter this deterministic implication. QED.

This already turns the partner's in-plane branch into a globally finite high-spectrum packet: arbitrarily many additional eigenvalues are still allowed, but every sixth and later singular value lies below `0.2015`.

## 3. A stronger rank-five physical paving at leverage 1/25

The previous low-rank paving compiler used the conservative leverage threshold `1/320`. The larger spectral gap in the completed fleet02/B20 packet permits a much stronger threshold.

### Lemma 3.1 — `QFORM-R5-PAVING-1OVER25-v1`

Let `L` be real symmetric, `rank(L)=r<=5`, and let `P_L` be the orthogonal projection onto `Ran(L)`. Suppose

`max_i (P_L)_{ii}<=1/25`.

Then there is a partition of the ORIGINAL coordinate indices

`I disjoint_union J=[n]`

such that, writing `G=U_I^T U_I` for any orthonormal-column factor `U` spanning `Ran(L)`, one has

`g_0 I_r <= G <= (1-g_0) I_r`,

`g_0 I_r <= I_r-G <= (1-g_0) I_r`,

where

`g_0=(1-1/sqrt(5))/2 =0.27639320225...`.

Consequently

`boxed: s_k(L[I,J])>=g_0 s_k(L),  1<=k<=r.`

### Proof

Write

`L=U Lambda U^T`, `U^T U=I_r`,

and denote the physical rows of `U` by `u_i^T`, with leverage

`ell_i=||u_i||^2=(P_L)_{ii}`.

Choose independent Rademacher signs `epsilon_i` and put

`I={i:epsilon_i=1}`, `J={i:epsilon_i=-1}`.

Then

`G-(1/2)I_r=(1/2) sum_i epsilon_i u_i u_i^T`.

By independence and cancellation of the cross terms,

`E ||G-(1/2)I_r||_F^2
 =(1/4) sum_i ||u_i u_i^T||_F^2
 =(1/4) sum_i ell_i^2
 <=(1/4)(1/25) sum_i ell_i
 =r/100
 <=1/20.`

Hence some deterministic sign choice satisfies

`||G-(1/2)I_r||_op
 <=||G-(1/2)I_r||_F
 <=1/sqrt(20)=1/(2sqrt(5)).`

This is exactly the asserted two-sided Gram bound with

`g_0=1/2-1/(2sqrt(5))`.

Because both Gram matrices are positive definite, use the polar decompositions

`U_I=Q_I G^(1/2)`,

`U_J=Q_J (I_r-G)^(1/2)`,

where `Q_I,Q_J` have orthonormal columns. Then

`L[I,J]
 =Q_I G^(1/2) Lambda (I_r-G)^(1/2) Q_J^T`.

The two outer square roots have smallest singular value at least `sqrt(g_0)`. The standard product singular-value inequality therefore gives

`s_k(L[I,J])>=g_0 s_k(L)`

for every `k<=r`. QED.

The randomization is only a deterministic-existence argument for a partition of ORIGINAL coordinate indices. It never rotates the random variables.

## 4. Perturbation-safe application to the completed fleet02/B20 packet

Use the safe rational consequences of the partner estimates

`s_3(S_0)>1597/2000`,

`||A-S_0||_op<403/2000`.

Assume first that

`max_i (P_{S_0})_{ii}<=1/25`.

Apply Lemma 3.1 to `L=S_0`, obtaining a literal physical cut `I|J`. Put

`M=A[I,J]`.

Coordinate restriction cannot increase operator norm, so

`||(A-S_0)[I,J]||_op<403/2000`.

Weyl's singular-value inequality and Lemma 3.1 give

`s_3(M)
 > g_0 (1597/2000)-403/2000.`

The right side is strictly larger than `19/1000`. Indeed the desired inequality is equivalent to

`1597 g_0>441`,

which is equivalent to

`1/sqrt(5)<715/1597`.

Both sides are positive, and this follows exactly after squaring because

`1597^2=2550409 < 5*715^2=2556125`.

Therefore

`boxed: s_3(M)>19/1000.`

Hence

`boxed: Z=e_3(M^T M)>(19/1000)^6.`

This is an actual use of the completed fleet02/B20 inequality: the rank-five lower singular resource and the retained non-diagonal residual are both present in the displayed lower bound. The residual is not deleted.

## 5. Two-sided D' compiler: payment or physical double anchor

Define both natural volume marginals for the same squared-minor probability law:

`alpha_i=P(i in R)`, for `i in I`,

`beta_j=P(j in C)`, for `j in J`.

Fix `h=2/3`.

### Theorem 5.1 — `QFORM-INPLANE-R5-PAY-OR-DOUBLEANCHOR-v1`

In the completed fleet02/B20 in-plane packet, at least one of the following holds.

**(H) Heavy physical leverage in the rank-five carrier**

`boxed: max_i (P_{S_0})_{ii}>1/25.`

**(P) Full density payment**

The full ambient quadratic form has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <1353.`

**(A) Quantitative physical row-column double anchor**

There are a physical row `i in I` and physical column `j in J` for the cut from Lemma 3.1 such that

`boxed:
 sum_{R contains i, C contains j, |R|=|C|=3}
 det(M[R,C])^2
 > 47045881/(3*10^18)
 =1.5681960333... *10^(-11).}`

Moreover, in case (A), there are pairwise-disjoint ORIGINAL-coordinate banks

`I\{i}=I_1 disjoint_union I_2`,

`J\{j}=J_1 disjoint_union J_2`,

such that the nested anchored mass obeys

`boxed:
 sum_{r_1 in I_1,r_2 in I_2,c_1 in J_1,c_2 in J_2}
 det M[{i,r_1,r_2},{j,c_1,c_2}]^2
 > 47045881/(12*10^18)
 =3.9204900833... *10^(-12).}`

No statement about one individual minor is made.

### Proof

If (H) holds there is nothing to prove. Suppose it fails. Section 4 constructs `M` with

`Z>(19/1000)^6`.

If `max_i alpha_i<=2/3`, theorem D' applies to `M` and gives

`||p_Q||_infinity
 <=6 sqrt(e) (4/3)^(-1/2) (1/3)^(-1) Z^(-1/6)
 <9 sqrt(3e) *1000/19
 =1352.6853197...<1353.`

This is (P), including continuity.

If the row gate fails but `max_j beta_j<=2/3`, apply the same theorem D' to the transposed literal cross block `M^T=A[J,I]`. It has the same `Z`, and its row marginals are exactly the `beta_j`. This again gives (P).

It remains to consider the case where both gates fail. Choose `i,j` with

`alpha_i>2/3`, `beta_j>2/3`.

Under the common squared-minor probability law,

`P(i in R and j in C)
 >=P(i in R)+P(j in C)-1
 >1/3`.

Multiplying by `Z` yields the double-anchor mass

`>Z/3>(19/1000)^6/3`.

Since `19^6=47045881`, this is exactly the displayed lower bound in (A).

For the nested four-bank statement, independently two-color every row in `I\{i}` and every column in `J\{j}`. For every anchored `3x3` minor in the preceding sum, its two residual rows are separated by the row coloring with probability `1/2`, and its two residual columns are separated by the column coloring with probability `1/2`. The two events are independent, so the expected captured anchored mass is one quarter of the total anchored mass. Some deterministic pair of colorings captures at least that expectation, giving

`>(1/4)(19/1000)^6/3=(19/1000)^6/12`.

This proves the final displayed bound. QED.

## 6. What has been closed and what remains

The completed fleet02/B20 in-plane rank-five carrier no longer survives merely because its range projection is not as diffuse as `1/320`. The product-coordinate paving threshold has been enlarged by a factor `12.8` to `1/25`.

Every such in-plane state is now one of only three explicit outcomes:

1. a full continuous density payment `<1353`;
2. a physical carrier coordinate with rank-five leverage `>1/25`;
3. a literal row-column double-anchor third-volume packet, and after disjointization a six-piece ORIGINAL-coordinate packet with nested squared-minor mass `>3.92049e-12`.

The full conjecture is still **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity is also OPEN. The partner's transverse absolute-rank-two Frobenius collar remains a separate unresolved branch, and the two in-plane survivors (heavy carrier leverage and the nested double-anchor packet) still require a whole-law receiver.

The first remaining closure edge after this run is therefore

`QFORM-ALIGNED-R5-HEAVY1OVER25-OR-NESTED-D3-PLUS-TRANSVERSE-R2-PAYMENT-v1`:

jointly spend either the physical `>1/25` carrier leverage, the nested row-column third-volume anchor above, or fleet02/B20's retained transverse rank-two Frobenius collar, while retaining all same-bank curvature, all exterior couplings and every small singular tail.

## 7. Scope audit

- All partitions are partitions of ORIGINAL coordinate indices.
- No spectral coordinate is declared probabilistically independent.
- The partner residual `A-S_0` is kept in the actual cross matrix and paid through Weyl, never removed from the random quadratic form.
- D' is applied only to a literal physical cross block and in its reviewed full-ambient scope.
- Aggregate third-volume currency remains aggregate; there is no one-good-minor inference.
- No law-uniform pointwise quadratic phase estimate is used.
- No arbitrary bounded joint density is substituted for a product projection.
- No Gaussian, moment, support, iid or log-concavity assumption appears.

Thus this is a supporting full-target structural compiler, not a claim of a complete solution.
