SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B07, 2026-09-24T01:39:15Z.
attacking: the near-rank-two common crossing plus low-diagonal/low-internal cloud — synchronize all anchor-to-bank couplings through the complete E2 determinant law, or force a genuine physical E3 crossing.

# account03/B07 r43 — two-sided determinant-heavy plane synchronization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260924T013915Z-account03-B07-qform-r43`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW TWO-SIDED E2 PLANE-SYNCHRONIZATION THEOREM + RANK-12 PHYSICAL CROSS-SKELETON COMPILER / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussian, moment, support, iid, log-concavity, diagonal-basis, or post-rotation-independence assumption is introduced. Every random-variable bank below consists of literal original coordinates. The spectral decompositions are used only on deterministic coefficient Gram matrices. No individual physical minor is divided by, and no nonzero crossing tail is deleted.

## 1. Fresh source state and exact incoming branch

Immediately before publication, fresh owner control from `yspennstate/math-research-brain` main remained programme `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.15`, with continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`, no B07 pause/reassignment, and the full theorem OPEN. The pre-publication main commit observed was `67340898014b6d913e553869c3cf306b34b9ceef`. The live correction inbox was reread; in particular the argument below uses none of the refuted universal one-minor, post-rotation-independence, arbitrary-joint coarea, conditional-cap, fiber-supremum, or pointwise quadratic-decay mechanisms.

The immediate predecessor is my r42 report

`yspennstate/math-open-problems@e91150711e87a3e9040e3b93333e55ab574d7c01`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260924T004021Z-account03-B07-qform-r42/REPORT.md`.

It leaves a low-diagonal bank `H` (after harmless relabeling of its surviving subset) coupled to two disjoint physical banks `I,J`, with common crossing

`K=A[I,J]`.

The newest completed complementary B07 result used here is account02/B07

