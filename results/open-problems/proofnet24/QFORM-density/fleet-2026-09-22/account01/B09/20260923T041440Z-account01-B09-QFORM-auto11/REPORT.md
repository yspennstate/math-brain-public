SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T04:14:40Z.
attacking: the exact global cut-rank-one N3 survivor; close the physical-star branch and rule out exact mixed-frame alignment in the clique branch before any reciprocal local-minor payment.

# account01/B09 auto11 — global star closure and aligned-clique exclusion

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T041440Z-account01-B09-QFORM-auto11`  
Assignment: Bilinear block mechanism  
Status: **ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL-ANALYTIC CLOSURE / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This report closes the entire exact physical-star branch of the strict no-pivot chamber and proves that the exactly aligned clique-factor branch cannot satisfy the target spectral hypothesis there. Consequently, inside the exact global cut-rank-one chamber, the only remaining B09 configuration is a nonaligned clique-factor frame with a physical row of leverage above `1/2`.

No step below uses law-uniform pointwise van der Corput decay, post-rotation independence, arbitrary-joint 3D coarea, conditional projection-height moments, deletion of a small quadratic coefficient, or a single-good-minor implication.

## 1. Source-pinned premises


The structural and analytic predecessor is

`yspennstate/math-open-problems@65e50ba0b12d5aff76bd5b4f3e44db2d01d07d0a`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260923T021354Z-account01-B09-QFORM-auto11/REPORT.md`.

It supplies two facts used here:

1. **Exact cut-rank-one classification.** If every disjoint physical cross block of the off-diagonal operator on the full complement of one hub has rank at most one, then the leaf off-diagonal graph is a star, a triangle, or a clique plus isolated vertices with exact factorization `A_ij=lambda v_i v_j` on the clique.
2. **Two-hub physical-star theorem.** For two physical hubs and a leaf bank with diagonal leaf self-block, if the two-column leaf-coupling Gram matrix has determinant `W>0` and all row leverages are at most `1/2`, then the full ambient form, with arbitrary physical hub block and arbitrary outside affine terms, has a continuous density satisfying

`||p_Q||_infinity <= 4 W^(-1/4)`.

The same predecessor already excludes the global triangle branch in strict `N3(1/128)`.

The designated partner source is account02/B09:

`yspennstate/math-open-problems@03ec6ccf1de2e2544e850cbda25d460aacae6a1b`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T024331Z-account02-B09-QFORM-auto12/REPORT.md`.

Its theorem `QFORM-ZERO-HUBPAIR-ARBITRARY-REMAINDER-v1` says: if two original-coordinate hubs have zero physical `2x2` core and their full complementary coupling rows `u,v` have wedge

`Delta=||u||^2||v||^2-<u,v>^2>0`,

then, with an otherwise arbitrary complementary quadratic operator,

`||p_Q||_infinity <= 2 sqrt(2) Delta^(-1/4)`,

with continuous density and the direct interval bound `P{Q in L}<=2sqrt(2)Delta^(-1/4)|L|`.

## 2. Strict N3 constants

Fix

`tau = 1/128`,
`eta = sqrt(tau+tau^2)`,
`delta = tau+eta`.

Numerically,

`eta = 0.0887329429031293`,
`delta = 0.0965454429031293`.

Inside strict `N3(tau)` we have, for every physical coordinate and every physical pair,

`|A_ii|<tau`,
`|det A[{i,j},{i,j}]|<tau`.

Therefore

`|A_ij|^2
 = |A_ii A_jj-det A[{i,j},{i,j}]|
 <= |A_ii A_jj|+|det|
 < tau^2+tau
 = eta^2`,

so

`boxed: |A_ij|<eta  for every i!=j.`                         (2.1)

The target condition implies `s_3(A)>=1`.

## 3. Entire global star branch is automatically diffuse and paid

Assume the exact cut-rank-one classification gives a star on the full complement of an outer physical hub `h`, with star center `s`. Let `L` be all remaining leaves. Then the `L x L` physical block is diagonal. Write

`H={h,s}`,
`C=A[L,H]`,
`B=A[H,H]`,
`D=A[L,L]`.

Thus

`A = A0 + E`,

where

`A0 = [[0,C^T],[C,0]]`,
`E  = [[B,0],[0,D]]`.                                         (3.1)

Every row of `C` has two entries of magnitude less than `eta`, hence

`||row_i(C)||_2^2 < 2 eta^2`.                                (3.2)

The physical `2x2` hub block obeys

`||B||_op <= tau+eta = delta`,                                (3.3)

by the maximum row-sum bound, and `||D||_op<tau`. Hence

`||E||_op <= delta`.                                          (3.4)

The nonzero singular values of `A0` are

`s_1(C),s_1(C),s_2(C),s_2(C)`

(with zeros appended if necessary), so

`s_3(A0)=s_2(C)`.                                             (3.5)

Weyl's singular-value perturbation inequality and `s_3(A)>=1` give

`boxed: s_2(C) >= 1-delta.`                                  (3.6)

Let

`G=C^T C`,
`W=det G=s_1(C)^2 s_2(C)^2`.

For a leaf row `r_i`, its leverage is

`ell_i=r_i^T G^{-1}r_i`.

Since `lambda_min(G)=s_2(C)^2`, (3.2)-(3.6) give

`ell_i
 <= ||r_i||^2/s_2(C)^2
 < 2 eta^2/(1-delta)^2
 = 0.0192924392321639
 < 1/2.`                                                      (3.7)

So the diffuse hypothesis of the predecessor two-hub theorem is **automatic**; there is no heavy-row star survivor at all. Moreover

`W^(1/4)=sqrt(s_1(C)s_2(C)) >= s_2(C) >=1-delta`.             (3.8)

Therefore

`boxed:
||p_Q||_infinity
 <=4 W^(-1/4)
 <=4/(1-delta)
 <4.428.
