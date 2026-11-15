# A conditional exponent for the largest free-boundary cluster

Consider nearest-neighbour Bernoulli bond percolation on Z^d, d>=2,
at a fixed parameter p in (0,1). All finite graphs have free boundary
conditions. Write

    B_n={x in Z^d: ||x||_infinity<=n},
    V_n=|B_n|=(2n+1)^d,
    pi(n)=P(0 <-> partial B_n),
    F(t)=P(|C(0)|>=t).

Here C(0) and unqualified connections refer to the whole lattice.
Let M_n be the number of vertices of the largest component of the open
graph induced by B_n. Let K_n be the number of components of the open
graph induced by B_{2n} meeting both B_n and partial B_{2n}. Assume

    pi(n)=n^{-a+o(1)},       0<a<d/2,                    (1)
    P(K_n>n^epsilon)->0 for every epsilon>0.            (P)

Put D=d-a and b=a/D. The verified round 3 theorem gives

    F(t)=t^{-b+o(1)}.                                  (2)

Only logarithmic asymptotics are assumed throughout.

## Theorem

Under (1) and (P),

    log M_n/log n -> D almost surely,                  (3)
    E M_n^r=n^{rD+o(1)} for every fixed r>0.            (4)

More precisely, for every epsilon>0 and A>0, eventually

    P(M_n>n^{D+epsilon}) <= n^{-A}.                     (5)

For every 0<epsilon<D, eventually

    P(M_n<n^{D-epsilon})
      <= exp[-3^{-d} n^{d*epsilon/(8D)}].              (6)

The thresholds implicit in these statements may depend on the displayed
parameters and on the percolation law. There is no assertion of bounded
ratios M_n/n^D, a limiting distribution, or a uniform constant in (4).

## 1. A finite-volume packing bound

Let H be a finite graph with V vertices and maximum degree at most an
integer Delta>=1, with independent Bernoulli edge states. Parameters
may differ between edges. Let M_H be its largest open component size,
and for an integer t>=1 set

    f_H(t)=max_{x in H} P(|C_H(x)|>=t).

For integers k,t>=1,

    P(M_H>=Delta*k*t)
      <= (V*f_H(t)/t)^k/k!.                           (7)

To prove the required deterministic packing, suppose an open component
has at least Delta*k*t vertices. Choose a spanning tree of this component
and root it. In the current rooted tree, select a vertex of greatest
depth among those whose descendant subtree has at least t vertices.
Such a vertex exists whenever the current tree has at least t vertices.
Every child's descendant subtree has fewer than t vertices, by the
choice of depth. Since there are at most Delta children, the selected
subtree S has

    t <= |S| <= 1+Delta*(t-1) <= Delta*t.              (8)

Remove S. If anything remains, it is a connected rooted tree: the only
edge from a descendant subtree to its complement is its parent's edge.
After j<k removals, at least Delta*(k-j)*t vertices remain, because each
removal took at most Delta*t. Thus the construction can be performed
k times. It produces vertex-disjoint sets S_1,...,S_k, each containing
at least t vertices and connected by open tree edges within that set.

For x in H let A_x(t) be the increasing event |C_H(x)|>=t. For an
ordered tuple of distinct vertices (x_1,...,x_k), let I(x_1,...,x_k)
indicate the disjoint occurrence of these k events. The finite-product
van den Berg–Kesten inequality, applied repeatedly to increasing events,
gives

    E I(x_1,...,x_k)
       <= product_{i=1}^k P(A_{x_i}(t)) <= f_H(t)^k.    (9)

For each root x in S_i, the open tree within S_i witnesses A_x(t).
Indeed a connected set of at least t vertices contains a connected
subset of exactly t vertices containing any specified root: start at
that root and repeatedly add an adjacent vertex until t have been
chosen. The chosen tree edges are a finite open witness. The witnesses
from distinct S_i use disjoint edge sets, because the S_i are
vertex-disjoint.

Let Z be the sum of I(x_1,...,x_k) over all ordered tuples of distinct
vertices. On {M_H>=Delta*k*t}, choosing one root from each S_i and
permuting their order gives at least

    k! product_{i=1}^k |S_i| >= k!*t^k

different tuples counted by Z. The tuples are distinct since the S_i
are disjoint. There are at most V^k tuples altogether, so (9) yields

    k!*t^k P(M_H>=Delta*k*t) <= E Z <= V^k f_H(t)^k.

This proves (7). If Delta*k*t>V, the left event is empty and the bound
remains valid. The proof includes t=1; empty witnesses cause no problem.

For H induced by B_n, Delta=2d and f_H(t)<=F(t), by translation
invariance and restriction of whole-lattice clusters. Therefore

    P(M_n>=2d*k*t) <= (V_n*F(t)/t)^k/k!.              (10)

This bound holds without (1), (P), or criticality.

## 2. Upper bounds for all positive moments and for the upper tail

Fix h>0 and put t_n=ceil(n^{D+h}). By (2),

    V_n F(t_n)/t_n
      = n^{d-(D+h)(1+b)+o(1)}
      = n^{-h*d/D+o(1)} -> 0,                        (11)

