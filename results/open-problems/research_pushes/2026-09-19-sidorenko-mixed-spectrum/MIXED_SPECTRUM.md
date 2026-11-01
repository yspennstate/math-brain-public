# Mixed-spectrum continuation for K(5,5) minus C(10)

19 September 2026. This note continues the spectral method, rather than the
small-host enumeration. All results below concern their stated classes. The
full Sidorenko inequality for the fixed graph is **not proved here**. The
arguments and finite certificates have been checked by the same assistant;
no independent audit or first-priority certification is claimed.

## 1. Target, notation, and what is inherited

Let H be the ten-vertex graph with edges i--(i+1) modulo 10, together with
i--(i+5), 0<=i<5. Its even/odd bipartition has five vertices per side and
the bipartite complement is a single ten-cycle. Thus H=K(5,5) minus C(10).
For a graph F and a kernel W on a probability space, write t_F(W) for the
integral of the product of W over the edges of F, including all vertex
variables independently. Isolated vertices contribute one.

Throughout the spectral argument, W is bounded, symmetric, nonnegative and
1-regular: integral W(x,y)dy=1 almost everywhere. Put U=W-1. Write U_j for
the **integral-operator power** U^j, not its entrywise power, and

    s_(2j)=Tr(U^(2j)) >= 0.

In finite rank, U=sum_i lambda_i f_i tensor f_i, with the f_i real,
orthonormal and orthogonal to constants. Jensen's inequality for the Markov
operator W implies |lambda_i|<=1. Its mixed third moments are

    M_ijk = integral f_i f_j f_k.

The previous continuation proved an exact rank-two minimum and the sharp
bound t_H(W)>=1+5 lambda^4+10|lambda|^6. It also gave positive, regular
rank-three counterexamples to unrestricted monotonicity under spectral
addition. We do not assume that truncating a positive kernel preserves
positivity, or that rank-two slacks add.

The older C30 note proved the arbitrary-rank case in which every M_ijk
vanishes. The present results do not impose that condition. Provenance and
literature boundaries are in SOURCES.md.

## 2. The first adverse cubic interaction can be paid in every rank

For positive integers a,b,c define

    theta_(a,b,c) = integral U_a(x,y) U_b(x,y) U_c(x,y) dxdy.

This is the density of the theta graph whose three internally disjoint
paths have lengths a,b,c. The first branching term in the expansion of
our H is 5 theta_(1,3,3), following 5s4+15s6. Crucially,

    A := s6 + theta_(1,3,3)
       = integral W(x,y) U_3(x,y)^2 dxdy >= 0.                 (2.1)

It follows, without a rank restriction, that

    15s6+5 theta_(1,3,3) = 10s6+5A >= 10s6.                  (2.2)

This is an exact use of positivity of the whole kernel. It does not
require positivity of its individual spectral truncations. In rank two,
theta_(1,3,3)=lambda^7(E f^3)^2; (2.2) explains why the sixth-order
coefficient 10 arises from paying the negative cubic interaction. It does
not, by itself, control the remaining terms of the expansion.

A second payment is also independent of rank. In finite rank,

    theta_(a,b,c)=sum_(i,j,k) M_ijk^2 lambda_i^a lambda_j^b lambda_k^c.

In particular theta_(2,2,4), theta_(2,4,4), and theta_(2,2,6) are
nonnegative. Let rho=||U||_op<=1. For a,b,c in [0,rho], AM--GM gives

    a^3 b^3 c^3 <= rho (a^2 b^2 c^4+a^2 b^4 c^2+a^4 b^2 c^2)/3.

Multiplication by the symmetric nonnegative weights M_ijk^2 and summation
therefore proves

    |theta_(3,3,3)| <= rho theta_(2,2,4),
    theta_(2,2,4)+theta_(3,3,3) >= 0.                        (2.3)

The same statements for bounded kernels follow by finite-partition
approximation; details of passing to the limit are given in Section 4.

## 3. Exact positive part and the surviving remainder

