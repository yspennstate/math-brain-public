# Disjoint marked pair over any weighted forest backbone, with any number of common neighbors

3 October 2026. Complete analytic derivation, awaiting its fresh independent
audit. The proof includes a direct tree-covariance determinant identity and
two explicit positive Stieltjes expansions. It does not assume real-rootedness
for cyclic backbones or claim negative association of a whole matching.
Historical novelty and external specialist review remain unverified.

## Theorem

Let H be any finite weighted FOREST with nonnegative finite edge activities.
Give its vertices nonnegative profile weights beta_j. Add four new vertices
u_1,...,u_4 with respective spoke activities `a beta_j,b beta_j,c beta_j,d beta_j`,
where a,b,c,d>=0. Add exactly two marked mutual edges e=u_1u_2 and f=u_3u_4,
of arbitrary positive activities. The new vertices have no other edges.

The two marked indicators are negatively correlated. The inequality is
strict exactly when all four row factors are positive and at least two
vertices of H have positive profile weights. It survives positive fields
on H and the marked edges and arbitrary positive-probability **coordinate
(cylinder) conditioning** that fixes any chosen H edges present or absent.
After conditioning H edges present, the strictness criterion
uses the number of positive profile sums on their contracted components.
No bound is imposed on the number of common neighbors, size of H, or
relative activities. Individual spoke fields are outside the claim.

## 1. A direct determinantal identity for the apex partition of a forest

All edge subsets of H are acyclic. Its forest measure is therefore
independent bond percolation with probabilities

    p_e=w_e/(1+w_e),    Z_H=product_e(1+w_e).

For each tree component, choose a root. Construct centered Gaussian variables
of unit variance along the tree: the root is a standard Gaussian, and each
child variable is

    Y_child=sqrt(p_e)Y_parent+sqrt(1-p_e)epsilon_child,

with all epsilon independent standard Gaussians. Different tree components
are independent. Their covariance matrix C is positive definite because
every p_e<1 and the Gaussian construction is triangular with positive
innovation variances. Its entries are

    C_ij=product_(e in path(i,j))sqrt(p_e)

within one component, and zero between components; C_ii=1.

For EVERY vertex subset S,

    det C_S=Pr(no two vertices of S are percolation-connected).  (1)

Here is a complete proof. The determinant is separately affine in each
edge probability. Cut an edge e; the selected vertices split into sets
S_L,S_R. The covariance block is

    [ A, sqrt(p_e) u v^T ; sqrt(p_e) v u^T, B ],

where A,B,u,v depend only on other edge probabilities. For interior
probabilities A,B are invertible and the Schur complement gives

    det=det A det B [1-p_e(u^T A^(-1)u)(v^T B^(-1)v)].

If one side is empty the determinant is independent of p_e. Thus separate
affinity holds on the interior and extends continuously to every boundary.
The percolation probability on the right of (1) is also separately affine.
At each vertex `p_e in {0,1}` of the probability cube, C_S is a block-diagonal
matrix whose blocks are all-ones matrices, one for each connected component.
Its determinant is one when each block has size at most one, and zero
otherwise. This is precisely the connection-event indicator. Two separately
affine functions agreeing at every cube vertex agree everywhere, proving (1).

Add one apex with spoke activity `s beta_j` to vertex j. For a fixed H
percolation configuration, an apex spoke subset S is allowed iff no two of
S lie in one H component. The ordinary unrooted-forest partition D(s) is
therefore

    D(s)/Z_H
      =sum_S s^|S| product_(j in S)beta_j det C_S
      =det[I+s diag(sqrt(beta)) C diag(sqrt(beta))]. (2)

The last equality is the principal-minor expansion of a determinant.
The matrix in (2) is positive semidefinite, with rank equal to the number k
of positive profile weights, because C is positive definite. Hence

    D(s)=Z_H product_(i=1)^k(1+s x_i),    x_i>0.      (3)