`yspennstate/math-open-problems@81d6956476fa400f61d266effb4123a42fe3185c`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260924T003945Z-account02-B07-qform-auto11/REPORT.md`.

Put

`Z=e2(KK^T)`, `V=e3(KK^T)`.

Its low-diagonal router uses

`eta=2^(-30)`, `zeta=2^(-12)`,

and on the only branch relevant below has

`boxed: V<eta,  Z>=zeta.`                                           (1.1)

It also proves the tail identity/inequality

`tau_2(K) Z <=3V`,                                                  (1.2)

where `tau_2(K)=sum_{j>=3}s_j(K)^2` is the squared Frobenius distance to the best rank-two approximation. Hence

`dist_F(K,rank<=2)^2 <=3V/Z`.                                      (1.3)

The completed marginal-free physical-third-volume receiver used below is account02/B03: any literal original-coordinate cross block `B` with `e3(BB^T)>0` gives the full ambient form a continuous `C_0` density with

`||p_Q||_infinity <= C3 e3(BB^T)^(-1/6)`,

`C3=3*2^(4/3)*e^(1/3)=10.5501688311648...`.                         (1.4)

Arbitrary same-bank curvature, outside couplings, affine terms and additional spectrum are retained in that theorem.

## 2. The complete E2 determinant law defines a canonical heavy plane

Let

`B=KK^T`, `S=tr(B)`, `Z=e2(B)>0`.

Write the eigenvalues of `B` as `x_j>=0` with orthonormal eigenvectors `u_j`. Define the natural E2 spectral inclusion marginal

`alpha_j = x_j(S-x_j)/Z`.                                          (2.1)

Equivalently, under the probability law on unordered singular-direction pairs

`P{a,b}=x_a x_b/Z`,

`alpha_j` is the probability that direction `j` is included. Therefore

`boxed: sum_j alpha_j=2.`                                         (2.2)

Let `P` be the spectral projection onto the directions satisfying

`alpha_j>2/3`.                                                      (2.3)

Then immediately

`boxed: rank P<=2.`                                                (2.4)

This is an aggregate determinant-weight selection. No physical coordinate minor has been chosen.

Define the second Newton transform

`H_2(B)=B^2-SB+ZI`.                                                 (2.5)

On `u_j`, its eigenvalue is

`x_j^2-Sx_j+Z
 = Z-x_j(S-x_j)
 = Z(1-alpha_j)`.                                                   (2.6)

Thus `H_2(B)>=0`, and by (2.3)

`boxed: H_2(B) >= (Z/3)(I-P).`                                    (2.7)

The same construction for `K^T K` gives a right-side projection `Q` with

`rank Q<=2`                                                        (2.8)

and the corresponding right Newton-transform lower bound.

Repeated singular values cause no ambiguity: `alpha_j` is a scalar function of the eigenvalue `x_j`, so the strict-threshold spectral projection is well-defined by functional calculus.

## 3. One-sided extension identity and synchronization

Let `U` be any additional collection of physical columns on the same row bank as `K`, and form

`T=[K U]`.

Cauchy--Binet partitions `e3(TT^T)` according to how many selected columns come from `U`. The terms with zero `U` columns give `e3(B)`. The terms with exactly one specified column `u` give the rank-one update

`e3(B+uu^T)-e3(B)=u^T H_2(B)u`.                                   (3.1)

All terms using two or three columns of `U` are nonnegative. Summing (3.1) over the columns of `U` therefore yields

`boxed:
e3(TT^T)-V >= tr(U^T H_2(B)U)
              >= (Z/3)||(I-P)U||_F^2.
}`                                                                  (3.2)

Consequently, if

`e3(TT^T)<eta`,                                                     (3.3)

then

`boxed:
||(I-P)U||_F^2
 < 3(eta-V)/Z.
}`                                                                  (3.4)

This is the synchronization step: **all physical columns in `U` are controlled simultaneously by the same determinant-heavy plane `P`**. There is no dimension factor and no per-column plane choice.

Apply the same argument to `K^T` and an added-column matrix `V_H^T`. If

`e3(K^TK+V_H^TV_H)<eta`,                                          (3.5)

then

`boxed:
||V_H(I-Q)||_F^2
 <3(eta-V)/Z.
}`                                                                  (3.6)

## 4. Actual physical routing of the r42/r02 rank-two survivor

Return to the disjoint original-coordinate banks `H,I,J`. Put

`U=A[I,H]`, `V_H=A[H,J]`.                                         (4.1)

The two literal enlarged physical crossings are

`T_R=A[I,J union H]=[K U]`,                                       (4.2)

and

`T_L=A[I union H,J]=[K;V_H]`.                                    (4.3)

The row and column banks in each crossing are disjoint original-coordinate sets.

### Theorem 4.1 — `QFORM-E2-TWO-SIDED-PLANE-SYNCHRONIZATION-v1`

Under (1.1), at least one of the following holds.

**A. Paid physical third volume.**

`e3(T_RT_R^T)>=eta` or `e3(T_LT_L^T)>=eta`.                        (4.4)

Then (1.4) gives the full ambient quadratic form a continuous density with

`boxed:
||p_Q||_infinity <= C3 eta^(-1/6)
                  =32 C3
                  =337.6054025972728... .
}`                                                                  (4.5)

**B. Two-sided synchronized determinant-heavy planes.**

There are fixed coefficient-space projections `P` on `R^I` and `Q` on `R^J`, each of rank at most two and determined only by the complete E2 determinant law of `K`, such that

`boxed:
||(I-P)A[I,H]||_F^2 <3(eta-V)/Z,
||A[H,J](I-Q)||_F^2 <3(eta-V)/Z.
}`                                                                  (4.6)

At the live thresholds,

`boxed:
||(I-P)A[I,H]||_F,
||A[H,J](I-Q)||_F
 < sqrt(3 eta/zeta)
 =sqrt(3)/512
 =0.003382911733533... .
}`                                                                  (4.7)

No anchor is assigned its own moving plane: both entire anchor interfaces are synchronized to the two fixed planes supplied by `K`.

Proof. If either enlarged crossing satisfies (4.4), use (1.4). Otherwise (3.4) applies to `U`, and (3.6) applies to `V_H`. This gives (4.6), and (1.1) gives (4.7). QED.

## 5. Rank-12 global physical cross-skeleton compiler

The synchronized statement can be packaged into a single low-rank deterministic coefficient skeleton while retaining every nonzero tail.

Let `K_2` be the best rank-two approximation to `K`; by (1.3),

`||K-K_2||_F^2 <=3V/Z`.                                           (5.1)

Set

`U_0=P U`, `V_0=V_H Q`.                                           (5.2)

On the physical direct sum `H direct_sum I direct_sum J`, define

`R_cross = [[0, U_0^T, V_0],
            [U_0, 0, K_2],
            [V_0^T, K_2^T, 0]].`                                  (5.3)

Each of the three symmetric off-diagonal pair-block matrices has rank at most four, because its rectangular block has rank at most two. Therefore

`boxed: rank R_cross <=12.`                                       (5.4)

Let the exact cross-bank residual be

`E_cross = [[0, (U-U_0)^T, V_H-V_0],
            [U-U_0, 0, K-K_2],
            [(V_H-V_0)^T, (K-K_2)^T, 0]].`                        (5.5)

Then no coefficient is deleted, and by (4.6) plus (5.1),

`||E_cross||_F^2
 =2[||U-U_0||_F^2+||V_H-V_0||_F^2+||K-K_2||_F^2]
 <2[6(eta-V)/Z+3V/Z]
 =(12eta-6V)/Z
 <=12eta/Z.`                                                       (5.6)

Hence the low-third-volume branch satisfies the dimension-free physical decomposition

`boxed:
A[H union I union J,H union I union J]
 =diag(A[H,H],A[I,I],A[J,J]) + R_cross + E_cross,
