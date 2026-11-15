# Independent checks and attempts to break the bound

## 1. The previous energy bound

For a replacement X_i' and deleted sample S_i, the tour difference is
d(X_i;S_i)-d(X_i';S_i). The two terms are conditionally independent
and identically distributed. Hence

\[
 \frac12\sum_i\mathbb E(L_n-L_n^{(i)})^2
   =n\mathbb E\operatorname{Var}_X(d(X;S)\mid S)=E_n.
\]

This independently checks the conditional-variance route used in the
proof. In particular there is no missing factor two in (9).
Centering at c/sqrt(n) gives an inequality, not an equality, unless that
constant is the conditional mean. The new proof never assumes it is.

For the old limiting envelope let W=pi Z^2, so W is exponential with
mean one. With a=sqrt(pi)c, direct truncated moments give

\[
 \mathbb E[W\mathbf1_{W>a^2}]=(a^2+1)e^{-a^2},\qquad
 \mathbb E[\sqrt W\mathbf1_{W>a^2}]
 =ae^{-a^2}+\frac{\sqrt\pi}{2}\operatorname{erfc}(a).
\]

Substitution into
c^2+4 E[Z(Z-c)1_(Z>c)] gives the displayed F(c), independently
of the tail integral in PROOF.md. Differentiating threshold integrals
gives F'=2c-4 E[Z 1_(Z>c)] and
F''=2+8pi c^2 exp(-pi c^2)>0, checking the old minimizer as well.
Both earlier results hold under this audit.

## 2. A second proof of spatial continuity

Starting with a tour through S union {z}, append the closed detour
z,x,z, of length 2|x-z|. Delete z if z is not required, and shortcut
all repeated vertices. This produces a tour through S union {x} with
length at most T(S union {z})+2|x-z|. Reversing x,z proves (6).
This proof does not move the two incident edges as in PROOF.md.
It handles a singleton S, repeated locations, and a point already in S.

## 3. Local constant checked by translating one disk

Work in coordinates v=sqrt(n)(x-y)/c. The disks have radius 1/8,
centers (5/8,0) and (11/8,0), and area pi/64. In these units the
nearest-distance ranges are [1/2,3/4] and [5/4,3/2]. Dividing u by c
makes its Lipschitz constant two.

Pair a in A_y with b=a+3c e/(4sqrt(n)), which maps the first disk
onto the second with Jacobian one. Then
u(b)-u(a)<=3c/2. From the same exact deficit factorizations,

\[
 q(a)+q(b)\ge\frac c2\{u(a)+2r(b)-u(b)\}
 \ge\frac c2\left(\frac{5c}2-\frac{3c}2\right)
 =\frac{c^2}2.
\]

Integrating this pairing gives pi c^4/(128n), which in particular
confirms the conservative pi c^4/(256n) used in the theorem. The theorem
does not claim the best constant obtainable from these disks. The main
proof's all-pairs method has the larger distance bound c/sqrt(n), hence
only c^2/4 for the pair deficit; its factor two is accounted for.

In normalized units its arithmetic is

\[
 2(3/4)=3/2,\quad 2(5/4)-2=1/2,\quad
 (11/8-5/8)+2/8=1,\quad
 \tfrac12(2\cdot\tfrac54-2)=\tfrac14,\quad
 (\pi/64)(1/4)=\pi/256.
\]

Thus both the coefficients in the deficit factorization and the area
factor have independent checks. The subtraction in (9) has the right
sign: subtracting q restores exactly the actual centered square.

## 4. Isolation and counting checks

All points in either disk are within 3c/(2sqrt(n)) of y. Another site
at distance greater than 3c/sqrt(n) is farther from each such point
than y is. If two admissible sites existed with overlapping supporting
open disks of radius 3c/(2sqrt(n)), the triangle inequality would put
the sites at distance less than 3c/sqrt(n), contradicting isolation.
Tangencies have zero area and cause no integral error.

For an alternative derivation of the count, the joint sample density is
one. Fix which label is the distinguished site and integrate its location
over Q_{n,c}; integrate every other label over the complement of its
radius-3c/sqrt(n) disk. The resulting integral is

\[
 (n-1)\int_{Q_{n,c}}
       (1-|B(y,3c/\sqrt n)|)^{n-2}\,dy
 =(n-1)(1-6c/\sqrt n)^2(1-9\pi c^2/n)^{n-2}.
\]

This checks the exponent n-2: S has n-1 points before choosing the
distinguished site. Dividing by n tends to exp(-9pi c^2). The same
limit is the elementary binomial void limit for a disk whose expected
number of other sample points tends to 9pi c^2.

A second check of the n factors is to choose X uniformly after S. The
probability it lies in the union of disk pairs is
(2 pi c^2/(64n)) E N, by disjointness. The all-pairs bound makes the
average deficit on that union at least c^2/8. Multiplying gives
(pi c^4/(256n)) E N, exactly (17) after expectation. There is no extra
factor two for the two disks.

## 5. Boundary, finite-sample, and endpoint cases

- The margin in Q_{n,c} is 3c/sqrt(n), so the entire isolation disk
  lies in Q. Its area is exactly 9pi c^2/n, without a boundary
  approximation. Its excluded strip has area tending to zero.
- The condition n>36c^2 makes this margin less than 1/2. It also
  makes 9pi c^2/n<pi/4<1, so (18) has a positive base.
- For n=2, S is a singleton and the avoidance exponent is zero.
  If n>36c^2, the same local argument applies. If that condition fails,
  the finite-sample formula is not asserted. This is harmless for every
  fixed c in the limiting theorem.
- Coincident sample locations have probability zero. Deterministic
  continuity and insertion bounds remain valid for repeated locations;
  the count calculation is an almost-sure distinct-sample calculation.
- At u=0, the inner-disk deficit is zero; then the outer disk must
  lose squared error because a 2-Lipschitz field cannot reach its
  preferred endpoint fast enough. At u=2r on the outer disk its
  deficit is zero, forcing a positive inner contribution. Intermediate
  values satisfy the same exact factorizations.
- The artificial field d=0 is feasible for the deterministic interval
  and Lipschitz constraints and has ample outer-disk deficit. The field
  d=2R has inner-disk deficit. Neither is a counterexample. The scalar
  extremizer d=2R 1_(sqrt(n)R>c) violates continuity across the
  radius-c threshold around an isolated point.
- The tail limit in PROOF.md is proved only at fixed interior x. The
  separate Gaussian tail bound controls expectations near the boundary;
  discarding a measure-zero boundary alone would not suffice.
- All centers c in the limit argument are fixed. The theorem does not
  substitute an n-dependent minimizing center.

## 6. Magnitude and inference checks

The deficit cannot make the claimed bound negative. Put t=9pi c^2.
Then

\[
 \frac{\eta(c)}{c^2}=\frac{t e^{-t}}{2304}
 \le\frac1{2304e}<1,
\]

whereas F(c)=E H_c(Z)>=c^2. Thus F(c)-eta(c)>0 for c>0.
Since c_*>0, eta(c_*) is strictly positive. No decimal evaluation or
claim that this is a large improvement is made.

The theorem controls a limsup. It supplies no monotonicity in n and
no uniqueness of a subsequential interaction spectrum. The earlier
oscillating order-one examples still rule out inferring convergence
from a smaller uniform energy bound. A bound on the total variance
also cannot identify the limiting variance.

No flaw in the new deterministic lemma, counting argument, or limit
passage was found. No claim of novelty relative to the complete literature
or comparison with the best published variance bound is made.
