SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T06:39:06.450560Z.
attacking: convert a robust third physical cross singular value directly into either a continuous density bound or two genuinely heavy opposite-side physical stars, using exact fixed-size volume-sampling marginals.

# account01/B08 r24 — fixed-order volume marginals and bilateral-star router

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** diffuse eigenvector case / analytic derivation and exact structural identities  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_ANALYTIC-STRUCTURAL THEOREM / DESIGNATED_PARTNER_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. Continuity for the unrestricted target remains OPEN. All variables below are ORIGINAL-coordinate independent cap-one inputs. No moments, Gaussianity, compact support, connected support, log-concavity, post-rotation independence, pointwise law-uniform van der Corput decay, arbitrary-joint coarea, worst fiber-density cap, or deletion of a small matrix tail is used.

## 1. Source-pinned inputs


The immediate B08 predecessor is

`yspennstate/math-open-problems@5d2f07b086dec22993a28780c0e98fd7aef4c464`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T053638Z-account01-B08-QFORM-auto11/REPORT.md`.

It proves `QFORM-SELF-DUAL-REDUCING-PROJECTION-LADDER-v1`. In particular, if a 3D reducing spectral subspace has projection leverage at most `1/3` and spectral scale `L`, then there is an ORIGINAL-coordinate cut `I|J` with the self-dual scale

`d/L >= 0.0766562902983031... > 3/40`,                              (1.1)

such that, if one child retains no eigenvalue of modulus at least `d`, the ACTUAL cross block `B=A[I,J]` satisfies

`s_3(B)>d`.                                                           (1.2)

The designated partner actually used is account02/B08 r22,

`yspennstate/math-open-problems@2df2c9bc0e4d9a0dcd2cdde85390d3c33ae8c334`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T054710Z-account02-B08-qform-diffuse-r22-54d75ca3/REPORT.md`.

Its completed theorem `QFORM-MIXED-ORDER-JENSEN-v1` says the following. For a probability law `Omega` on nonzero square physical minors of an ORIGINAL-coordinate cross block, write

`alpha_i=P(i in S)`, `kbar=E|S|`,
`K=exp(E log det(B[S,T])^2 + H(Omega))`.

If `q>=1`, `q<kbar/2`, and every row marginal `alpha_i<=q/2`, then the full ambient quadratic form, with arbitrary same-bank quadratic blocks, outside couplings and affine terms retained, has a continuous `C0` density satisfying

`||p_Q||_infinity <= 2 sqrt(e) [kbar/(kbar-2q)] q^(-1/2) K^(-1/(2kbar)).` (1.3)

I apply (1.3) below to the canonical order-three squared-minor law, at an actual target inequality.

## 2. Exact marginal identity for fixed-size squared-minor sampling

Let `B` be an `m x n` real matrix of rank at least `k`, with singular values

`s_1>=s_2>=...`, `lambda_j=s_j^2`,

and define

`Z_k=e_k(B^T B)=sum_{|S|=|T|=k} det(B[S,T])^2`.                    (2.1)

On the nonzero `k x k` physical minors define the probability law

`P(S,T)=det(B[S,T])^2/Z_k`.                                       (2.2)

Let `alpha_i=P(i in S)` be the row inclusion marginals.

### Lemma 2.1 — `QFORM-FIXED-K-VOLUME-MARGINAL-STAR-v1`

For every physical row `i`,

`boxed: alpha_i <= k ||B[i,*]||_2^2 / s_k(B)^2.`                   (2.3)

The transpose statement holds for every physical column.

### Proof

Put `L=BB^T`. Summing (2.2) over column sets by Cauchy--Binet shows that the induced row-set law is

`P(S)=det L[S,S]/e_k(lambda)`.                                     (2.4)

Write `L=U diag(lambda_j) U^T`. The exact fixed-size determinantal marginal identity is

`alpha_i=sum_j theta_j u_ij^2`,
`theta_j=lambda_j e_(k-1)(lambda without lambda_j)/e_k(lambda).`   (2.5)

For completeness, (2.5) follows by multiplying the `i`th physical coordinate of `L` on both sides by `sqrt(t)`, differentiating the principal-minor partition function at `t=1`, and using the spectral derivative

`grad e_k(L)=U diag(e_(k-1)(lambda without lambda_j)) U^T`;
`grad e_k(L)` commutes with `L`, so the derivative is exactly the right side of (2.5) times `Z_k`.

The only estimate needed is the elementary symmetric-polynomial inequality

`lambda_k e_(k-1)(lambda without lambda_j) <= k e_k(lambda).`       (2.6)

To prove (2.6), take any `(k-1)`-set `R` not containing `j`. Among the top `k` eigenvalue indices there is an index `r` not in `R`. Hence

`lambda_k prod_(a in R)lambda_a <= lambda_r prod_(a in R)lambda_a`, (2.7)

and the right side is the weight of the `k`-set `R union {r}`. After summing over all `R`, each `k`-set can receive at most `k` preimages, which proves (2.6).

Combining (2.5)-(2.6),

`alpha_i
 <= (k/lambda_k) sum_j lambda_j u_ij^2
 = (k/s_k(B)^2) L_ii
 = k ||B[i,*]||_2^2/s_k(B)^2`.                                    (2.8)

This proves (2.3). Applying the same argument to `B^T` gives the column statement. QED.

