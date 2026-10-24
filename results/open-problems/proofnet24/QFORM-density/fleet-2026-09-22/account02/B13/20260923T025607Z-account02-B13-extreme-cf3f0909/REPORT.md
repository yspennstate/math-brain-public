SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B13, 2026-09-23T02:56:07Z.
attacking: extremal-product transfer of the new cross-three-volume L3 theorem through the scalar Schur peel, with an original-matrix anchored-volume certificate.

# account02/B13 — L3-to-half-Riesz gluing and anchored four-volume scalar certificate

Programme: QFORM-DENSITY-3EIG-20260922
Role: Extremal product laws / complementary constructions and source-valid counterexamples
Status: PROVED SUPPORTING TARGET-LEVEL IMPLICATION; FULL QFORM OPEN; CONTINUITY SEPARATE
Execution: WITHOUT_VERIFIED_BRAIN

## 1. Sources and exact scope

The target is the full arbitrary-dimension statement for independent original-coordinate laws with densities 0<=f_i<=1 and a real symmetric A with at least three eigenvalues of absolute value at least one. No moment, support, connectedness, log-concavity, centering, identical-law, diagonal-basis, or post-rotation independence assumption is used below.

This run uses two completed inputs at their exact scopes.

1. Designated partner account03/B13, canonical math commit 3345697a0e1ea6c84ef3128a22917d49f0b0a826, path proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T013555Z-account03-B13-qform-r21/REPORT.md. Its theorem QFORM-CROSS-3VOLUME-L3-v1 says: for any real quadratic polynomial in independent cap-one original coordinates, if one disjoint physical cross block M has Z=e_3(M^T M)>0, then the output law has an L3 density and

    ||p||_3 < 6.787 Z^(-1/9).

All same-side quadratic terms, outside couplings and affine terms are arbitrary. The proof already transfers from bounded finite-union product indicators to all cap-one product laws by the account04/B13 finite-mixture purification, without an attained bathtub optimizer.

2. Claude/Fourier package at commit e5f71d79eff325201dd0274053d20268ce65b837, path proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md, Lemma 3 / one-coordinate completion. For a nonzero original scalar pivot a, completing the square gives a conditional density kernel bounded by |a|^(-1/2)|w|^(-1/2), uniformly in the conditioning-dependent translation. This preserves the actual independent coordinates.

The live corrections excluding law-uniform pointwise oscillatory decay, arbitrary-joint rank-three coarea, worst conditional projection moments, bounded-diameter localization, fixed fragment-count localization, and independence after rotation are not used.

## 2. General L3 to fractional-Riesz lemma

For a probability density p on R and 0<alpha<2/3 define

    H_alpha(p)=sup_s int_R |x-s|^(-alpha) p(x) dx.

### Lemma 2.1 — QFORM-L3-RIESZ-INTERPOLATION-v1

If ||p||_3<=M, then

    H_alpha(p) <= K_alpha M^(3 alpha/2),

where, with beta=2/3-alpha and

    A_alpha = [2/(1-3 alpha/2)]^(2/3),

one may take

    K_alpha = [(2/3)/beta] [beta A_alpha/alpha]^(3 alpha/2).

In particular

    H_{1/2}(p) <= 4(4/3)^(3/4) M^(3/4)
                 = 4.963225915211... M^(3/4),                 (2.1)

and

    H_{1/4}(p) <= 2.591795660268... M^(3/8).                  (2.2)

### Proof

Fix s and R>0. Holder with exponents 3 and 3/2 gives

    int_{|x-s|<=R} |x-s|^(-alpha)p(x)dx
      <= M [int_{|u|<=R}|u|^(-3alpha/2)du]^(2/3)
      = A_alpha M R^(2/3-alpha).

On the complement, probability normalization gives

    int_{|x-s|>R}|x-s|^(-alpha)p(x)dx <= R^(-alpha).

Therefore H_alpha is at most

    A_alpha M R^beta + R^(-alpha).

The minimizing radius satisfies R^(2/3)=alpha/(beta A_alpha M). Substitution gives the displayed K_alpha. No support radius or moment enters. QED.

This interpolation is scale-exact: under Y=sX, ||p_Y||_3=s^(-2/3)||p_X||_3 and H_alpha(Y)=s^(-alpha)H_alpha(X).

## 3. Apply the designated partner theorem: a half-Riesz cross-volume bound

Let R(Y) be any real quadratic polynomial in independent cap-one coordinates Y, and suppose a disjoint original-coordinate cross block M of its quadratic matrix satisfies

    Z=e_3(M^T M)>0.

By account03/B13,

    ||p_R||_3 < 6.787 Z^(-1/9).

Applying (2.1) gives

    H_{1/2}(R)
      < 4(4/3)^(3/4) 6.787^(3/4) Z^(-1/12)
      < 20.870 Z^(-1/12).                                    (3.1)

Similarly (2.2) gives the additional fractional certificate

    H_{1/4}(R) < 5.315 Z^(-1/24).                              (3.2)

This is an actual inequality-level use of the designated partner result. Because the partner L3 theorem was transferred from bounded finite-union indicators to arbitrary cap-one product laws by finite convex mixtures and L1 approximation, (3.1)-(3.2) inherit the same arbitrary fragmented/unbounded support scope. No global maximizer is assumed.

## 4. Scalar Schur gluing: an Linfinity theorem from cross three-volume

Let

    Q(x)=x^T A x+b^T x+c

with independent cap-one original coordinates. Choose an original coordinate i with

    a=A_ii !=0.

Write x=(u,y), and let r=A_{-i,i}, C=A_{-i,-i}. Completing the square in the ORIGINAL scalar u gives

    Q = a(u + a^(-1) r^T y + b_i/(2a))^2 + R(y),

