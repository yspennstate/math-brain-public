SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T12:59:27Z.
attacking: the actual third-volume marginal-failure branch — convert failure of the q=4/3 integrated-Fourier marginal gate directly into a double-anchor Schur/two-star packet, then pay the exact-rank-two Schur subbranch.

# account03/B02 r30 — third-volume marginal overload compiles directly to an anchored Schur / two-star resource

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Owner control:** revision `2026-09-22.15`, QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport only  
**Full QFORM target:** **OPEN**  
**Target-wide universal unweighted Fourier L1 criterion:** **OPEN / not refuted**  
**Continuity:** proved on the diffuse-third-volume and exact-rank-two anchored exits below; full-target continuity remains open.

## 1. What this run changes

The preceding B02 run ended with a small-tail collar whose rank-three base had high physical-coordinate leverage on both sides. Rather than perturb that high-leverage base again, this run changes mechanism and works with the **actual third-volume determinant law of the full physical cross block**. The key observation is elementary but strong: if the completed fractional-three-volume Fourier theorem fails its marginal gate on both physical banks, then one heavy row and one heavy column must have a quantitatively large **joint** incident third-volume. That joint mass is exactly a scalar-edge times aggregate Schur pair-volume whenever the anchor edge is nonzero, and otherwise forces the two-star transverse packet.

This removes the old six-coordinate compound-hub pigeonhole loss on this route. No row/column disjointness parameter is needed.

## 2. Source-pinned inputs actually applied

Fresh owner controls and the live correction ledger were reread on `yspennstate/math-research-brain` before publication. The active programme remains QFORM-only, and the full conjecture remains open.

The mathematical inputs used below are:

1. **Fractional third-volume Fourier theorem**, canonical source
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.
   For an ORIGINAL-coordinate physical cross block `B`, put
   `Z=E3(B)=e3(B^T B)>0`, and let `alpha_i` be its determinant-weighted third-volume row inclusion marginals. If, for `1<=q<3/2`, every `alpha_i<=q/2`, then the full quadratic-plus-affine form, retaining arbitrary same-bank curvature and outside couplings, has a continuous `C_0` density satisfying

   `||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`.       (2.1)

   The same statement holds after transposing `B`, hence with the column marginals in place of the row marginals. The proof supplies genuine `phi_Q in L1`.

2. **Joint-star block compiler**, account02/B02,
   `yspennstate/math-open-problems@e8d024801adae701d47d58d85c41acb5b8ec4454`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T020523Z-account02-B02-QFORM-auto11-c1a7e2f4/REPORT.md`.
   If a row anchor `i` and column anchor `j` carry joint incident third-volume `J_ij` and

   `B=[[a,r^T],[c,N]]`,                                        (2.2)

   then with

   `F_perp=||P_(c^perp) N P_(r^perp)||_F`,

   `sqrt(J_ij) <= |a| sqrt(E2(N)) + ||c|| ||r|| F_perp`.      (2.3)

   For `a!=0`, the exact cross-Schur identity is

   `J_ij=a^2 E2(S)`, `S=N-c r^T/a`.                           (2.4)

3. **Bankwise Schur grouped-L1 theorem**, account02/B02,
   immutable containing source
   `yspennstate/math-open-problems@e28bdce394cdb3d096de191390ea5cca0b3cdef9`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T110948Z-account02-B02-QFORM-r11/REPORT.md`.
   For a physical `k x k` cross pivot `P`, cross Schur residual `S` of rank `r`, and `d=k+r>2`, it gives an integrated Fourier estimate. In the scalar-pivot/exact-rank-two case,

   `||p_Q||_infinity <= 3 e^(2/3) (|a| Delta_2(S))^(-1/3)`,    (2.5)

   with a continuous `C_0` density, where `Delta_2(S)` is the product of the two nonzero singular values.

4. **Designated partner account04/B02**, canonical source
   `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.
   If a nonsingular physical zero-diagonal principal triple `H0` exists, then

   `int_R |phi_Q(t)|^2 dt <= 6 pi 2^(2/3)|det H0|^(-1/3)`.     (2.6)

No law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea lemma, positive conditional projection-height moment, or fiberwise supremum argument is used.

## 3. Canonical third-volume law

Let `B=A[I,J]` be any physical cross block between two disjoint sets of ORIGINAL coordinates, with

`Z=E3(B)=sum_(|R|=|S|=3) det B[R,S]^2 >0`.                    (3.1)

Give every row-triple / column-triple pair the probability

`w(R,S)=det B[R,S]^2/Z`.                                      (3.2)

Define physical inclusion marginals

`alpha_i=P_w(i in R)`, `beta_j=P_w(j in S)`.                  (3.3)

They satisfy `0<=alpha_i,beta_j<=1` and

`sum_i alpha_i=sum_j beta_j=3`.                               (3.4)

For a fixed physical row `i` and column `j`, write

`J_ij=sum_(R contains i, S contains j) det B[R,S]^2`.          (3.5)

Thus

`J_ij/Z=P_w(i in R AND j in S)`.                              (3.6)

## 4. Main theorem: Fourier gate or direct anchored packet

### Theorem 4.1 — `QFORM-E3-MARGINAL-OVERLOAD-ANCHOR-COMPILER-v1`

Fix `1<q<3/2`. For every physical cross block `B` with `Z=E3(B)>0`, at least one of the following holds.

**(F) Fractional-volume Fourier exit.**  
At least one physical bank has all its third-volume marginals at most `q/2`. Then the full ambient quadratic form has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= [3e/((3-2q)sqrt(q))] Z^(-1/6).
`                                                               (4.1)