Let b_(4,4,2) be the density of two disjoint four-cycles joined by a path
of length two. With a(x)=U_4(x,x), it is

    b_(4,4,2) = <a,U^2 a> = ||Ua||_2^2 >= 0.                 (3.1)

Expansion over all 2^15 edge subsets and deletion of the terms with a
selected degree-one vertex give the exact identity

    t_H(W) = 1+5s4+10s6 + P_+(U) + R(U),                    (3.2)

where

    P_+(U) = 5A + 10(theta_(2,2,4)+theta_(3,3,3))
             +25s8+8s10+5s4^2+5s4 A
             +30 theta_(2,4,4)+30 theta_(2,2,6)
             +10 b_(4,4,2).                                 (3.3)

Every term displayed in (3.3), with the indicated grouping, is
nonnegative for the original positive regular kernel W.

For completeness R is defined by actual edge subsets, rather than an
unspecified error. Among the subsets without degree-one vertices remove:

* the empty set and all unions of disjoint cycles;
* theta graphs with path lengths (1,3,3), (2,2,4), (3,3,3),
  (2,4,4), or (2,2,6);
* the (4,4,2) barbell; and
* the disjoint union of a four-cycle and a (1,3,3) theta graph.

Then R is the sum of t_(H[F])(U) over all remaining edge subsets F, with
their labeled multiplicities. The exact counts are

| Number of selected edges | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Terms in R | 50 | 15 | 150 | 155 | 75 | 15 | 1 |

The nine-edge part is 40 theta_(1,3,5) plus ten barbells consisting of
two four-cycles joined by one edge. Higher terms include four, six, eight,
and ten selected degree-three vertices. Thus R still contains genuine
mixed-tensor interactions, including the full signed density t_H(U).

The cycle part before regrouping is

    1+5s4+15s6+25s8+8s10+5s4^2+5s4s6.

The disconnected (four-cycle, theta_(1,3,3)) terms combine with
5s4s6 to give 5s4 A. These details matter: a rank-two polynomial alone
cannot distinguish theta graphs from barbells that happen to give the
same scalar monomial.

The program check.py enumerates every edge subset, classifies these
particular configurations by connected components and branch-to-branch
paths, and checks all coefficients in (3.2). It requires no graph
isomorphism library. There are 625 surviving subsets including the empty
set. Finite enumeration proves the combinatorial identity, not R>=0.

## 4. A quantitative theorem with no rank restriction

### Theorem 4.1

For a bounded symmetric nonnegative 1-regular W, put delta=||W-1||_infinity
and U=W-1. Define

    E(delta)=50delta^5+15delta^6+150delta^7+155delta^8
             +75delta^9+15delta^10+delta^11.

Then

    t_H(W) >= 1+[5-E(delta)]Tr(U^4)+10Tr(U^6).               (4.1)

In particular, throughout the full infinite-dimensional class

    1/2 <= W(x,y) <= 3/2,   integral W(x,y)dy=1,

one has

    t_H(W) >= 1+(2589/2048)Tr(U^4)+10Tr(U^6) >= 1.          (4.2)

Equality in t_H(W)>=1 in this class forces W=1 almost everywhere.
No vanishing of the cubic tensor and no finite-rank hypothesis is assumed.

### Proof

We first prove the signed-cycle estimate needed for every term of R. If F
is a bipartite simple graph containing a cycle and m edges, then, for a
bounded symmetric real U with ||U||_infinity<=delta,

    |t_F(U)| <= delta^(m-4)Tr(U^4).                          (4.3)

For delta=0 this is immediate. Otherwise choose a shortest cycle in F.
Its length ell is even and at least four; it has no chord. Fix all vertex
variables outside that cycle. Edges from the cycle to the fixed vertices
supply one bounded multiplication function at each cycle vertex. The
cycle integral is the trace of an alternating product of these ell
multiplication operators and ell copies of U. Schatten--Holder bounds
its absolute value by the product of the multiplication-operator norms
times Tr(|U|^ell). Bound the outside edges by their suprema and integrate
the fixed variables. This gives

    |t_F(U)| <= delta^(m-ell)Tr(|U|^ell).

