SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-24T09:46:40Z.
attacking: triangle-crossing pivot cancellation: convert a macroscopic literal rank-two cross volume into adjugate Schur-star currency before any reciprocal scalar pivot, then isolate the near-singular/indefinite third-resource endpoint.

# account01/B09 r34 — adjugate-star exterior compiler for a physical rank-two crossing

## Status

**NEW SUPPORTING THEOREM / REQUIRED ACCOUNT02-B09 RESULT APPLIED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN.**

This run does not prove or disprove the unrestricted conjecture. It proves a dimension-free full-ambient density bound for every **definite literal physical pair** carrying nonzero aggregate rank-two cross volume. The theorem has no reciprocal scalar pivot and no `sigma_min(B)` loss. It converts the physical crossing produced in r33 into the polynomial-star currency paid by account03/B09 r47.

Execution remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval and actual mathematical receiver use occurred, but native learned-memory ingestion/restoration was not independently exposed.

## 1. Fresh sources and corrections consumed



Corrections actively enforced include:

- bounded input density does not imply law-uniform pointwise quadratic-phase decay;
- a rank-two cross minor alone is not a density theorem;
- the target does not force one uniformly usable scalar Schur pivot plus rank-two cross block;
- arbitrary rotations of source coordinates destroy independence;
- bounded joint density alone does not control an indefinite quadratic pushforward;
- worst conditional projection-height moments and naive fiber-sup integration are invalid;
- small matrix coefficients cannot be discarded as small random errors under arbitrary unbounded cap-one laws.

The direct predecessor is account01/B09 r33:

`yspennstate/math-open-problems@174f2ac95a7e63dc88172bc6fcf5b319e8613d44`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260924T081556Z-account01-B09-QFORM-auto11-r33/REPORT.md`.

Its theorem `QFORM-TRIANGLE-CYCLIC-CROSSING-v1` produces, in a rank-one fixed-hub packet, either a high-leverage literal leaf coordinate or a literal physical pair whose disjoint cross bank contains a macroscopic `2 x 2` determinant. The live correction says that crossing determinant is not by itself enough.

The completed receiver used here is account03/B09 r47:

`yspennstate/math-open-problems@fd800c8358502f8e947f77f47e06ac3e5fae1742`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260924T091232Z-account03-B09-QFORM-r47/REPORT.md`.

For a literal definite physical pair

`B=[[a,c],[c,b]]`

with outside arm rows `u,v`, it defines the polynomial star

`H_2=a v-c u`

and proves, with completely arbitrary remaining curvature,

`||p_Q||_infinity <= C_star ||H_2||_2^(-1/2)`,

`C_star=2^(5/4) pi sqrt(3)=12.941898654808462...`,

with the same coefficient in the linear interval bound. Interchanging the two original pair coordinates gives the same theorem with the other star `H_1=b u-c v`. Essential boundedness is proved; continuity is not separately asserted.

The designated account02/B09 theorem applied in Section 7 is `QFORM-JOINT-HUB-CAP-MIXEDFRAME-v1` from

`yspennstate/math-open-problems@2cce202879f9b0fa629f4fd1b464e271b11895c0`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260924T081042Z-account02-B09-QFORM/REPORT.md`.

## 2. First missing implication attacked

The r33 crossing theorem produces a real physical rank-two cross determinant, but a crossing alone cannot be converted to `L^infinity`. The first missing implication is therefore:

> Given a literal two-coordinate hub pair carrying a rank-two physical cross bank, can the cross volume be combined with the **pair itself** without selecting and dividing by a scalar pivot?

For a definite pair the answer is yes. The exact object is not a scalar Schur complement. It is the two-row **adjugate-star matrix**.

## 3. Exact exterior identity

Use two ORIGINAL independent coordinates `X,Y` and collect every remaining original coordinate into `Z`. Write

`Q = [X Y] B [X Y]^T + 2 X <u,Z> + 2 Y <v,Z> + Z^T C Z + affine`,

where

`B=[[a,c],[c,b]]`

and `C` is arbitrary symmetric. Put the physical pair-to-remainder cross matrix

`M = [u^T; v^T]`  (`2 x m`).

Define its rank-two physical cross volume

`Delta = sqrt(det(M M^T))
       = ( sum_{j<k} (u_j v_k-u_k v_j)^2 )^(1/2)`.

No selection of one minor appears in `Delta`.

Define the two polynomial-star rows

`H_1 = b u-c v`,
`H_2 = a v-c u`,

and assemble

`H = [H_1; H_2] = adj(B) M`.

### Theorem `QFORM-ADJUGATE-STAR-EXTERIOR-IDENTITY-v1`

For every pair of remainder coordinates `j<k`,

`det H[:,{j,k}] = det(B) det M[:,{j,k}]`.                         (3.1)

Consequently,

`det(H H^T) = det(B)^2 det(M M^T)`,                              (3.2)

and therefore

`max( ||H_1||_2, ||H_2||_2 )^2 >= |det B| Delta`.                (3.3)

#### Proof

The first identity is just multiplicativity of the `2 x 2` determinant:

`H[:,J]=adj(B) M[:,J]`,

so

`det H[:,J]=det(adj B) det M[:,J]=det(B) det M[:,J]`,

because for a `2 x 2` matrix `det(adj B)=det B`.

Sum the squares of (3.1) over `j<k` and use Cauchy--Binet on `H` and on `M` to obtain (3.2).

If `s_1,s_2` are the singular values of `H`, then

`||H||_F^2=s_1^2+s_2^2 >=2 s_1 s_2
          =2 sqrt(det(HH^T))
          =2 |det B| Delta`.

At least one of the two row norms squared is at least half the Frobenius norm squared. This is (3.3). QED.

The identity is source-coordinate exact. It uses no stochastic rotation and remains true with completely arbitrary same-remainder curvature `C`.

## 4. Full-ambient density theorem for a definite pair plus cross volume

### Theorem `QFORM-DEFINITEPAIR-CROSSVOLUME-STAR-COMPILER-v1`

In the setup above, assume the literal physical pair `B` is definite and `Delta>0`. Then the complete quadratic form `Q`, with arbitrary remaining curvature and arbitrary affine terms, has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_star ( |det B| Delta )^(-1/4),                              (4.1)
`

