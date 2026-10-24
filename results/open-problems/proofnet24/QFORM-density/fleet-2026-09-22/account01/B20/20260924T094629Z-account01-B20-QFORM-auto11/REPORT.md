SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-24T09:46:29Z.
attacking: the first r50/r51 survivor after the new pair-free gate; show that any target form with a moderate physical diagonal and no universal-size physical star is already paid, by combining exact scalar Schur geometry, the completed account02/B20 strong-pair theorem, and aggregate disjoint-tetrad smoothing.

# account01/B20 — moderate diagonal to physical-star funnel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T094629Z-account01-B20-QFORM-auto11`  
Status: **ESSENTIAL_STEP_APPLIED / NEW GLOBAL STRUCTURAL FUNNEL / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted theorem remains OPEN. No counterexample is claimed. Full-target continuity remains OPEN separately. The argument below proves an essential `L^infinity` payment/funnel; it does not claim continuity on every paid subbranch.

No Gaussian, moment, iid, compact-support, connected-support, log-concavity, conditional projection-density cap, post-rotation independence, arbitrary-joint coarea, fiber-supremum, one-good-minor inference, law-uniform pointwise quadratic oscillatory decay, or deletion of a nonzero coefficient tail is used. All coordinate pivots, stars, pairs and Schur complements are in literal ORIGINAL coordinates.

## 1. Fresh source-pinned inputs

Fresh owner control from `yspennstate/math-research-brain/main` remains OWNER CONTROL revision `2026-09-22.15`, QFORM-only, with the unrestricted theorem explicitly OPEN.

The newest completed designated partner is account02/B20 r51:

`yspennstate/math-open-problems@212611f51310745be444342dc5b1da66065f31c3`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260924T093443Z-account02-B20-QFORM-auto11-r51/REPORT.md`.

Its theorem `QFORM-R51-STRONGPAIR-DIRECT-TERMINATION-v1` states that, under the full target `s_3(A)>=1`, any literal original-coordinate invertible **indefinite** principal pair `B` satisfying

`|det B| >= D_0`, `s_min(B) >= kappa_0`,                         (1.1)

where

`D_0 = 9.530157744638501e-7`,                                    (1.2)

`kappa_0 = 6.075614261408114e-5`,                                (1.3)

pays the full ambient law with

`||p_Q||_infinity < 9763`.                                       (1.4)

This partner result is consumed below at two explicit inequalities.

The scalar-Schur inputs are account01/B19 r55:

`yspennstate/math-open-problems@9de5ec75262ec906bf195c067ea323443b73a159`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260924T082048Z-account01-B19-QFORM-auto11-r55/REPORT.md`.

Two exact statements from that source are used:

1. `QFORM-SCALAR-SCHUR-SINGULAR-INHERITANCE-v1`: for a nonzero physical scalar pivot `a=A_ii` and exact Schur complement `S`,

`    s_(k+1)(A) <= s_k(S)`,                                      (1.5)

so `s_3(A)>=1` implies

`    s_2(S)>=1`.                                                  (1.6)

2. `QFORM-SCALARPIVOT-AGGREGATE-TETRAD-LINFINITY-v1`: with ordered disjoint tetrad energy

`W_2(S)=sum_{I,J: |I|=|J|=2, I cap J=empty} det S[I,J]^2`,       (1.7)

one has, whenever `W_2(S)>0`,

`||p_Q||_infinity <= 8 sqrt(2) e^(1/4) |a|^(-1/2) W_2(S)^(-1/8)`. (1.8)

The immediately preceding account01/B20 frontier is

