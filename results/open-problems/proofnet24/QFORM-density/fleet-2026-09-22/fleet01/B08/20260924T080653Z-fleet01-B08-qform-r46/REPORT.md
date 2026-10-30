SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-24T08:06:53Z.
attacking: the q=1/q=2 diffuse overlap packets by an aggregate shared-hub determinant-slice compiler, spending any off-diagonal leakage with the completed fleet02/B08 third-compound crossing theorem before any reciprocal minor selection.

# fleet01/B08 r46 — overlap-diagonalization cascade for the diffuse Pluecker survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING END-TO-END DIFFUSE ROUTER + EXACT NORMAL-FORM TUBES / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. Full-target continuity remains OPEN. Every density payment proved below has a continuous `C_0(R)` representative because it is obtained from the completed marginal-free physical-crossing theorem. No random-variable rotation, moment assumption, support regularity, Gaussianity, log-concavity, arbitrary-joint coarea, fiber supremum, pointwise law-uniform quadratic-phase decay, or Monte Carlo input is used.

## 1. Fresh state and exact dependencies


The incoming own result is r45:

`yspennstate/math-open-problems@3072b9b3222e7814b77d1293bb62810fbe177c15`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260924T064330Z-fleet01-B08-qform-r45/REPORT.md`.

For a selected genuine three-eigenvector frame

`A R = R Lambda`, `R^T R=I_3`, `min_j |lambda_j|>=L`,
`mu=max_i ||R_{i,*}||_2^2<=1/48`,

r45 proves either a continuous density bound `||p_Q||_infinity<=24/L`, or one overlap class `q in {1,2,3}` has banked third-minor currency. The product-preserving packet lower bounds inherited from fleet03/B07 are

`q=1: P1>4L^6/9375`,
`q=2: P2>L^6/384`,
`q=3: P3>2L^6/27`.

The q=3 branch was already reduced in the r45 addendum to either a continuous `<197.779/L` payment or a rank-two-per-bank tripartite carrier tube.

The completed designated-partner result actually applied here is fleet02/B08 r34,

`yspennstate/math-open-problems@3452feca9a3efbb5a716eb7453be7ae0433e463f`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/fleet02-B08-20260924T053906Z-r34/REPORT.md`.

Its marginal-free theorem says that for every literal ORIGINAL-coordinate crossing `B=A[S,T]`,

`||p_Q||_infinity <= 6^(4/3) e_3(BB^T)^(-1/6)`                 (1.1)

whenever the third compound is positive, retaining arbitrary same-side quadratic curvature, outside couplings, affine terms, signs and complementary spectrum. The resulting density is in `C_0(R)`.

The overlap-bank source is fleet03/B07 at

`yspennstate/math-open-problems@391688138f7f481a2c8688c2d27f9508db7af6af`.

All banks below are subsets of the original independent coordinates.

## 2. q=1 packet as a family of hub matrices

Let

`H,R1,R2,C1,C2`

be pairwise-disjoint original-coordinate banks. For a wing tuple

`w=(r1,r2,c1,c2) in R1 x R2 x C1 x C2`,                         (2.1)

write `R_w=(r1,r2)`, `C_w=(c1,c2)` and define the literal hub matrix

`M_w(h,k)=det A[{h,r1,r2},{k,c1,c2}],   h,k in H`.              (2.2)

Define

`P1=sum_w sum_(h in H) |M_w(h,h)|^2`,                            (2.3)

`Z1=sum_w sum_(h!=k in H) |M_w(h,k)|^2`.                         (2.4)

The diagonal energy `P1` is exactly the colored q=1 packet. Every term in `Z1` is a disjoint-third-minor (`q=0`): the row triple uses `h,R1,R2`, the column triple uses `k,C1,C2`, and for `h!=k` all six coordinates are distinct. Hence

`Z1<=E0(A)`.                                                       (2.5)

### Theorem 2.1 — `QFORM-Q1-HUBSLICE-DIAGONAL-OR-CROSS-v1`

For every `0<tau<=1`, one of the following holds.

**A. Physical-crossing payment.** If `Z1>=tau P1`, then some literal original-coordinate cut `S disjoint_union T=[n]` satisfies

`e_3(A[S,T]A[S,T]^T)>=tau P1/64`,                                (2.6)

and therefore

`boxed:
 ||p_Q||_infinity
 <=2*6^(4/3) (tau P1)^(-1/6),
 p_Q in C_0(R).
`                                                                       (2.7)

