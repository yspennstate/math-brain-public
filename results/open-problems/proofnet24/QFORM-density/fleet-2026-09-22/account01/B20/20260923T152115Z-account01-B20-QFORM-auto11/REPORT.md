SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-23T15:21:15Z.
attacking: close the R1/R2 absolute rank-two physical-cross survivor by spending the second singular direction before localization and the many-small singular tail before any deletion.

# account01/B20 — R1 same-side recursion and R2 Frobenius-tail compiler

**Run:** `20260923T152115Z-account01-B20-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREMS / FULL QFORM OPEN`.  
Global continuity remains **OPEN** separately.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source discipline

The exact target remains: arbitrary dimension; independent real coordinates with probability densities bounded by one; arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No Gaussian, moment, iid, support, log-concavity, diagonal-basis, or post-rotation-independence assumption is introduced.

The fresh completed designated partner actually consumed is account02/B20 run `20260923T142651Z-account02-B20-QFORM-auto11`, canonical mathematics

`yspennstate/math-open-problems@a996362199678ee069db30c5ab31a44b2d3d29d6`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260923T142651Z-account02-B20-QFORM-auto11/REPORT.md`.

Together with the current cross-cut compiler, the live N3 survivor has an ORIGINAL-coordinate full partition `[n]=J disjoint_union K`, cross block `N=A[J,K]`,

`E=||N||_F^2 > 11907/16384`,

and, after already-paid branches, either

- **R1:** `s2<=s1/16` and `sum_(r>=2) s_r^2 < s1^2/36`, or
- **R2:** `sum_(r>=3) s_r^2 < (3/64)E` and `s1*s2 > delta`, where

`delta=726327/33554432`.

The fresh account02/B20 closure used below is

`boxed{s3(N)<1/64}`                                                        (1.1)

for every still-unpaid state. If `N2` is the best rank-two SVD truncation, then for every literal physical subblock

`dist_op(N[L,R], rank<=2) <= ||N[L,R]-N2[L,R]||op <= s3(N)<1/64`.          (1.2)

This is the required direct application of the completed account02/B20 result to an actual inequality. The SVD is deterministic coefficient geometry only; no rotated random variable is declared independent.

The unrestricted physical fifth-volume theorem and fractional third-volume theorem used below are the already source-pinned D5/D' receivers retained by account02/B20. They act on literal original-coordinate cross blocks and retain arbitrary same-bank quadratic blocks, outside variables, couplings and extra spectrum.

## 2. R1: either a very strong rank-two four-bank packet or a nested same-side cross cut

Write the singular values of `N` as `s1>=s2>=...`.

### Theorem 2.1 — `QFORM-R1-CROSS2-OR-NESTED-SAMESIDE-v1`

Assume R1 and (1.1). Then one of the following holds.

1. There are physical partitions `J=J1 disjoint_union J2`, `K=K1 disjoint_union K2` such that the separated squared `2x2`-minor mass `P2` satisfies

   `P2 >= 1/64`,                                                        (2.1)

   and, with `E_pq=||N[Jp,Kq]||_F^2`,

   `max(E11 E22, E12 E21) >= 1/256`.                                   (2.2)

   Every one of the four physical subblocks is within operator distance `<1/64` of rank at most two by (1.2).

2. There is one of the two physical sides, call it `S`, and a partition `S=L disjoint_union R`, for which

   `F:=||A[L,R]||_F^2 > 3025/16384 = (55/128)^2`.                       (2.3)

   If the four largest squared singular values of `A[L,R]` carry at most `(63/64)F`, the full law has a continuous `C_0` density with

   `||p_Q||_infinity < 231.138`.                                       (2.4)

   Otherwise the literal nested cross block satisfies

   `sum_(r=1)^4 s_r(A[L,R])^2 > 190575/1048576`.                        (2.5)

#### Proof

Split according to whether `s2>=1/8`.

If `s2>=1/8`, the R1 inequality `s2<=s1/16` gives `s1>=16s2>=2`, hence

`(s1 s2)^2 >= 1/16`.                                                    (2.6)

By Cauchy--Binet,

`e2(N^T N)=sum_(|I|=|K|=2) det N[I,K]^2 >= s1^2 s2^2 >=1/16`.          (2.7)

Independently two-colour the physical rows and physical columns. A fixed row pair is separated with probability `1/2`, as is a fixed column pair, so the expected separated minor mass is `e2/4`. Therefore some deterministic physical four-bank partition has

`P2 >= e2/4 >=1/64`, proving (2.1).

For each separated minor with entries `a,b,c,d`,

`(ad-bc)^2 <=2(a^2d^2+b^2c^2)`.

Summing gives

`P2 <=2(E11E22+E12E21) <=4 max(E11E22,E12E21)`,

so (2.2) follows. Equation (1.2), which is exactly the fresh account02/B20 closure, gives the inherited absolute rank-two tube on all four blocks.

Now suppose `s2<1/8`. Let `N1=s1 u v^T` be the top rank-one term and form the symmetric rank-two matrix on the full physical partition

`S0 = [[0,N1],[N1^T,0]]`.

Since `rank S0<=2`, the Eckart--Young variational characterization gives

`||A-S0||op >= s3(A) >=1`.                                              (2.8)

Writing `B=A[J,J]`, `C=A[K,K]`, and `R=N-N1`,

`A-S0=[[B,R],[R^T,C]]`, `||R||op=s2<1/8`.

Hence

`1 <= ||A-S0||op <= max(||B||op,||C||op)+s2`,

so one physical principal side `D` satisfies

`||D||op>7/8`.                                                          (2.9)

All physical diagonals in the N3 state have modulus `<1/64`. Therefore, with `H=D-diag(D)`,

`||H||op > 7/8-1/64 =55/64`.                                           (2.10)

Randomly bipartition the coordinates of that side as `L disjoint_union R`. Because `H` is symmetric and zero diagonal,

`E ||H[L,R]||_F^2 = (1/4)||H||_F^2 >= (1/4)||H||op^2 > (55/128)^2`.

Thus a deterministic physical cut gives (2.3). The unrestricted D5 theorem says that if its top four squared singular values have mass at most `(63/64)F`, then

`e5 >= F^5/(120*64^4)`

and

`||p_Q||_infinity <=5 sqrt(2e) e5^(-1/10) <231.137088 <231.138`,

with continuous density. Otherwise (2.5) follows directly from `(63/64)(3025/16384)=190575/1048576`. QED.

### Consequence

The former vague R1 two-source packet is gone. Its unpaid content is now either a **very strong physical four-bank second-volume packet** with matching energy product at least `1/256`, or a **nested same-side strong-top-four physical cross packet**. In the latter branch the old near-rank-one cross `N` and the new nested cut coexist; no small random quadratic perturbation has been deleted.

## 3. R2: spend the entire many-small singular tail before calling the block rank two

Let

`T=sum_(r>=3)s_r(N)^2`.

### Theorem 3.1 — `QFORM-R2-TAIL-SPEND-OR-FROBENIUS-TUBE-v1`

Assume R2 and (1.1). Put

`Z0 := delta^2/4096
    =527550910929/4611686018427387904
    =1.14394368745...e-7`.                                              (3.1)

Then one of the following holds.

1. The full law has a continuous `C_0` density with

   `||p_Q||_infinity <368.879`;                                        (3.2)

2. there are a physical row anchor `i` and column anchor `j` and physical two-colourings of the remaining rows and columns for which the doubly anchored separated third-minor mass exceeds

   `Z0/12
    =175850303643/18446744073709551616
    =9.5328640621...e-9`;                                              (3.3)

3. the entire singular tail is genuinely small in Frobenius norm:

   `sum_(r>=3)s_r^2 <1/4096`,
   `||N-N2||_F <1/64`.                                                  (3.4)

   Consequently every literal physical subblock obeys

   `dist_F(N[L,R], rank<=2)<1/64`.                                     (3.5)

   In addition the R2 four-bank compiler from the preceding B20 run still supplies a physical partition with

   `max(E11E22,E12E21) > delta^2/16
    =527550910929/18014398509481984
    =2.92849583988...e-5`.                                             (3.6)

#### Proof

The exact elementary-symmetric identity contains all terms with indices `(1,2,r)`, hence

`e3(N^T N) >= s1^2 s2^2 sum_(r>=3)s_r^2 > delta^2 T`.                  (3.7)

If `T>=1/4096`, then `e3>Z0`. If all normalized third-volume row marginals are at most `2/3`, or all normalized column marginals are at most `2/3`, the reviewed D' theorem at `h=2/3` gives

`||p_Q||_infinity <=9 sqrt(3e) e3^(-1/6)
                   <9 sqrt(3e) Z0^(-1/6)
                   =368.8781547... <368.879`,

with continuous `C_0` density.

If neither orientation is diffuse, choose a physical row `i` and physical column `j` whose inclusion marginals both exceed `2/3`. Under the probability measure proportional to squared physical `3x3` minors, inclusion-exclusion gives joint inclusion probability `>1/3`. Thus the total third-minor mass containing both anchors is `>e3/3>Z0/3`.

Independently two-colour the two remaining rows and the two remaining columns of each anchored minor. Both pairs are separated with probability `1/4`, so some deterministic physical colouring retains more than `Z0/12`. This is (3.3). It is an aggregate anchored resource; no single good minor is inferred.

The only remaining case has `T<1/4096`, which is exactly (3.4). Restricting the deterministic residual `N-N2` to literal coordinate subblocks cannot increase its Frobenius norm, proving (3.5). The matching-energy statement (3.6) is the already-proved R2 physical four-bank consequence and is simply retained. QED.

### Consequence

The R2 phrase “absolute rank-two tube” can now be strengthened: unless a source-valid D' payment or a concrete doubly anchored third-volume packet is present, the cross block lies in an **absolute Frobenius** rank-two tube of radius `1/64`, not merely an operator-norm tube. This explicitly spends a potentially high-rank cloud of small singular directions instead of deleting it.

## 4. Updated first unpaid implication

The first remaining closure edge is now

`QFORM-N3-RANK2-FOURBANK-OR-NESTED-TOP4-ANCHOR-PAYMENT-v1`.

A still-unpaid N3 state has been reduced to one of the following explicit original-coordinate packets:

1. an R1-derived four-bank rank-two packet with matching energy product `>=1/256` and inherited operator rank-two error `<1/64` on each block;
2. an R2-derived four-bank packet with matching energy product `>delta^2/16` and **Frobenius** rank-two error `<1/64` on every subblock;
3. an R1-derived nested same-side physical cross block with top-four squared singular mass `>190575/1048576`, coexisting with the original near-rank-one cut;
4. an R2-derived physical row/column double anchor with separated third-minor mass `>Z0/12`.

The next payment should use the existing augmented-three-volume/fractional-volume receiver on packets 3--4 and the physical indefinite-pair/Schur-cross or grouped random-slope machinery on packets 1--2. Any such payment must retain same-bank curvature, outside couplings and the exact tail; the aligned/concentrated complement is the genuine remaining issue.

## 5. Corrections retained

No law-uniform pointwise quadratic oscillatory decay is used. No independence after a spectral rotation is asserted. No arbitrary-joint coarea cap, worst-fiber conditional supremum, random-tail deletion, or inference from aggregate minor mass to a single universally good physical pivot/minor is made. The full conjecture remains OPEN; continuity is claimed only on the D5/D' paid branches where the cited source theorem supplies it.

## 6. Arithmetic self-check

Exact constants used above:

- `(55/128)^2 =3025/16384 =0.18463134765625`;
- `(63/64)(3025/16384)=190575/1048576 =0.1817464828491211`;
- `delta^2/4096 =527550910929/4611686018427387904`;
- `(delta^2/4096)/12 =175850303643/18446744073709551616`;
- `delta^2/16 =527550910929/18014398509481984`;
- nested D5 numerical bound `231.1370879955...`;
- R2 D' numerical bound `368.8781547499...`.

These computations check constants only; the proof is the argument above.