rank R_cross<=12,
||E_cross||_F < sqrt(12eta/zeta)
              =sqrt(12)/512
              =0.006765823467066... .
}`                                                                  (5.7)

The three same-bank quadratic blocks are retained **exactly**, as are all outside coordinates/couplings in the full problem. Equation (5.7) is not a perturbative density argument; it is deterministic structural currency for the next receiver.

This improves the previous statement “the common crossing is near rank two.” Failure of the E3 exit now forces **all three inter-bank interfaces `H-I`, `H-J`, and `I-J` into one bounded-rank cross-skeleton**, with one absolute Frobenius error budget independent of `|H|,|I|,|J|`.

## 6. Actual application of the designated account04/B07 result

The designated completed partner is

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md`.

Its theorem says: on an actual physical `r+3` coordinate block, if

`A_C=D+R+E`, `|D_ii|>=d`, `rank R<=r`, `|E|_max<=epsilon`,

then

`s3(A_C)>=d-(r+3)epsilon`,                                        (6.1)

and, when positive,

`||p_Q||_infinity <=2sqrt(6pi(r+3))/[d-(r+3)epsilon]`.            (6.2)

I apply it to the actual high-diagonal complement from the predecessor routing, because that paid complement is what permits the present run to focus only on the low-diagonal survivor. If three physical anchors satisfy

`|A_hh|>=1/64`

and all three mutual off-diagonals satisfy

`|A_hk|<=1/768`,                                                   (6.3)

then on that actual triple take `r=0`, `D=diag(A_hh)`, `R=0`, and `E=A_C-D`. Thus

`boxed:
s3(A_C)>=1/64-3/768=3/256.
}`                                                                  (6.4)

The partner theorem therefore gives the full ambient essential-density bound

`boxed:
||p_Q||_infinity
 <=2sqrt(18pi)/(3/256)
 =1283.393676611072... .
}`                                                                  (6.5)

Continuity is not claimed by this partner gate. If (6.3) fails throughout the high-diagonal set, r42's determinant-weighted internal-cut theorem closes the resulting dense-edge graph by a physical E3 crossing. Thus the current synchronized-plane analysis genuinely starts only after an actual application of the designated partner result has removed the finite-core complement.

## 7. Regression checks

A deterministic checker in this run directory verifies:

1. `sum alpha_j=2` and at most two `alpha_j>2/3` on random Gram matrices;
2. the eigenvalue identity `H_2(B)u_j=Z(1-alpha_j)u_j`;
3. the Loewner inequality `H_2(B)>=(Z/3)(I-P)`;
4. the extension inequality `e3(B+UU^T)-e3(B)>=tr(U^T H_2(B)U)`;
5. engineered low-third-volume synchronization examples;
6. all displayed constants in (4.5), (4.7), (5.7), and the partner bound (6.5).

The finite checks are regression evidence only; the proof is the Cauchy--Binet/Newton-transform argument above.

## 8. Exact remaining implication

This run closes neither the full QFORM theorem nor the complete r42 low-diagonal chamber. It sharpens the first remaining branch to

`QFORM-R12-CROSS-SKELETON-PLUS-LOWCURVATURE-BANK-RECEIVER-v1`:

> Pay the full product-law quadratic form when the three physical inter-bank interfaces admit the exact decomposition (5.7), while retaining the arbitrary same-bank blocks and outside couplings. In the r42 residual subset, a positive fraction of the projected-E2 anchor mass additionally has `|A_hh|<1/64`, `||A[h,J]||_2<1/64`, and `||A[h,H\{h}]||_2<1/64`. The receiver may use the finite-rank cross carrier, but it may not discard `E_cross`, rotate the independent random coordinates, or replace the arbitrary same-bank quadratic blocks by constants.

The account02/B07 alternative `E2(K)<2^-12`, which yields the separate diffuse low-diagonal cloud, remains a distinct unpaid branch. The r40 skew-mismatch, overlap-two, and principal-triple residual packets also remain distinct unless paid by other workers.

**Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.** Continuity is proved in this run only on the physical-E3 exit (4.4); the designated partner core exit proves essential boundedness only.