`yspennstate/math-open-problems@53dfdb0cadf8b6d79f8a85ce0969981e02d93a63`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260924T093049Z-account01-B20-QFORM-auto11h/REPORT.md`.

It left the r50/r52 retained-tail state with both mixed incident currencies below `2^-20`; the present theorem is orthogonal to that compiler and narrows the same still-unpaid global chamber by exploiting the new r51 pair-free information.

## 2. Main theorem

### Theorem 2.1 — `QFORM-R51-MODERATE-DIAGONAL-OR-PHYSICALSTAR-PAYMENT-v1`

Let `A=A^T` satisfy the exact QFORM target hypothesis

`    s_3(A)>=1`.                                                   (2.1)

Put

`    m=max_i |A_ii|`.                                             (2.2)

If

`    m >= 2^-6 = 1/64                                            (2.3)`

and every literal physical off-diagonal row star obeys

`    ||A[i,[n]\{i}]||_2 <= 1007/4096                             (2.4)`

for all `i`, then the full ambient law has an essentially bounded density with

`    boxed: ||p_Q||_infinity < 9763.                              (2.5)`

Equivalently, every target-valid state not already paid with constant `<9763` satisfies the structural dichotomy

`    boxed: max_i |A_ii| < 1/64`

or

`    boxed: max_i ||A[i,[n]\{i}]||_2 > 1007/4096
             =0.245849609375.                                    (2.6)`

No continuity conclusion is asserted by Theorem 2.1.

The proof has four exact steps.

## 3. Step one: a maximal moderate diagonal forbids a relatively larger edge

Choose a physical index `i` with

`    |a|:=|A_ii|=m>=1/64.                                        (3.1)`

Fix `j!=i`, and write the literal principal pair

`    B=[[a,b],[b,d]],  b=A_ij, d=A_jj`.                           (3.2)

By maximality of `m`, `|d|<=m`.

Suppose first that

`    |b| >= (65/64)m.                                             (3.3)`

Multiplying `B` by `sign(a)` does not change its singular values or determinant magnitude, so assume `a=m>0`. Then `|d|<=m<|b|`, hence `B` is indefinite and

`|det B|=b^2-ad >= b^2-m^2
          >=[(65/64)^2-1]m^2
          >=129/2^24
          =7.68899917602539e-6
          >D_0`.                                                  (3.4)

For an indefinite symmetric `2x2` matrix,

`s_min(B)
 = [sqrt((a-d)^2+4b^2)-|a+d|]/2
 >= |b|-m
 >= m/64
 >=1/4096
 =6.103515625e-5
 >kappa_0`.                                                       (3.5)

Thus the **completed account02/B20 r51 theorem applies at the actual inequalities (3.4)-(3.5)** and pays the full law by `<9763`.

Consequently, in every state still unpaid after this step,

`    boxed: |A_ij| < (65/64)m for every j!=i.                     (3.6)`

This is the first concrete use of the designated partner result.

## 4. Step two: every diagonal of the exact scalar Schur complement is microscopic

Let `T=[n]\{i}` and write

`A=[[a,c^T],[c,D]]`,                                              (4.1)

with exact scalar Schur complement

`    S=D-c c^T/a.                                                 (4.2)`

For a fixed `j in T`, put

`    s_j=S_jj=A_jj-A_ij^2/a.                                     (4.3)`

The same physical pair `B` from (3.2) has the exact congruence

`B=L^T diag(a,s_j)L`,

`L=[[1,b/a],[0,1]].                                               (4.4)`

By (3.6), `|b/a|<65/64`. Since

`L^(-1)=I+[[0,-b/a],[0,0]]`,

`||L^(-1)||_op <=1+|b/a|<129/64`, hence

`s_min(L)>64/129`.                                                (4.5)

Therefore

`s_min(B)
 >=s_min(L)^2 min(|a|,|s_j|)
 >(64/129)^2 min(m,|s_j|).                                       (4.6)

Assume

`    |s_j| >=2^-11=1/2048.                                       (4.7)`

Then

`|det B|=|a s_j| >=2^-17
        =7.62939453125e-6
        >D_0`,                                                    (4.8)

and, since `m>=2^-6`,

`s_min(B)
 >(64/129)^2 2^-11
 =1.2018508503094766e-4
 >kappa_0`.                                                       (4.9)

