# Two hubs: a density bound for the four-eigenvalue obstructions

Notation as in "Quadratic forms with five large eigenvalues have bounded densities" (this folder's sibling
`five-eigenvalues-paper-2026-09-25/`): X in R^n has independent coordinates with densities at most one,
Q = X^T A X + b^T X + c, and for index sets S, T, A_{S,T} is the submatrix with rows in S and columns in T.

## The lemma

**Lemma (two hubs).** Let H = {h_1, h_2} and R = [n] \ H, suppose A_{H,H} = 0, and let
G = A_{H,R} A_{H,R}^T, a 2 x 2 matrix. If det G > 0, then for every b and c the density of Q is at most

    sqrt(2 pi e) * det(G)^(-1/4).

*Proof.* Since A_{H,H} = 0,
Q = V . X_H + X_R^T A_{R,R} X_R + b_R . X_R + c with V = 2 A_{H,R} X_R + b_H in R^2,
and V together with everything except V . X_H is a function of X_R. Given X_R, the variable V . X_H has density at
most 1/max(|V_1|, |V_2|) <= sqrt2/|V|: condition on the hub coordinate with the smaller coefficient, and the other
term has density at most 1/max|V_i|. Hence the density of Q is at most sqrt2 E|V|^{-1}. By Lemma 3.2(b), applied to
B = 2 A_{H,R}, whose rank is two, V has a density bounded by M = e (det 4G)^{-1/2} = e/(4 sqrt(det G)). Among
densities on R^2 bounded by M, the integral of |v|^{-1} is largest for M times the indicator of the disc of area
1/M centred at the origin, which gives E|V|^{-1} <= 2 sqrt(pi M). So the density of Q is at most
2 sqrt(2 pi M) = sqrt(2 pi e) det(G)^{-1/4}. []

The same argument with m >= 2 hubs and A_{H,H} = 0 gives the bound
sqrt(m) (m/(m-1)) (omega_m e^{m/2} 2^{-m} det(G)^{-1/2})^{1/m}, with omega_m the volume of the unit ball. One hub
is not enough: E|V|^{-1} diverges logarithmically on the line, and 2 U L, with U and L independent, has a
logarithmic singularity.

## What it covers

Remark 8.2 of the paper: two stars, the direct sum of two copies of [[0, w^T], [w, 0]] with w in R^N,
|w| = 1, N > 256. The centres form H, the hub block is zero, and G = I, so the density is at most
sqrt(2 pi e) < 4.14 for every b and c. The remark's Fourier argument gives 4 sqrt(e) < 6.60 and uses the
independence of the two stars.

Two stars sharing their leaves: A = e_1 w_1^T + w_1 e_1^T + e_2 w_2^T + w_2 e_2^T with unit vectors w_1, w_2
supported on the same N coordinates. When w_1 is orthogonal to w_2 the nonzero eigenvalues are 1, 1, -1, -1,
there is no pivot for N > 256, and every off-diagonal block A_{I,J} has rank at most two (each star contributes
the single row or the single column of its centre). This is a second four-eigenvalue matrix with no order-three
crossing in any partition, and the two summands 2 X_1 (w_1 . X) and 2 X_2 (w_2 . X) are dependent, so the argument
of Remark 8.2 does not apply. The lemma does: G = I and the density is at most sqrt(2 pi e). For hub rows at an
angle theta, det G = sin^2(theta) and the bound is sqrt(2 pi e)/sqrt|sin theta|.

`two_hub.py` checks both claims on centred uniform coordinates, N = 400, 10^6 samples per case: spectrum
{1, 1, -1, -1}, no pivot, largest cut rank two over 200 random partitions; empirical densities 2.48 (b = 0),
2.23 and 2.31 (affine terms on the hubs and on the leaves) against the bound 4.13, and 3.22 (theta = pi/6, bound
5.84) and 5.09 (theta = 0.1, bound 13.08). The growth as theta decreases is the one-hub logarithm appearing.

## Four eigenvalues: what is left

Every no-pivot matrix known so far with s_4(A) >= 1 and no partition with a large s_3(A_{I,J}) is a pair of stars
(disjoint or sharing leaves), and the lemma bounds all of them. A proof at four eigenvalues along these lines
would need two steps, both open.

1. A dichotomy. Without a pivot and with s_4(A) >= 1 (and s_5(A) < tau, since s_5(A) >= tau already gives
   270/tau by the five-eigenvalue theorem at scale tau), either some partition has s_3(A_{I,J}) >= c, or there are
   two coordinates H whose rows carry most of two eigen-directions, with |A_{H,H}| small and
   det(A_{H,R} A_{H,R}^T) >= g. The heavy rows are the natural candidates: no pivot forces a heavy row phi_h of the
   eigenvector matrix to have phi_h Lambda phi_h^T close to zero (a_hh is small although |phi_h|^2 is not), which is
   the signature of a star centre. Light rows alone give, for a random partition, Gram matrices close to half the
   light Gram matrix (matrix concentration), but the compression of Lambda to the light span can still lose rank,
   so the dichotomy is not just heavy against light.
2. A small but nonzero hub block. With A_{H,H} = B small, Q given X_R is a quadratic polynomial in X_H. Its
   critical point -B^{-1}V/2 carries a singularity of size about pi/sqrt(det B) (definite) or a logarithm
   (indefinite), but V has a density bounded by M, so the probability that the critical point falls where X_H has
   mass is about 4 M det B per unit area; the product is of order sqrt(det B) and suggests a bound uniform as
   B -> 0. Making this precise, with X_H of unbounded support, is the step to do first.

A worker who takes this up: search for counterexamples to step 1 before proving it (small no-pivot matrices with
s_4(A) >= 1 and the largest s_3(A_{I,J}) over partitions small, which are not two stars).
