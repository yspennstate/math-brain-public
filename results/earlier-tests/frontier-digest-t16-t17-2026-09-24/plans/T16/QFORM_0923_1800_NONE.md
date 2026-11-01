# Plan: bounded density of quadratic forms with three large eigenvalues

## What the hypothesis buys

Three eigenvalues of modulus at least 1 force two of the same sign, and that is the real content. In the coordinate case two same-sign eigenvalues suffice: each X_i^2 has density at most s^{-1/2}, and the integral of ds/sqrt(s(t-s)) over [0,t] is pi, so X_1^2 + X_2^2 has density at most pi, and convolution with anything independent keeps that. One pair of opposite sign fails: x_1^2 - x_2^2 is a rotated 2 x_1 x_2, whose density has a logarithmic singularity. So the target is two same-sign eigenvalues of size at least 1, all others arbitrary.

## Where the difficulty is

If A had rank two, Q = l_1 Y_1^2 + l_2 Y_2^2 with Y = PX a rank-2 projection. The Rudelson-Vershynin projection bound bounds the density of Y, and an elliptical annulus has area pi eps / sqrt(l_1 l_2), so that case is done. The remainder W = sum over j >= 3 of l_j Y_j^2 breaks this: W depends on the complementary projection, which is not independent of Y, and conditioning on it destroys the product structure. A bounded density of the three-dimensional projection is not enough either once signs are mixed: a hyperboloid shell of width eps has infinite volume, and a bounded density can put all its mass there. The proof must use independence of the coordinates, not only bounds on projections.

## Known results to build on

- Ball's cube slicing and Bobkov-Chistyakov: a unit linear form has density at most sqrt 2. Rogozin's comparison with uniform variables.
- Rudelson-Vershynin, with sharp constants by Livshyts-Paouris-Pivovarov: k-dimensional projections have density at most C^k.
- The extreme points of {0 <= f <= 1, integral f = 1} are indicators of measure-one sets, so each X_i may be taken uniform on such a set.
- Bourgain-Tzafriri restricted invertibility and random coordinate sampling of matrices, to locate good coordinate blocks.
- Rudelson-Vershynin's compressible/incompressible split and Costello-Tao-Vu's quadratic Littlewood-Offord work, as models.

## What I would avoid

Decoupling by Cauchy-Schwarz squares the probability, so it gives eps^{1/2} and never a density bound. Carbery-Wright needs log-concavity and also stops at eps^{1/2}. The characteristic function need not be integrable (one uniform variable gives sinc), so Fourier methods can serve at most in a spread regime. CLT and Hanson-Wright steps are out: the X_i need have no moments.

## Strategy

Conditioning on some coordinates keeps the class and turns Q into an inhomogeneous quadratic; translations are free. So the inductive statement is about x^T A x + b^T x + c, and I would first check that this version is not false. Three regimes:

1. Local. A bounded block J with A_JJ already carrying two same-sign eigenvalues of size at least c. Condition on the rest; a finite-dimensional lemma finishes.
2. Linearizable. A pair J = {i,k} with a small 2x2 block, where A_{J,J^c} has two singular values of order one. Given X_{J^c}, Q is nearly a linear form in (X_i, X_k) with coefficient b = A_{J,J^c} X_{J^c}, so its density is about 1/|b|. E[1/|b|] is bounded, because b is a two-dimensional linear image with bounded density and 1/|y| is integrable in the plane. In one dimension it is not, which is the 2 x_1 x_2 example again.
3. Spread. The top eigenvectors are incoherent, so blocks see nothing and pairs give 1/|b| of order sqrt n. This is the expected core: condition on a random half of the coordinates, let the other half enter linearly through a high-dimensional coefficient, and control its quadratic remainder.

The linear-algebra question behind this: does every such A fall into one of the regimes with absolute constants?

## First concrete step

Prove the two-variable lemma: the density of a quadratic polynomial in two independent variables of density at most 1, bounded explicitly by its Hessian block and linear coefficient in the definite, indefinite and rank-one cases. In parallel, try to break the conjecture: compute the density on a rotated y_1^2 + y_2^2 - y_3^2, a delocalized rank-three form, and both with heavy-tailed multi-scale inputs (uniform on unions of intervals across scales), which the hypothesis allows.
