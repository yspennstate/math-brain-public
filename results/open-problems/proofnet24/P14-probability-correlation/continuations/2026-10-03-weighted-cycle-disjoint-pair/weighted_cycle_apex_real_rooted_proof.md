# Arbitrary weighted-cycle apex real-rootedness and disjoint-pair negative correlation

3 October 2026.  Complete analytic derivation; the fresh independent audit
passes.  This supersedes the uniform-cycle Chebyshev route in scope.  It is a
restricted cyclic-backbone theorem, not the general forest negative-
correlation conjecture.

## Theorem

Let `H=C_n`, `n>=3`, with arbitrary finite nonnegative rim activities
`lambda_0,...,lambda_(n-1)` and arbitrary nonnegative vertex profile
`beta_0,...,beta_(n-1)`.  Add four new vertices whose spoke activities to
rim vertex i are `a beta_i,b beta_i,c beta_i,d beta_i`, respectively, and
add exactly the two disjoint marked edges joining the first pair and the
second pair.  There are no other edges incident to the new vertices.

The two marked indicators are negatively correlated at every pair of
positive marked-edge activities.  Strictness holds exactly when

1. `a b c d>0`, and
2. at least two profile entries are positive.

The conclusion survives arbitrary positive-probability cylinder conditioning
of rim edges.  After deleting forced-absent edges, contracting forced-present
edges, deleting resulting loops, and combining parallel edges in the usual
forest partition, the same strictness test uses the number of contracted
vertices with positive profile sum.  Individual spoke fields,
nonproportional rows, and whole-vector negative association are not claimed.

The analytic input is stronger.  If `D(s)` is the unrooted-forest partition
after adding one apex with spoke activity `s beta_i` to rim vertex i, then D
has only negative real zeros; its degree is the number of positive beta_i.

## 1. Exact two-state transfer for the apex polynomial

Temporarily assume every `lambda_i,beta_i` is positive.  While traversing
the oriented rim, record whether the current open rim component contains an
apex spoke.  At vertex i, either add no spoke or, only in state zero, add the
spoke of weight `s beta_i`.  Across rim edge i, a closed edge resets the
state to zero and an open edge of weight `lambda_i` preserves it.  The
combined transfer matrix is

    T_i(s) = [[1+lambda_i+s beta_i, s beta_i lambda_i],
              [1,                     lambda_i       ]].  (1)

The trace of the cyclic product counts every allowed marked/unmarked-cluster
configuration exactly once, except that the configuration with every rim
edge open and no spoke is counted in both persistent states.  That
configuration is cyclic and must instead be excluded completely.  Therefore

    D(s)=tr M(s)-2 Lambda,
    M(s)=T_0(s)T_1(s)...T_(n-1)(s),   Lambda=product_i lambda_i. (2)

This identity can also be checked directly: any missing rim edge forces the
state to zero there and removes the trace ambiguity; any spoke fixes state
one on precisely its forward open component; two spokes in one component
are forbidden.  The only trace paths without a reset or a spoke are the two
all-open paths just subtracted.

Each factor has determinant `lambda_i(1+lambda_i)`, independent of s.  Put

    c_i=lambda_i(1+lambda_i),
    delta=det M=product_i c_i.

Since all rim activities are positive,

    delta=Lambda product_i(1+lambda_i)>Lambda^2.          (3)

The leading coefficient of D is `product_i beta_i`: selecting every spoke
forces every rim edge absent.  Thus D has degree n.

## 2. Every complex zero is real

Let s be any zero of D.  By (2), `tr M(s)=2 Lambda`, so an eigenvalue rho of
M satisfies

    rho^2-2 Lambda rho+delta=0.

Equation (3) makes the two eigenvalues nonreal conjugates and gives

    |rho|^2=delta.                                       (4)

Choose a nonzero eigenvector and propagate row states

    (x_(i+1),y_(i+1))=(x_i,y_i)T_i(s).

The eigenvector condition means `x_(i+n)=rho x_i`.  From (1),

    x_(i+1)=(1+lambda_i+s beta_i)x_i+y_i,
    y_(i+1)=lambda_i(y_i+s beta_i x_i).

Eliminating y gives the second-order equation

    x_(i+1)=(1+lambda_(i-1)+lambda_i+s beta_i)x_i
             -c_(i-1) x_(i-1).                          (5)

The x-sequence is not identically zero, since two consecutive zero x's
would force the propagated two-vector to vanish.

Write (5) as the generalized cyclic eigenproblem

    (L_rho x)_i
      := x_(i+1)+c_(i-1)x_(i-1)
          -(1+lambda_(i-1)+lambda_i)x_i
       = s beta_i x_i,                                   (6)

