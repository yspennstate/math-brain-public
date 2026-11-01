SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-23T15:46:28Z.
attacking: the fresh aligned STAR4 third-resource carrier; force every surviving self-bank contribution either into a literal transverse original-coordinate cross packet or into a strongly conditioned in-plane rank-at-most-five skeleton.

# fleet03/B20 auto11 — transverse-self compiler and in-plane rank-five carrier

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T154628Z-fleet03-B20-QFORM-auto11`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Status: **NEW TARGET-LEVEL STRUCTURAL COMPILER + TWO PAID SUBBRANCHES / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

The unrestricted conjecture remains open. All random variables stay in the original independent coordinates. No Gaussianity, moments, compact support, connected support, log-concavity, post-rotation independence, arbitrary-joint coarea, conditional-cap substitution, pointwise quadratic-phase decay, or deletion of a small random quadratic tail is used.

## 1. Fresh proof graph consumed

The immediate synthesis input is fleet03/B19 r36:

`yspennstate/math-open-problems@6dfd43d5519df1fc40ea26f7d0bbe300ad32412d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T145843Z-fleet03-B19-QFORM-r36/REPORT.md`.

In the true low-selected-volume aligned STAR4 survivor, with `tau=2^-20`, there is a literal physical partition

`{h} disjoint_union J disjoint_union K`

and top-two singular projections `P` on `J`, `Q` on `K` for the physical cross block `N=A[J,K]`. Writing

`B=A[J,J]`, `C=A[K,K]`, `a=A_hh`,

and

`S = [[a,u_2^T,v_2^T],[u_2,0,N_2],[v_2,N_2^T,0]]`,

r36 proves

`A = S + diag(0,B,C) + R`,                                           (1.1)

`rank(S)<=5`,                                                        (1.2)

and

`||R||_op < eps_* := 0.07641336241474038218...`.                    (1.3)

Here `N_2=PNQ` and the two stars have been projected into `Ran P`, `Ran Q`. The full target supplies

`s_3(A)>=1`.                                                         (1.4)

The newer fleet02/B19 r35 counterexample is also respected: a target-valid strict-N3 family can have its entire third source inside these same two cross singular planes, so no theorem below claims a source-disjoint or transverse third direction is forced.

The designated fleet04/B20 theorem actually applied below is r10:

`yspennstate/math-open-problems@c6f29397b3d45a7cf7ab67633a5451767b478912`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260923T142031Z-fleet04-B20-QFORM-r10/REPORT.md`.

Its parametric fifth-volume receiver says that for any literal original-coordinate cross block `M`, if the first four squared singular values carry at most `(63/64)||M||_F^2`, then

`e_5(M^T M) >= (1/64)^4 ||M||_F^10 / 120`,                         (1.5)

and the full ambient form has a continuous `C_0` density with

`||p_Q||_infinity <=5 sqrt(2e) e_5(M^T M)^(-1/10)`.                (1.6)

The grouped physical rank-three receiver already in the current compiler is

`||p_Q||_infinity <=3e [s_1(M)s_2(M)s_3(M)]^(-1/3)`,              (1.7)

again for the full ambient form and with a continuous `C_0` density.

## 2. New dichotomy: transverse self action or a much stronger in-plane skeleton

Define the self-bank transverse-action scales

`theta_B = ||(I-P)B||_op`, `theta_C = ||(I-Q)C||_op`.              (2.1)

Fix

`eta=1/16`.                                                         (2.2)

### Theorem 2.1 — `QFORM-ALIGNED-TRANSVERSE-OR-INPLANE-R5-v1`

In the aligned survivor (1.1)-(1.4), at least one of the following holds.

**(T) Transverse self action:**

`max(theta_B,theta_C) >=1/16`.                                     (2.3)

**(F) Strong in-plane finite-rank carrier:** if

`B_0=PBP`, `C_0=QCQ`,

and

`S_0 = S + diag(0,B_0,C_0)`,                                      (2.4)

then

`rank(S_0)<=5`                                                     (2.5)

and

`boxed: s_3(S_0) > 0.7985866375852596.`                           (2.6)

#### Proof

Suppose (T) fails. Because `B` is symmetric,

`||B(I-P)||_op = ||(I-P)B||_op = theta_B`.

The exact identity

`B-PBP = (I-P)B + PB(I-P)`                                        (2.7)

therefore gives

`||B-PBP||_op <2eta=1/8`.                                         (2.8)

Similarly

`||C-QCQ||_op <1/8`.                                              (2.9)

Since these two errors occupy disjoint physical banks,

`||diag(0,B-B_0,C-C_0)||_op <1/8`.                                (2.10)

Together with (1.1),(1.3),

`||A-S_0||_op < eps_*+1/8
               =0.20141336241474038...`.                          (2.11)

The matrix `S_0` acts on the five-dimensional space

`span{e_h}+Ran(P)+Ran(Q)`,                                        (2.12)

so (2.5) holds. Singular-value perturbation and (1.4) yield

`s_3(S_0) >= s_3(A)-||A-S_0||_op
          >1-eps_*-1/8
          =0.7985866375852596178...`,                             (2.13)

which is (2.6). QED.

This strengthens the preceding r36 split. The third spectral resource is now either visible as a fixed transverse action of an actual self bank, or it is concentrated to better than `0.202` operator error around an explicit `1+2+2` physical skeleton whose third singular value is almost `0.8`, not merely `1/4`.

The fully overlapping strict-N3 stress family of fleet02/B19 r35 lies in alternative (F), so the new theorem is compatible with that correction.

