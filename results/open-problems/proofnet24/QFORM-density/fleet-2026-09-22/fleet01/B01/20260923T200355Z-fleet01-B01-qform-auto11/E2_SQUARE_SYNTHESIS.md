# Scalar-square plus row-gate-free E2 synthesis

Status: **PROVED SUPPORTING COROLLARY; FULL QFORM OPEN**.

This note combines the current fleet02/B06 row-gate-free E2 half-Riesz theorem with the source-valid scalar-square peel. It is useful precisely when a physical scalar pivot may be small but a rank-two residual cross packet is large enough to compensate.

## Theorem — `QFORM-SCALAR-SQUARE-PLUS-E2-v1`

Let `X_0` be one original coordinate with density at most one, and let `Y` denote all remaining original independent coordinates. Suppose, after exact completion of the `X_0` coordinate,

`Q = a (X_0+h(Y))^2 + R(Y)`, `a!=0`.                              (1)

No independence between `h(Y)` and `R(Y)` is required. Let `I,J` be disjoint original-coordinate banks inside `Y`, and let

`M=A_R[I,J]`,
`Z=e_2(M^T M)>0`.                                                   (2)

Then

`boxed:
 ||p_Q||_infinity
 <= 8 e^(1/4) |a|^(-1/2) Z^(-1/8).`                               (3)

This is an essential-supremum statement. Continuity is not asserted by this argument.

## Proof

The row-gate-free E2 theorem proved in fleet02/B06, canonical report

`yspennstate/math-open-problems@c2ce876df8b5483a00802170001d4144bb4cdbfa:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260923T192839Z-auto11/REPORT.md`,

gives for the full residual `R`, retaining arbitrary same-bank quadratic curvature, outside couplings and affine terms,

`H_(1/2)(R):=sup_s E|R-s|^(-1/2)
 <= 8 e^(1/4) Z^(-1/8).`                                         (4)

Condition on `Y`. Translation of `X_0` by `h(Y)` preserves the cap-one density bound. For either sign of `a`, the conditional density of `a(X_0+h)^2` is bounded by

`|a|^(-1/2)|u|^(-1/2)`                                           (5)

on the appropriate half-line. Therefore, for every output level `s`,

`p_Q(s)
 <= |a|^(-1/2) E|s-R(Y)|^(-1/2)
 <= |a|^(-1/2) H_(1/2)(R)`.                                     (6)

Insert (4) to obtain (3). QED.

The proof does not use pointwise scalar Fresnel decay. It uses a direct distribution-function / square-density kernel after the two-bank E2 geometry has already been aggregated.

## Strict no-pivot scaling family

Let `epsilon in (0,1]`, let `m` be large, and let `R,S` be `m x 2` matrices with orthonormal columns and flat entries of magnitude `m^(-1/2)`. Use one original scalar coordinate `X_0` and two disjoint `m`-coordinate banks. Set the scalar coefficient

`a=epsilon`,

and take the residual cross block

`M=epsilon^(-1) R S^T`.                                           (7)

The two nonzero singular values of `M` are both `epsilon^(-1)`, so

`Z=e_2(M^TM)=epsilon^(-4)`.                                       (8)

Hence (3) gives the uniform bound

`boxed:
 ||p_Q||_infinity
 <= 8 e^(1/4) epsilon^(-1/2) epsilon^(1/2)
 = 8 e^(1/4)
 = 10.2722033335... .`                                             (9)

The symmetric residual block `[[0,M],[M^T,0]]` has four nonzero eigenvalues `+epsilon^(-1),+epsilon^(-1),-epsilon^(-1),-epsilon^(-1)`, so the target spectral hypothesis is satisfied for `epsilon<=1`. Every leaf diagonal is zero, the scalar diagonal is `epsilon`, and every physical cross entry is at most `2/(epsilon m)`. Therefore every physical `2x2` principal determinant can be made arbitrarily small by first taking `epsilon` small and then `m` much larger than `epsilon^(-2)`. This is a genuine aggregate-before-inversion branch rather than a uniformly good physical pair.

## Relation to the main run theorem

`QFORM-SCALAR-SQUARE-PLUS-E2-v1` and `QFORM-ONEHUB-TWOBANK-GENERAL-BILINEAR-SCHUR-L4-v1` are complementary.

- The E2-square theorem allows an arbitrary-size cross bank and needs an actual nonzero original scalar square after completion; it pays only aggregate two-volume `Z`.
- The Schur-L4 theorem can work even when the original hub diagonal `a` is zero, because bank self-curvature and unequal hub couplings can create a nonzero exact slope-kernel curvature `d_B`.

Thus a near-singular transverse state is now paid either by scalar-square plus aggregate E2 currency, or by a two-bank invertible cross packet with nonzero slope-kernel curvature. The remaining endpoint is simultaneous loss of these currencies: no usable scalar square/E2 product and a singular or nearly singular two-bank cross, or simultaneous vanishing of both product-preserving kernel curvatures.