**(H) Heavy double-anchor exit.**  
There are an actual physical row `i` and physical column `j` satisfying

`boxed: J_ij>(q-1)Z.`                                         (4.2)

Writing the actual cross block around these anchors as

`B=[[a,r^T],[c,N]]`,                                          (4.3)

one has the quantitative resource dichotomy

`boxed:
 max{a^2 E2(N), ||c||^2||r||^2 F_perp^2}
 >= J_ij/4 > (q-1)Z/4.
`                                                               (4.4)

Moreover, the heavy branch has the following exact refinement:

- if `a!=0`, then for `S=N-cr^T/a`,

  `boxed: a^2 E2(S)=J_ij>(q-1)Z`;                             (4.5)

- if `a=0`, then

  `boxed: ||c||^2||r||^2 F_perp^2 >= J_ij>(q-1)Z`.            (4.6)

Thus failure of the genuine fractional-Fourier marginal gate does not leave an unspecified high-leverage state: it forces a quantitatively large original-coordinate scalar-Schur pair-volume or a quantitatively large zero-edge two-star/transverse packet.

### Proof

If all row marginals obey `alpha_i<=q/2`, apply (2.1) directly. If all column marginals obey `beta_j<=q/2`, apply (2.1) to `B^T`. This proves (F).

Otherwise choose a row `i` and a column `j` with

`alpha_i>q/2`, `beta_j>q/2`.                                  (4.7)

By inclusion-exclusion for the two events `{i in R}` and `{j in S}` under the **same canonical determinant law**,

`J_ij/Z
 =P(i in R AND j in S)
 >=alpha_i+beta_j-1
 >q-1`.                                                        (4.8)

This proves (4.2).

Apply the source-valid joint-star compiler (2.3). If both summands on its right were `<sqrt(J_ij)/2`, their sum would be `<sqrt(J_ij)`, impossible. Hence at least one is `>=sqrt(J_ij)/2`; squaring gives (4.4).

If `a!=0`, the exact anchored cross-Schur determinant identity (2.4) gives (4.5), with no loss. If `a=0`, the first summand in (2.3) vanishes, so (2.3) itself yields `||c||||r||F_perp>=sqrt(J_ij)`, proving (4.6). QED.

### The useful `q=4/3` specialization

At `q=4/3`, either

`boxed: ||p_Q||_infinity
 <= (9 sqrt(3)e/2) Z^(-1/6)
 =21.1869100628... Z^(-1/6),`                                 (4.9)

with a continuous density, or there are physical anchors with

`boxed: J_ij>Z/3.`                                             (4.10)

Consequently, if the anchor edge is nonzero,

`a^2E2(S)>Z/3`,                                                (4.11)

whereas if the anchor edge is zero,

`||c||^2||r||^2F_perp^2>Z/3`.                                 (4.12)

Compare this with the earlier B02 six-coordinate compound-hub compiler, whose generic joint-star currency incurred a factor `1/36` after hub pigeonholing. Here no disjointness/hub hypothesis is used: the strong packet comes directly from the failure of the analytic marginal gate itself.

## 5. Exact-rank-two heavy Schur branch is now fully paid

Assume branch (H), `a!=0`, and

`rank(S)=2`.                                                   (5.1)

Then

`E2(S)=Delta_2(S)^2`,                                         (5.2)

so from (2.4)

`|a|Delta_2(S)=sqrt(J_ij)`.                                   (5.3)

Apply the completed bankwise Schur grouped-L1 theorem (2.5):

`||p_Q||_infinity
 <=3e^(2/3) J_ij^(-1/6)`                                      (5.4)

`<3e^(2/3)(q-1)^(-1/6) Z^(-1/6).`                             (5.5)

The characteristic function is in `L1`, so the density is continuous and vanishes at infinity.

At `q=4/3`,

`boxed:
 ||p_Q||_infinity
 <3^(7/6)e^(2/3) Z^(-1/6)
 =7.0173173663... Z^(-1/6).
`                                                               (5.6)

Thus the old B02 debt `EDGE-E2-TO-L1` is **fully paid on the exact-rank-two cross-Schur subbranch**. Since `J_ij>0`, the nonzero-edge branch cannot have `rank(S)<=1`; the remaining nonzero-edge heavy case is specifically `rank(S)>=3`.

