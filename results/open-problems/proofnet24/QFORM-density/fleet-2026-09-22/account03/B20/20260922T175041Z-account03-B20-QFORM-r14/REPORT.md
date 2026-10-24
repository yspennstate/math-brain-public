# account03/B20 QFORM r14 — half-barrier nested resource extraction

**Run:** `20260922T175041Z-account03-B20-QFORM-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh control used for publication:** `yspennstate/math-research-brain@b7325a4d01f03ddcd0dabbfbbdbecaec8e647a8d`, OWNER CONTROL revision `2026-09-22.9`  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_REDUCTION_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and scope

The target is the unrestricted statement: for every dimension, every independent real input vector `X` whose coordinate densities satisfy `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or give a valid counterexample. Continuity is a separate obligation.

No Gaussian, moment, compact-support, connected-support, log-concavity, diagonal-basis, or post-rotation independence assumption is used here. The argument below is purely deterministic matrix analysis until the final explicitly identified paid density branches.

The live correction ledger was reread after the derivation. In particular this run does not use a single good local minor, a rank-three physical cut, a conditional-density-cap surrogate, pointwise van-der-Corput decay, or bounded-projection-density alone.

## 2. Source-pinned inputs actually used

### 2.1 Fresh account03/B19 half-barrier theorem

Account03/B19 run `20260922T170047Z-account03-B19-QFORM-r15`, canonical mathematics

`yspennstate/math-open-problems@539d1d9953c616bf0e1ab2dafeef55102f89c2b9`

proves the following full-target branch. Put

`H=A-diag(A)`.

For every fixed `0<=theta<1/2`, if `s_2(H)<=theta`, then

`||p_Q||_infinity <= max(50(1-theta)^(-3/4), pi/sqrt(1-2theta)).`       (2.1)

In particular at

`theta=499/1000`,                                                     (2.2)

this is `<84`. Therefore every still-unpaid target configuration satisfies

`boxed( s_2(H)>theta. )`                                              (2.3)

### 2.2 Assigned partner account04/B20

The required partner run is account04/B20 `20260922T172057Z-account04-B20-QFORM-r3`, canonical mathematics

`yspennstate/math-open-problems@25ad8faaac5064b6814d51ae63d894fe97c1eac4`.

Its theorem `QFORM-CROSS-DOMINATED-SECOND-SCHUR-CLOSURE-v1` says that inside the already-established diagonal-dominated first-pivot chain, with

`|a|>=tau>=1/4`, `S=[[d,c^T],[c,C]]`, `||c||>|d|`, `||c||>tau/9`,      (2.4)

the branch is paid with

`||p_Q||_infinity<5262`.                                               (2.5)

The exact inequalities from that proof that will be used below are, in the nonzero-second-pivot case,

`|d| sigma > tau^2/256`                                               (2.6)

for a product-preserving residual cross bank and

`||p_Q||_infinity <=48 B |a|^(-1/2)(|d|sigma)^(-1/4)`,                 (2.7)

where

`B=(2+sqrt(pi))(4e)^(1/4)`.                                           (2.8)

The zero-second-pivot branch satisfies `<48*2^(3/4)`.

## 3. A parameterized physical-cut theorem beyond the half barrier

The main new result is deterministic and can be stated for any `theta in (0,1/2)` satisfying `s_2(H)>theta`.

### Theorem 3.1 — `QFORM-HALF-BARRIER-NESTED-RESOURCE-v1`

Let `A` be real symmetric with `s_3(A)>=1`, and put `H=A-diag(A)`. Suppose

`s_2(H)>theta>0`.                                                      (3.1)

Then there is a bipartition of the original physical coordinates `L disjoint_union R` and `C=A[L,R]` such that

`s_1(C)+s_2(C)>theta/2`.                                               (3.2)

Consequently at least one of the following holds.

**I. Two-direction outer bank**

`s_2(C)>=theta/8`.                                                     (3.3)

**II. Strong one-direction outer bank plus a large physical pivot**

`s_1(C)>3theta/8` and, in one of the physical side blocks, there is an original coordinate `i` with

`|A_ii| >= (1-theta/8)/2`.                                            (3.4)

**III. Strong one-direction outer bank plus a nested inner bank**

`s_1(C)>3theta/8` and, inside one of the same physical side blocks, there is a further physical partition `S_1 disjoint_union S_2` satisfying

`s_1(A[S_1,S_2]) > (1-theta/8)/4`.                                   (3.5)

No coordinate rotation is made. Every bank consists of disjoint subsets of the original independent coordinates.

### Proof

Let `eps_i` be independent Rademacher signs and `D_eps=diag(eps_i)`. Since `H` has zero diagonal,

`K_eps := (H-D_eps H D_eps)/2`                                       (3.6)

is exactly the symmetric cross matrix associated with the physical cut induced by the signs. After a permutation,

`K_eps = [[0,C],[C^T,0]].`                                           (3.7)

Moreover `E[D_eps H D_eps]=0`, hence

`E K_eps=H/2`.                                                        (3.8)

The Ky-Fan four norm is convex. Therefore

`||H||_(4)/2 = ||E K_eps||_(4) <= E ||K_eps||_(4)`.                   (3.9)

For (3.7), the nonzero singular values occur in duplicated pairs, so

`||K_eps||_(4)=2(s_1(C)+s_2(C)).`                                    (3.10)