**B. Aggregate diagonal hub-slice tube.** Otherwise

`boxed:
 sum_w ||M_w-diag(M_w)||_F^2
 <tau sum_w ||diag(M_w)||_F^2=tau P1.
`                                                                       (2.8)

No individual wing tuple or hub is selected.

#### Proof

Only A needs proof beyond the definitions. Color every original coordinate independently into a Bernoulli half-cut `(S,T)`. A fixed ordered disjoint triple pair represented in `Z1` lands with its row triple inside `S` and column triple inside `T` with probability exactly `2^(-6)=1/64`. Therefore

`E e_3(A[S,T]A[S,T]^T)>=Z1/64>=tau P1/64`.                       (2.9)

Some actual physical cut attains at least the expectation. Apply the designated-partner theorem (1.1) to that actual crossing. Since `64^(1/6)=2`, (2.7) follows. QED.

### Numerical specialization to the r45 q=1 packet

Use the r45 lower bound

`P1>4L^6/9375`                                                   (2.10)

and choose

`tau=1/16`.                                                       (2.11)

Then branch A gives

`boxed: ||p_Q||_infinity<126.155/L, p_Q in C_0(R).`             (2.12)

Thus every still-unpaid q=1 state satisfies the strong dimension-free slice condition

`sum_w ||offdiag M_w||_F^2 < (1/16) P1`;                         (2.13)

i.e. the root-mean-square off-diagonal hub leakage is less than one quarter of the retained diagonal q=1 currency.

## 3. Exact adjugate normal form behind the q=1 tube

The q=1 tube has a useful denominator-free structural identity. For a wing tuple `w`, let

`B_w=A[R_w,C_w]`                                                  (3.1)

be the literal `2 x 2` wing crossing and define

`T_w=A[H,C_w] adj(B_w) A[R_w,H]`.                                (3.2)

Then `rank(T_w)<=2` and, entrywise for every `h,k in H`, expansion of the bordered determinant gives

`boxed:
 M_w=(det B_w) A[H,H]-T_w.
`                                                                       (3.3)

This identity is polynomial and remains valid when `B_w` is singular; no inverse or tiny-minor denominator appears.

Put

`D_w=diag(M_w)`, `F_w=M_w-D_w`.                                  (3.4)

Then exactly

`(det B_w) A[H,H]=D_w+T_w+F_w`.                                  (3.5)

Since the left side and `D_w` are symmetric, symmetrizing gives

`(det B_w) A[H,H]
 =D_w+(T_w+T_w^T)/2+(F_w+F_w^T)/2`,                              (3.6)

where the middle matrix has rank at most four and

`||(F_w+F_w^T)/2||_F<=||F_w||_F`.                                (3.7)

Let

`C4(H)={D+K: D physical diagonal on H, K=K^T, rank(K)<=4}`        (3.8)

and define the banked wing second-compound mass

`Delta2=sum_w |det B_w|^2`.                                      (3.9)

Because `C4(H)` is a cone, (3.6) implies the single-hub-block estimate

`boxed:
 Delta2 * dist_F(A[H,H],C4(H))^2
 <= sum_w ||F_w||_F^2=Z1.
`                                                                       (3.10)

Consequently every unpaid q=1 state with the choice (2.11) satisfies

`boxed:
 Delta2 * dist_F(A[H,H],C4(H))^2 < P1/16.
`                                                                       (3.11)

This is a genuine aggregate-before-inversion statement. If `Delta2` is appreciable, the entire physical hub block is forced near diagonal plus symmetric rank four; if `Delta2=0`, every mixed `2 x 2` wing determinant in the chosen product-preserving banks is exactly zero. No assertion that one `det B_w` is large is made.

## 4. q=2 packet: an overlap-diagonalization cascade

Now let

`H1,H2,R,C`

be pairwise-disjoint original-coordinate banks carrying a q=2 packet. Put

`K=H1 x H2`.                                                       (4.1)

For each `(r,c) in R x C`, define a matrix `N^(r,c)` on the pair index set `K` by

`N^rc[(h1,h2),(k1,k2)]
 =det A[{h1,h2,r},{k1,k2,c}]`.                                    (4.2)

Its diagonal energy is exactly

`P2=sum_(r,c) sum_(h1,h2) |N^rc[(h1,h2),(h1,h2)]|^2`.           (4.3)

Every off-diagonal entry falls into exactly one of three classes:

`Z0`: `h1!=k1` and `h2!=k2` (overlap zero),

`Z11`: `h1=k1` and `h2!=k2` (overlap one),

`Z12`: `h1!=k1` and `h2=k2` (overlap one).                       (4.4)

Thus

`sum_(r,c)||N^rc-diag(N^rc)||_F^2=Z0+Z11+Z12`.                   (4.5)

### Theorem 4.1 — `QFORM-Q2-OVERLAP-DIAGONALIZATION-CASCADE-v1`

Fix `0<tau2,tau1<=1`.

If

`Z0+Z11+Z12<tau2 P2`,                                           (4.6)

then the q=2 packet already lies in the **pair-index diagonal tube** (4.6).

Otherwise one of the following occurs.

1. **Direct q=0 payment:** `Z0>=tau2 P2/3`. Then an actual physical crossing pays

   `||p_Q||_infinity
    <=2*6^(4/3)(tau2 P2/3)^(-1/6)`, `p_Q in C_0`.               (4.7)

2. **Reduction to a q=1 packet:** one of `Z11,Z12` is at least `tau2 P2/3`. Suppose it is `Z11` (the other case is symmetric). Independently split the original bank `H2=U disjoint_union V` by fair coins. Every ordered pair `h2!=k2` is accepted with probability `1/4` as `h2 in U,k2 in V`. Hence some deterministic split gives the q=1 product-preserving packet

   `H=H1, R1=U, R2=R, C1=V, C2=C`

   with energy

   `boxed: P1' >= Z11/4 >= tau2 P2/12.`                         (4.8)

   Apply Theorem 2.1 to this actual packet with parameter `tau1`. Either it pays the full form continuously via

   `||p_Q||_infinity
    <=2*6^(4/3)(tau1 tau2 P2/12)^(-1/6)`,                       (4.9)

   or the resulting q=1 hub-slice family satisfies its aggregate diagonal tube

   `sum_w ||offdiag M_w||_F^2<tau1 P1'`.                         (4.10)

#### Proof

If (4.6) fails, one of the three nonnegative terms in (4.5) is at least one third of the total and hence at least `tau2 P2/3`. `Z0` consists of disjoint third minors, so the same Bernoulli-half-cut argument as in Theorem 2.1 gives (4.7). For `Z11`, the stated binary coloring of `H2` accepts each ordered overlap-one term with probability `1/4`; expectation gives (4.8), after which Theorem 2.1 applies. QED.

### Denominator-free identity for the q=2 diagonal tube

There is also an exact polynomial form. Let

`H=H1 union H2`, `a=A_rc`,
`K^(r,c)=a A[H,H]-A[H,c]A[r,H]`.                                 (4.11)

For pair indices `alpha=(h1,h2)`, `beta=(k1,k2)`, direct bordered-determinant expansion gives

`boxed:
 a * N^rc[alpha,beta]
 =det K^(r,c)[alpha,beta].
`                                                                       (4.12)

This remains valid at `a=0` because then `K^(r,c)` has rank at most one. Thus an unpaid q=2 diagonal tube is an exact statement that a family of mixed second compounds of rank-one corrections of the physical hub block is almost diagonal in the `H1 x H2` pair basis. No Schur inverse is introduced.

## 5. Explicit r45 q=2 constants

For the r45 packet

`P2>L^6/384`,                                                     (5.1)

choose

`tau2=tau1=1/16`.                                                (5.2)

If the direct `Z0` branch occurs, (4.7) gives

`boxed: ||p_Q||_infinity<112.072/L, p_Q in C_0.`                (5.3)

If an overlap-one off-diagonal class occurs, the binary split gives

`P1'>L^6/73728`.                                                  (5.4)

If that q=1 packet is not in its diagonal tube, the partner payment gives

`boxed: ||p_Q||_infinity<224.143/L, p_Q in C_0.`                (5.5)

Therefore every unpaid q=2 state is forced into either

- the q=2 pair-index diagonal tube with relative squared leakage `<1/16`, or
- a q=1 hub-slice diagonal tube with relative squared leakage `<1/16`.

## 6. New exhaustive diffuse overlap router

Combine r45 with Theorems 2.1 and 4.1 and the r45 q=3 addendum.

### Corollary 6.1 — `QFORM-DIFFUSE-OVERLAP-DIAGONALIZED-ROUTER-v1`

Assume a selected genuine three-eigenvector frame with