where

`C_star=2^(5/4) pi sqrt(3)=12.941898654808462...`.

Hence for every interval `I`,

`boxed:
 P{Q in I}
 <= C_star ( |det B| Delta )^(-1/4) |I|.                         (4.2)
`

Continuity is not claimed.

#### Proof

Since `B` is definite, both diagonal entries are nonzero and swapping `X,Y` preserves definiteness and the original product-law hypotheses. By (3.3), one of `H_1,H_2` has norm at least

`(|det B| Delta)^(1/2)`.

If it is `H_2`, apply account03/B09 r47 directly. If it is `H_1`, interchange the two literal original pair coordinates and apply the same theorem. In both cases

`||p_Q||_infinity
 <= C_star [max(||H_1||,||H_2||)]^(-1/2)
 <= C_star (|det B| Delta)^(-1/4)`.

The r47 theorem retains all of `C` and all affine terms, so no unproved perturbative deletion occurs. The interval bound follows from the density bound. QED.

### Why this is different from a scalar-pivot receiver

The paid currency is

`|det B| Delta`,

not `|a| sigma_min(cross)` and not `|det B| sigma_min(B)`. There is no division by either diagonal entry of `B`, and the whole physical cross bank is aggregated before any reciprocal power is paid.

Dimensional scaling is correct: `det B` and `Delta` each have coefficient scale squared, so `( |det B| Delta )^(-1/4)` has density scale `A^(-1)`.

## 5. Splice with the r33 triangle crossing

In the r33 rank-one fixed-hub geometry, a literal triangle in the low-disjointness branch supplies a cyclic physical pair `P_i={h,i}` and two disjoint leaf coordinates `j,k` such that

`|det M_i[:,{j,k}]| >= 0.202030... |lambda theta|`.

Therefore the aggregate cross volume of that pair obeys

`Delta_i >= 0.202030... |lambda theta|`.

If that pair is definite, equivalently `det B_i>0`, Theorem 4 gives

`boxed:
 ||p_Q||_infinity
 < 19.304 [ det(B_i) |lambda theta| ]^(-1/4),                    (5.1)
`

with the same coefficient times interval length. Thus a macroscopic cyclic crossing plus any non-negligible **positive pair determinant** is now an end-to-end paid branch.

The genuinely remaining triangle endpoint is consequently narrower:

- the useful cyclic pairs are indefinite (`det B_i<0`), or
- their positive determinants tend to zero, or
- the r33 alternative is a high-leverage literal coordinate.

This matches the new account03/B09 r47 boundary: the definite side is analytically regularized without a determinant denominator in the star theorem, while the indefinite side genuinely needs a third resource because a two-resource opposite-sign quadratic can retain a logarithmic singularity.

## 6. Singular face and exact qualitative endpoint

At `det B=0`, identity (3.1) says the two polynomial-star rows have rank at most one as a matrix, so Theorem 4 cannot be obtained by taking a limit of the exterior product. Nevertheless, a useful exact fact survives:

if `B` is nonzero singular and `Delta>0`, then `adj(B)M` cannot vanish identically. Indeed `adj(B)` has rank one and its kernel is the one-dimensional range of `B`; if every column of `M` lay in that kernel, `M` would have rank at most one, contradicting `Delta>0`. Hence at least one singular polynomial star is nonzero and the completed singular-star receiver applies with a finite law-specific bound.

No universal lower bound on that star follows from `Delta` alone without an additional scale resource; no such claim is made.

## 7. Required designated account02/B09 result applied to an actual target inequality

Apply `QFORM-JOINT-HUB-CAP-MIXEDFRAME-v1` to a fresh target-valid family.

