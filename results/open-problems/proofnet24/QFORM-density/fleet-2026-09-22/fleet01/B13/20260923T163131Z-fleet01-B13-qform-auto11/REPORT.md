SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-23T16:31:31Z.
attacking: the newest physical third-volume bi-hub obstruction by exact anchored-minor identities, while making the arbitrary-law-to-product-indicator transfer quantitative and optimizer-free.

# fleet01/B13 — exact anchored third-volume currency in the partner bi-hub branch

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: extremal product laws / geometric sublevel reduction  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**  
Full continuity: **OPEN**.

## 1. Fresh scope and source-pinned inputs

The target is unchanged: for independent ORIGINAL real coordinates with arbitrary probability densities `0<=f_i<=1`, and real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal finite essential density bound for `Q=X^T A X`, or give a genuine counterexample. No moment, centering, iid, log-concavity, compact-support, connected-support, or post-rotation independence hypothesis is permitted.


The newest completed designated-partner result actually used below is fleet02/B13 r30:

`yspennstate/math-open-problems@f6ad7b994c1ba509af30fceaf45e8b464db86af8`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T155736Z-fleet02-B13-rank4star-r30/REPORT.md`.

For a genuine ORIGINAL-coordinate physical cross block `B` in a slab witness of ratio

`rho = P(Q in J)/|J|`,

that report proves the following matrix alternative. With

`C3 = 9 sqrt(3e)`,

one has either

`(I) s3(B) <= C3/rho`,

or the natural squared-third-minor law of `B` has a physical row `i` and physical column `j` whose marginals satisfy

`alpha_i>2/3`, `beta_j>2/3`.

In the latter branch the joint event that a sampled third minor contains both `i` and `j` has probability greater than `1/3`. The partner also proves its rank-at-most-two low-spectral-misalignment conclusion in branch (I); I do not reprove it here.

The no-attainment product-purification source used below is fleet04/B13:

`yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260922T231352Z-fleet04-B13-rough-geometric-transfer-r5/REPORT.md`.

It proves `L1` approximation of every cap-one marginal by finite convex mixtures of indicators of bounded finite unions of intervals of measure one, via the finite-dimensional hypersimplex. I use that theorem only in its proved no-attainment form.

## 2. Quantitative optimizer-free purification of a slab witness

The following explicit ratio bookkeeping is useful because later structural theorems often begin from a strict observed slab ratio.

### Lemma 2.1 — `QFORM-STRICT-WITNESS-PURIFICATION-v1`

Let `J` be an interval of length `ell>0`, let `A` be fixed, and suppose a cap-one product law with marginals `f_1,...,f_n` has

`P_f(X^T A X in J)=rho ell`.

For every `eta>0` there are bounded finite unions of intervals `E_1,...,E_n`, each of Lebesgue measure one, such that

`|{x in prod_i E_i : x^T A x in J}| >= (rho-eta) ell`.

No optimizer, centered interval, bounded diameter, or uniform fragment count is asserted.

#### Proof

For each `i`, apply the source-pinned hypersimplex approximation with accuracy

`||f_i-g_i||_1 < eta ell/n`,

where

`g_i = sum_nu theta_(i,nu) 1_(E_(i,nu))`,

`theta_(i,nu)>=0`, `sum_nu theta_(i,nu)=1`, and every `E_(i,nu)` is a bounded finite union of intervals of measure one.

The product densities obey the elementary telescoping inequality

`|| prod_i f_i - prod_i g_i ||_1 <= sum_i ||f_i-g_i||_1 < eta ell`,

because every marginal has `L1` norm one. Therefore for the bounded slab kernel

`K(x)=1_{x^T A x in J}`

we have

`int K prod_i g_i >= rho ell-eta ell`.

Expanding the finite product mixture writes the left side as a convex average of the slab volumes of unit product indicators. One component is at least the average, proving the claim. QED.

A useful logical consequence is that any **strict** matrix-only implication of the form

`slab ratio > R  ==>  C(A)`

proved for bounded finite-union unit product indicators automatically holds for arbitrary cap-one product laws: if `rho>R`, choose `eta<rho-R` and purify the same matrix and same slab. This avoids every infinite-line attainment issue.

## 3. Anchored third-volume notation

Let `B` be an `m x n` real matrix of rank at least three. Put

`Z = e3(B^T B)
   = sum_{|S|=|T|=3} det B[S,T]^2`.

Normalize the squared minors to the probability law

`w(S,T)=det B[S,T]^2/Z`.

Fix a physical row `i` and physical column `j`, and define their joint anchored third-volume

`Z_ij
 = sum_{R subset [m]\{i}, |R|=2}
     sum_{T subset [n]\{j}, |T|=2}
       det B[{i} union R,{j} union T]^2`.

Thus

`Z_ij/Z = P_w(i in S and j in T)`.

After harmless permutations of the physical rows and columns, write the coefficient matrix as

`B = [[b, r^T],
      [c, D]]`,

where `b=B_ij`, `r` is row `i` with column `j` removed, `c` is column `j` with row `i` removed, and `D` is the doubly deleted block. The next identities concern only deterministic coefficient geometry. No random coordinate is rotated.

## 4. Main exact identities

### Theorem 4.1 — `QFORM-ANCHORED-E3-SCALAR-OR-STARSTAR-v1`

With the notation above:

**(a) Nonzero anchor.** If `b!=0` and

`S = D - c r^T/b`,

then

`boxed: Z_ij = b^2 e2(S^T S).`

Here `S` is the scalar Schur residual of the **cross matrix** `B`; this statement does not call `S` a principal Schur complement of the full symmetric matrix `A`.

**(b) Zero anchor.** If `b=0`, let `P_r` denote orthogonal projection onto `r^perp` in the residual column space and `P_c` orthogonal projection onto `c^perp` in the residual row space. Then

`boxed:
 Z_ij = ||r||_2^2 ||c||_2^2 ||P_c D P_r||_F^2.