Thus some physical cut obeys

`s_1(C)+s_2(C) >= ||H||_(4)/4`.                                      (3.11)

Since `s_1(H)>=s_2(H)>theta`, one has `||H||_(4)>2theta`; (3.2) follows.

If (3.3) fails, then

`s_2(C)<theta/8`,                                                     (3.12)

and (3.2) forces

`s_1(C)>theta/2-theta/8=3theta/8`.                                  (3.13)

Choose top singular vectors `u,v` of `C` and put

`R_1=[[0,s_1(C)uv^T],[s_1(C)vu^T,0]]`                               (3.14)

in the same physical block decomposition. This matrix has rank at most two. By the Eckart-Young characterization of the third singular value,

`||A-R_1||_op >= s_3(A)>=1`.                                        (3.15)

The cross block of `A-R_1` is `C-s_1(C)uv^T`, whose operator norm is `s_2(C)`. Its diagonal side blocks are unchanged. Hence

`1 <= ||A-R_1||_op
   <= max(||A_LL||_op,||A_RR||_op)+s_2(C).`                           (3.16)

Using (3.12), one of the physical side blocks, call it `M`, must satisfy

`||M||_op > beta := 1-theta/8`.                                     (3.17)

If some physical diagonal of `M` has modulus at least `beta/2`, alternative II holds.

Otherwise

`||diag(M)||_op < beta/2`.                                           (3.18)

Set `O=M-diag(M)`. Then

`||O||_op >= ||M||_op-||diag(M)||_op > beta/2`.                      (3.19)

Apply the same Rademacher-cut construction to `O` inside this physical side block. If `J_delta=(O-D_delta O D_delta)/2`, then `E J_delta=O/2`. Convexity of operator norm yields some cut with

`||J_delta||_op >= ||O||_op/2 > beta/4`.                             (3.20)

The operator norm of this symmetric cross matrix is exactly the top singular value of the corresponding inner physical cross block. This is (3.5). QED.

## 4. Explicit full-target constants at the current half barrier

Take the paid B19 threshold

`theta=499/1000`.                                                     (4.1)

Then either B19 already gives `||p_Q||_infinity<84`, or every survivor has one of the three exact physical-resource forms

`two-cross:       s_2(C) >= 499/8000 = 0.062375`,                    (4.2)

or

`outer-one:       s_1(C) > 1497/8000 = 0.187125`,                    (4.3)

plus either

`physical-pivot:  |A_ii| >= 7501/16000 = 0.4688125`,                 (4.4)

or

`nested-bank:     s_1(A[S_1,S_2]) > 7501/32000 = 0.23440625`.        (4.5)

This strictly strengthens the preceding B20 r13 resource constants, which had been based on the older `s_2(H)>3/20` barrier.

The parameterized form shows the limiting deterministic constants as the paid barrier tends to `1/2` from below:

`theta/8 -> 1/16`, `3theta/8 ->3/16`, `(1-theta/8)/2 ->15/32`, and `(1-theta/8)/4 ->15/64`.   (4.6)

## 5. Assigned-partner payment on the new physical-pivot branch

Alternative II produces a genuine original-coordinate scalar pivot with

`|a|>=7501/16000>1/4`.                                               (5.1)

Whenever this pivot enters the completed account04/B20 diagonal-dominated first-pivot chain and its selected second Schur row is cross-dominated as in (2.4), the branch is now fully paid.

Indeed, for the nonzero second pivot, combine (2.6)-(2.7):

`||p_Q||_infinity
 <48B tau^(-1/2)(tau^2/256)^(-1/4)
 =192B tau^(-1)
 <=768B
 =5261.066290... <5262`,                                             (5.2)

because `tau>=1/4`. If `d=0`, the partner gives `<48*2^(3/4)<81`. Thus the new structural pivot is not merely identified: on the entire completed partner subbranch it feeds directly into a universal density inequality.

What remains of alternative II is precisely the complement of that established first-pivot/second-row chain; no claim is made that (5.1) by itself forces those additional Schur hypotheses.

## 6. Why this is not one of the refuted local-minor mechanisms

The proof never selects a reciprocal tiny `3x3` minor. It first preserves an entire cross bank by a physical random cut, and when that bank is effectively rank one it removes only its top symmetric rank-two contribution. The third large singular direction of `A` then forces a whole side block to remain large. The second cut is again bank-valued and product-preserving. This is compatible with the known singleton-plus-many-bank stress families in which every fixed local principal block degenerates with dimension.

## 7. Remaining implication

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Continuity is not proved by Theorem 3.1; it is a structural reduction.

After combining the fresh B19 half-barrier with the assigned account04/B20 payment, the first unpaid synthesis target can be stated more sharply as

`QFORM-HALF-BARRIER-BANK-PAYMENT-v1`:

> Under the full product-law quantifiers, pay either (a) an outer physical cross bank with `s_2>=499/8000`, or (b) an outer bank with `s_1>1497/8000` together with a nested inner bank with `s_1>7501/32000`, while retaining arbitrary same-bank quadratic terms and all remaining spectrum; in the physical-pivot branch only the complement of the already-paid account04/B20 Schur regimes remains.

A successful next step should use a bank-level fractional/Riesz or regularized-determinant argument before choosing local coordinates, because the live correction ledger rules out replacing these grouped resources by one uniformly good local minor.