## 3. Turn alternative (T) into a literal original-coordinate packet

Assume without loss of generality that

`theta_B>=eta`.                                                     (3.1)

Strict N3 gives

`||diag(B)||_op < tau=2^-20`.                                      (3.2)

Put

`H=B-diag(B)`.

Then

`||(I-P)H||_op
 >= ||(I-P)B||_op-||(I-P)diag(B)||_op
 > eta-tau`,                                                       (3.3)

hence

`||H||_F > eta-tau`.                                              (3.4)

Randomly two-color the literal ORIGINAL coordinates of `J` into `D_1,D_2`. Since `H` is symmetric with zero diagonal,

`E ||H[D_1,D_2]||_F^2 = ||H||_F^2/4`.                             (3.5)

Therefore some deterministic original-coordinate bipartition satisfies, with

`M=A[D_1,D_2]=H[D_1,D_2]`,

`boxed: E_M:=||M||_F^2 > E_perp}`,                                (3.6)

where

`E_perp = (1/16-2^-20)^2/4
        = 4294836225/4398046511104
        = 0.000976532697904986... .`                              (3.7)

This packet is obtained before any reciprocal minor is selected.

## 4. Actual fleet04/B20 payment on the new transverse packet

Apply the designated fleet04/B20 r10 fifth-volume theorem to the exact literal cut `M` from Section 3.

If

`s_1(M)^2+...+s_4(M)^2 <= (63/64)E_M`,                            (4.1)

then (1.5),(3.7) give

`e_5(M^T M) > (1/64)^4 E_perp^5/120`,                             (4.2)

and hence from (1.6)

`boxed: ||p_Q||_infinity <3178.184`.                              (4.3)

The density in this branch is continuous and vanishes at infinity.

Suppose instead that the top four directions are strong:

`s_1^2+...+s_4^2 >(63/64)E_M`.                                    (4.4)

If also

`s_3(M)>=1/256`,                                                   (4.5)

then, writing `x_r=s_r(M)^2`, ordering gives

`x_1 >(63/256)E_M >(63/256)E_perp`,                               (4.6)

while `x_2,x_3>=1/65536`. Therefore

`s_1s_2s_3
 > sqrt((63/256)E_perp)/65536
 =2.36544991144844e-7... .`                                       (4.7)

The grouped rank-three receiver (1.7) now gives the second actual payment

`boxed: ||p_Q||_infinity <1318.595`,                              (4.8)

again with a continuous `C_0` density.

Consequently every still-unpaid state in alternative (T) has a literal original-coordinate self-bank cross packet satisfying all three fixed conditions

`||M||_F^2 >0.0009765326979`,                                     (4.9)

`top4(M) >(63/64)||M||_F^2`,                                     (4.10)

`s_3(M)<1/256`.                                                    (4.11)

So the transverse-action obstruction is reduced to an **absolute-rank-two physical self-bank tube** of fixed energy. This is substantially narrower than the preceding generic overlapping self-bank Frobenius packet.

## 5. Exact in-plane rank-three endpoint is already paid

Alternative (F) isolates the genuinely different mechanism. One exact endpoint can be closed immediately.

Assume in addition that

`A = S_0 + D`                                                      (5.1)

for a physical diagonal matrix `D`, that `rank(S_0)=3`, and that the physical leverage of every coordinate in `Ran(S_0)` is at most `1/2`. These are extra hypotheses only for this endpoint; they are not asserted in the general survivor.

The completed Fresnel--Brascamp--Lieb Theorem F from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

applies directly to the original product source. If `lambda_1,lambda_2,lambda_3` are the nonzero eigenvalues of `S_0`, then

`||p_Q||_infinity <=12 |lambda_1 lambda_2 lambda_3|^(-1/3)`.      (5.2)

By (2.6), every nonzero singular value is at least `s_3(S_0)>m_*` with

`m_*=0.7985866375852596...`,                                      (5.3)

so

`boxed: ||p_Q||_infinity <12/m_* <15.027`.                        (5.4)

This endpoint has a continuous `C_0` density. It contains, but is more general than, the fully overlapping exact-rank-three stress family that motivated the union-bank Fresnel exit. The unresolved point is the non-diagonal residual and/or extra rank in the general alternative (F), not the in-plane geometry by itself.

## 6. Updated closure edge

The first missing implication in this aligned chamber is now

`QFORM-ALIGNED-INPLANE-R5-OR-TRANSVERSE-R2-PAYMENT-v1`:

1. pay the strong in-plane carrier `S_0`, `rank(S_0)<=5`, `s_3(S_0)>0.7985866`, while retaining the actual non-diagonal residual `A-S_0` of operator norm below `0.201414` rather than deleting it; or
2. pay the fixed-energy self-bank cross tube (4.9)-(4.11), which is strong-top-four and has `s_3<1/256`.

The exact rank-three plus diagonal diffuse endpoint of (1) is already paid by `<15.027`. The D5 and grouped-rank-three portions of (2) are already paid by `<3178.184` and `<1318.595`, respectively.

This is not a full solution. The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains open; continuity is proved only for the paid branches explicitly identified above.

## 7. Corrections and scope audit

The argument uses only deterministic matrix geometry, random partitioning of ORIGINAL coordinate indices, and previously completed receivers in their stated scopes. It does not regard `P^T X` or `Q^T X` as independent coordinates. It does not replace a product projection by an arbitrary bounded joint density. No small matrix coefficient is deleted from the random quadratic form. The fleet02/B19 moving-ridge and in-plane counterexamples therefore remain intact.