`

The identity includes the degenerate convention that the right side is zero if `r=0` or `c=0`.

#### Proof of (a)

For every residual two-row set `R` and residual two-column set `T`, block determinant elimination gives

`det [[b,r_T^T],[c_R,D_(R,T)]]
 = b det(D_(R,T)-c_R r_T^T/b)
 = b det S[R,T].`

Squaring and summing over all `R,T` gives

`Z_ij=b^2 sum_(R,T) det S[R,T]^2
      =b^2 e2(S^T S)`

by Cauchy-Binet. QED.

#### Proof of (b)

The anchored squared-minor sum is the squared Hilbert-Schmidt norm of the block of `wedge^3 B` from `e_j wedge wedge^2(j^perp)` to `e_i wedge wedge^2(i^perp)`. Hence independent orthogonal changes of basis in the residual row and residual column spaces preserve `Z_ij`.

If `r,c` are nonzero, rotate those residual spaces so that

`r=||r|| e_1`, `c=||c|| f_1`.

For an anchored `3 x 3` determinant to be nonzero, the chosen residual column pair must contain `e_1` and the chosen residual row pair must contain `f_1`. For residual indices `a,b>1`, the corresponding determinant is, up to sign,

`||r|| ||c|| D_(a,b)`.

Therefore

`Z_ij
 = ||r||^2 ||c||^2 sum_(a>1,b>1) D_(a,b)^2
 = ||r||^2 ||c||^2 ||P_c D P_r||_F^2`.

If `r=0` or `c=0`, every anchored determinant is zero and the same formula holds. QED.

This second identity is the exact zero-anchor analogue of a rank-one-update exterior identity: third-volume cannot disappear at a zero hub intersection; it becomes the product of two physical star energies and a genuinely transverse Frobenius packet.

## 5. Apply the designated partner r30 theorem at an actual inequality

Assume now that `B` is the physical cross block in the partner theorem and that its small-third-singular-value alternative fails:

`s3(B)>C3/rho`, `C3=9 sqrt(3e)`.

The partner gives physical `i,j` with

`alpha_i>2/3`, `beta_j>2/3`.

By inclusion-exclusion under the same squared-minor law,

`Z_ij/Z >= alpha_i+beta_j-1 >1/3`.

Also

`Z=e3(B^T B)
 >=s1(B)^2 s2(B)^2 s3(B)^2
 >=s3(B)^6
 >C3^6/rho^6`.

Consequently

`sqrt(Z_ij)>C3^3/(sqrt(3) rho^3)
              =2187 e^(3/2)/rho^3.`

Inserting Theorem 4.1 gives the two exact target-level currencies:

### Corollary 5.1 — nonzero heavy-heavy entry

If `b=B_ij!=0`, then

`boxed:
 |b| sqrt(e2(S^T S))
 > 2187 e^(3/2)/rho^3.
`

### Corollary 5.2 — zero heavy-heavy entry

If `b=B_ij=0`, then

`boxed:
 ||r||_2 ||c||_2 ||P_c D P_r||_F
 > 2187 e^(3/2)/rho^3.
