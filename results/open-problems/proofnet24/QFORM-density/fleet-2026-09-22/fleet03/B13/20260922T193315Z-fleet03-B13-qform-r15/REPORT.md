SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B13, 2026-09-22T19:33:15Z.
attacking: the rank-one physical-pair branch in original product coordinates, seeking a sharper aggregate determinant-mass estimate and then transferring the extreme-product inequality to every cap-one product law.

# fleet03/B13 — rank-one pair, original-pivot smoothing, and exact extreme-product transfer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T193315Z-fleet03-B13-qform-r15`  
**Assignment:** Extremal product laws  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING FULL-MATRIX BRANCH PROVED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Source-corrected target

The full target remains open: for every dimension, every product law of independent real coordinates with one-dimensional densities at most one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal essential-supremum bound for the density of `Q=X^T A X`, or give a valid counterexample. Continuity is tracked separately.

This run uses none of the refuted arbitrary-joint rank-three coarea bound, normalized conditional-projection positive moments, scalar-rest conditional supremum, pointwise law-uniform Fresnel decay, one-good-minor extraction, bounded-support localization, or finite-fragment extremality.

The designated partner result actually applied is fleet04/B13's exact fixed-volume random-set representation and continuity-transfer theorem:

`yspennstate/math-open-problems@722a87d180720473e3c3e08010d62caedf298484:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260922T171018Z-b13-fixed-volume-mixture-r4/REPORT.md`.

It proves that every cap-one one-dimensional density of mass one is an exact barycenter of indicators of arbitrary unit-measure sets, independently across coordinates. Therefore any uniform interval-small-ball inequality proved for all product indicators transfers with exactly the same constant to every admissible product density. No connectedness, bounded diameter, bounded support, or fragment-count hypothesis is introduced.

A compatible completed peer result used for comparison is fleet01/B16's rank-one physical-pair theorem:

`yspennstate/math-open-problems@2010f649637870b226dafc2d54791819c4cb2aaa:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/20260922T190433Z-fleet01-B16-QFORM-auto11/REPORT.md`.

That theorem gives `18*2^(1/3)(|lambda| eta^2)^(-1/3)` for a rank-one physical pair. The new theorem below is complementary and improves the reciprocal exponent in the broad regime where the nonzero pair eigenvalue is not tiny relative to its transverse cross-bank norm.

## 2. One-dimensional extremal kernel lemma

If `f` is a probability density with `0<=f<=1`, then for every `s in R`,

`int f(y) |s-y|^(-1/2) dy <= 2 sqrt(2)`.

This is the exact bathtub bound: the even decreasing kernel is maximized by filling the interval of length one centered at `s`, and

`int_{-1/2}^{1/2} |y|^(-1/2) dy = 2 sqrt(2)`.

More generally, if `Y` has density cap `K`, then

`E |Y-s|^(-1/2) <= 2 sqrt(2K)`                                      (2.1)

uniformly in the translation `s`.

## 3. Original-pivot rank-one pair theorem

Let `I={i,j}` be two original coordinates. Write the physical pair and its cross block as

`P=A[I,I]=[[a,b],[b,c]]`,

`C=A[I,I^c]=[p^T; q^T]`.

Assume `rank(P)=1` and choose a nonzero physical diagonal pivot `a=A_ii`. Then necessarily

`c=b^2/a`.

Define the product-coordinate transverse cross vector

`w := q - (b/a) p`.

### Theorem 3.1 — `QFORM-RANK1-ORIGINAL-PIVOT-SMOOTHER-v1`

If `w!=0`, then for arbitrary independent cap-one input densities and arbitrary complementary matrix `A[I^c,I^c]`,

`boxed( ||p_(X^T A X)||_infinity <= 2^(11/4) (|a| ||w||_2)^(-1/2). )`   (3.1)

The same statement survives an arbitrary deterministic affine term in the full quadratic polynomial. Essential boundedness is proved; continuity is not claimed.

### Proof

Condition on `Z=X_(I^c)=z`, and abbreviate

`u=p dot z`, `v=q dot z`, `R= z^T A[I^c,I^c] z`.

For the two remaining original independent coordinates `x=X_i`, `y=X_j`,

`Q_z(x,y)=a x^2+2bxy+c y^2+2ux+2vy+R`.

Since `c=b^2/a`, complete the square only in the ORIGINAL coordinate `x`:

`Q_z(x,y)
 = a (x+(b/a)y+u/a)^2
   +2(v-(b/a)u)y
   +R-u^2/a.`                                                       (3.2)

Put

`delta(z)=v-(b/a)u = w dot z`.

For fixed `(y,z)`, the shifted square `a(X_i+h)^2` has density bounded by

`|a|^(-1/2) |t|^(-1/2)`

at distance `|t|` from its vertex. Averaging over the independent `Y=X_j` and applying the exact bathtub lemma to the coefficient `2 delta(z)` gives, for almost every `z` with `delta(z)!=0`,

`||p_(Q|Z=z)||_infinity
 <= |a|^(-1/2) sup_s int f_j(y)|s-2 delta(z)y|^(-1/2)dy`

`<= 2 (|a| |delta(z)|)^(-1/2).`                                     (3.3)

Now `delta(Z)=w dot Z` is a linear form in genuinely independent original coordinates. The Rogozin--Ball one-dimensional projection bound used throughout the current QFORM programme gives

