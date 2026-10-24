# Möbius-ladder density is Schur-convex on four-state Klein-group hosts

2 October 2026. This is a restricted-host theorem with a complete exact
integer polynomial certificate and a second, independent transfer-matrix
certificate. It does not prove Sidorenko for general hosts. Historical
novelty has not been established.

## The host family and conclusion

Let G=(Z/2Z)^2, with uniform measure. For arbitrary nonnegative numbers
p_0,p_1,p_2,p_3, define the symmetric kernel

    W_p(x,y)=4p_(x+y),  x,y in G.

Its edge density and every vertex degree equal s=sum_i p_i. Equivalently,
its four-by-four matrix is

    4 * [[p0,p1,p2,p3],
         [p1,p0,p3,p2],
         [p2,p3,p0,p1],
         [p3,p2,p1,p0]].

This includes arbitrary full-rank centered parts with three eigenfunctions;
it is not restricted to one nonconstant eigenfunction. Any graphon blow-up
into four equal-measure classes with this matrix has the same density.

Let H be the ten-vertex fifteen-edge bipartite Möbius ladder. Write
F(p)=t(H,W_p). Then F is Schur-convex on the nonnegative orthant and obeys
the quantitative bound

    F(p)>=s^15+1024 sum_(i<j)|p_i−p_j|^15.                 (1)

Thus Sidorenko holds for all kernels in this family, and equality holds
only at the constant kernel (apart from the all-zero case).

The proof is computational algebra with exact integers, not a numerical
optimization or tolerance check. The complete polynomial and all
certificate coefficients are in `continuation_20261002_klein4_schur.json`;
both regenerators are provided below.

## 1. The exact homogeneous density polynomial

Fix one vertex label to zero. Simultaneous translation of all ten vertex
labels preserves every edge sum, giving four assignments per fixed-label
assignment. For the 4^9 fixed-label assignments let N_(a,b,c,d) count those
with a,b,c,d edges whose endpoint sum is respectively 0,1,2,3. Then

    F(p)=4^6 sum_(a+b+c+d=15) N_(a,b,c,d) p0^a p1^b p2^c p3^d.   (2)

The factor is 4^15 from edge weights, divided by 4^10 from the vertex
measure, times four from restoring the fixed label. All coefficients in
(2) are nonnegative integers, and the certificate contains its 476
nonzero monomials. Since there are exactly 4^9 assignments, F(1/4,...,1/4)=1;
homogeneity gives F(s/4,...,s/4)=s^15.

The polynomial is invariant under every permutation of its four arguments.
Conceptually, translating all labels on one side of the bipartition
translates the edge sums, and applying an automorphism of G permutes the
three nonzero group elements. These operations generate the affine group
AGL(2,2), which is S4 on G. The first verifier additionally checks all 24
coefficient permutations exactly.

## 2. A polynomial certificate for pairwise gradient ordering

Symmetry makes partial_0 F−partial_1 F divisible by p0−p1. Define the
homogeneous degree-thirteen polynomial

    Q(p)=(partial_0 F−partial_1 F)/(p0−p1),                (3)

with the quotient interpreted polynomially, including the equality plane.
The raw Q coefficient list has 434 nonzero terms and 164 negative
coefficients. Consequently raw coefficient nonnegativity is NOT the
certificate; that shortcut fails.

Instead substitute ordered differences

    p0=A+D, p1=A, p2=B+E, p3=B.

The exact expansion is

    Q(A+D,A,B+E,B)=sum C_(a,b,d,e) A^a B^b D^d E^e,
    a+b+d+e=13,                                        (4)

and every one of its 436 nonzero coefficients is a positive integer. In
particular

    C_(0,0,13,0)=61440.                                (5)

The full list is the `ordered_quotient_coefficients` field in the JSON.
Equation (4), rather than an approximate fitted polynomial, is regenerated
by exact binomial expansion of the exact quotient. Therefore

    Q(p)>=61440|p0−p1|^13>=0                           (6)

for all nonnegative p: exchange p0,p1 if necessary, and independently
exchange p2,p3. Q is invariant under both exchanges by symmetry of F, so
these operations reduce every point to the nonnegative substitution in
(4). By permuting arguments, the same inequality holds for every pair i,j.
It follows that

    (p_i−p_j)(partial_i F−partial_j F)
       >=61440|p_i−p_j|^15.                            (7)

This proves gradient ordering and therefore Schur-convexity. The following
direct integration also establishes (1), without appealing to any general
Schur-convexity theorem.

## 3. Integrate toward the uniform vector

Put u=s/4 and p(t)=u*1+t(p−u*1), 0<=t<=1. For t>0,

    d/dt F(p(t))
       =1/(4t) sum_(i<j)
           [p_i(t)−p_j(t)]
           [partial_i F(p(t))−partial_j F(p(t))].       (8)

The factor 1/t is necessary: p_i(t)−p_j(t)=t(p_i−p_j).
Identity (8) follows from
sum_i (x_i−mean(x))g_i=(1/4)sum_(i<j)(x_i−x_j)(g_i−g_j).
Using (7) gives

    d/dt F(p(t))>=15360 t^14 sum_(i<j)|p_i−p_j|^15.

Integration from zero to one yields a factor 1/15, hence
F(p)−F(u*1)>=1024 sum_(i<j)|p_i−p_j|^15. Since F(u*1)=s^15,
this proves (1). Boundary points and the zero vector follow directly by
polynomial continuity. This completes the theorem.

## 4. Exact reproducibility and independent algebraic audit

`continuation_20261002_klein4_schur.py` regenerates (2) by vertex assignments,
checks S4 invariance, forms the exact gradient difference, divides it using
the antisymmetric monomial-pair identity, checks multiplication back by
p0−p1, and performs the exact ordered binomial expansion.

`continuation_20261002_klein4_independent_transfer_audit.py` regenerates the
ENTIRE density polynomial without enumerating ten-vertex assignments. It
uses the sixteen-state root-free transfer

    T_(x,y),(k,l)=p_(x+y) p_(x+l) p_(k+y).

Exact dictionary matrix multiplication computes trace(T^5). Multiplying
by 4^5 yields the density polynomial, which agrees coefficient by
coefficient with (2). This is the root-free version of Rossman's prior
ladder transfer identity; the identity itself is not claimed as new.
The second verifier then uses polynomial long division (different from
the author's antisymmetric-pair quotient algorithm) and independently
regenerates all 436 ordered nonnegative coefficients and coefficient
61440 in (5). Its result is saved in a separate JSON.

These are complete exact coefficient checks with ordinary Python integers.
They require no numerical library, eigenvalue approximation, logarithm,
floating-point threshold, or optimization inference. The accompanying
symbolic finite certificate is the mathematical input in (4).

## 5. Scope and remaining obstruction

Equal-diagonal regular symmetric four-state hosts all have precisely this
matrix form. Unequal diagonal values, unequal atom sizes, larger groups,
and general graphons are not covered. The affine S4 argument uses the
special four-element group: on larger elementary abelian groups, affine
permutations do not give every permutation of the host weights. Moreover
Schur-convexity of this restricted polynomial supplies no positive-spectrum
pairing or trace bound for arbitrary Rossman transfers.

The result is therefore a certified finite-step partial theorem on the
famous unresolved target, not its solution. No earlier statement of this
particular Schur-convexity and quantitative bound was located in a bounded
primary search, but that does not prove novelty. The already known complete
graph host and various two-state host results must not be claimed as new.
