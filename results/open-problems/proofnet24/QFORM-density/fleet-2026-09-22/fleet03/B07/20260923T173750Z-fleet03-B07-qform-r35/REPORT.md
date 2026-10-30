SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B07, 2026-09-23T17:37:50Z.
attacking: the r34 aggregate-E2 survivor — average all two-minor weight against the entire remaining physical interface, forcing a literal E3 payment or a common rank-two interface tube without inverting any minor.

# fleet03/B07 r35 — compound-interface descent: E2 pays E3 or forces a rank-two physical interface

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260923T173750Z-fleet03-B07-qform-r35`  
Initial brain main: `c803a4055c0d2074fa55c1f3cf8e67356666b02b`  
Pre-publication brain main: `1296067e6893015e19621787427759a2920a4367`  
Owner continuation: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **NEW SUPPORTING DETERMINANT-WEIGHTED COMPILER WITH A PAID CONTINUOUS BRANCH / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

The unrestricted conjecture is not proved or disproved here. No Gaussianity, moments, compact support, connected support, log-concavity, iid hypothesis, post-rotation independence, pointwise van-der-Corput estimate, worst-fiber density supremum, or deletion of a nonzero quadratic tail is used. Every matrix block below is on literal original-coordinate banks. No individual tiny physical minor is selected for reciprocal payment.

## 1. Source-pinned incoming packet

The previous B07 report is

`yspennstate/math-open-problems@d82a9db01d8e89e36f85d634df0ab364d74e7a8e`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T164042Z-fleet03-B07-qform-r34/REPORT.md`.

On its aggregate-minor branch there are disjoint original-coordinate banks `L,R` and a literal cross block

`K=A[L,R]`                                                        (1.1)

with

`Z:=e_2(KK^T)>854675.100194511 h^4`,                              (1.2)

where the source-pinned strict-N3 scale is

`h=(2sqrt(2)-1)/1572864
  =1.1624826588606455e-6`.                                        (1.3)

The completed designated-partner theorem actually applied quantitatively below is fleet04/B07 r1,

`yspennstate/math-open-problems@842652e93680813d356fde0f15f12ab70b59c3c3`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T091740Z-fleet04-B07-actual-core-diffuse-banks-r1/REPORT.md`.

At its genuine strict-N3 threshold `tau0=h^2/128`, every relevant physical off-diagonal coefficient satisfies

`|A_ij|<=h/8`.                                                     (1.4)

The newer designated-partner r2 report was also refreshed:

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T161510Z-fleet04-B07-coordinate-core-r2/REPORT.md`.

Its diagonal-plus-rank theorem is valid, but it requires `r+3` large physical diagonals. The present strict-N3 branch has tiny physical diagonals, so that theorem is not silently substituted here.

The analytic receiver used below is the same-hour completed fleet03/B02 theorem

`QFORM-CROSS-E3-MARGINALFREE-L1-v1`,

at

