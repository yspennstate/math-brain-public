# r20 correction and genuine advance — compound-hub to explicit joint-star resources

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** `fleet03/B02`  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.

## 0. Correction to the first r20 report

After the first r20 derivation was saved, the worker-owned `LATEST.json` revealed a same-hour r19 addendum that had already proved a **strictly stronger** all-cross-minor theorem:

`yspennstate/math-open-problems@601f3b5a79ffc72be9e2ef68b8d23c679eebdf50`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T040049Z-fleet03-B02-qform-r19/ADDENDUM_BALANCED_CROSSMINOR.md`.

That earlier result is `QFORM-BALANCED-CROSSMINOR-ENTROPY-L1-v1` and gives

`||p_Q||_infinity <= (3e/sqrt(2)) delta_row^(-1/6) W3(B)^(-1/6)`,

which is stronger than the valid but weaker `3e` constant rederived in the initial r20 `REPORT.md`. Therefore **the initial r20 all-volume theorem is not counted as new progress**. The present addendum changes mechanism immediately and attacks the actual first unpaid implication recorded in r19's `STRUCTURAL_COROLLARY.md`.

No mathematical conclusion of the weaker r20 derivation is false; it is simply subsumed by the earlier same-worker theorem. This correction prevents double counting.

## 1. Inputs actually joined

### 1.1 Previous B02 structural residue

The r19 structural corollary at the same prior commit proves the following. For an arbitrary original-coordinate cross block `B=A[I,J]`, let

`Z=W3(B)=sum_(|R|=|S|=3) det(B[R,S])^2>0`

and let `w_(R,S)=det(B[R,S])^2/Z` be its canonical three-minor law. Define

`delta_r=P(R cap R'=empty)`,
`delta_c=P(S cap S'=empty)`

for iid minor pairs. If both are small, there exist a physical row triple `H` and physical column triple `L` such that

`P_w(R cap H != empty AND S cap L != empty) >=1-delta_r-delta_c`.    (1.1)

Thus almost all determinant-weighted three-volume passes through a fixed six-coordinate compound hub.

### 1.2 New fleet02/B02 joint-star compiler

The current independent B02 review/extension is

`yspennstate/math-open-problems@e8d024801adae701d47d58d85c41acb5b8ec4454`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T020523Z-fleet02-B02-QFORM-auto11-c1a7e2f4/REPORT.md`.

Its Lemma `QFORM-JOINT-STAR-BLOCK-COMPILER-v1` says: if a fixed physical row `i` and column `j` carry joint incident three-volume

`J_ij=sum_(R contains i,S contains j) det B[R,S]^2`,                  (1.2)

and after reindexing

`B=[[a,r^T],[c,N]]`,                                                 (1.3)

then, writing

`F_perp=||P_(c^perp) N P_(r^perp)||_F`,

one has

`sqrt(J_ij) <= |a| sqrt(E2(N)) + ||c|| ||r|| F_perp`.               (1.4)

This is an exact source-valid aggregate block compiler; it does not select one tiny minor.

## 2. New theorem: six-coordinate compound hub forces one explicit joint-star resource

### Theorem 2.1 — `QFORM-COMPOUND-HUB-TO-JOINT-STAR-RESOURCE-v1`

In the setup above, assume

`delta_r+delta_c<1`.

Then there exist an original physical row `i` and column `j` such that, in the decomposition (1.3),

`boxed{
max{ a^2 E2(N), ||c||^2 ||r||^2 F_perp^2 }
 >= [(1-delta_r-delta_c)/36] Z.
}`                                                                    (2.1)

In particular, if `delta_r,delta_c<eta<1/2`, then

`max{ a^2 E2(N), ||c||^2 ||r||^2 F_perp^2 }
 > [(1-2eta)/36] Z`.                                                  (2.2)

At the concrete threshold `eta=1/64`, one of the two resources is at least

`(31/1152) Z =0.0269097... Z`.                                       (2.3)

#### Proof

Take the hub triples `H,L` supplied by (1.1). Sum the incident masses over the nine anchor pairs:

`sum_(i in H,j in L) J_ij
 = Z E_w[ |R cap H| |S cap L| ]`.                                   (2.4)

On the event in (1.1), both intersection counts are at least one, so

`sum_(i in H,j in L) J_ij
 >=(1-delta_r-delta_c) Z`.                                           (2.5)

Therefore some one of the nine physical anchor pairs satisfies

`J_ij >=[(1-delta_r-delta_c)/9] Z`.                                 (2.6)

Apply (1.4). If both terms on its right were below `sqrt(J_ij)/2`, their sum would be below `sqrt(J_ij)`. Hence at least one term is at least `sqrt(J_ij)/2`; squaring and using (2.6) gives (2.1). QED.

This is the first direct compiler from the previous six-coordinate **incidence** witness to a quantitative matrix resource already recognized by the current Fourier fleet. It reduces the compound-hub residue to exactly two mechanisms: `physical edge x aggregate E2`, or `two stars x transverse Frobenius packet`.

## 3. Strict no-pivot consequence: edge branch amplifies residual E2

Suppose additionally that the full symmetric matrix is in the source's no-`tau`-pivot class:

`|A_kk|<tau` for every physical coordinate `k`,

and

`|det A[{k,l},{k,l}]|<tau` for every pair `k!=l`,                    (3.1)

with `0<tau<=1`. For the anchor pair `(i,j)`, `a=A_ij`. The pair determinant identity gives

`a^2 = A_ii A_jj - det A[{i,j},{i,j}]`,

hence

`boxed{ a^2 < tau^2+tau=tau(1+tau). }`                               (3.2)

Consequently, on the first branch of (2.1),

`boxed{
E2(N) >= [(1-delta_r-delta_c)/(36 tau(1+tau))] Z.
}`                                                                    (3.3)

At `tau=eta=1/64`, (3.3) becomes

`E2(N) > (992/585) Z =1.695726... Z`.                                (3.4)

Thus a strict no-pivot matrix cannot hide the compound-hub three-volume in a single moderately large edge: if the edge/E2 alternative fires, the complementary physical cross block is forced to carry **amplified aggregate second exterior volume**. This is precisely the resource targeted by the fractional-`E2` `L^3` Fourier theorem; its remaining marginal gate still has to be routed rather than silently assumed.

The second alternative in (2.1) is exactly the aggregate mixed-hub/two-star quantity proposed by fleet02/B02. It remains unpaid in full generality, but now receives a universal fraction of `Z` whenever both determinant-weighted disjointness parameters are small and the first alternative fails.

## 4. Exact anchored Schur identity (useful when a is nonzero)

For `a!=0`, set the rectangular cross Schur complement

`S=N-c r^T/a`.                                                       (4.1)

Every incident `3x3` minor satisfies

`det B[{i,k,l},{j,s,t}]
 = a det S[{k,l},{s,t}]`.                                            (4.2)

Therefore the entire joint incident mass has the exact aggregate form

`boxed{ J_ij=a^2 E2(S). }`                                           (4.3)

This identity is stronger than paying one selected incident minor. It says that the heavy joint star is literally a cross-edge coefficient times the full second exterior volume of a physical rectangular Schur packet. The analytic difficulty is not algebraic extraction anymore; it is to exploit (4.3) while retaining the original product provenance and arbitrary same-bank curvature.

Equation (4.3) follows either by direct block determinant expansion or from the Sylvester identity

`det(aN-cr^T)[{k,l},{s,t}]=a det B[{i,k,l},{j,s,t}]`.

## 5. Current proof map after this run

Combining r19 with Theorem 2.1 gives an explicit aggregate-before-inversion compiler for the `T^(0)` branch of the full spectral three-volume:

1. a random physical cut extracts `W3(B)>=T^(0)/64` from disjoint row/column triples;
2. if `delta_r` or `delta_c` is not small, r19's balanced-crossminor theorem gives a continuous `L1` Fourier density bound;
3. if both are small, the previous six-coordinate compound hub is now converted by (2.1) to one of **two explicit quantitative resources**, with no tiny-minor selection;
4. in a strict no-pivot branch, the edge/E2 resource further forces the amplified `E2` lower bound (3.3).

This is genuine progress on `QFORM-COMPOUND-HUB-OR-OVERLAP-COMPILER-v1`, but not its completion. The still-unpaid analytic transducers are:

- `QFORM-EDGE-E2-TO-L1-v1`: exploit the invariant product `a^2 E2(S)=J_ij` (or the lower bound in (2.1)) without requiring a large scalar diagonal pivot and while retaining arbitrary same-bank quadratic phases;
- `QFORM-TWOSTAR-TRANSVERSE-TO-L1-v1`: spend `||c||^2||r||^2 F_perp^2` by a dependence-safe mixed-Fresnel/graph-BL estimate;
- the overlap-one/two/principal compound-mass branches `T^(1)+T^(2)+T^(3)` remain to be joined to paid pivot/pair/principal-triple exits.

The full conjecture and target-wide `int|phi_Q|` criterion therefore remain OPEN.

## 6. Designated partner result retained

The designated fleet04/B02 zero-diagonal physical-triple theorem remains an actual completed input on its overlap:

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`.

The initial r20 report already combined its `L2` Fourier credit with the (valid, though non-new) all-volume high-frequency tail. That hybrid inequality remains correct, but it is not the principal new result of r20 after the duplicate was discovered. The principal new result is Theorem 2.1 plus the no-pivot amplification (3.3).