The factor `k` is not an artifact of this proof: for spectrum `(1,...,1,epsilon)` with exactly `k` unit eigenvalues and the tail direction `j=k+1`, the ratio `e_(k-1)(lambda without lambda_j)/e_k(lambda)` tends to `k` as `epsilon downarrow0`.

## 3. Robust third cross singular value: paid or bilateral physical stars

Set

`sigma=s_3(B)>0`,
`Z_3=e_3(B^T B)`.                                                     (3.1)

### Theorem 3.1 — `QFORM-S3-VOLUME-OR-BILATERAL-STAR-v1`

For every `q` with

`1 <= q < 3/2`,                                                       (3.2)

at least one of the following holds:

**PAID.** The full ambient quadratic form has a continuous `C0` density with

`boxed:
 ||p_Q||_infinity
 <= [6 sqrt(e)/((3-2q)sqrt(q))] sigma^(-1).
`                                                                         (3.3)

**BILATERAL STAR.** There is a physical row `i` and a physical column `j` of the same ORIGINAL-coordinate cross block such that

`boxed:
 ||B[i,*]||_2 > sigma sqrt(q/6),
 ||B[*,j]||_2 > sigma sqrt(q/6).
`                                                                         (3.4)

At `q=1`, this becomes the particularly clean alternative

`boxed: ||p_Q||_infinity <= 6 sqrt(e)/sigma`                            (3.5)

with continuous `C0` density, or there are opposite-side physical stars each of norm `>sigma/sqrt(6)`.

### Proof

Use the canonical order-three law

`P(S,T)=det(B[S,T])^2/Z_3`.                                             (3.6)

For this law `kbar=3`. Its entropy-determinant currency in (1.3) is **exactly**

`K=Z_3`: indeed

`H(P)=-E log P=-E log det^2 + log Z_3`,                                (3.7)

so `E log det^2+H(P)=log Z_3`.

If every row star obeys

`||B[i,*]||_2 <= sigma sqrt(q/6)`,                                     (3.8)

Lemma 2.1 with `k=3` gives

`alpha_i <= 3 ||B[i,*]||_2^2/sigma^2 <= q/2`.                         (3.9)

The designated partner theorem (1.3) applies and yields

`||p_Q||_infinity
 <= 2 sqrt(e) [3/(3-2q)] q^(-1/2) Z_3^(-1/6).`                        (3.10)

But

`Z_3=sum_{a<b<c}s_a^2s_b^2s_c^2 >= s_1^2s_2^2s_3^2 >= sigma^6`,       (3.11)

hence (3.3). The partner theorem also supplies continuity and vanishing at infinity.

Apply the same argument to `B^T`. Therefore if the PAID conclusion fails, neither orientation can satisfy (3.8): some row and some column must both violate it, which is exactly (3.4). QED.

This theorem retains **all** extra singular directions of `B` and all ambient same-bank/outside curvature. It does not select one local determinant and does not require exact cross rank three.

## 4. Actual application to the basis-invariant diffuse spectral branch

Return to the predecessor self-dual cut. Assume the full high-spectral projector is diffuse in the basis-invariant sense used there,

`rank 1_(|A|>=L) >=3`,
`max_i (1_(|A|>=L))_ii <=1/3`,                                       (4.1)

and take its guaranteed cut `I|J`. On the `k=0` child-count branch, (1.1)-(1.2) give

`sigma=s_3(A[I,J]) > d > 3L/40`.                                    (4.2)

Applying Theorem 3.1 at `q=1` gives the exhaustive source-valid alternative

`boxed:
 ||p_Q||_infinity < 80 sqrt(e)/L
 =131.897701656.../L,
`                                                                         (4.3)

with a continuous `C0` density, or there are a physical row and a physical column of the true cross block with

`boxed:
 ||B[i,*]||_2,\ ||B[*,j]||_2
 > 3L/(40 sqrt(6))
 =0.0306186217848... L.
`                                                                         (4.4)

This is an actual use of the completed account02/B08 theorem on the live B08 spectral branch. Relative to the preceding third-volume router, the no-payment survivor no longer needs to be carried as an abstract double-nested determinant packet: a robust `s_3` forces a **bilateral physical-star witness** unless the full density is already paid. The price is that the star threshold in (4.4) is smaller than the predecessor's one-sided `d` threshold; the gain is bilateral physical geometry and the sharper direct paid constant.

For a stronger structural threshold one may take, for example, `q=4/3`: either

`||p_Q||_infinity <= 9 sqrt(3e)/sigma`,                               (4.5)

or each side has a star `> (sqrt(2)/3)sigma`. The parametric form (3.3)-(3.4) records the full constant/structure tradeoff.

## 5. What remains unpaid

This run does **not** close the full diffuse branch. The immediate remaining implication is

`QFORM-BILATERAL-STAR-WITH-ARBITRARY-LEAKAGE-v1`:

> Starting from two opposite-side original-coordinate stars supplied by (3.4), pay them while retaining arbitrary quadratic curvature on and between both arm banks and the full complementary spectrum.

The leakage-free two-arm receiver is already known, but the live problem allows dependent-bank leakage through those same arm coordinates, so it cannot be silently applied. Likewise, a bilateral star does not justify selecting one large edge: star mass can be spread over arbitrarily many coordinates. The `k=1,2,3` child-count branches of the self-dual ladder remain parallel open states.

The new theorem is therefore a supporting analytic/structural result, not a full solution. It proves continuity only on the PAID branches (3.3), not on the bilateral-star survivor or the unrestricted conjecture.