because 1+b=d/D. In particular this ratio is at most one eventually.
With Delta=2d, (10) gives

    P(M_n>=Delta*k*t_n)<=1/k!, k>=1.                 (12)

Partition the values of M_n into [0,Delta*t_n) and the intervals
[Delta*k*t_n,Delta*(k+1)*t_n), k>=1. For each fixed r>0,

    E M_n^r
      <= (Delta*t_n)^r [1+sum_{k>=1}(k+1)^r/k!]
      = O_r(t_n^r).                                  (13)

The series converges by the ratio test. Consequently

    limsup log E M_n^r/log n <= rD,                   (14)

by letting h decrease to zero after taking the upper limit.

For (5), fix epsilon,A>0. Choose a fixed integer k with
k*epsilon*d/D>A. Set

    t=floor(n^{D+epsilon}/(Delta*k)).

Eventually t>=1, Delta*k*t<=n^{D+epsilon}, and
log t/log n->D+epsilon. Hence

    V_n F(t)/t=n^{-epsilon*d/D+o(1)}.

The event in (5) implies {M_n>=Delta*k*t}. Applying (10) bounds its
probability by n^{-k*epsilon*d/D+o(1)}/k!, which is at most n^{-A}
eventually. The floor, rather than a ceiling, makes this implication
valid at integer thresholds.

## 3. A lower bound for the expectation at all scales

We give the buffered mass argument behind the round 3 lower bound,
including how to pass from its selected scales to every n.

For an integer m>=1 put

    A_m={x: 8m<=||x||_infinity<=16m}.

Let J_m count components of the induced open graph on A_m meeting both
its boundary surfaces. A deterministic shell cover gives

    J_m <= sum_{z in m*partial B_{12}} K_m(z),         (15)

where K_m(z) is the translate of K_m. Here the sum has the fixed number
c_d=25^d-23^d of centers. To verify the cover, take a crossing path in
each annulus component and a vertex y on partial B_{12m}. Round y/m
coordinatewise to the nearest integer and multiply by m to obtain z.
An extremal coordinate is unchanged, so z lies in m*partial B_{12},
and ||y-z||_infinity<=m/2. The box z+B_{2m} lies between radii 10m and
14m, entirely inside A_m. The path toward partial B_{16m} must leave
this small box, since its endpoint is at distance at least 4m from z.
Stopping at its first boundary hit gives a component counted by K_m(z).
Two distinct annulus components cannot use the same small-box component,
since its connecting edges lie inside the annulus. This proves (15).

For e>0 let L_m=ceil(m^e) and q_m=P(J_m>L_m). The union bound and
translation invariance give, eventually,

    q_m <= c_d P(K_m>m^e/c_d)
        <= c_d P(K_m>m^{e/2}) -> 0.                  (16)

Let W_m count x in B_{4m} connected to partial B_{16m} inside B_{16m}.
An arm of length 20m from x reaches that outer boundary, so

    E W_m >= V_{4m} pi(20m).                         (17)

Let U_m count x in B_{4m} connected to partial B_{7m} inside B_{7m}.
Then W_m<=U_m and E U_m<=V_{4m} pi(3m). Moreover U_m depends on edges
inside B_{7m}, while J_m depends on edges inside A_m, so they are
independent. Thus

    E[W_m 1_{J_m>L_m}]
      <= V_{4m} pi(3m) q_m.                          (18)

The box components supplying W_m number at most J_m. For each such
component, take a path from the core to partial B_{16m} and retain
its segment after its last visit to partial B_{8m}. This produces an
annulus crossing component. Distinct box components cannot contain
the same annulus component. On {J_m<=L_m} it follows that

    W_m <= L_m M_{16m}.                              (19)

It remains to select scales at which the arm ratio in (18) is bounded.
Set f_j=pi(3*8^j). Assumption (1) gives

    log f_j=-a*j*log 8+o(j).

Call m=8^j good when f_j/f_{j+1}<=C, with C=8^{a+1}. For every fixed
zeta>0 and all sufficiently large N, there is a good m in
[N,N^{1+zeta}]. Otherwise all ratios with
j from ceil(log_8 N) to floor((1+zeta)log_8 N) would exceed C.
Multiplying them gives a logarithmic drop greater than
(a+1)*zeta*log N+O(1). The displayed asymptotic for f_j gives instead
a*zeta*log N+o(log N), a contradiction. At a good scale,

    pi(3m)/pi(20m) <= pi(3m)/pi(24m) <= C.            (20)

Fix e>0. Eventually q_m<=1/(2C) by (16). Equations (17)–(20) give

    E M_{16m} >= V_{4m} pi(20m)/(2 L_m)
               >= (1/4)m^{D-2e}                     (21)

at all sufficiently large good scales. In the last inequality use
V_{4m}>=m^d, L_m<=2m^e, and pi(20m)>=m^{-a-e}, all valid eventually.

Fix also zeta>0 and choose e<D/2. Given large n, set
N=(n/16)^{1/(1+zeta)} and choose a good m in [N,N^{1+zeta}]. Then
16m<=n. The largest restricted cluster cannot decrease when its box
is enlarged: each earlier component remains connected and may merge
with others. Thus (21) implies

    E M_n >= (1/4)(n/16)^{(D-2e)/(1+zeta)}.