If `a s_j<0`, the pair is indefinite. The completed account02/B20 r51 theorem therefore applies **again at the actual inequalities (4.8)-(4.9)** and pays the full law by `<9763`.

If `a s_j>0`, the pair is definite. Condition on all other original variables. The remaining two-variable quadratic polynomial has quadratic part `B`; after translation it is `y^T B y+constant`. The joint conditional input density is bounded by one. For a positive-definite `B`,

`Leb{x:y^T Bx in [u,u+epsilon]} <= pi epsilon/sqrt(det B)`,        (4.10)

because the sublevel ellipses have area `pi t/sqrt(det B)`; the negative-definite case is identical after multiplying by `-1`. Hence the full conditional and therefore unconditional density obeys

`||p_Q||_infinity
 <=pi/sqrt(|det B|)
 <=pi 2^(17/2)
 =1137.378032...<1138`.                                          (4.11)

Thus every still-unpaid state after Steps 1-2 satisfies the exact physical Schur-diagonal gate

`    boxed: ||diag(S)||_op < 2^-11.                               (4.12)`

No sign assumption was introduced: opposite-sign Schur diagonals are paid by account02/B20, and same-sign Schur diagonals are paid by the elementary definite-pair area bound.

## 5. Step three: a zero-diagonal matrix with two large singular modes has either universal tetrad energy or a large row star

The scalar-Schur inheritance theorem (1.5)-(1.6) gives

`    s_2(S)>=1.                                                   (5.1)`

Set

`Delta=diag(S)`, `O=S-Delta`,                                    (5.2)

so `O=O^T` and `O_jj=0`. By (4.12) and Weyl,

`    s_2(O)>sigma:=1-2^-11=2047/2048.                            (5.3)`

We now prove a deterministic lemma which is useful beyond this run.

### Lemma 5.1 — `QFORM-ZERODIAG-S2-TETRAD-OR-STAR-v1`

Let `O=O^T` have zero diagonal and `s_2(O)>sigma>0`. If

`    rho:=max_i ||Oe_i||_2 <=sigma/2,                             (5.4)`

then its ordered disjoint tetrad energy satisfies

`    boxed: W_2(O) >= sigma^4/2.                                 (5.5)`

#### Proof

Write

`w_ij=O_ij^2`, `R_i=sum_{j!=i} w_ij=||Oe_i||_2^2`,

`T=sum_i R_i=||O||_F^2`.                                         (5.6)

Let `x_1>=x_2>=...` be the squared singular values of `O`. Then `x_2>sigma^2`, `T=sum_r x_r`, and Cauchy-Binet gives

`e_2(OO^T)=sum_{I,J:|I|=|J|=2} det O[I,J]^2`.                   (5.7)

The terms with non-disjoint row and column pairs can be counted exactly. If `P=sum_{i<j}w_ij^2`, the `I=J` terms sum to `P`; the terms with `|I cap J|=1` sum to

`sum_i R_i^2-2P`.                                                 (5.8)

Hence their total is

`sum_i R_i^2-P <=sum_i R_i^2 <=rho^2 T`.                         (5.9)

The remaining terms are exactly the ordered disjoint tetrad energy `W_2(O)`. Therefore

`W_2(O)>=e_2(OO^T)-rho^2 T`.                                    (5.10)

Moreover

`e_2(OO^T)>=x_1(T-x_1)`.                                        (5.11)

Both `x_1` and `T-x_1` are at least `sigma^2`, so the concavity of `x(T-x)` on `[sigma^2,T-sigma^2]` gives

`x_1(T-x_1)>=sigma^2(T-sigma^2)`.                               (5.12)

Combining (5.10)-(5.12), using `rho<=sigma/2` and `T>=2sigma^2`,

`W_2(O)
 >=(sigma^2-rho^2)T-sigma^4
 >=(3sigma^2/4)(2sigma^2)-sigma^4
 =sigma^4/2`.                                                     (5.13)

QED.

For disjoint `I,J`, a physical diagonal never appears, so

`    W_2(S)=W_2(O).                                               (5.14)`

