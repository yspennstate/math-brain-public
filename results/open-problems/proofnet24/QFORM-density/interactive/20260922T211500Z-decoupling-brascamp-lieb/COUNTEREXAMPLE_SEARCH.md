# Counterexample search and three proved bounds

Programme QFORM-DENSITY-3EIG-20260922. Notation: X independent with densities <= 1, p the density of
Q(X) = X^T A X, V the span of eigenvectors with |lambda| >= 1, P the projection onto range(A).

## Outcome

No counterexample. No tested family has a peak density that grows with n or with any parameter; every
attack lowered the density. Largest value in the conjecture's class: about 4.14 (Hadamard rank-3 form,
n = 64, uniform laws), below the Gaussian limit 3 sqrt(2) ~ 4.2426.

## Proved

1. Fibre identity. For a.e. s, p(s) = sum_i E_{X_{-i}} [ sum over roots t of Q(t, X_{-i}) = s of
   f_i(t) |d_i Q| / |grad Q|^2 ] (partition of unity (d_i Q)^2/|grad Q|^2 and one-dimensional coarea
   along each coordinate). It is also the bin-free estimator used for all numerics.
2. Theorem A (all |eig(A)| >= sigma, linear terms allowed): p <= (n/sigma)(d/(d-1)) kappa_d^{1/d},
   d = n - 1; for n = 3, p <= 6 sqrt(pi)/sigma. Localized regime: if a principal 3x3 block has all
   |eig| >= c, then p <= 6 sqrt(pi)/c (condition on the other coordinates, apply Theorem A with n = 3).
3. Theorem B (three eigenvalues >= 1, any n): p <= 2 sqrt(2 pi) sum_i |P e_i| (<= 5.01 n; <= 8.68 sqrt(n) for
   rank 3). Proof: |grad Q| >= 2|P_V x|; choose orthonormal w_1, w_2 in V with i-th coordinate zero, so
   W_i = (<w_1,X>, <w_2,X>) does not involve X_i; |d_i Q| <= |P e_i| |grad Q|; W_i has density <= 2 and
   the bathtub principle gives E|W - w|^{-1} <= 2 sqrt(2 pi). So a counterexample needs n -> infinity and
   sum_i |P e_i| -> infinity (eigenvectors spreading over more and more coordinates).
4. Theorem C (ruled level sets, dimension-free; linear terms in the range of A only, since a component
   outside the range adds a fourth coordinate). For Q = lambda_1 <r_1,X>^2 + lambda_2 <r_2,X>^2
   - mu <r_3,X>^2 with lambda_1, lambda_2, mu >= 1 and every s >= 0,
      p(s) <= (lambda_1 lambda_2 mu)^{-1/2} integral_0^{2 pi} dtheta / sqrt(sin^2 theta/lambda_1 + cos^2 theta/lambda_2 + 1/mu)
           <= pi sqrt(2).
   After rescaling, {Q = s} is a one-sheet hyperboloid (the cone at s = 0), which is doubly ruled. In the
   ruling parametrisation y = sqrt(s) e_theta + t (e_theta^perp + e_3) the coarea measure delta(Q - s) dy is
   exactly (1/2) d theta dt, so p(s) is an average over theta of line integrals of the three-dimensional
   density along the rulings. A line integral of the density of Y = (<r_k, X>) is a value of a
   two-dimensional marginal density of the product measure, hence <= 2 (Ball; Livshyts-Paouris-Pivovarov).
   For (1,1,-1) this is an identity, p(s) = (pi/sqrt 2) avg_theta rho_theta(sqrt(s) e_theta), checked
   numerically against the fibre estimator (Hadamard n = 8, s = 0.02, 0.1, 0.3: 3.475/2.290/0.775 against
   3.473/2.289/0.774). On the one-sheet side the sharp constant lies in [3 sqrt 2, pi sqrt 2]. What stays
   open for rank three is the convex side: definite forms and the two-sheet side s < 0, where shells are
   not excluded by bounds on line integrals.
5. Rank-2 positive semidefinite forms: p <= pi ||f_Y||_inf / sqrt(lambda_1 lambda_2) <= 2 pi / sqrt(lambda_1 lambda_2),
   sharp (attained as s -> 0+ by ((X1+X2)^2 + (X3+X4)^2)/2). Hence the stronger statement "two same-sign
   eigenvalues >= 1 suffice" needs a constant >= 2 pi; nothing tested exceeded 2 pi.

## Heuristic (Edgeworth near 3 sqrt 2)

p(0) = 3 sqrt(2) {1 + sum_i (kappa_4,i/(24 sigma^4)) |v_i|^4 g(c_i) + ...}, g(c) = (57 + 6c^2 - 39c^4)/32 in
[3/4, 1.79]; uniform laws have kappa_4/sigma^4 = -6/5, so the correction is negative, and any other law has
variance above 1/12 and loses at leading order. Hadamard forms, uniform laws: predicted 3.43/3.84/4.04/
4.14/4.19 against measured 3.32/3.87/4.04/4.13/4.14 at n = 4/8/16/32/64.

## Numerics (scripts and raw outputs in the programme scratch folder)

- Estimator reproduces pi, 2 pi sqrt(s) and the log singularity of X1^2 - X2^2 (rising by ln 10 per decade).
- Adversarial optimiser: p is multilinear in the laws, so the best response in each coordinate is the
  indicator of the top measure-one set of its partial density; alternating best responses with
  Nelder-Mead over eigen-subspaces and random multi-interval starts (about 40 local optimisations,
  n <= 16).
- Peaks: n = 3 diagonal pi, rotated 2.5-2.7, bathtub starts converge to unit intervals; n = 4 Hadamard 3.32;
  n = 4-8 subspace search 3.52-3.87; n = 6 pair-sum block 4.078 +- 0.008 (histogram extrapolation 4.07);
  n = 64 Hadamard 4.14; I - 2ee^T for n = 3..12 decreasing 2.53 -> 1.35.
- Comb laws tuned to the lattice (m teeth of width 1/m): pair-sum block 4.02 -> 1.65 (m = 3) -> 0.50 (m = 9);
  Hadamard n = 16: 4.17 -> 0.68 (m = 3); the drop is about 1/m.
- Convex sides: definite rank-3 at n = 4/6: 3.11/2.87; two-sheet side about 2.8. Linear terms lower the peak.
- (1,1,-eps): p(0) rises toward 2 pi as eps -> 0 (4.20, 4.87, 5.40, 5.72 at eps = 0.3, 0.1, 0.03, 0.01).

## Where a counterexample could still hide

Rank three: only convex level sets (definite forms, two-sheet side). Higher rank: delocalised eigenvectors
with every 3x3 principal block nearly singular. The searches were local; a multi-scale arithmetic
structure at large n would not be found by them. At s = 0, p(0) equals (pi/sqrt 2) times an average over a
circle of 2-planes of codimension-2 cube section volumes, so "sup = 3 sqrt 2" is an averaged Ball-type
section question: is that average always <= 6/pi?