This establishes the required negative real roots from a direct Gaussian
construction and elementary multilinearity. No general cyclic-backbone
real-rootedness theorem is invoked.

The identity survives this coordinate H-edge conditioning by first contracting required-
present components, summing their beta weights, and deleting absent edges.
The resulting graph is again a forest with finite remaining activities.
The fixed required-edge activity product is a common positive factor, and
does not change logarithmic derivatives or the proof.

## 2. Four-core component-transfer identity for an arbitrary backbone

This section is an exact algebraic identity for any finite weighted H;
the sign will use the forest-specific factorization (3).
Write `s=a+b+c+d>0`. For an H forest A, contract its components and let
`x_C=sum_(j in C)beta_j`. Its four-column rank-one terminal transfer is

    T(x)=(1+s x)I+x^2P+x^3Q+x^4R,

where P,Q,R join respectively two, three, or four distinct core blocks.
They obey

    PQ=QP=3sR,   P^3=6s^2R,
    PR=QR=Q^2=R^2=0.                               (4)

For the first identity, only four separate initial blocks contribute.
The six possible first pair joins followed by a triple join sum to
`3s abcd`; the reverse order gives the same weight. The second identity
counts ordered weighted spanning trees on four vertices: the sum over
trees with edge weights column_i column_j is `abcd s^2`, and the three
join orders give the multiplier 3!=6. For completeness, this weighted
tree sum follows directly from the sixteen labeled four-vertex trees:
the four star terms give `abcd sum_i column_i^2`, and the twelve path
terms give `2abcd sum_(i<j)column_i column_j`, hence `abcd s^2`.
All remaining products exceed the three available merges.

Put `d(x)=1+s x`, `alpha=x^2/d`, `v=x^3/d`, and
`chi=x^4(1-s x)/d^3`. The finite nilpotent logarithm gives

    log[T(x)/d(x)]=alpha P+v Q-(alpha^2/2)P^2+chi R. (5)

Indeed the R term is `x^4/d-3s x^5/d^2+2s^2x^6/d^3=chi`.
Let

    U_A=sum_C x_C^2/d(x_C),
    G_A=sum_C x_C^3/d(x_C)^2,
    H_A=sum_C x_C^4/d(x_C)^3,
    D_A=product_C d(x_C).

Expanding (5) on an initially empty four-core gives

    Z_A/D_A
      =1+e_2 U_A+e_3(G_A+sU_A^2)
        +e_4[2H_A-U_A^2+3sU_A G_A+s^2U_A^3],       (6)

where e_i are elementary symmetric polynomials of a,b,c,d. To verify all
coefficients, on the empty core

    P1=e_2, Q1=e_3, R1=e_4,
    P^2 1=2s e_3-2e_4, PQ1=3s e_4, P^3 1=6s^2e_4.

The P^2 count comprises joined triples and two disjoint joined pairs; their
weights are `2s e_3-8e_4` and `6e_4`. Substitution into the truncated
exponential proves (6).

Normalize `weight(A)D_A` by D(s) to nu_s. Define

    U=E U_A,
    Gamma=E G_A+s Var(U_A),
    Omega=E H_A-(1/2)Var(U_A)
           +(3s/2)Cov(U_A,G_A)+(s^2/2)Cum_3(U_A).   (7)

The mixture of (6) is exactly

    Z/D=1+e_2 U+e_3(Gamma+sU^2)
        +e_4[2Omega-U^2+3sU Gamma+s^2U^3].          (8)