If (5.4) holds, Lemma 5.1 and the aggregate scalar-pivot receiver (1.8) give

`||p_Q||_infinity
 <=8 sqrt(2)e^(1/4) m^(-1/2)(sigma^4/2)^(-1/8)
 <=126.766179<127.                                                (5.15)

Thus every still-unpaid state after Step 3 must contain a literal Schur row satisfying

`    boxed: ||Oe_j||_2 > sigma/2
           =2047/4096
           =0.499755859375.                                      (5.16)`

This step uses all disjoint tetrads in aggregate; no individual minor is selected or inverted.

## 6. Step four: a large Schur star forces a universal-size PHYSICAL star

Return to the pivot row `c=A[i,T]`.

If

`    ||c||_2 >=1/4,                                               (6.1)`

then the literal physical row star centered at `i` is already at least `1/4>1007/4096`.

Otherwise `||c||_2<1/4`. Take `j` from (5.16). For `k in T\{j}` the exact Schur identity gives

`    O_jk=S_jk=A_jk-(A_ij/a)A_ik.                                (6.2)`

By the no-strong-edge consequence (3.6),

`    |A_ij/a|<65/64.                                             (6.3)`

Hence

`||A[j,T\{j}]||_2
 >=||O[j,T\{j}]||_2-(|A_ij|/|a|)||c_{T\{j}}||_2
 >sigma/2-(65/64)(1/4)
 =2047/4096-1040/4096
 =boxed: 1007/4096.                                               (6.4)`

Thus a literal original-coordinate physical row star exceeds the threshold in (2.6). This contradicts (2.4), and completes the proof of Theorem 2.1.

## 7. Consequence for the live r50/r51 proof frontier

The preceding account01/B20 run reduced the moderate-residual r50/r52 state to the retained rank-12/rank-11 tail endpoint together with

`    Gamma_R<2^-20,  Gamma_C<2^-20                               (7.1)`

for the two exact mixed 2+1 incident currencies.

The newest designated account02/B20 r51 run then added the global pair-free constraint for every still-unpaid literal indefinite pair.

Theorem 2.1 now removes an entire additional degree of freedom from that same chamber:

> **Any still-unpaid target state in the r50/r51 chamber must either have every physical diagonal smaller than `1/64`, or contain a literal physical row star of norm `>1007/4096`.**

In particular, there is no longer a separate “moderate diagonal + diffuse/no-star” endpoint.

The sharpened first remaining implication is therefore

`QFORM-R51-TINYDIAG-OR-STAR02458-WITH-TWOSIDED-INCIDENT-COLLAPSE-ENDPOINT-v1`:

- either pay the literal physical star `||A[i,-i]||_2>1007/4096` jointly with the retained third spectral resource, without a worst-fiber shortcut; or
- in the all-tiny-diagonal chamber `max_i|A_ii|<1/64`, combine the r50/r52 rank-12/rank-11 retained-tail structure and both incident-volume collapse inequalities (7.1) with an existing physical-E3, grouped-star, hub+square, ridge/window, pair-log, or fractional receiver.

This is a strict narrowing of the previous endpoint. It does not assert that a single star alone is an endpoint density receiver; the known hub-star mixed-norm counterexample forbids that shortcut, so the third source must remain coupled.

## 8. Scope, regularity and correction boundary

Theorem 2.1 is sign-free and dimension-free. Repeated eigenvalues and kernels are allowed. Every conditional argument conditions only literal original variables. The only coefficient-space operation is deterministic Schur algebra and singular-value accounting; no rotated random variables are declared independent.

No coefficient tail is discarded. The previous r50/r52 retained tails remain fully present. The partner r51 theorem is applied only to actual original-coordinate principal pairs satisfying its exact quantitative determinant and minimum-singular-value gates.

Regularity: Theorem 2.1 establishes essential boundedness on its paid side. The argument combines branches whose source theorems do not uniformly assert `C_0` regularity, so **no new continuity claim is made here**. Full-target continuity remains OPEN.

Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