`                                                               (3.9)

The density is continuous, and every interval `L0` satisfies

`boxed: P{Q in L0}<4.428 |L0|.`                              (3.10)

This pays the **entire exact global star branch** of the strict N3 cut-rank-one chamber, with arbitrary signs in the hub block and without selecting a local leaf minor.

### 3.1 Designated partner applied to an actual inequality

In the zero-core subbranch

`A_hh=A_ss=A_hs=0`,

the newest account02/B09 theorem applies with the same two full complementary hub rows. Its wedge is exactly

`Delta=W=det(C^TC)`.

Using (3.8),

`Delta^(-1/4)<=1/(1-delta)`.

Hence the partner theorem gives the concrete sharpened estimate

`boxed:
||p_Q||_infinity
 <= 2 sqrt(2) Delta^(-1/4)
 <= 2 sqrt(2)/(1-delta)
 < 3.131,
`                                                               (3.11)

and

`boxed: P{Q in L0}<3.131 |L0|.`                              (3.12)

This is an actual application of the designated partner result, not a citation-only dependency. The partner theorem additionally allows an arbitrary complementary quadratic block; the star structure is used here only to force the quantitative wedge from `s_3(A)>=1`.

## 4. Exact alignment in the clique-factor branch is impossible

Assume now that the exact global cut-rank-one classification gives a clique-factor leaf block. Extend `v` by zero on isolated leaves, so for distinct leaves

`A_ij=lambda v_i v_j`,                                       (4.1)

with `lambda!=0`. Let

`c_i=A_ih`.

Consider the **exactly aligned** mixed frame

`c=theta v`                                                   (4.2)

for some real `theta`. I prove that this cannot coexist with strict `N3(1/128)` and `s_3(A)>=1`.

Write

`a=A_hh`,
`b_i=A_ii`,
`x_i=|lambda| v_i^2 >=0`.                                    (4.3)

For distinct leaves, the pair determinant condition gives

`x_i x_j
 = |lambda v_i v_j|^2
 = |A_ij|^2
 < eta^2`.                                                    (4.4)

Likewise every hub-leaf edge obeys

`theta^2 v_i^2=|A_hi|^2<eta^2`.                              (4.5)

Let `k` maximize `x_i`.

### Case 1: `x_k<=eta`

Define

`R=lambda vv^T + theta(e_h v^T+v e_h^T)`.                    (4.6)

Its range lies in `span{e_h,v}`, so `rank R<=2`. The difference `A-R` is diagonal. Its hub entry has magnitude `<tau`; every leaf entry is

`b_i-lambda v_i^2`,

whose magnitude is at most

`tau+x_i <= tau+eta=delta`.                                  (4.7)

Therefore

`||A-R||_op<=delta`,

and by Eckart--Young

`s_3(A)<=delta<1`,                                            (4.8)

contradicting the target.

### Case 2: `x_k>eta`

From (4.4), for every `i!=k`,

`x_i < eta^2/x_k < eta`.                                     (4.9)

From (4.5) at `k`,

`|theta^2/lambda|
 = theta^2 v_k^2/x_k
 < eta^2/x_k
 < eta`.                                                      (4.10)

Set

`d_k=b_k-lambda v_k^2`                                       (4.11)

and define

`R=lambda vv^T
   +theta(e_h v^T+v e_h^T)
   +d_k e_k e_k^T
   +(theta^2/lambda)e_h e_h^T`.                              (4.12)

I claim `rank R<=2`.

Indeed its range lies in

`span{e_h,e_k,w}`,
`w=v-v_k e_k`.

If `w=0`, the claim is immediate. If `w!=0`, put `r=||w||` and use the orthonormal basis

`(e_h,e_k,w/r)`.

The representing matrix is

`[[alpha, theta v_k, theta r],
  [theta v_k, lambda v_k^2+d_k, lambda v_k r],
  [theta r, lambda v_k r, lambda r^2]]`,                     (4.13)

with

`alpha=theta^2/lambda`.

A direct determinant expansion gives the exact identity

`det = d_k r^2 (alpha lambda-theta^2)`.                       (4.14)

Hence the determinant vanishes identically at the chosen `alpha`, so the three-dimensional compression has rank at most two; therefore `rank R<=2`.

Now `A-R` is diagonal. Its `k` entry is exactly zero. Its hub entry is

`a-theta^2/lambda`,

whose magnitude is `<tau+eta=delta` by (4.10). For every other leaf, (4.9) gives

`|b_i-lambda v_i^2|<tau+eta=delta`.                           (4.15)

Thus again

`||A-R||_op<=delta`,

so

`s_3(A)<=delta<1`,                                            (4.16)

contradicting the target.

We have proved:

### Theorem 4.1 — `QFORM-N3-ALIGNED-CLIQUE-IMPOSSIBLE-v1`

Inside strict `N3(1/128)`, an exact global clique-factor complement with hub coupling exactly parallel to its clique vector cannot satisfy `s_3(A)>=1`.

The key point is that the apparently dangerous single huge diagonal correction is absorbed into a **rank-two** approximant by the exact compensating hub coefficient `(theta^2/lambda)e_h e_h^T`; the determinant identity (4.14) is what prevents a spurious third large singular direction.

## 5. Combined cut-rank-one frontier

The predecessor classification leaves star, triangle, or clique-factor geometry on the full complement of the outer hub.

- The triangle branch was already excluded in strict `N3(1/128)`.
- Section 3 of this report pays the **entire star branch** with continuous density `<4.428`.
- Section 4 excludes the **exactly aligned clique branch** from the target spectral chamber.
- The predecessor mixed-frame theorem already pays the nonaligned clique branch whenever every mixed-frame row leverage is at most `1/2`.

Therefore the only exact global cut-rank-one B09 configuration still unpaid is

`QFORM-N3-CLIQUE-HEAVYROW-NONALIGN-v1`:

> the leaf off-diagonal block is an exact clique factor `lambda vv^T` off diagonal; the outer-hub coupling `c` is genuinely transverse to `v`; and some physical row of the two-vector frame `(v_i,c_i)` has leverage greater than `1/2`.

Because two-dimensional leverage sums to two, at most three physical rows can exceed `1/2`. The next step is to elevate those finitely many rows while preserving the third target spectral resource and route the remainder to the completed zero-hubpair, physical-pair, grouped-square, ridge, or mixed-hub theorems. The result above shows that **exact alignment is not the obstruction**; only physical-row concentration remains in this exact chamber.

## 6. Finite verification

`CHECK.py` and `CHECK_OUTPUT.txt` in this run directory verify

- `delta=0.0965454429031293<1`;
- the automatic star leverage bound is `0.0192924392321639<1/2`;
- the star density constant is `<4.428`;
- the designated-partner zero-core specialization is `<3.131`;
- the exact determinant identity in (4.14) vanishes when `alpha=theta^2/lambda`.

These checks support arithmetic and the explicit rank-two identity; the proof itself is the argument above.

## 7. Status

New proved supporting claims:

- `QFORM-N3-GLOBAL-STAR-CLOSURE-v1`;
- `QFORM-N3-ALIGNED-CLIQUE-IMPOSSIBLE-v1`;
- combined frontier reduction to `QFORM-N3-CLIQUE-HEAVYROW-NONALIGN-v1`.

The full conjecture remains OPEN. Continuity is proved for the newly closed star branch (and for the partner zero-core specialization), but not for the unrestricted target.
