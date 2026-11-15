# A rectangular crossing criterion for subpolynomial component counts

Consider nearest-neighbour Bernoulli bond percolation on Z^d, d>=2,
at a fixed parameter p in (0,1). Let P and E be its probability and
expectation. Define

    B_n = {x in Z^d : ||x||_infinity<=n},
    partial B_n = {x : ||x||_infinity=n}.

Let K_n be the number of open components of the graph induced by B_{2n}
meeting both B_n and partial B_{2n}. Every finite graph below has free
boundary conditions. Connections used to define components are confined
to the indicated graph.

For an integer n>=1, let R(n) be the probability that the rectangle

    T_n = ([0,n] x [-2n,2n]^{d-1}) intersect Z^d

has an open path from its face x_1=0 to its face x_1=n, contained in T_n.
Write

    delta(n)=1-R(n).

In particular, delta(n)>0. Closing every edge between the slices x_1=0
and x_1=1 prevents a crossing, and has positive probability.

## Theorem 1: explicit finite-scale bounds

For every n>=1 and integer u>=1,

    P(K_n>=u) <= 2d R(n)^{ceil(u/(2d))}
              <= 2d exp[-delta(n) u/(2d)],                  (1)

and

    E K_n <= 2d R(n)/delta(n).                             (2)

There is also a comparison between different scales. For integers
1<=m<=n/8 set

    h=floor(3n/(2m)),
    S(n,m)=(2h+1)^d-(2h-1)^d,
    N(n,m)=2d S(n,m).

Then for every integer u>=1,

    P(K_n>=u) <= N(n,m) R(m)^{ceil(u/N(n,m))},              (3)

and

    E K_n <= N(n,m) R(m)/delta(m)
           <= C_d (n/m)^{d-1}/delta(m),                    (4)

where the explicit choice

    C_d=4d^2 4^{d-1}                                      (5)

is valid. These inequalities hold at every p in (0,1), without an
exponent assumption.

### Disjoint paths in a single rectangle

For a finite rectangle T let A be its open face-to-face crossing event,
and let D(T) be the maximum number of pairwise edge-disjoint open paths
between those faces in T. This variable counts paths, rather than open
components. For an integer k>=1, the event {D(T)>=k} is the disjoint
occurrence of k copies of A: each path's open edges witness one copy.
Conversely, disjoint witnesses for the crossing events contain
edge-disjoint crossing paths. The crossing event is increasing in the
edge configuration.

The van den Berg–Kesten inequality for increasing events under a finite
Bernoulli product measure says that the probability of disjoint
occurrence is at most the product of the probabilities. Applying it
repeatedly gives

    P(D(T)>=k) <= P(A)^k.                                 (6)

Here repeated disjoint occurrence is increasing, and disjoint witnesses
for k+1 copies give disjoint witnesses for the first k and the last
copy, which justifies induction from the two-event inequality.
As D(T) is a nonnegative integer, summing its tail gives

    E D(T) = sum_{k>=1} P(D(T)>=k)
           <= P(A)/(1-P(A))                              (7)

when P(A)<1. No inequality is applied to a component-count event.

### Proof of (1) and (2)

For 1<=i<=d and sigma in {-1,1}, let

    T_{i,sigma}(n) = {x : n<=sigma*x_i<=2n,
                              |x_j|<=2n for j!=i}.

Each is congruent to T_n, by translation and a signed permutation of
coordinates. Put D_{i,sigma}(n)=D(T_{i,sigma}(n)).

In each component counted by K_n, choose an open path in B_{2n}
from B_n to partial B_{2n}. At its final vertex some coordinate has
sigma*x_i=2n; choose one such signed coordinate. Along the chosen path
there is a vertex with sigma*x_i=n, since the starting coordinate is
at most n and steps are nearest-neighbour. Retain the segment after its
last such vertex. Every subsequent vertex has sigma*x_i>=n: a later
value below n would force a return to n before the endpoint. All the
vertices have sigma*x_i<=2n and all transverse coordinates bounded
by 2n. This segment therefore crosses T_{i,sigma}(n) in its short
direction.

Distinct components of B_{2n} are vertex-disjoint. Thus the paths
assigned to a fixed signed coordinate are edge-disjoint. Consequently,
configuration by configuration,

    K_n <= sum_{i=1}^d sum_{sigma in {-1,1}} D_{i,sigma}(n). (8)

If the sum of 2d nonnegative integers is at least u, one of them is
at least ceil(u/(2d)). A union bound and (6) prove the first inequality
in (1). The elementary inequality 1-t<=exp(-t) for 0<t<1 proves
the second. Taking expectations in (8) and using (7) proves (2).
The rectangles can overlap; no independence among them is used.

### Proof of (3)–(5)

Put r=mh and

    Z(n,m)={mv : v in Z^d, ||v||_infinity=h}.

This set has S(n,m) centers. For every z in Z(n,m), the box z+B_{2m}
is contained in B_{2n}. Indeed, the definition of h gives

    3n/2-m < r <= 3n/2,
    r+2m <= 3n/2+2m <= 7n/4 < 2n.                       (9)

It also gives

    r-2m > 3n/2-3m >= 9n/8 > n.                       (10)

Write K_m(z) for the translated free-boundary count: the number of
components of z+B_{2m} meeting z+B_m and partial(z+B_{2m}). We claim

    K_n <= sum_{z in Z(n,m)} K_m(z).                       (11)