Taking logarithms, then letting e and zeta decrease to zero, gives

    liminf log E M_n/log n >= D.

Together with (14) at r=1, this proves

    E M_n=n^{D+o(1)}.                                (22)

## 4. Lower moments and a probability of seeing a large cluster

For completeness, the elementary second-moment argument gives

    P(M_n>=E M_n/2) >= (E M_n)^2/(4 E M_n^2).        (23)

Indeed E[M_n 1_{M_n>=E M_n/2}]>=E M_n/2. Cauchy–Schwarz bounds
its left side by sqrt(E M_n^2 * P(M_n>=E M_n/2)); square and rearrange.

By (14) at r=2 and (22), for every b_0>0, eventually

    P(M_n>=E M_n/2) >= n^{-b_0}.                     (24)

For clarity, one can bound E M_n below by n^{D-h} and E M_n^2 above
by n^{2D+h}. The right side of (23) is then at least n^{-3h}/4.
Taking 3h<b_0 proves (24). It follows for every r>0 that

    E M_n^r >= (E M_n/2)^r n^{-b_0}.

Use (22), take logarithms, and let b_0 decrease to zero. This gives
the lower bound complementary to (14), proving (4), also for 0<r<1.

## 5. Independent smaller boxes and the lower tail

Fix 0<epsilon<D and set

    delta=epsilon/(4D),   h=epsilon/4,
    m=floor(n^{1-delta}), b_0=d*delta/2.              (25)

By (22) and (24), the event M_m>=E M_m/2 has probability at least
m^{-b_0} eventually, and on this event

    M_m >= (1/2)m^{D-h} >= n^{D-epsilon}              (26)

for all sufficiently large n. To check the last comparison, m is at
least n^{1-delta}/2 eventually, and

    (1-delta)(D-h)-(D-epsilon)
      = epsilon-delta*D-h+delta*h
      >= epsilon/2 >0.                              (27)

Inside B_n place disjoint lattice boxes of side 2m+1 by partitioning
each coordinate interval into consecutive blocks of that length and
discarding the remainder. Each box is an integer translate of B_m.
Their number is

    ell=floor((2n+1)/(2m+1))^d >= (n/(3m))^d
          >= 3^{-d} n^{d*delta}                      (28)

eventually. In fact floor x>=x/2 for x>=1 and 2m+1<=3m imply the
first lower bound. Each box event uses only edges with both endpoints
in that box. These edge sets are disjoint, so the events are independent.
Edges between the boxes are ignored; they can only merge or enlarge
components of B_n.

If any one box has the event in (26), M_n>=n^{D-epsilon}. Therefore,
using 1-u<=exp(-u), m<=n, and (24),

    P(M_n<n^{D-epsilon})
      <= (1-m^{-b_0})^ell
      <= exp[-ell*m^{-b_0}]
      <= exp[-3^{-d} n^{d*delta-b_0}]
       = exp[-3^{-d} n^{d*epsilon/(8D)}].             (29)

This is (6). No independence of overlapping whole-lattice clusters is
asserted; only the restricted configurations in disjoint boxes are used.

## 6. Almost sure limit and the rectangular criterion

For each fixed epsilon in (0,D), the probabilities in (5), with A=2,
and (6) are summable over the positive integers n. The first
Borel–Cantelli lemma therefore gives

    n^{D-epsilon} <= M_n <= n^{D+epsilon}

eventually, almost surely. Intersect these probability-one statements
over a sequence of positive rational epsilon tending to zero. Dividing
their logarithms by log n proves (3). This step does not require
independence between different n.

The round 5 theorem supplies (P), even its expected-count version, if
the no-crossing deficit delta_R(m)=1-R(m) for the rectangle
[0,m] x [-2m,2m]^{d-1} obeys

    log(1/delta_R(m_j))/log m_j -> 0,
    log m_{j+1}/log m_j -> 1                          (30)

along an increasing sequence m_j tending to infinity. Thus (30) plus
(1) is sufficient for every conclusion above. Alternatively, under
(P), the round 4 reverse theorem turns

    X(n)=sum_{x in B_n}P(0<->x)=n^{s+o(1)}, 0<s<d,

into (1) with a=(d-s)/2. In that formulation

    D=(d+s)/2.

For d=3, the conditional largest-cluster exponent is 3-1/rho, or
(3+s)/2. No assumption in (1), (P), or (30) is proved here at the
critical parameter on Z^3. No near-critical exponent or pointwise
two-point exponent follows from this finite-volume conclusion.

Largest-cluster estimates and conditional hyperscaling are classical;
compare C. Borgs, J. T. Chayes, H. Kesten and J. Spencer, *Uniform
Boundedness of Critical Crossing Probabilities Implies Hyperscaling*,
MSR-TR-98-26 (1998), Sections 5–6:
https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf .
The extension relative to the predecessor folders is (3)–(6), with the
explicit packing estimate (7), under their probabilistic count
hypothesis and logarithmic exponent convention. No priority claim over
the literature is made.