The Schur bound gives ||U||_op<=delta on a probability space, and hence
Tr(|U|^ell)<=delta^(ell-4)Tr(U^4). This proves (4.3).

Every subset contributing to R has selected minimum degree at least two,
so contains a cycle. Apply (4.3) termwise using the exact table in
Section 3. Then R>=-E(delta)s4. Substitution into (3.2), with P_+>=0,
proves (4.1) for finite-rank kernels.

To remove finite rank, on [0,1] use conditional expectations W_n on the
squares of refining finite partitions generating the sigma-field. They
remain symmetric, nonnegative, 1-regular, and within the same sup-norm
bounds. Also W_n converges to W in L^2. For a fixed graph and uniformly
bounded kernels, telescoping the edge product proves continuity of every
density in L^1. Hilbert--Schmidt convergence and uniform operator bounds
imply continuity of Tr(U_n^4) and Tr(U_n^6). Alternatively their cycle
integrals have the same bounded-kernel continuity. All theta and barbell
terms used above are finite graph densities, so their inequalities pass
to the limit as well. Thus (4.1) holds without a rank restriction.

Finally E(1/2)=7651/2048 and 5-E(1/2)=2589/2048>0. This proves (4.2).
A self-adjoint Hilbert--Schmidt operator with Tr(U^4)=0 is zero, so the
kernel U is zero almost everywhere in the equality case. QED.

**Prior-art boundary.** Qualitative local Sidorenko theorems are already
known from Lovasz (2010/2011), with signed graphon/cycle inequalities as
an ingredient. We are not claiming to discover local Sidorenko. The
particular mixed-theta payments, explicit remainder, and displayed
constant are the calculation recorded here; their publication novelty
has not been certified. Theorem 4.1 does not extend to all W merely
because it has no rank restriction.

## 5. An all-rank construction in which mixed cubic moments are allowed

The next theorem gives a different extension, with no smallness assumption
beyond nonnegativity of the constructed kernel.

### Theorem 5.1 (conditional-sign extension)

Let B be a bounded symmetric nonnegative kernel on a probability space Z.
Let a_1,...,a_r be bounded real functions, and lambda_1,...,lambda_r real
numbers. On Z times r independent fair signs define

    W((z,epsilon),(w,eta))
       = B(z,w)+sum_i lambda_i a_i(z)a_i(w)epsilon_i eta_i.

Suppose W>=0. For every bipartite graph F of maximum degree at most three,

    t_F(W) >= t_F(B).                                       (5.1)

If B is 1-regular, so is W. When E a_i^2>0, a_i(z)epsilon_i is an
eigenfunction with eigenvalue tau_i=lambda_i E a_i^2, orthogonal to the
base functions and to the other added eigenfunctions.

### Proof

Expand the edge factors by choosing either B or an added sign mode.
Average all signs independently, vertex by vertex. At a vertex each sign
index must occur an even number of times. Since the degree is at most
three, the selected sign-mode degree is either zero or two, and in the
second case both edges have the same index. Therefore the selected
edges are vertex-disjoint cycles, each monochromatic. All cycles are
even because F is bipartite. Their scalar factors lambda_i^(cycle length)
are nonnegative. At every cycle vertex the amplitude is a_i(z)^2, and
all remaining edges contribute B>=0. Every surviving summand is thus
nonnegative. The all-base term is t_F(B), proving (5.1).
Averaging over the second endpoint's signs proves regularity. Integrating
against a_i(w)eta_i proves the eigenvalue assertion directly. QED.

If B>=b>0, define sigma_j=sum_i tau_i^j for j=4,6,8,10. The same argument
and the six cycle-subset counts give the quantitative H-specific bound

    t_H(W)-t_H(B) >= 5b^11 sigma4+15b^9 sigma6
       +25b^7 sigma8+8b^5 sigma10+5b^7 sigma4^2
       +5b^5 sigma4 sigma6.                                 (5.2)