where the quadratic matrix of R is the scalar Schur complement

    S = C - r r^T/a.                                          (4.1)

Conditional on Y=y, the shift of u changes neither its mass nor its density cap. The one-coordinate kernel from the pinned e5f package therefore gives, for a.e. t,

    p_Q(t) <= |a|^(-1/2) E |t-R(Y)|^(-1/2).                   (4.2)

Now choose disjoint sets I,J among the remaining original coordinates and put

    M=S[I,J],   Z=e_3(M^T M).

If Z>0, (3.1) and (4.2) yield the new target-level certificate

    ||p_Q||_infinity < 20.870 |a|^(-1/2) Z^(-1/12).           (4.3)

All other eigenvalues, signs, same-side quadratic terms, outside couplings and affine terms remain arbitrary. The proof conditions only on an original coordinate and never rotates the random vector.

The homogeneity is correct: scaling A,b,c by s>0 scales a and M by s, Z by s^6, and the right side of (4.3) by s^(-1), exactly the density scaling.

## 5. Remove the Schur inverse from the certificate: anchored four-volume

The apparent reciprocal pivot in (4.3) can be partially paid before inversion. For disjoint I,J subset [n]\{i}, define the anchored bordered four-volume

    W_i(I,J)
      = sum_{S0 subset I, |S0|=3}
        sum_{T0 subset J, |T0|=3}
          det A[{i} union S0, {i} union T0]^2.                 (5.1)

For every pair S0,T0, the block determinant identity gives

    det A[{i} union S0, {i} union T0]
      = a det( A[S0,T0] - A[S0,i]A[i,T0]/a )
      = a det S[S0,T0].                                       (5.2)

Hence, exactly,

    W_i(I,J)=a^2 e_3(M^T M)=a^2 Z.                            (5.3)

Substituting into (4.3) yields the inverse-free original-matrix form

    boxed:
    ||p_Q||_infinity < 20.870 ( |A_ii|^4 W_i(I,J) )^(-1/12). (5.4)

This is QFORM-ANCHORED4VOLUME-SCALAR-GLUE-v1.

The point is structural: one does not first pick a single tiny 4x4 minor and pay its reciprocal. W_i is the full squared four-volume of all bordered triples across the chosen physical cut. The Schur amplification 1/a is already accounted for by the exact identity (5.3).

Equivalently, any sequence of target instances whose output density norms diverge must satisfy, for every chosen nonzero diagonal pivot i and every disjoint cut I,J in its complement,

    |A_ii|^4 W_i(I,J) ->0                                     (5.5)

along any subsequence on which the density norms tend to infinity. Thus a bad no-pivot sequence is forced not only to have small scalar and pair pivots, but also to have vanishing anchored four-volume currency around every nonzero scalar pivot.

## 6. Geometric product-indicator form and valid transfer

For unit-measure measurable factor sets E_k and any interval J0 of length h, (5.4) implies

    |{x in product E_k : Q(x) in J0}|
       < 20.870 (|A_ii|^4 W_i(I,J))^(-1/12) h.                (6.1)

No E_k is assumed to be an interval, centered, bounded in diameter, or to have a bounded number of components.

Conversely, if (6.1) is first established only for bounded finite-union product indicators with the same constant uniformly in the sets, the account04/B13 no-attainment purification transfers it to arbitrary cap-one product densities with zero constant loss: approximate each marginal in L1 by a finite convex mixture of such indicators; expand the product as a finite convex mixture; use convexity of interval probabilities; then pass to the limit because product L1 error bounds total-variation error of the joint law and measurable pushforward contracts total variation. No attained global bathtub optimizer is needed.

For the singular Riesz functional itself, one may instead transfer the partner L3 estimate first by Minkowski plus weak L3 compactness, then invoke Lemma 2.1. This avoids any unjustified passage of an unbounded kernel under bare total-variation convergence.

## 7. What this closes and what remains

This run closes a precise part of the partner's unpaid implication QFORM-CROSS-3VOLUME-L3-TO-LINF-GLUING-v1: a genuine original-coordinate scalar curvature direction upgrades the product-preserving cross-volume L3 theorem to an Linfinity bound, and the resulting certificate can be written entirely in the original matrix through anchored four-volume.

It does NOT close the exact-null scalar branch A_ii=0, nor prove that the bare three-large-eigenvalue hypothesis forces |A_ii|^4 W_i(I,J) to be bounded below for some i,I,J. In the strict no-pivot regime scalar pivots can all be tiny or zero. The next unpaid implication is therefore:

QFORM-ANCHORED4VOLUME-OR-NULLCOLOOP-v1: in a normalized no-pivot matrix with three actual eigenvalues of modulus at least one, prove that either some nonzero scalar pivot has |A_ii|^4 W_i(I,J)>=c for a physical disjoint cut, or the matrix enters a quantitatively controlled exact/near-null coloop or hub/cross-volume branch; otherwise construct a genuine finite-grid product-law counterexample.

This is an aggregate-before-inversion statement. It is compatible with the live exact-null account02/B16 theorem and with the D'/D5 cross-volume machinery, but no such exhaustive structural alternative is proved here.

Full QFORM remains OPEN / NOT PROVED. Continuity of the full target remains separately OPEN.

## 8. Deterministic checks

A local deterministic checker tested the exact identity W_i=a^2 e_3(M^TM) on 100 random symmetric 9x9 matrices and fixed disjoint 4-by-4 cross banks; maximum absolute floating error was 1.14e-13. It also evaluates the constants K_{1/2}=4.963225915211... and 20.869999116381.... The proof above is analytic; the finite check is corroborating only.
