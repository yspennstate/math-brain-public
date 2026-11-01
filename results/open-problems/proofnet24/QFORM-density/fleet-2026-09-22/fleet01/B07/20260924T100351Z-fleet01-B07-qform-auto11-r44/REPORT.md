SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-24T10:03:51Z.
attacking: determinant-weight preserving heavy-coordinate deletion for physical E3 crossings, and a physical-rank-three compiler for the r43 exact-singular anchored-C4 shadow.

# fleet01/B07 r44 — E3 heavy-delete/pivot-star selection and anchored-C4 to physical rank-three compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection  
Status: **NEW EXACT COORDINATE-SELECTION THEOREMS / ONE DESIGNATED-PARTNER r51 BRANCH PAID / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**

The unrestricted conjecture remains open. No Gaussianity, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or independence after a spectral rotation is used. No pointwise law-uniform quadratic-phase decay, arbitrary-joint coarea bound, fiber-supremum argument, deletion of a nonzero coefficient tail, or Monte Carlo extremality claim is used.

## 1. Source-pinned incoming state


The exact-singular anchored-fourth-compound input is fleet01/B07 r43:

`yspennstate/math-open-problems@0d782a4c89b6e45e7e38a4aedd3eeb38cda538a7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/20260924T070328Z-fleet01-B07-qform-auto11-r43/REPORT.md`.

On that branch a literal physical pair `H={h,h'}` has rank-one principal block. After a determinant-one shear inside that pair only, the coefficient matrix is written algebraically as

`A'=[[a,0,u^T],[0,0,w^T],[u,w,C]]`,                               (1.1)

where `C=A[O,O]`, `O=H^c`, is the unchanged ORIGINAL-coordinate residual principal block. Put

`S=C-u u^T/a`, `e=w/||w||`, `P=I-ee^T`,

and let `F=F_H^(4)` be the complete matrix of anchored physical 4x4 minors indexed by residual physical pairs. The r43 exact identity is

`F=-a E_w^T S E_w`, `E_w E_w^T=||w||^2 P`,                        (1.2)

and therefore

`||F||op=gamma ||P S P||op`, `gamma:=|a| ||w||^2 >=7/96`.          (1.3)

The latest completed designated partner used below is fleet02/B07 r51:

`yspennstate/math-open-problems@0489be649867dd226d4b6cea9ded74c973f19d46`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260924T093902Z-fleet02-B07-qform-r51/REPORT.md`.

Its balanced physical-cut theorem says that for a symmetric rank-r physical principal approximant `R=U Lambda U^T`, with `delta=max_i ||U(i,:)||^2`, `rho=sqrt(r delta)<1`, and `a0=(1-rho)/2`, there is a literal original-coordinate partition `I|J` satisfying

`s_k(R[I,J])>=a0 s_k(R)`.                                           (1.4)

The source-refresh upgrade in the same completed partner result combines this with the completed fleet02/B03 marginal-free physical-E3 crossing theorem

`yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T184716Z-fleet02-B03-QFORM-auto11/REPORT.md`.

For every literal physical crossing `M=A[I,J]`, with `Z3=e3(MM^T)>0`, that theorem gives a continuous density and

`||p_Q||infinity <= C3 Z3^(-1/6)`,
`C3=3*2^(4/3)*e^(1/3)=10.5501688311648...`.                         (1.5)

All same-side blocks, affine terms, outside couplings and additional spectrum are arbitrary in (1.5).

The pinned determinant-volume source `e5f71d79eff325201dd0274053d20268ce65b837`, Theorem D, was also read. Its row-marginal-gated estimate is used only in Theorem 2.1 below, exactly in its proved scope.

## 2. Physical E3 determinant law: diffuse deletion or one complete pivot star

Let `I,J` be disjoint ORIGINAL-coordinate banks, let

`M=A[I,J]`,
`Z=e3(MM^T)=sum_{|R|=|C|=3} det M[R,C]^2 >0`,                      (2.1)

and normalize the squared-minor law

`p(R,C)=det M[R,C]^2/Z`.                                            (2.2)

Write row and column inclusion marginals

`alpha_i=P_p(i in R)`, `beta_j=P_p(j in C)`.                        (2.3)

Then `sum_i alpha_i=sum_j beta_j=3`.

### Theorem 2.1 — `QFORM-Z3-HEAVYDELETE-OR-PIVOTSTAR-v1`

At least one of the following holds.

**(A) Row-diffuse physical restriction.** There is a literal row restriction `I0 subset I` such that

`Z0=e3(M[I0,J] M[I0,J]^T) >= Z/3`,                                 (2.4)

and every row-volume marginal of the restricted crossing is at most `1/2`. Hence the pinned Theorem D gives the FULL ambient law a continuous density with

`boxed: ||p_Q||infinity <=6 sqrt(e) 3^(1/6) Z^(-1/6)`
`                         <11.881 Z^(-1/6).`                         (2.5)

**(B) Column-diffuse physical restriction.** The transpose statement holds on the column side, and the same bound (2.5) follows after swapping the two physical banks.

**(C) One literal row-column pivot carries a complete third-minor star.** There are actual physical coordinates `i in I`, `j in J` such that

`boxed:
 W_ij:=sum_{R containing i, C containing j, |R|=|C|=3}
             det M[R,C]^2
      > Z/972.
}`                                                                  (2.6)

Moreover this complete packet has the following exact inverse-free description. Reorder only for notation and write

`M=[[m,r^T],[c,N]]`, `m=M_ij`.                                     (2.7)

If `m!=0`, with the true scalar Schur cross

`S_ij=N-c r^T/m`,                                                   (2.8)

one has

`boxed: W_ij=m^2 e2(S_ij S_ij^T).`                                  (2.9)

If `m=0`, then

`boxed:
 W_ij=||c||^2 ||r||^2
      ||P_(c^perp) N P_(r^perp)||_F^2.
}`                                                                  (2.10)

Thus the zero-pivot face is retained exactly; no reciprocal `m` is introduced there.

#### Proof

Define heavy physical row and column sets

`H_R={i:alpha_i>=1/6}`, `H_C={j:beta_j>=1/6}`.                     (2.11)

Because each family of marginals sums to three,

`|H_R|<=18`, `|H_C|<=18`.                                          (2.12)

Let

`theta_R=P_p(R cap H_R=empty)`, `theta_C=P_p(C cap H_C=empty)`.     (2.13)

If `theta_R>=1/3`, restrict M to the rows `I\H_R`. Its total squared 3-minor mass is `Z0=theta_R Z>=Z/3`. For every retained row i, `alpha_i<1/6`; therefore its new normalized marginal obeys

`alpha_i' <= alpha_i/theta_R < (1/6)/(1/3)=1/2`.                   (2.14)

