# QFORM fleet03/B14 r26 — collective aligned-curvature bank localization

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-23T04:37:07Z.

attacking: aligned quadratic bank curvature under collective compression, preserving arbitrary shifts, unbounded fragmented supports and outside affine terms.

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T043707Z-fleet03-B14-QFORM-r26`  
Status: `SUPPORTING TARGET-LEVEL THEOREM PROVED / FULL QFORM OPEN`  
Continuity: `OPEN for the full target; the new aligned-curvature branch below proves essential boundedness only`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and sources actually used

The target remains the unrestricted statement: independent real original coordinates, each with probability density at most one; arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one; prove a dimension-free essential density bound for `X^T A X`, or give a valid counterexample. No support, moment, log-concavity, Gaussianity, connectedness, identical-law, centering, or spectral-coordinate independence is assumed.

This run consumes the current correction boundary: no law-uniform pointwise quadratic-phase decay; no independence after rotation; no arbitrary-joint rank-three coarea bound; no positive moment of a worst conditional projection-density cap; no universally good single physical minor or rank-three physical cross cut; and no small-operator-norm-as-small-random-quadratic-error step on unbounded laws.

Two completed sources are applied at equations, not merely cited:

1. **Designated partner fleet04/B14 r6.** `yspennstate/math-open-problems@6442bbe9d4647a730b27b8e0786bc54b2546b7ec`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260923T011517Z-fleet04-B14-kernel-leakage-core-r6/REPORT.md`. Its fixed physical-core compiler states that an actual four-coordinate symmetric block with at least three eigenvalues of modulus at least `sigma>0` gives, uniformly in arbitrary affine terms and arbitrary cap-one product laws,

   `||p||_infinity <= C4/sigma`,

   where

   `C4 = 1000(8+log 4) = 9386.294361119892...`.

   Conditioning on all outside **original** coordinates preserves the same constant and allows arbitrary outside quadratic blocks and couplings. Its rough-law transfer permits unbounded and arbitrarily fragmented supports.