`

Both inequalities are statements about ORIGINAL-coordinate coefficient banks. No distribution of a rotated projection is used.

## 6. A self-normalized pivot-or-aggregate dichotomy

Set

`kappa0 = (2187 e^(3/2))^(1/3)
        = 3^(7/3) sqrt(e)
        = 21.400807898...`.

Then Corollary 5.1 has a particularly clean interpretation. If `b!=0`, at least one of

`|b| >= kappa0/rho`

or

`e2(S^T S)^(1/4) > kappa0/rho`

holds.

The first alternative is an actual physical scalar/pair pivot in the original symmetric matrix. Indeed, for the physical principal pair

`H=[[A_ii,b],[b,A_jj]]`,

if

`max(|A_ii|,|A_jj|)>=|b|/2`,

there is a genuine scalar pivot of magnitude at least `kappa0/(2rho)`. Otherwise

`H = [[0,b],[b,0]] + diag(A_ii,A_jj)`

has

`sigma_min(H) >= |b|-max(|A_ii|,|A_jj|) > |b|/2`

and

`det H=A_ii A_jj-b^2< -3b^2/4<0`.

So it is a genuine invertible indefinite physical pair with

`boxed: sigma_min(H)>kappa0/(2rho)=10.700403949.../rho.`

Thus the partner's third-volume bi-hub branch with a nonzero hub intersection has become

`physical scalar/pair pivot at scale 10.70/rho`

**or**

`cross-Schur E2 scale e2(S^T S)^(1/4)>21.40/rho`.

No inversion is performed before this aggregate E2 packet is identified.

In the zero-anchor branch, Corollary 5.2 reads

`||r|| ||c|| ||P_c D P_r||_F > (kappa0/rho)^3`.

Therefore at least one of the three aggregate physical quantities satisfies

`boxed:
 max(||r||,||c||,||P_c D P_r||_F)>kappa0/rho.
`

This is not yet a density estimate: a large Frobenius/star bank can still be spread over arbitrarily many coordinates. It is, however, a dimension-free exact resource that survives the forbidden zero hub intersection.

## 7. Finite heavy-hub geometry

There is one further deterministic compression. Since a third-minor has exactly three rows and three columns,

`sum_i alpha_i=3`, `sum_j beta_j=3`.

Hence the sets

`H_R={i:alpha_i>2/3}`, `H_C={j:beta_j>2/3}`

have cardinalities at most four each. Moreover, for **every** pair `i in H_R`, `j in H_C`,

`Z_ij/Z>1/3`.

Thus the partner bi-hub branch admits the following exhaustive refinement:

1. some entry of the at-most-`4 x 4` physical block `B[H_R,H_C]` is nonzero, in which case the pivot-or-cross-Schur-E2 dichotomy of Section 6 applies to that heavy-heavy pair; or
2. `B[H_R,H_C]=0`, in which case every heavy-heavy pair obeys the zero-anchor star-star-transverse identity and lower bound of Corollary 5.2.

The second state is a finite zero rectangle carrying large routed third-volume around every heavy-heavy intersection. This is substantially more rigid than an unnamed `third-volume bi-hub` but is not yet paid by a universal density theorem.

## 8. Diagnostic check

`check_anchored_volume.py` tests both exact identities on 100 random `5 x 6` matrices. The saved output is

`max_relative_error_nonzero = 3.967600580207126e-15`,

`max_relative_error_zero    = 1.2628544173526711e-15`.

The check is diagnostic only. The proofs are the determinant calculation and orthogonal-invariance calculation above.

## 9. What changed and what remains unpaid

The newest designated-partner r30 result had left a physical third-volume bi-hub as one of its two principal survivors. This run resolves the algebra inside that survivor exactly:

`QFORM-BIHUB-ANCHOR-EXACT-CURRENCY-v1`:

- nonzero heavy-heavy intersection -> genuine physical pivot **or** a quantified cross-Schur E2 packet;
- zero heavy-heavy intersection -> a quantified product of two star energies and a transverse Frobenius packet;
- the complete heavy row/column sets contain at most four physical coordinates on each side.

The finite-mixture argument also gives a quantitative strict-witness transfer to bounded finite-union unit product indicators with arbitrary small **ratio** loss, not merely a vague equality of suprema. This is exactly the no-attainment interface required by the current B13 assignment.

The first unpaid implication after this run is

`QFORM-BIHUB-E2-OR-ZERORECT-RECEIVER-v1`:

> Feed the nonzero-anchor cross-Schur `E2` packet, or the zero-rectangle star-star-transverse packet, into a dependence-safe Fourier/fractional-volume receiver while retaining all same-side quadratic curvature and all outside coefficients. In the nonzero case, when the actual symmetric physical pair is used as a pivot, track the anchored E2 packet through that genuine principal Schur complement rather than identifying the cross-block Schur residual with it by assertion. In the zero-rectangle case, aggregate the star banks before any reciprocal payment.

The very recent fleet01/B02 star-leg E2 Fourier receiver is a plausible receiver for part of this currency, but its hypotheses concern a specific invertible `2 x 2` anchor and `E2` of a star leg. No identification with the present cross-Schur `E2` packet has been proved here, so I do not claim that closure.

Full QFORM remains OPEN. No scheduler/task mutation, email/push, cross-account authentication, paid call, public release, remote workflow, permission expansion, or FEI/unrelated research was performed.