This proves (A), including (2.5) by Theorem D. The proof of (B) is identical after transposition.

Suppose neither (A) nor (B) occurs. Then

`P_p(R hits H_R)>2/3`, `P_p(C hits H_C)>2/3`,                       (2.15)

so the union bound gives

`P_p(R hits H_R AND C hits H_C)>1/3`.                              (2.16)

For each `i,j`, let `W_ij` be (2.6). Summing over `i in H_R,j in H_C`, every squared minor in the event (2.16) is counted at least once. Hence

`sum_{i in H_R,j in H_C} W_ij >Z/3`.                               (2.17)

There are at most `18^2=324` pairs, so one pair satisfies

`W_ij>Z/(3*324)=Z/972`, proving (2.6).

For the structural identities, a fixed 3x3 minor containing pivot row i and pivot column j is indexed by residual row and column pairs `R,C`. If `m!=0`, the block determinant identity gives

`det [[m,r_C^T],[c_R,N_RC]]
 =m det(N_RC-c_R r_C^T/m)`.                                        (2.18)

Summing the squares over all residual 2x2 minors and applying Cauchy-Binet gives (2.9).

If `m=0`, orthogonally change bases only in the residual row and residual column index spaces, sending `c` and `r` to `||c||e_1` and `||r||e_1`. This is an algebraic proof step; it does not rotate random variables. The sum of squares of all fixed-pivot minors is invariant because the second exterior powers of the two orthogonal changes are orthogonal. In the aligned bases, a fixed-pivot 3x3 determinant can be nonzero only when both residual pairs contain the first aligned direction, and then it equals `-||c|| ||r||` times the corresponding entry of the doubly projected residual block. Summing squares gives (2.10). QED.

### Interpretation

The theorem is deliberately aggregate-before-inversion. It does not say that one 3x3 minor is uniformly large. It says that a complete physical E3 determinant law either remains sufficiently diffuse after deleting a bounded heavy set and is paid analytically, or it concentrates a universal fraction of its own total weight into one full scalar-pivot star. The scalar star is then represented by a true Schur `E2` packet or an exact zero-pivot projected-cross packet.

This interface is useful even when `Z` itself is below universal scale: it preserves the entire determinant weight needed by later conditioning, instead of paying a reciprocal cost of one tiny selected minor.

## 3. The r43 anchored-C4 shadow forces an ORIGINAL-coordinate rank-three tube

The previous r43 report described a rank-three tube only after scalar Schur elimination in the sheared pair coordinate. The following observation moves that tube back to the untouched physical residual principal block `C=A[O,O]`, where product-coordinate receivers are legal.

Write, as in (1.1)-(1.3),

`S=C-u u^T/a`, `e=w/||w||`, `P=I-ee^T`,                           (3.1)

and put

`alpha=e^T S e`, `b=P S e`, `T=P S P`.                            (3.2)

Then exactly

`S=alpha e e^T+e b^T+b e^T+T`.                                   (3.3)

Define the symmetric matrix on the literal residual physical coordinates

`R_C:=u u^T/a + alpha e e^T+e b^T+b e^T`.                          (3.4)

Its range is contained in `span{u,e,b}`, so

`rank R_C<=3`.                                                      (3.5)

Since `C=u u^T/a+S`, one has the exact decomposition

`boxed: C=R_C+T`,                                                   (3.6)