2. **Newest volume-stability package.** `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, path `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/`. In particular, if an original-coordinate cross block `M=M0+E` satisfies `s3(M0)>=a`, maximum row leverage of `Range(M0)` at most `1/2`, and `||E||op<=a/16`, then the full ambient quadratic-plus-affine form has a bounded continuous density `<23/a`. Its tail extension permits two substantial singular directions plus a collective tail under the stated volume-marginal gate. These are scoped exits, not the full conjecture.

The preceding fleet03/B14 r25 report is used only as a predecessor: it handled a **pure** collective bank with zero `V` self-block. The present run changes mechanism by allowing a nonzero, arbitrarily large, aligned quadratic curvature on that same diffuse bank.

## 2. Main theorem: collective aligned-curvature bank

Split the original independent coordinates as

`X=(U,V,Z)`, with `U in R^3`, `V in R^m`.

Assume that, in these original coordinates, the coefficient matrix has block form

`A = [[B,        k a^T,       C],
      [a k^T,    theta a a^T, a b^T],
      [C^T,      b a^T,       D]],`                         (2.1)

where

- `B=B^T` is `3x3`;
- `k in R^3`, `||k||_2=1`, and `Bk=0`;
- `a in R^m` is nonzero, with `L=||a||_2`;
- `theta in R` is completely arbitrary;
- `C,D,b` are arbitrary of compatible sizes.

Thus the same original-coordinate bank direction `a` carries the `U-V` leakage, the within-`V` quadratic curvature, and the `V-Z` coupling. No restriction is imposed on the magnitude or sign of `theta`.

Set

`r=L/sqrt(2)`.                                                (2.2)

### Theorem 2.1A — two-large-core version, uniform in bank curvature

Suppose the two eigenvalues of `B|_(k^perp)` both have modulus at least `nu>0`. Then for every collection of independent cap-one input laws,

`boxed:
 ||p_(X^T A X)||_infinity
 <= C4 / min(nu,r)
 = C4 max(1/nu,sqrt(2)/L).`                                  (2.3)

The constant is independent of `theta`, the dimension of `V` and `Z`, all outside blocks/couplings, every translation, every support radius, every support gap, and every fragment count.

### Theorem 2.1B — one-large-core quantitative version

Assume only that `B` has one eigenvalue of modulus at least `nu>0`. Define

`delta(theta,r)
 = [sqrt(theta^2 r^4+4r^2)-|theta|r^2]/2
 = 2r^2/[sqrt(theta^2 r^4+4r^2)+|theta|r^2]
 = r/[sqrt(1+(theta r/2)^2)+|theta|r/2].`                   (2.4)

Then

`boxed:
 ||p_(X^T A X)||_infinity
 <= C4 / min(nu,delta(theta,r)).`                            (2.5)

For `theta=0`, `delta(0,r)=r`, recovering the pure-bank scale of the preceding r25 theorem. For large aligned curvature, (2.5) records the genuine deterioration of the second hyperbolic eigenvalue rather than hiding it.

## 3. Proof

### 3.1 Condition only on outside original coordinates

Fix `Z=z`. Because this is conditioning in the original product basis, the three coordinates of `U` and all coordinates of `V` remain mutually independent with their original density caps. Put

`W=a^T V`.                                                     (3.1)

By the exact factorization in (2.1), the entire bank `V` enters the conditional form only through `W`:

`Q_z
 = U^T B U + 2(k^T U)W + theta W^2
   + 2(Cz)^T U + 2(b^T z)W + z^T D z.`                     (3.2)

No part of the `V` law has been rotated or conditioned on.

### 3.2 Compress the whole bank before inversion

The sharp one-dimensional product-projection theorem gives

`||p_W||_infinity <= sqrt(2)/L.`                              (3.3)

Let

`Y=(sqrt(2)/L)W = W/r.`                                      (3.4)

Then `Y` has a probability density bounded by one and is independent of the three original coordinates of `U`. Since `W=rY`, the conditional form is an arbitrary affine perturbation of the four-variable quadratic form with coefficient matrix

`H = [[B,   r k],
      [r k^T, theta r^2]].`                                  (3.5)

This is the crucial aggregate-before-inversion step: the proof pays the full bank norm `||a||_2`, never the reciprocal of one tiny coefficient `a_j`.

### 3.3 Exact spectrum of the aligned-curvature enlargement

Choose a deterministic orthonormal basis of coefficient space in which the third basis vector is `k` and the first two diagonalize `B|_(k^perp)`. This is matrix algebra only; the random variables are not rotated. In that basis, the spectrum of `H` consists of the two eigenvalues of `B|_(k^perp)` together with the two eigenvalues of

`T = [[0,r],[r,theta r^2]].`                                 (3.6)

They are

`tau_+ = [theta r^2 + sqrt(theta^2 r^4+4r^2)]/2,`
`tau_- = [theta r^2 - sqrt(theta^2 r^4+4r^2)]/2.`            (3.7)

Since

`det T=-r^2`,                                                  (3.8)

the two eigenvalues have opposite signs and

`min(|tau_+|,|tau_-|)=delta(theta,r)`                         (3.9)

with `delta` given by (2.4). Also

`max(|tau_+|,|tau_-|)>=r`,                                   (3.10)

because their absolute product is `r^2`.

If both nonzero eigenvalues of `B` have modulus at least `nu`, equations (3.7)-(3.10) show that `H` has at least three eigenvalues of modulus at least

`sigma_A=min(nu,r)`,                                          (3.11)

**uniformly for every real `theta`**: the two `B` eigenvalues supply two directions and the larger hyperbolic eigenvalue of `T` supplies the third.

If only one eigenvalue of `B` is known to have modulus at least `nu`, both hyperbolic eigenvalues are needed, and `H` has three eigenvalues of modulus at least

`sigma_B=min(nu,delta(theta,r)).`                             (3.12)

### 3.4 Apply the designated partner theorem to the actual inequality

For every fixed `z`, the active variables `(U_1,U_2,U_3,Y)` are four independent cap-one variables, and all `z`-dependence in (3.2) is affine or scalar. Fleet04/B14 r6 therefore gives

`||p_(Q|Z=z)||_infinity <= C4/sigma_A`                        (3.13)

under the hypotheses of Theorem 2.1A, or

`||p_(Q|Z=z)||_infinity <= C4/sigma_B`                        (3.14)

under Theorem 2.1B. The estimates are uniform in `z`. Averaging the conditional laws proves (2.3) and (2.5).

This application retains every outside quadratic coefficient and every outside cross coupling. It does not approximate `theta a a^T` as a small perturbation; `theta` may be arbitrarily large.

## 4. Exact translation and rough-support invariance

The theorem is genuinely translation-uniform.

- Translating `V` by a deterministic vector replaces `W` by `W+c`. Then `theta W^2` becomes `theta W^2+2theta cW+theta c^2`: only the affine/scalar terms change, while the quadratic matrix (3.5) is unchanged.
- Translating `U` changes only affine/scalar terms after expansion.
- Translating `Z` changes the affine parameters generated in (3.2), again without changing the active four-variable quadratic matrix.

The designated partner theorem is uniform over every affine vector and scalar. The projection estimate (3.3) has no moment or support hypothesis. Consequently arbitrary distant fragments, unbounded supports, and arbitrary shifts pay **zero localization tax** in (2.3)-(2.5).

Equivalently, by fleet04/B14's completed finite-mixture purification, the same inequalities may be proved on compact finite-fragment product indicators of total marginal measure one and transferred back with exactly the same constants. No uniform fragment-count or support-diameter bound is required or asserted.

## 5. Valid target stress family: dense aligned bank curvature

For every `N>=1`, take

`B=diag(1,-1,0)`, `k=e_3`,
`a_N=sqrt(2/N)(1,...,1) in R^N`,                               (5.1)

with no outside `Z` bank and arbitrary `theta in R`. Then

`L=||a_N||_2=sqrt(2)`, `r=1`.                                (5.2)

The full matrix is

`A_N=[[B, k a_N^T],[a_N k^T, theta a_N a_N^T]].`             (5.3)

Let `u_N=a_N/L`. On the deterministic coefficient subspace spanned by `e_3` and `u_N`, the remaining two eigenvalues are those of

`[[0,sqrt(2)],[sqrt(2),2theta]],`                             (5.4)

whose determinant is `-2`. Hence one of them has modulus at least `sqrt(2)>1`. Together with the two eigenvalues `+1,-1` of `B`, the matrix `A_N` has at least three eigenvalues of modulus at least one for **every** `N` and every real `theta`.

At the same time every individual leakage coefficient equals `sqrt(2/N)` and tends to zero, while the `V` self block `theta a_N a_N^T` is dense and can have arbitrarily large operator norm as `|theta|` grows. Any one-coordinate leakage selection therefore becomes arbitrarily badly scaled as `N` increases, but Theorem 2.1A gives

`boxed: ||p_(X^T A_N X)||_infinity <= C4}`                   (5.5)

for every `N`, every `theta`, and every independent cap-one input law. Numerically `C4=9386.294361119892...`.

For `theta!=0`, this family is outside the zero-`V`-self-block hypothesis of the preceding r25 pure-bank theorem. Thus (5.5) is a genuine extension, not a restatement.

## 6. Application of the newest volume-stability result: a two-exit reduction

The newest required volume theorem can be combined with Theorem 2.1 without any support localization.

Consider a proposed original-coordinate reduction that exposes a cross bank `M`.

**Diffuse-volume exit.** If

`M=M0+E`, `s3(M0)>=a>0`,
`max_i (P_Range(M0))_ii<=1/2`, `||E||op<=a/16`,              (6.1)

then the newest package at `c2414ef...` gives directly

`||p_Q||_infinity <23/a`                                     (6.2)

and a continuous density. Arbitrary self-block curvature, outside couplings, affine terms, translations and rough/unbounded supports are already included. No `small quadratic random error` interpretation is used.

**Aligned rank-one survivor.** A rank-one cross block has `E3(M^T M)=0`, so the three-volume exit is unavailable. If its same-bank quadratic block and outside coupling factor through the same bank direction as in (2.1), Theorem 2.1A/2.1B gives instead (2.3)/(2.5), paying the **whole** bank norm before inversion.

Thus any structural argument may safely remove both classes in (6.1) and (2.1) without adding bounded support, moments, or coordinate-selection taxes. What remains is a genuinely smaller structural debt: low-cross-rank/high-leverage configurations with **unaligned** bank curvature or several bank coupling directions, plus the corresponding low-total-tail N3 survivors.

This is an equation-level use of the newest result: (6.2) and (2.3) are compatible exits with disjoint failure modes. Neither is promoted beyond its hypotheses.

## 7. What is still open

The full conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`.