`||p_delta||_infinity <= sqrt(2)/||w||_2.`                            (3.4)

Applying (2.1) with `K=sqrt(2)/||w||_2`,

`E |delta|^(-1/2)
 <=2 sqrt(2 sqrt(2)/||w||_2)
 =2^(7/4)||w||_2^(-1/2).`                                            (3.5)

Average (3.3) over `Z`:

`||p_Q||_infinity
 <=2 |a|^(-1/2) E|delta|^(-1/2)
 <=2^(11/4)(|a| ||w||_2)^(-1/2).`

The right side is finite, so the same disintegration proves absolute continuity. A deterministic affine term only translates `delta(Z)` and the square vertex, and both bounds are translation-uniform. QED.

The proof never rotates the input pair and therefore retains genuine independence at the only place it is needed. This is the point at which it improves on a rotation-invariant curve estimate.

## 4. Coordinate-free form and determinant mass

Let `lambda!=0` be the nonzero eigenvalue of `P`, let `u=(u_i,u_j)` be its unit eigenvector, and let `n=(-u_j,u_i)` be the unit null vector. Put

`eta := ||C^T n||_2`.

Choose the physical pivot so that `|u_i|>=1/sqrt(2)`. Then

`a=lambda u_i^2`,

`C^T n = u_i w`,

and hence

`|a| ||w||_2 = |lambda| |u_i| eta >= |lambda| eta/sqrt(2).`           (4.1)

Therefore (3.1) yields the invariant branch bound

`boxed( ||p_Q||_infinity <= 8 (|lambda| eta)^(-1/2). )`               (4.2)

For every `k notin I`, an orthogonal change inside the two-dimensional pair shows

`det A[I union {k}] = -lambda (n^T C e_k)^2`.

Thus the total principal-triple determinant mass is exactly

`M_I := sum_(k notin I) |det A[I union {k}]|
     = |lambda| eta^2.`                                               (4.3)

Equation (4.2) is equivalently

`boxed( ||p_Q||_infinity <= 8 |lambda|^(-1/4) M_I^(-1/4). )`          (4.4)

This pays the whole transverse bank before any reciprocal individual triple determinant. The checker verifies (4.1)--(4.3) exactly on a rational test packet and records `QFORM_B13_R15_CHECK_PASS`.

## 5. Exact application of the designated fleet04/B13 extremal-law theorem

First take every input density to be an indicator `1_(E_k)` of an arbitrary measurable set with `|E_k|=1`. Sections 2--4 give, for every interval `J`,

`P_E{Q in J} <= 8 (|lambda| eta)^(-1/2) |J|`                          (5.1)

under the rank-one-pair hypotheses. The sets `E_k` may be unbounded and infinitely fragmented.

Now apply fleet04/B13's fixed-volume product-mixture representation to arbitrary cap-one product densities. Each product component satisfies the SAME matrix-dependent inequality (5.1), so Tonelli gives

`P_f{Q in J}
 = int P_E{Q in J} dnu(E)
 <=8 (|lambda| eta)^(-1/2)|J|.`                                      (5.2)

Thus the extreme-product geometric inequality transfers with zero constant loss. This is an actual use of the designated partner theorem, not merely a citation to it.

Continuity does NOT follow from the partner's continuity-transfer clause here because the present branch has only established essential boundedness for each extreme component, not a uniform continuous representative.

## 6. Hybrid with the completed rank-one pair theorem

Fleet01/B16 supplies

`||p_Q||_infinity <=18*2^(1/3)(|lambda| eta^2)^(-1/3).`               (6.1)

Combining (4.2) and (6.1) gives the strictly no-worse hybrid

`boxed(
 ||p_Q||_infinity <= min{
   8(|lambda|eta)^(-1/2),
   18*2^(1/3)(|lambda|eta^2)^(-1/3)
 }.
)`                                                                    (6.2)

The new branch is numerically smaller whenever

`eta/|lambda| <= (18*2^(1/3)/8)^6
               = 518.9853515625.`                                    (6.3)

The point is not this generous numerical threshold; structurally, the reciprocal determinant-mass exponent is reduced from `1/3` to `1/4` whenever the physical rank-one scale is retained.

## 7. Relation to the full target and next unpaid implication

Together with the preceding B13 zero-pair result, the low physical-pair ranks now have two aggregate-before-inversion mechanisms:

- rank zero physical pair: a rank-two cross-bank Gram determinant pays the density directly;
- rank one physical pair: the transverse cross bank pays by (4.2)/(4.4), with the hybrid fallback (6.1).

This still does NOT prove that the bare hypothesis `s_3(A)>=1` supplies one rank-zero or rank-one pair with a universally favorable aggregate. Nor does it close an invertible near-singular pair. The full QFORM conjecture and full continuity statement remain OPEN.

The next target-relevant implication is therefore:

`QFORM-PAIR-RANK-STRATIFIED-AGGREGATE-EXHAUSTION-v1`:
from the current overlap / grouped-coordinate geometry under `s_3(A)>=1`, prove that either a rank-zero/rank-one physical pair has one of the aggregate invariants above at universal scale, or dispersion of all such invariants forces an already-paid diffuse/ridge/grouped-bank branch, without selecting one tiny principal minor first.

This is the required structural bridge to the full theorem; it is not assumed here.