using quasi-periodic boundary values `x_(i+n)=rho x_i`.

This problem is Hermitian in an explicit weighted inner product.  Set

    m_0=1,  m_(j+1)=m_j/c_j,
    <u,v>_m=sum_(j=0)^(n-1) m_j conjugate(u_j)v_j.

For every interior neighbor pair, `m_j*1=m_(j+1)c_j`, so the two off-
diagonal terms are adjoints.  Across the boundary, the coefficient from row
`n-1` to column zero is rho, while the reverse coefficient is
`c_(n-1)rho^(-1)`.  The adjoint equality is exactly

    m_(n-1)rho = c_(n-1)/conjugate(rho),

which is equivalent to `|rho|^2=product_i c_i=delta`, already proved in
(4).  The diagonal is real.  Hence L_rho is Hermitian.  The right-hand
weight `diag(beta_(j-1))` is positive definite, so (6) gives

    s=<x,L_rho x>_m / <x,diag(beta_i)x>_m in R.           (7)

Thus every zero of D is real.  All coefficients of D are nonnegative, its
constant and leading coefficients are positive, and it has no zero at a
nonnegative real number.  Its n zeros are therefore strictly negative.

## 3. Boundary activities and profiles

If at least one rim activity is zero, its edge may be deleted and the
positive-support backbone is a forest.  The determinant theorem in
`forest_disjoint_rank_one_attachment_forest_backbone_proof.md` gives the
same negative-real-root conclusion.

If some profile entries vanish, replace them by positive epsilon, apply the
proved result, and let epsilon decrease to zero.  Coefficients converge.
The degree drops precisely to the number k of positive profile entries;
roots of a real polynomial depend continuously as a multiset, so a nonreal
finite root in the limit would force nearby nonreal roots before the limit.
Hence the k remaining roots are real.  Positivity of the constant and all
positive-degree coefficients makes them negative.  We have proved

    D(s)=D(0) product_(h=1)^k(1+s x_h),   x_h>0.          (8)

Also `sum_h x_h=D'(0)/D(0)=sum_i beta_i`, because one apex spoke is always
admissible.

The same reasoning includes the two-vertex cycle with two parallel rim
edges, which occurs when a triangle edge is contracted, with one small
matrix-bookkeeping qualification.  The forward and backward neighbors then
coincide, so the two off-diagonal contributions must be added.  They are

    (L_rho)_(0,1)=1+c_1/rho,   (L_rho)_(1,0)=c_0+rho.

With `m_0=1,m_1=1/c_0`, weighted adjointness is
`1+c_1/rho=1+conjugate(rho)/c_0`, again exactly
`|rho|^2=c_0c_1`.  Thus unequal parallel-edge C2 is genuinely covered.  A
one-vertex result after further contraction is the degree-one boundary of
(8).

## 4. The disjoint marked pair

Sections 2 and 3 of the prior forest-backbone proof derive, for an arbitrary
backbone and `sigma=a+b+c+d`, the exact identity

    (EF-AC)/(D^2 abcd)
      =2(U T-Omega)
       +(a+b)(c+d)(Gamma^2+U^2T-2U Omega).               (9)

Those sections sum over the backbone's acyclic configurations and do not
assume that the ambient backbone is itself acyclic.  Their only later sign
input is factorization (8).  Substituting it gives

    U T-Omega=sum_(h!=j) alpha_h tau_j,                  (10)

and

    Gamma^2+U^2T-2U Omega
      =sum_(h!=j)alpha_h^2 tau_j
       +2sum_(h<j)gamma_h gamma_j
       +2sum_(h<j,ell notin {h,j})alpha_h alpha_j tau_ell, (11)

where all `alpha,tau,gamma` are positive.  Thus (9) is nonnegative and is
strict exactly when `abcd>0` and `k>=2`.  The usual two-marked-edge
coefficient calculation converts `EF-AC>=0` to negative correlation.

Deleting and contracting conditioned rim edges leaves either a weighted
cycle/multicycle or a forest, with profile weights added under contraction.
Loops are forbidden in a forest and disappear; parallel edges retain the
same two-cycle transfer or combine by deletion/contraction.  Therefore the
argument is closed under every positive-probability rim cylinder
conditioning, with the stated contracted-profile strictness criterion.

## Scope

This proves a new cyclic-backbone family with arbitrary rim weights and
profiles, but not arbitrary cyclic graphs.  The four spoke rows must be
proportional and the only new-new edges are the two marked edges.  It gives
pairwise negative correlation for that pair, not whole-vector negative
association.  The full forest/arboreal-gas conjecture remains open.