There is a tunable constant tradeoff. If one only wanted to minimize the larger coefficient between (4.1) and the exact-rank-two payment (5.5), their coefficients are equal at

`q=1.068330632392...`,                                        (5.7)

where both are

`9.13864210173...`.                                           (5.8)

For structural continuation I retain `q=4/3`, because its unpaid heavy packet is much stronger: `J_ij>Z/3` rather than only about `0.06833 Z`.

## 6. Designated account04/B02 result applied at an actual inequality

On the exact-rank-two heavy branch, the bankwise grouped theorem also gives the explicit high-frequency envelope. Since its grouped projection factors satisfy the universal cap used in that theorem,

`|phi_Q(t)|
 <=min{1, A |t|^(-3/2)},`                                     (6.1)

where

`A=pi^(3/2)e J_ij^(-1/4)`.                                    (6.2)

Assume additionally that the full physical matrix contains a nonsingular zero-diagonal principal triple `H0`. The designated account04/B02 theorem gives

`L:=int_R |phi_Q(t)|^2 dt
 <=6pi 2^(2/3)|det H0|^(-1/3)`.                               (6.3)

For every `T>0`, Cauchy--Schwarz on the low-frequency interval and (6.1) on its complement give

`||phi_Q||_1
 <=sqrt(2LT)+4A T^(-1/2)`.                                    (6.4)

The exact optimizer is

`T=4A/sqrt(2L)`.                                               (6.5)

Substitution yields

`||phi_Q||_1 <=4 A^(1/2)(2L)^(1/4)`.                          (6.6)

Fourier inversion, (6.2), and (6.3) therefore give the new hybrid inequality

`boxed:
 ||p_Q||_infinity
 <=2^(5/3) 3^(1/4)e^(1/2)
   |det H0|^(-1/12) J_ij^(-1/8)
`                                                               (6.7)

`=6.88881011759...
  |det H0|^(-1/12) J_ij^(-1/8).`

At the `q=4/3` heavy threshold `J_ij>Z/3`,

`boxed:
 ||p_Q||_infinity
 <2^(5/3)3^(3/8)e^(1/2)
  |det H0|^(-1/12) Z^(-1/8)
`                                                               (6.8)

`=7.90286150083...
  |det H0|^(-1/12) Z^(-1/8).`

This is an equation-level use of the designated partner result, not a citation-only mention. Continuity on this overlap already follows from the exact-rank-two grouped-L1 theorem.

## 7. Deterministic numerical regression

A seeded `20260923` finite regression was used only to catch algebra/indexing errors; it is not part of the proof.

For 100 random real `5 x 5` cross blocks, the code enumerated all physical `3 x 3` minors, formed `Z`, the row/column marginals, and all `J_ij`, then selected the maximally heavy row and column. It checked

`J_ij/Z >= alpha_i+beta_j-1`                                   (7.1)

and the exact identity

`J_ij=a^2 E2(N-cr^T/a)`.                                      (7.2)

The maximum relative error in (7.2) was `1.27e-14`; there were zero inclusion-exclusion violations.

A second 200-instance regression checked the source joint-star inequality (2.3); the minimum observed numerical slack was `8.05e-3` and there were zero violations.

The constants in (4.9), (5.6), (6.7), (6.8), and the balancing value (5.7) were recomputed independently.

## 8. Exact remaining implication

The full QFORM conjecture is **not** solved by this run, and neither is the target-wide statement `int |phi_Q| <= C` under the bare spectral hypothesis.

For any actual physical cross block carrying useful `Z=E3(B)`, the marginal obstruction is now sharply reduced to only two heavy-anchor geometries:

1. **nonzero anchor edge with higher Schur rank:**

   `a!=0`, `rank(S)>=3`, and `a^2E2(S)>Z/3`;                  (8.1)

2. **zero anchor edge two-star/transverse packet:**

   `a=0`, `||c||^2||r||^2F_perp^2>Z/3`.                      (8.2)

The next B02 step is therefore `QFORM-E3-HEAVY-ANCHOR-HIGHRANK-OR-ZEROEDGE-v1`: use the higher-rank Schur packet's actual third-volume/ridge content or route the zero-edge two-star packet through the fresh curvature compiler/grouped-hub receivers, while retaining arbitrary same-bank curvature and every small cross direction. In particular, do **not** return to a generic high-leverage perturbation argument; the determinant-law overload has already produced stronger physical currency.

No target-valid counterexample to the universal unweighted characteristic-function `L1` criterion was found in this run. The criterion remains open; the present theorem establishes it only on the stated diffuse and exact-rank-two anchored branches.

## 9. Integrity boundary

All random variables remain in original independent coordinates. Spectral/SVD objects are used only for deterministic matrix invariants in already-proved source theorems. No new assumptions on moments, support, log-concavity, Gaussianity, signs, compactness, or diagonalizability in the product coordinates are introduced. Essential boundedness versus continuity is tracked separately as above.