Here each remaining base edge is bounded below by b; integration of an
amplitude squared yields E a_i^2 at each cycle vertex. This proves (5.2)
without a numerical optimization.

This theorem really does allow mixed cubic moments. For a centered base
eigenfunction f(z),

    E[f(z)(a_i(z)epsilon_i)^2] = E[f(z)a_i(z)^2]

can be nonzero. Those interactions are retained in the positive B factors,
rather than discarded or assumed zero. The added modes can have either
sign and r is arbitrary. The saved rank-three counterexample is consistent:
it permits removing its antisymmetric F mode first, but not arbitrary
removal of the other mode.

## 6. Biased recursive refinements: nonzero skewness as well

Conditional fair signs are not necessary for a second, hierarchical class.
The finite core is the following strengthening of the earlier rank-two
calculation.

### Lemma 6.1 (all induced source graphs)

If L is any bounded nonnegative symmetric 1-regular kernel of rank at most
two, then

    t_(H[S])(L) >= 1 for every S subset V(H).                 (6.1)

### Proof with the complete finite certificate

Write L=1+lambda u tensor u, E u=0, E u^2=1, z=(E u^3)^2.
For an induced graph F=H[S], expansion gives

    P_F(lambda,z)=sum_(e,k) c_F(e,k)lambda^e z^k,

where c_F(e,k) counts its edge subsets with no degree-one vertices,
e selected edges, and 2k vertices of selected degree three. The empty
set gives one. Every c_F is a nonnegative integer, so lambda>=0 is
immediate.

For lambda=-r<0, the rank-two positivity argument gives
0<=z<=(1-r)^2/r. Put z=(1-a)^2/a and r=ay with 0<a<=1, 0<y<=1;
the decreasing bijection a->(1-a)^2/a parametrizes the whole domain.
The polynomial

    [P_F(-ay,(1-a)^2/a)-1]/(a^4 y^4)

has nonnegative tensor-product Bernstein coefficients for every induced
F. The coefficients are computed exactly from all 1024 vertex subsets.
Only ten distinct P_F arise, including the constant polynomial. The nine
nonconstant certificates are summarized here; a vertex mask encodes the
labeling in Section 1.

| Representative mask | Bidegree | Minimum Bernstein coefficient |
|---:|---:|---:|
| 63 | (2,2) | 0 |
| 99 | (0,0) | 1 |
| 127 | (5,4) | 1 |
| 231 | (4,3) | 2 |
| 255 | (8,6) | 2 |
| 447 | (6,5) | 1 |
| 495 | (8,6) | 3 |
| 511 | (11,8) | 3 |
| 1023 | (16,11) | 5 |

For p(a,y)=sum c_uv a^u y^v of degrees at most (n,m), the coefficient is

    beta_ij=sum_(u<=i,v<=j) c_uv binom(i,u)/binom(n,u)
                                  binom(j,v)/binom(m,v).

Every basis function is nonnegative on the unit square and their sum is
one. Thus the displayed coefficient sign proves P_F>=1 on the entire
negative-eigenvalue domain. check.py reconstructs every polynomial from
its full Bernstein coefficients and tests equality of all power
coefficients. It also verifies coverage of all 1024 induced vertex sets,
not just the nine representatives. The zero-eigenvalue case is constant.
This proves (6.1). QED.

### Theorem 6.2 (module replacement)

Let B be a nonnegative finite-step kernel on blocks C_1,...,C_m with
positive measures p_1,...,p_m. For each i with B_ii>0 replace its constant
diagonal block by B_ii L_i, where L_i is a nonnegative symmetric kernel
on C_i with its conditional probability measure. Leave every off-diagonal
block constant at B_ij. If each L_i satisfies (6.1), then

    t_H(W)>=t_H(B).                                         (6.2)

If (6.1) holds for B and each L_i, it also holds for W. If B and each L_i
are 1-regular, W is 1-regular.

### Proof