`min_j |lambda_j|>=L`, `max_i ||R_i||^2<=1/48`.                 (6.1)

Then either

`boxed:
 ||p_Q||_infinity<224.143/L,
 p_Q in C_0(R),
`                                                                       (6.2)

or at least one of the following three explicit product-preserving coefficient tubes occurs:

**Q1 tube.** Five disjoint original-coordinate banks `H,R1,R2,C1,C2` carry `P1>0` and matrices `M_w` satisfying

`sum_w ||offdiag M_w||_F^2<P1/16`,                               (6.3)

with the exact denominator-free adjugate normal form (3.3)-(3.11).

**Q2 tube.** Four disjoint original-coordinate banks `H1,H2,R,C` carry `P2>0` and the pair-index matrices `N^rc` satisfy

`sum_(r,c)||offdiag N^rc||_F^2<P2/16`,                           (6.4)

with the exact polynomial mixed-second-compound identity (4.12); or the q=2 packet has already reduced to a Q1 tube.

**Q3 tube.** Three disjoint original-coordinate banks carry the r45 rank-two-per-bank tripartite carrier: unless `<197.779/L` has already paid the form, every inter-bank block lies within `0.110252099L` of a common rank-two-per-bank carrier and the complete tripartite cross interaction lies within `0.220504198L` of rank at most six.

Thus after the marginal-free crossing theorem is fully spent, the remaining selected-three diffuse obstruction is no longer generic overlap mass. It is **overlap-diagonal carrier geometry**: q=1 is nearly diagonal in the shared-hub index, q=2 is nearly diagonal in the shared-pair index, and q=3 is confined to a fixed two-dimensional carrier on each physical bank.

This is not a proof of the unrestricted theorem; the next analytic step must consume these diagonal carrier tubes while retaining arbitrary same-bank quadratic curvature.

## 7. Exact constant check

Let `C3=6^(4/3)=10.902723556992836...`.

For q=1,

`2 C3 [(1/16)(4/9375)]^(-1/6)
 =126.15473068468918...`.                                        (7.1)

For the direct q=2 q=0 exit,

`2 C3 [(1/16)(1/3)(1/384)]^(-1/6)
 =112.07112713654548...`.                                        (7.2)

For q=2 -> q=1 -> q=0,

`P1'>(1/16)(1/12)(1/384)L^6=L^6/73728`,                         (7.3)

and therefore

`2 C3 [(1/16)/73728]^(-1/6)
 =224.14225427309097...`.                                        (7.4)

A deterministic algebra check also verified on random symmetric matrices that (3.3) and (4.12) hold to floating error; those checks are regression evidence only, not part of the proofs.

## 8. Correction and scope audit

- Every probabilistic partition is a partition of ORIGINAL independent coordinates.
- The deterministic matrices `M_w,N^rc`, adjugates and compounds are coefficient identities only; no transformed random variables are declared independent.
- Aggregate squared-minor mass is never converted to one universally good individual minor.
- The designated partner is applied only to an actual literal physical crossing.
- Same-side curvature, arbitrary affine terms and all complementary spectrum remain present on paid branches by the partner theorem.
- No pointwise stationary-phase estimate is used.
- No small coefficient matrix is deleted from an unbounded-input random quadratic form.
- The payments (2.12), (5.3), (5.5) and the r45 q=0/q=3 payments give continuous `C_0` densities. No continuity assertion is made inside the unpaid Q1/Q2/Q3 tubes.
- Full QFORM remains OPEN.

## 9. First unpaid implication

The next B08 target is

`QFORM-OVERLAP-DIAGONAL-CARRIER-RECEIVER-v1`:

> Consume the Q1/Q2/Q3 diagonal carrier tubes uniformly. For Q1, use the exact family `(det B_w)A_H = diagonal + rank<=2 + small offdiagonal` before selecting any wing minor; for Q2, classify or spend the nearly diagonal mixed second compound in (4.12); for Q3, fuse the two-dimensional-per-bank carrier with same-bank curvature. Any receiver must preserve the original-coordinate product law and retain arbitrary same-bank quadratic terms.

The most concrete next subcase is Q1 with appreciable aggregate wing second-compound `Delta2`: (3.11) then forces the shared physical hub block near a literal diagonal plus symmetric rank four, which can be intersected with existing diagonal-plus-low-rank Fourier receivers. The complementary `Delta2`-small branch is itself a rank-one mixed-wing geometry and should be attacked separately rather than by reciprocal minor selection.
