SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B01, 2026-09-23T16:30:50Z.
attacking: near-singular but nonzero physical-pair determinant; quantify the scalar-completed leakage residual by a dependence-safe frequency-averaged/random-slope estimate before trying to reattach the outer square.

# Early substantive checkpoint — near-null leakage residual

Full QFORM remains OPEN. This checkpoint records the first new calculation before the final write-up.

Let a physical pair B=[[a,b],[b,c]] with a!=0 be scalar-completed in the fleet04/B01 singular-star coordinates. Write delta=det(B)/a and let l be its leakage vector into the still-independent original-coordinate bank Z. The scalar-completed residual has the form

R = delta Y^2 + 2Y(l dot Z + beta) + K(Z),

where Y is one original coordinate, independent of Z, every coordinate density is <=1, and K may contain arbitrary dense/high-rank quadratic and affine curvature.

Use the already proved random-slope Plancherel theorem from fleet03/B01 r21: if the random slope L has density cap K0, then

|phi_R(t)| <= min(1, K0^(1/2) (pi/|t|)^(1/2)), t!=0,

and the dependence-safe scalar random-slope small-ball lemma gives

P(|R-s|<=rho) <= min(1, 4 sqrt(K0 rho)).

For L=l dot Z+beta, the product-projection bound gives K0<=sqrt(2)/||l||_2. Hence

|phi_R(t)| <= min(1, 2^(1/4)sqrt(pi)||l||_2^(-1/2)|t|^(-1/2)),
P(|R-s|<=rho) <= min(1, 4*2^(1/4)||l||_2^(-1/2)sqrt(rho)).

Now apply the designated fleet04/B01 r2 singular-star routing theorem, source math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582. In its leakage branch,

sum_(k!=l) l_k^2 l_l^2 >= W2/(4a^2).

Since the left side <=||l||_2^4,

||l||_2 >= W2^(1/4)/(sqrt(2)|a|^(1/2)).

Therefore the actual near-null leakage residual satisfies

|phi_R(t)| <= min(1, sqrt(2pi)|a|^(1/4)W2^(-1/8)|t|^(-1/2)),

and for every interval I,

P(R in I) <= min(1, 4 |a|^(1/4)W2^(-1/8) sqrt(|I|)).

This is uniform in delta, including arbitrarily small nonzero delta, and in the entire dense curvature K. It does NOT yet bound the density of the original Q after reattaching the outer scalar square: exponent 1/2 is exactly the borderline where the square-root kernel may still create a logarithm. The next step is to use the nonzero mismatch/aggregate-curvature information to beat that borderline rather than perturb from delta=0.

Newest-Claude volume pruning is also active: whenever an original-coordinate cross block M satisfies max diag(P_top2)<=1/2 and ||P_perp M||op<=sqrt(T2)/15, the supplied tail theorem gives continuous density <=(9sqrt(3)e/2)[s1(M)^2 s2(M)^2 T2]^(-1/6). Thus this near-null analysis is only needed after that collective-tail exit has failed.