The new theorem does **not** handle an arbitrary `V` self block. If `A[V,V]` has components outside the rank-one line `span(a)`, or if `A[V,Z]` has row space larger than `span(a)`, the conditional form cannot be compressed to the one scalar `W=a^T V` without losing quadratic information or creating dependence. This is the first essential missing implication for this B14 route.

A useful next target is therefore a multi-statistic version: compress `V` simultaneously to a small original-bank image `R^T V` that contains the leakage direction and the range of the within-bank curvature/couplings, while obtaining a dimension-free joint density or a direct fixed-core quadratic estimate. The volume-stability theorem already pays the sufficiently diffuse rank-at-least-three version; the unresolved regime is low-rank/high-leverage and must preserve original product provenance.

Continuity is separate. The diffuse-volume branch (6.2) gives a continuous density. The fixed four-coordinate partner theorem used for (2.3)-(2.5) supplies interval domination/essential boundedness; no full-target or branch-wide continuous representative is claimed here.

## 8. Integrity/status

- New theorem: `QFORM-COLLECTIVE-ALIGNED-CURVATURE-BANK-v1`, proved above in two quantitative versions.
- Designated partner applied: fleet04/B14 r6 at (3.13)-(3.14), source commit `6442bbe9d4647a730b27b8e0786bc54b2546b7ec`.
- Newest required package applied: volume-stability theorem at (6.2), source commit `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`.
- Early checkpoint for this run was committed before the full argument.
- No Monte Carlo or histogram is used as proof; all stress-family spectral statements above are exact algebra.
- Full QFORM remains open and requires two independent end-to-end reviews before any full candidate could be declared complete.
- Repository transport is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