All covariance and third-cumulant terms are retained. They are not given
unproved signs. Let `A_0=sum_j beta_j`, independent of the H forest.
Differentiating the actual finite apex sum gives the useful exact identities

    U=(A_0-(log D)')/s,
    Gamma=-U'(s),   Omega=U''(s)/2,
    T_0:=U-s Gamma=-(log D)''(s).                   (9)

For the first, `(log D)'=E sum_C x_C/d(x_C)` and
`U_A=(A_0-sum_C x_C/d(x_C))/s`. The second is the variance differentiation
of this equality. For the third, writing W_A=sum x_C/d and
Y_A=sum x_C^2/d^2 gives
`(log D)'''=2E(G_A-sH_A)-3Cov(W_A,Y_A)+Cum_3(W_A)`;
use `W_A=A_0-sU_A` and `Y_A=U_A-sG_A` to obtain (7),(9).

## 3. Disjoint marked coefficients and exact difference

Set `p=a+b`, `q=c+d`, `u=ab`, `v=cd`, and let

    H_3=Gamma+sU^2,
    H_4=2Omega-U^2+3sU Gamma+s^2U^3.

Contraction of a marked pair sums its column factors. Formula (8) gives
the coefficients in `Z(w_e,w_f)=A+E w_e+F w_f+C w_e w_f`:

    A/D=1+(pq+u+v)U+(uq+vp)H_3+uvH_4,
    E/D=1+(pq+v)U+vp H_3,
    F/D=1+(pq+u)U+uq H_3,
    C/D=1+pq U.

Direct cancellation yields

    (E F-A C)/(D^2 abcd)
      =2(U T_0-Omega)
         +pq[Gamma^2+U^2T_0-2U Omega].              (10)

When abcd=0, the un-divided difference has that factor and is zero.
Identity (10) does not yet give a sign for a general cyclic H; scalar
log-concavity alone only controls T_0, not the needed Omega combinations.

## 4. Both Stieltjes brackets have explicit nonnegative expansions

Now use the established forest-backbone factorization (3). Its derivative
at zero also satisfies `D'(0)/D(0)=A_0`, since a single apex spoke always
may be added. Hence `sum_i x_i=A_0`. Equation (9) becomes

    U=sum_i alpha_i,   Gamma=sum_i gamma_i,
    Omega=sum_i eta_i,   T_0=sum_i tau_i,

    alpha_i=x_i^2/(1+s x_i),
    gamma_i=x_i^3/(1+s x_i)^2,
    tau_i=x_i^2/(1+s x_i)^2,
    eta_i=alpha_i tau_i.

In particular `gamma_i^2=alpha_i^2 tau_i`. The first bracket is exactly

    U T_0-Omega=sum_(i!=j)alpha_i tau_j>=0.          (11)

For the second bracket, the repeated-index terms cancel and give exactly

    Gamma^2+U^2T_0-2U Omega
      =sum_(i!=j)alpha_i^2 tau_j
         +2sum_(i<j)gamma_i gamma_j
         +2sum_(i<j, k notin {i,j})alpha_i alpha_j tau_k>=0. (12)

These are finite sums of explicitly positive terms. If k>=2, (11) is
strict. If k=0 or 1, both expressions vanish. Equations (10)-(12) prove
the theorem for positive row factors. Zero factors make the corresponding
marked edge a bridge and give equality. If s=0 all spokes vanish and the
matching is independent. Thus the stated strictness criterion is exact.

For positive marked activities their covariance is
`-w_e w_f(EF-AC)/Z(w_e,w_f)^2`. Conditioning H gives the contracted forest
discussed after (3), so the same proof and profile-rank criterion apply.
Positive fields on H or the marked edges change allowed activities only.

## Verification and scope

The companion `forest_disjoint_rank_one_attachment_forest_backbone_exact.py`
checks the tree-covariance principal-minor identity with exact rational
arithmetic, the actual apex polynomial, the four-core transfer coefficients,
the third-cumulant identities, and the two bracket cancellations. It also
enumerates small whole uncontracted graphs and all recorded H conditionings.

The determinant step relies on H being a forest. Whether an arbitrary
cyclic H has a real-rooted apex polynomial is not established here. Even
if that stronger property held, the current derivation would prove only
the marked-pair inequality, not negative association of a whole matching.
The new vertices' profiles must be proportional and they have only the two
specified mutual edges. The general forest conjecture remains unresolved.