and r43 gives

`boxed:
 ||T||op=||F_H^(4)||op/gamma
       <=(96/7)||F_H^(4)||op.
}`                                                                  (3.7)

This is `QFORM-EXACTSINGULAR-C4-PHYSICAL-RANK3-COMPILER-v1`.

The important point is provenance: `C` is the ORIGINAL-coordinate residual principal block and the pair shear does not alter it. Therefore (3.6) is a legal input to physical-cut theorems for the independent residual variables. The possibly enormous rank-one coefficient `u u^T/a` is retained inside the finite-rank approximant; no small-pivot reciprocal is paid in the error term.

## 4. Actual application of designated partner fleet02/B07 r51

Assume `rank R_C=3`; let

`sigma=s3(R_C)>0`,
`delta=max_i (P_R)_{ii}`,                                          (4.1)

where `P_R` is the orthogonal projector onto `range(R_C)`. Suppose first that

`delta<=1/12`.                                                      (4.2)

For partner r51 with `r=3`,

`rho=sqrt(3 delta)<=1/2`,
`a0=(1-rho)/2>=1/4`.                                               (4.3)

Thus its completed balanced-cut theorem produces a literal partition `O=I disjoint_union J` with

`s3(R_C[I,J])>=sigma/4`.                                           (4.4)

Let

`eta=||T||op=||F||op/gamma`.                                       (4.5)

The actual crossing of the ORIGINAL coefficient matrix is

`C[I,J]=R_C[I,J]+T[I,J]`,

and `||T[I,J]||op<=eta`; hence Weyl gives the actual inequality

`boxed: s3(C[I,J])>=sigma/4-eta.`                                  (4.6)

If `sigma>4 eta`, the completed marginal-free physical-E3 receiver used in partner r51 applies directly to this actual residual crossing, with every pair variable and every other coefficient retained outside the cut:

`boxed:
 ||p_Q||infinity
 <=10.5501688311648/(sigma/4-eta),
}`                                                                  (4.7)

and the density is continuous on this paid branch.

A convenient completely numerical sufficient condition uses the live exact-singular scale `gamma>=7/96`. If

`boxed: ||F_H^(4)||op <= (7/768) sigma`,                            (4.8)

then

`eta<= (96/7)(7/768)sigma=sigma/8`,                                (4.9)

so (4.6) yields

`s3(C[I,J])>=sigma/8`,                                              (4.10)

and therefore

`boxed:
 ||p_Q||infinity
 <=84.4013506493182/sigma,
}`                                                                  (4.11)

with a continuous density.

This is an equation-level application of the latest completed designated fleet02/B07 result to the actual r43 coefficient state.

### Exact remaining alternatives on this subbranch

Consequently, after the r43 exact-singular reduction, a state with `rank R_C=3` can remain unpaid by (4.11) only if at least one of the following holds:

1. **anchored-C4 currency is relatively large:**
   `||F_H^(4)||op>(7/768) s3(R_C)`;
2. **the rank-three physical range is heavy:**
   `max_i(P_R)ii>1/12`;
3. the approximant has rank at most two (so `sigma=0`).

In the heavy case, the set

`K_R={i:(P_R)ii>1/12}`                                             (4.12)

has cardinality at most 35, since the leverages sum to `rank R_C=3`. This is only a localization statement; it does NOT assert that deleting `K_R` preserves three target eigenvalues or that `A[K_R,K_R]` is itself well-conditioned.

Thus the old `anchored C4 OR rank-three tail` debt is sharpened to an explicit three-way physical state:

`ANCHORED-C4-LARGE / <=35-ROW-HEAVY-RANK3-RANGE / PHYSICAL-RANK<=2-RESIDUAL`,

with the diffuse-small-C4 rank-three state paid continuously.

## 5. What is and is not closed

Theorem 2.1 gives a dimension-free determinant-weight selection principle for every actual physical E3 crossing: diffuse after heavy-coordinate deletion, or one complete pivot star carrying `>Z/972`. It is structural and does not by itself turn a tiny `Z` into a universal-scale crossing.

Theorem 3/4 advances the exact-singular r43 branch: a small anchored fourth-compound packet is not merely a rank-three tube in a sheared Schur coordinate. It makes the untouched residual physical principal block operator-close to rank at most three. The latest designated partner then pays the diffuse, nonweak rank-three portion with a literal physical E3 crossing and a continuous density.

The exact next B07 debts are:

`QFORM-C4-LARGE-OR-HEAVY-R3-OR-R2-RESIDUAL-RECEIVER-v1`: spend the relatively large anchored C4 packet, the <=35-coordinate heavy rank-three range, or the physical rank<=2 residual together with the exact-singular pair, without deleting nonzero tails;

and

`QFORM-PIVOTSTAR-COMPOUND-OVERLAP-ROUTER-v1`: apply the new complete pivot-star interface when global third-compound mass is forced into an overlap-one/two packet, preserving the determinant weights through conditioning.

Full unrestricted QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**; continuity is established only on the physical-E3 paid branches above.