For each component counted by K_n choose a crossing path as above.
Since n<r<2n, it hits a vertex y of norm r. Round each coordinate of
y/m to a nearest integer to obtain v and let z=mv. A coordinate
of y/m attaining h or -h is unchanged, and all other rounded
coordinates lie between -h and h. Therefore z belongs to Z(n,m),
and ||y-z||_infinity<=m/2, so y belongs to z+B_m.

The chosen path's endpoint on partial B_{2n} has distance at least
2n-r>=n/2>=4m from z. Follow the path from y to that endpoint, stopping
at its first visit to partial(z+B_{2m}). Its retained part is a path
inside z+B_{2m} from z+B_m to that boundary, and lies in a component
counted by K_m(z).

Assign the original component to the pair (z, this small-box component).
Different components of B_{2n} cannot receive the same pair, because
the small-box connection is contained in B_{2n} by (9). This proves
(11). A component can split into several components on restriction to
a small box; the injection only uses one of them.

Apply (8), translated to center z and with scale m, to every summand
of (11). The resulting deterministic upper bound is a sum of N(n,m)
maximal edge-disjoint path counts, each in a rectangle congruent to T_m.
The union bound and (6) give (3). Taking expectations and using (7)
gives the first bound in (4).

By integrating the derivative of x^d between 2h-1 and 2h+1,

    S(n,m) <= 2d(2h+1)^{d-1}.

Since h<=3n/(2m) and n/m>=8,

    2h+1 <= 3n/m+1 <= 4n/m.

Thus N(n,m)<=4d^2 4^{d-1}(n/m)^{d-1}. Together with R(m)<=1
this proves the second bound in (4) and the constant in (5).

## Corollary 2: a scale-dependent deficit suffices

Suppose

    log(1/delta(n))/log n -> 0.                            (12)

Equivalently, for every b>0, delta(n)>=n^{-b} eventually. Then

    log(1+E K_n)/log n -> 0,                              (H)

and hence

    for every epsilon>0, P(K_n>n^epsilon) -> 0.            (P)

Indeed, (2) gives 1+E K_n<=1+2d/delta(n), which proves (H).
Markov's inequality implies (P). More quantitatively, if epsilon>0,
then delta(n)>=n^{-epsilon/2} for all sufficiently large n. With
u=floor(n^epsilon)+1 in (1),

    P(K_n>n^epsilon)
       <= 2d exp[-n^{epsilon/2}/(2d)]                     (13)

eventually. The threshold may depend on epsilon.

Condition (12) allows R(n) to approach one. For example a bound
delta(n)>=(log n)^{-b}, for a fixed b>0 and all large n, is sufficient.
These are examples of sufficient assumptions, not proved crossing
estimates for critical Z^3.

## Corollary 3: estimates on logarithmically dense scales suffice

It is enough to have an increasing sequence of integers m_j tending
to infinity, with m_j>=2, such that

    log(m_{j+1})/log(m_j) -> 1,
    log(1/delta(m_j))/log(m_j) -> 0.                       (14)

Under (14), (H) and (P) hold at all integer scales n.

For each sufficiently large n choose the largest j with m_j<=n/8,
and put m=m_j. The choice implies

    log m_j <= log(n/8) < log m_{j+1}.

The first limit in (14) squeezes log m/log n to one. Consequently,

    log(n/m)/log n -> 0,
    log(1/delta(m))/log n -> 0.                           (15)

By (4), using C_d>=1, n/m>=1, and delta(m)<=1,

    log(1+E K_n)
       <= log(1+C_d)+(d-1)log(n/m)+log(1/delta(m)).

Divide by log n and use (15). This proves (H), and Markov gives (P).
Thus the criterion requires no deficit estimate at the intervening
scales. For example, m_j=floor(exp(j^2)) has the first property in
(14) although its consecutive scale ratios are unbounded.

## Consequence for the predecessor reductions

At a parameter satisfying either (12) or (14), the exact K_n satisfies
both crossing-count hypotheses used in the predecessor folders. Their
verified theorems therefore apply. In particular, the statements

    pi(n)=P(0 <-> partial B_n)=n^{-a+o(1)}, 0<a<d/2,
    X(n)=sum_{x in B_n}P(0 <-> x)=n^{s+o(1)}, 0<s<d,

are equivalent, with s=d-2a. Whenever either holds,

    P(|C(0)|>=t)=t^{-a/(d-a)+o(1)},
    delta_volume=(d-a)/a.

Here the unqualified connections and C(0) are in the whole lattice;
delta_volume denotes the volume-tail critical exponent and is distinct
from the rectangle deficit delta(n). These are conditional consequences,
not an existence proof for any critical exponent on Z^3. The rectangular
deficit criteria themselves have not been established at p_c on Z^3.

The component-to-disjoint-path comparison and the use of BK for
rectangular crossings are classical; compare C. Borgs, J. T. Chayes,
H. Kesten and J. Spencer, *Uniform Boundedness of Critical Crossing
Probabilities Implies Hyperscaling*, MSR-TR-98-26 (1998), Lemma 4.2:
https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf .
The additions relative to the predecessor folders are the explicit
comparison for their exact K_n, its scale-dependent deficit criterion,
and its sufficient condition using only the sequence (14). No priority
claim over classical conditional hyperscaling is made.