Condition each vertex of H on its block label c:V(H)->[m]. Its contribution
is

    (product_v p_(c(v)))
    (product_(uv in E(H)) B_(c(u),c(v)))
    product_i t_(H[c^{-1}(i)])(L_i).

Every factor outside the final product is nonnegative, and every factor
in that product is at least one. Summing over c proves (6.2). A zero
diagonal B_ii needs no L_i: assignments containing an edge inside that
block contribute zero and the other assignments have no such factor.
Apply the same argument to H[S] to prove preservation of (6.1), since
its induced subgraphs are again induced subgraphs of H. The weighted
row-sum identity proves preservation of regularity. QED.

### Corollary 6.3 (arbitrarily many biased spectral directions)

Start from any nonnegative symmetric 1-regular two-block kernel. Inside
any diagonal block replace the constant by a scaled nonnegative regular
two-block kernel with arbitrary positive conditional block measures.
Repeat finitely many times, in arbitrary blocks. Every resulting kernel
satisfies t_H(W)>=1 and in fact (6.1). The same holds for uniformly bounded
L^1 limits of these kernels.

Proof: two-block kernels have rank at most two; apply Lemma 6.1 and
Theorem 6.2 inductively. Bounded density continuity proves the limit
statement. QED.

The resulting eigenfunctions are weighted Haar functions on the nested
blocks. A new split is constant on each child and has mean zero on its
parent. Subsequent finer modes are orthogonal to all earlier modes.
Consequently every nonzero split adds a genuine spectral direction. If
phi_C is an ancestor mode and phi_D a normalized descendant mode, then

    E[phi_C phi_D^2]=the constant value of phi_C on D,

which is nonzero. Biased splits also have E phi_D^3 != 0. Thus the
construction is not contained in the older cubic-tensor-zero theorem,
or in the conditionally symmetric subclass of Theorem 5.1.

An exact rank-four example has leaf weights (1/10,1/5,3/10,2/5), orthogonal
mean-zero unnormalized modes

    f0=(7,7,-3,-3), f1=(2,-1,0,0), f2=(0,0,4,-3),

and nonconstant eigenvalues (-1/10,-23/500,-67/400). Set
W_ij=1+sum_k lambda_k f_k(i)f_k(j)/E f_k^2.
This is obtained by a root split (3/10,7/10), followed by child splits
(1/3,2/3) and (3/7,4/7), with conditional child eigenvalues -1/5 and -1/4.
The exact checker verifies positivity, regularity, all eigenvalue
equations, t_H(W)>1, E[f0 f1^2]=21/5 and E f1^3=3/5.

## 7. Why these theorems do not finish the unrestricted conjecture

Equation (3.2) is valid for the whole regular class, but we have only
bounded R by a smallness-dependent error. Theorem 4.1 does not prove
R>=0 or R>=-5s4-10s6-P_+ at arbitrary amplitude. The conditional-sign
and module-replacement theorems give sufficient structures, not a
decomposition of every positive regular kernel into permitted steps.
Generic step kernels have cross-block variation that module replacement
forbids. Generic eigenfunctions do not have the required conditional sign
symmetries. No density or monotonic coarsening theorem bridges that gap.

A natural stronger target suggested by (3.2) is

    t_H(W)>=1+5Tr(U^4)+10Tr(U^6)                              (7.1)

for every nonnegative regular W. Proving P_++R>=0 would establish it and
finish this fixed Sidorenko case. This is an **unproved target**, not an
inference from the local theorem or the experiments. The R>=0 variant is
stronger still and is also unproved. The leading theta payments remove
two actual mixed interactions, but leave 461 labeled terms whose full
collective sign has not been controlled.

The next mathematical task is to group that remainder using positivity of
the whole W, rather than paying its terms by sup-norm bounds. Separate
rank-two optimization, unqualified spectral addition, and arbitrary
conditional averaging are not valid substitutes. The exact previous
counterexamples remain mandatory tests. The supplied structured classes
show one way interactions can be retained without loss; they do not
justify assigning the same sign to generic interactions.