`yspennstate/math-open-problems@52cef3abd27c641ae6666d6ee3bbc25d90cb4813`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T170106Z-fleet03-B02-qform-r35/REPORT.md`.

For every literal original-coordinate cross block `T=A[I,J]`, `I cap J=empty`, with

`V=e_3(TT^T)>0`,                                                  (1.5)

it gives the full ambient law a continuous `C_0` density satisfying

`||p_Q||_infinity <= C_E3 V^(-1/6)`,                              (1.6)

where

`C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775...`.                  (1.7)

It retains arbitrary same-bank quadratic terms, outside variables, affine terms and signs. Its proof is source-pinned to the current projected-crossing theorem; I do not enlarge its hypotheses.

## 2. The two-compound defect operator

Let `K` be any real `m x n` matrix and put

`B=KK^T`, `S=tr(B)`, `Z=e_2(B)>0`.                                (2.1)

Define

`H_K := B^2-SB+ZI_m`.                                             (2.2)

Let the nonzero squared singular values of `K` be `x_1,x_2,...`, with left singular vectors `u_r`. Since `B u_r=x_r u_r`,

`H_K u_r = h_r u_r`,                                              (2.3)

where

`h_r=Z-x_r(S-x_r)
    =e_2(x_1,...,x_(r-1),x_(r+1),...)
    >=0`.                                                         (2.4)

Thus `H_K` is positive semidefinite.

Define the natural second-compound inclusion marginals

`alpha_r := x_r(S-x_r)/Z`.                                        (2.5)

They satisfy the exact identity

`sum_r alpha_r=2`,                                                 (2.6)

because every pair `x_p x_q` is counted twice. Let `P` be the spectral projection onto the span of those `u_r` with

`alpha_r>2/3`.                                                     (2.7)

Then (2.6) implies

`rank(P)<=2`,                                                      (2.8)

and on `Ran(I-P)`, equations (2.4)-(2.5) give

`H_K >= (Z/3)(I-P)`.                                               (2.9)

This projection is selected by aggregate determinant weight, not by the size of any individual coordinate minor.

## 3. Exterior identity: all two-minor weight tested against one new column

For every `y in R^m`,

`boxed: y^T H_K y
 = sum_(1<=a<b<=n) ||k_a wedge k_b wedge y||^2`,                   (3.1)

where `k_a` are the physical columns of `K`.

Indeed the right side is the squared Hilbert norm of `(wedge^2 K) wedge y`; expanding its Gram polynomial gives

`y^T[B^2-SB+e_2(B)I]y`.                                           (3.2)

Equivalently, Cauchy-Binet expands (3.1) into the sum of squares of all literal physical `3x3` minors formed from two columns of `K` and the column `y`.

There is also an exact internal identity:

`tr(K^T H_K K)
 =sum_r x_r e_2(x with x_r removed)
 =3e_3(B)`.                                                        (3.3)

Every singular-value triple is counted once for each of its three entries.

## 4. Main theorem — `QFORM-E2-COMPOUND-INTERFACE-R2-OR-E3-v1`

Let `T=[K Y]` be any column extension of `K` on the same physical row bank, and put

`V=e_3(TT^T)`.                                                     (4.1)

Then there is a physical-row-space orthogonal projection `P` of rank at most two such that

`boxed: ||(I-P)T||_F^2 <= 9 V/Z`.                                (4.2)

In particular,

`boxed: dist_F(T,{rank<=2}) <= 3 sqrt(V/Z)`.                      (4.3)

### Proof

Sum (3.1) over every column of `Y`. The result is precisely the squared-minor mass `M_21` formed from two columns of `K` and one column of `Y`. With (3.3),

`tr(T^T H_K T)=3e_3(KK^T)+M_21`.                                 (4.4)

Now expand `V=e_3(TT^T)` by physical column types. It contains nonnegative contributions from:

- three columns of `K`, totaling `e_3(KK^T)`;
- two columns of `K` and one of `Y`, totaling `M_21`;
- one column of `K` and two of `Y`;
- three columns of `Y`.

Therefore

`tr(T^T H_K T)
 =3e_3(KK^T)+M_21
 <=3[e_3(KK^T)+M_21+M_12+M_03]
 =3V`.                                                            (4.5)

On the other hand (2.9) gives

`tr(T^T H_K T)
 >=(Z/3)||(I-P)T||_F^2`.                                         (4.6)

Combine (4.5)-(4.6) to get (4.2), and use `rank(PT)<=rank(P)<=2` for (4.3). QED.

### Threshold form

For every `mu>0`, either

`boxed: e_3(TT^T)>=mu`,                                           (4.7)

or

`boxed: dist_F(T,{rank<=2})<3 sqrt(mu/Z)`.                        (4.8)

The point is that the reciprocal quantity is `Z^(-1/2)`, where `Z` is the **entire aggregate second-minor mass**. No small selected determinant ever enters a denominator.

## 5. Application to the r34 aggregate-E2 branch

Take the actual block (1.1) and its full one-sided physical interface

`T_L=A[L,L^c]`.                                                    (5.1)

It contains `K=A[L,R]` as a literal column subblock. Set

`mu=h^6`.                                                         (5.2)

By (1.2) and Theorem 4.1, one of two alternatives holds.

### Branch E3-L: paid continuously

If

`e_3(T_L T_L^T)>=h^6`,                                            (5.3)

then fleet03/B02's marginal-free physical-E3 theorem gives the **full ambient** bound

`boxed: ||p_Q||_infinity <= C_E3/h
       =9075549.429274965...`.                                    (5.4)

Moreover `phi_Q in L^1`, so this branch has a continuous `C_0` density.

### Branch R2-L: the whole physical interface is rank-two up to a tiny retained tail

Otherwise there is a rank-at-most-two physical-row-space projection `P_L` with

`||(I-P_L)A[L,L^c]||_F
 < [3/sqrt(854675.100194511)] h`                                  (5.5)

and hence

`boxed: ||(I-P_L)A[L,L^c]||_F
 <0.003245045039388 h
 =3.772308585510006e-9`.                                          (5.6)

No coefficient in this tail is discarded; (5.6) is the exact deterministic residual to be carried into the next receiver.

Apply the same theorem to `K^T=A[R,L]` and

`T_R=A[R,R^c]`.                                                    (5.7)

Thus, unless the E3 payment occurs on either orientation, there is a paired rank-at-most-two projection `P_R` with the same bound

`||(I-P_R)A[R,R^c]||_F<0.003245046 h`.                            (5.8)

The heavy singular indices in the two applications are the paired left/right singular directions of the same `K`, so this is a genuine two-sided physical-interface tube, not two unrelated coordinate rotations.

## 6. Rank-four carrier for the union bank

Let

`S0=L union R`, `O=(L union R)^c`,                                (6.1)

and set `P0=P_L direct_sum P_R` on the original-coordinate row bank `S0`. Then

`rank(P0)<=4`.                                                     (6.2)

The outside cross block is

`C=A[S0,O]`.                                                       (6.3)

Using (5.6) and (5.8) on its two row pieces,

`||(I-P0)C||_F^2
 <=||(I-P_L)A[L,L^c]||_F^2
  +||(I-P_R)A[R,R^c]||_F^2
 <18 h^6/Z`.                                                       (6.4)

Consequently the fully unpaid branch has the explicit physical carrier

`boxed: dist_F(A[S0,O],{rank<=4})
 <3 sqrt(2/854675.100194511) h
 <0.004589186706 h
 =5.334849963084716e-9`.                                          (6.5)

This is a deterministic coefficient statement only. It does not say a small coefficient tail is a small random quadratic perturbation; no moment assumption is available, so the tail must remain in the eventual analytic argument.

## 7. Required designated-partner application at an actual inequality

The completed fleet04/B07 r1 coefficient cap (1.4) gives a second quantitative consequence on Branch E3-L.

Every constituent physical `3x3` cross determinant in `e_3(T_L T_L^T)` uses nine off-diagonal entries, each of modulus at most `h/8`. Hadamard therefore gives

`|det| <= (sqrt(3)h/8)^3 = (3sqrt(3)/512)h^3`.                   (7.1)

If (5.3) holds, the number `N_3` of nonzero literal physical `3x3` cross minors satisfies

`N_3 [(3sqrt(3)/512)h^3]^2 >= h^6`,                              (7.2)

hence

`N_3 >= ceil(262144/27)=9710`.                                   (7.3)

Thus the E3 payment is necessarily diffuse over at least 9710 nonzero physical third minors under the actual strict-N3 cap. This is an equation-level use of the designated partner theorem, not a nominal citation. The count is structural corroboration; the density bound itself comes from aggregate `E3`, not from selecting one of those minors.

## 8. Relation to the newest fleet geometry

The same-hour fleet01/B20 mixed-E3 compiler independently identifies an unpaid `rank-one tube / common four-plane` geometry after paying misaligned rank-two structure through a physical E3 receiver. The present theorem reaches a compatible but distinct statement from the B07 aggregate-E2 branch: **the entire one-sided interfaces** are forced into rank-two Frobenius tubes, and the union-to-outside block into a rank-four tube, unless a literal E3 cross block already pays.

This does not by itself satisfy fleet04/B07 r2's diagonal-plus-rank hypothesis, because the strict-N3 branch has tiny physical diagonals. Nor does a small Frobenius coefficient tail permit deletion under arbitrary unbounded product inputs. Those are genuine remaining analytic debts.

## 9. First remaining implication

The precise next B07 debt is

`QFORM-R2-INTERFACE-TUBE-RECEIVER-v1`:

> Starting from the two-sided original-coordinate interface tubes (5.6), (5.8), or equivalently the rank-at-most-four union carrier (6.5), retain the nonzero tail exactly and combine it with the remaining internal block / hub / diagonal resources to obtain a full ambient density payment; alternatively force a new literal physical E3 packet or an actual bounded physical principal core.

The r34 hub/12-bank and 12-by-2-grid siblings remain separate branches. They are not silently declared closed by the present aggregate-E2 descent.

**Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.** Continuity is proved only on the E3-paid branch (5.3)-(5.4).

## 10. Regression checks

`CHECKS.py` and `CHECKS.txt` sit beside this report. They verify:

- 270 exact integer instances of
  `tr(T^T H_K T)=3e_3(KK^T)+M_21<=3e_3(TT^T)`;
- 1438 finite numerical instances of the spectral-projection inequality (4.2);
- all propagated constants in Sections 5-7, including the partner-derived count 9710.

The captured output ends `STATUS=PASS`. These computations are regression evidence only; the proof is the algebra in Sections 2-7.