Choose `m=8` literal independent leaf coordinates and flat orthonormal Walsh vectors `c,d,w in R^8`. For arbitrary independent cap-one source laws define

`Q_0
 = X_1^2+2X_1X_2+X_2^2
   +4X_1<c,Y>+4X_2<c+d,Y>
   +<w,Y>^2`.                                                     (7.1)

Make only the determinant-one **hub-only** shear

`U=X_1+X_2`, `V=X_2`.

The joint hub density is

`F_{U,V}(u,v)=f_1(u-v) f_2(v) <=1`,

and `(U,V)` remains independent of the original product leaf bank as a vector. Equation (7.1) becomes

`Q_0
 = U^2 + 4U<c,Y> + 4V<d,Y> + <w,Y>^2`.                         (7.2)

This uses no assertion that `U,V` are independent.

For Theorem 3.1 of account02/B09, take `h=2`, `r=1`, `lambda=1`, `M=1`. The mixed rows are

`rho_i=(w_i,2c_i,2d_i)`,

so

`G=diag(1,4,4)`, `det G=16`,

and every normalized physical-leaf leverage is

`w_i^2+c_i^2+d_i^2=3/8 <=1/2`.

Thus `alpha=5/2` and the account02 theorem gives a **continuous** density with

`boxed:
 ||p_{Q_0}||_infinity
 <= (5/3) 2^(2/5)
 = 2.1991798512881573... .                                      (7.3)
`

Therefore

`boxed:
 P{Q_0 in I}
 <= 2.199180 |I|                                                 (7.4)
`

for every interval `I`. There is no probability squaring or square-root small-ball loss.

### Target certificate

The `w` direction is an exact eigenvector with eigenvalue `1`. The compression of the original physical matrix to `span{e_1,c}` is

`[[1,2],[2,0]]`,

whose eigenvalues are

`(1+sqrt(17))/2 >1`,
`(1-sqrt(17))/2 <-1`.

By Cauchy interlacing, the full symmetric matrix has an eigenvalue at least `(1+sqrt17)/2` and one at most `(1-sqrt17)/2`; together with the exact `w` eigenvalue `1`, it has at least three eigenvalues of absolute value at least one. Hence (7.3) is an actual inequality inside the owner's full target class.

## 8. Independent target-valid check of the new theorem

Take

`Q_* = 2X^2+2Y^2+4XZ_1+2YZ_2`.

Here

`B=diag(2,2)`, `det B=4`,

`M=diag(2,1)`, `Delta=2`.

The new theorem gives

`||p_{Q_*}||_infinity
 <= C_star 8^(-1/4)
 = pi sqrt(6)
 = 7.695298980971184...`,                                        (8.1)

and the same coefficient times interval length.

The spectrum is

`{1+sqrt5, 1-sqrt5, 1+sqrt2, 1-sqrt2}`,

so exactly three eigenvalues have modulus greater than one. This is again a genuine target instance. Continuity is not asserted by (8.1).

## 9. Deterministic verification

A seeded 1000-instance algebra regression checked, for random symmetric `B` and random `2 x 5` cross matrices `M`, every identity

`det((adj B M)[:,J]) = det(B) det(M[:,J])`.

The maximum floating-point discrepancy was `1.43e-14`. The aggregate Cauchy--Binet identity

`sqrt(det(HH^T)) = |det B| sqrt(det(MM^T))`

was verified to maximum discrepancy `1.74e-13`.

Exact constants checked:

`C_star = 12.941898654808462...`,

`C_star * 8^(-1/4) = pi sqrt(6) = 7.695298980971184...`,

`(5/3)2^(2/5)=2.1991798512881573...`.

These numerical checks support only the exact algebra and arithmetic; the proof is the identities above plus the cited completed receivers.

## 10. What is and is not closed

Closed in this run:

1. A literal **definite** physical pair plus aggregate rank-two cross volume is paid end to end with arbitrary remainder curvature.
2. The r33 triangle crossing is paid whenever its chosen physical pair has non-negligible positive determinant.
3. The designated account02 joint-hub mixed-frame theorem is applied to an actual full-target inequality with continuous density and an `O(|I|)` bound.

Not closed:

- a macroscopic triangle crossing whose relevant pair is **indefinite**;
- quantitative passage through a positive determinant tending to zero when the star is simultaneously tiny;
- the high-leverage literal-coordinate alternative from r33;
- the unrestricted QFORM conjecture and full-target continuity.

The exact next debt is

`QFORM-INDEFINITE-CROSSING-THIRD-RESOURCE-COMPILER-v1`:

retain, in original coordinates, a genuine third spectral/crossing resource jointly with the logarithmic indefinite pair, or prove that the near-singular/high-leverage cancellation routes into an already-paid mixed-frame, singular-star, grouped-crossing, finite-core, or principal-triple receiver. A cross minor by itself must not be promoted to a density theorem.
