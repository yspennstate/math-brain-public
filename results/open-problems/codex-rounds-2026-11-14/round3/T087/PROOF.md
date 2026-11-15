# A volume-tail exponent from subpolynomial crossing counts in probability

Consider nearest-neighbour Bernoulli bond percolation on Z^d, d>=2,
at a fixed parameter p in (0,1). Write P and E for probability and
expectation. Let

    B_n = {x : ||x||_infinity <= n},
    partial B_n = {x : ||x||_infinity = n},
    V_n = (2n+1)^d,
    pi(n) = P(0 <-> partial B_n),
    tau(x) = P(0 <-> x),
    X(n) = sum_{x in B_n} tau(x),
    F(t) = P(|C(0)| >= t),   t>0.

Connections without a specified domain are in the whole lattice. A
connection to the boundary of a box can be witnessed inside that box by
stopping a nearest-neighbour path at its first boundary visit. The cluster
C(0) is the whole-lattice cluster, and its size is its number of vertices.

Let K_n be the number of open components in the graph induced by B_{2n}
that meet both B_n and partial B_{2n}. All finite graphs below have free
boundary conditions. For z in Z^d, let K_n(z) denote the translated count
in z+B_{2n}, with inner box z+B_n.

## Theorem

Suppose that, for some a with 0<a<d/2,

    pi(n) = n^{-a+o(1)},                              (1)

and that the crossing count is subpolynomial in probability:

    for every epsilon>0, P(K_n > n^epsilon) -> 0.      (P)

Then the volume-tail exponent exists and

    F(t) = t^{-a/(d-a)+o(1)} as t -> infinity.         (2)

In particular, with the convention F(t)=t^{-1/delta+o(1)},

    delta = (d-a)/a = d rho - 1,   rho=1/a.          (3)

Also

    X(n) = n^{d-2a+o(1)}.                            (4)

These are logarithmic limits. No uniform scale-ratio estimate is assumed.
The hypotheses have not been proved at p_c on Z^3.

The expected-count hypothesis of the earlier report implies (P). Indeed,
if E K_n <= n^{epsilon/2} eventually, Markov's inequality gives
P(K_n>n^epsilon) <= n^{-epsilon/2}. Tightness of K_n also implies (P).
No converse implication to an expected-count bound is used.

## 1. Upper estimates requiring no crossing-count assumption

Put pi(0)=1. If ||x||_infinity=r>=1 and h=floor(r/3), a connection
0<->x implies an arm from each endpoint to the boundary of its own box
of radius h. When h>=1 the two boxes have disjoint vertex sets, since
2h<r, so the arm events depend on disjoint sets of edges. Each has
probability pi(h). When h=0 the following bound is trivial. Thus

    tau(x) <= pi(floor(r/3))^2.                       (5)

There are (2r+1)^d-(2r-1)^d <= b_d r^{d-1} vertices at distance r,
where b_d is a finite constant depending only on d.
For any e>0, (1) and (5), with the finitely many small radii absorbed in
a constant, give

    X(n) <= C_e [1+sum_{r=1}^n r^{d-1-2a+2e}]
         <= C'_e n^{d-2a+2e}.                        (6)

The last sum bound follows by splitting into dyadic intervals; it applies
because d-2a+2e>0. Consequently

    limsup log X(n)/log n <= d-2a.                   (7)

For every integer n>=1 and real t>0,

    F(t) <= pi(n) + X(n)/t.                          (8)

To see this, split according to whether 0 reaches partial B_n. If it does
not, its entire cluster lies inside B_n, so on {|C(0)|>=t} its intersection
with B_n has at least t vertices. Markov's inequality bounds this second
event by E|C(0) intersect B_n|/t=X(n)/t.

Write D=d-a. Choose n=floor(t^{1/D}). By (1) and (6), the two terms on
the right of (8) are at most t^{-a/D+o(1)}: the exponent of the second is

    (d-2a)/D - 1 = -a/D.

Their sum therefore satisfies

    liminf [-log F(t)]/log t >= a/D.                 (9)

## 2. A buffered annulus controlled by the exact K_m

For an integer m>=1 set

    A_m = {x : 8m <= ||x||_infinity <= 16m}.

In the open graph induced by A_m, let J_m count components meeting both
partial B_{8m} and partial B_{16m}. Define the finite set of centers

    Z_m = {m v : v in Z^d, ||v||_infinity=12},
    c_d = |Z_m| = 25^d-23^d.

The count |Z_m| is independent of m. There is a deterministic inequality

    J_m <= sum_{z in Z_m} K_m(z).                    (10)

For its proof, choose a crossing path in each component counted by J_m.
Such a path visits a vertex y on partial B_{12m}. Round each coordinate
of y/m to a nearest integer to obtain v. A coordinate attaining 12 or
-12 is unchanged, and all other rounded coordinates remain in [-12,12].
Thus z=mv belongs to Z_m, and ||y-z||_infinity<=m/2<=m.

Every vertex w in z+B_{2m} satisfies

    10m <= ||w||_infinity <= 14m,

so this entire box lies in A_m. Follow the chosen path from y towards its
endpoint on partial B_{16m}. That endpoint is at distance at least 4m
from z. Before leaving z+B_{2m} the path therefore hits its boundary.
Its initial segment is a connection in z+B_{2m} from a vertex in z+B_m
to the outer boundary. It belongs to a component counted by K_m(z).

Assign the annulus component to one such pair (z, small-box component).
Distinct annulus components cannot be assigned the same pair: a
connection inside the small box would also connect them inside A_m.
This proves (10). Components of a single annulus cluster may split
inside a small box; the argument needs only the stated injection.

By translation invariance all K_m(z) have the law of K_m. The union
bound in (10) gives, for each epsilon>0 and all sufficiently large m,

    P(J_m>m^epsilon)
       <= c_d P(K_m>m^epsilon/c_d)
       <= c_d P(K_m>m^{epsilon/2}) -> 0.              (11)

No independence between the different small-box counts is needed.

## 3. Scales with a bounded arm ratio

Let f_j=pi(3*8^j), j>=0. From (1),

    log f_j = -a j log 8 + o(j).                     (12)

Call m=8^j good if

    f_j/f_{j+1} <= C,   C=8^{a+1}.                  (13)

For each fixed zeta>0 and all sufficiently large real N, there is a good
m in [N,N^{1+zeta}]. Suppose otherwise. Put

    j_0=ceil(log N/log 8),
    j_1=floor((1+zeta)log N/log 8).

Every j in [j_0,j_1] would violate (13), and multiplication would give

    log(f_{j_0}/f_{j_1+1})
       > (a+1)(j_1+1-j_0) log 8.                    (14)

But (12) gives for the same left side

    a(j_1+1-j_0) log 8 + o(log N).

Since (j_1+1-j_0)log 8=zeta log N+O(1), (14) is impossible for large N.
This proves the assertion. At each good scale monotonicity of pi gives

    pi(3m)/pi(20m) <= pi(3m)/pi(24m)
                  = f_j/f_{j+1} <= C.               (15)

Only selected scales have (15); no assertion about all fixed-ratio
comparisons follows from (1).

## 4. A lower bound for the expected largest cluster at good scales

Let M_m be the size of the largest open component in B_{16m}. Let W_m
count the vertices x in B_{4m} connected to partial B_{16m} by paths in
B_{16m}. For such x, a connection to the boundary of x+B_{20m} must
hit partial B_{16m}, because any endpoint y has

    ||y||_infinity >= ||y-x||_infinity-||x||_infinity >= 16m.

Its first boundary hit supplies the required restricted path. Hence

    E W_m >= V_{4m} pi(20m).                         (16)

The components in B_{16m} containing the vertices counted by W_m all
cross the annulus A_m. More precisely, in a path from B_{4m} to
partial B_{16m}, take its last visit to partial B_{8m} before its final
endpoint. Its remaining segment lies in A_m, and lies in one of the
J_m annulus components. Two different B_{16m} components cannot contain
the same annulus component. Therefore, for any L>0,

    W_m <= L M_m on {J_m<=L}.                        (17)

For the exceptional event, let U_m count the x in B_{4m} connected to
partial B_{7m} inside B_{7m}. Then W_m<=U_m. Each such connection
implies an arm of length 3m from x, so

    E U_m <= V_{4m} pi(3m).                          (18)

U_m is a function of edges with both endpoints in B_{7m}. J_m is a
function of edges with both endpoints in A_m, whose vertices have norm
at least 8m. These deterministic edge sets are disjoint. Product
independence, applied to U_m and the event {J_m>L}, gives

    E[W_m 1_{J_m>L}]
       <= E U_m * P(J_m>L)
       <= V_{4m} pi(3m) P(J_m>L).                   (19)

This does not assert independence of W_m and J_m.

Fix epsilon>0 and put L=ceil(m^epsilon). By (11), eventually
P(J_m>L)<=1/(2C). At good scales (15), (16), and (19) imply

    E[W_m 1_{J_m<=L}] >= (1/2)V_{4m} pi(20m).

Taking expectations in (17) now gives the explicit bound

    E M_m >= V_{4m} pi(20m)/(2 ceil(m^epsilon))      (20)

for all sufficiently large good m. By (1), pi(20m)>=m^{-a-epsilon}
eventually, while V_{4m}>=m^d and ceil(m^epsilon)<=2m^epsilon. Thus

    E M_m >= (1/4)m^{D-2epsilon}.                    (21)

The threshold after which this holds can depend on epsilon. No
expectation of J_m or K_m appears in (19)–(21).

## 5. From largest-cluster mass to the volume tail

For any real q>0 and each configuration in B_{16m},

    sum_{x in B_{16m}} 1_{|C_{B_{16m}}(x)|>=q}
       >= M_m 1_{M_m>=q}.

Indeed, if the largest component has at least q vertices, all of its
vertices appear in the sum. Taking expectations, using
M_m 1_{M_m<q}<=q, and using unrestricted cluster size as an upper bound
on restricted cluster size, yields

    V_{16m} F(q) >= E M_m-q.                         (22)

Translation invariance is applied to the unrestricted size at x; no
translation invariance within the finite box is asserted.

Choose epsilon with 0<3epsilon<D and set q=m^{D-3epsilon}. By (21),
at all sufficiently large good scales E M_m>=2q and
E M_m-q >= (1/8)m^{D-2epsilon}. Since V_{16m}<=(33m)^d, (22) gives

    F(m^{D-3epsilon})
       >= [1/(8*33^d)]m^{-a-2epsilon}
       >= m^{-a-3epsilon}                           (23)

for all sufficiently large good m.

To cover every large real t, fix zeta>0 and put
N=t^{1/(D-3epsilon)}. Section 3 supplies a good m in
[N,N^{1+zeta}]. Since m^{D-3epsilon}>=t and F is decreasing, (23) gives

    F(t) >= F(m^{D-3epsilon}) >= m^{-a-3epsilon}
         >= t^{-(1+zeta)(a+3epsilon)/(D-3epsilon)}.

Thus

    limsup [-log F(t)]/log t
       <= (1+zeta)(a+3epsilon)/(D-3epsilon).

First let zeta decrease to zero, and then epsilon decrease to zero.
Together with (9) this proves (2) and (3). Since a>0, (1) also implies
P(|C(0)|=infinity)=lim_n pi(n)=0; an atom at infinity is absent.

## 6. Recovering the averaged two-point exponent

For any n>=1 and t>0, splitting {|C(0)|>=t} according to the arm event
gives the other direction of the estimate used in (8):

    X(n) >= t [F(t)-pi(n)].                         (24)

On {|C(0)|>=t} without an arm to partial B_n, the entire cluster is
in B_n and contributes at least t to its intersection. The probability
of that event is at least F(t)-pi(n), which proves (24).

Fix h in (0,1) and take t=n^{(1-h)D}. By (2),

    F(t)=n^{-(1-h)a+o(1)},
    pi(n)/F(t)=n^{-ha+o(1)} -> 0.

It follows from (24) that

    X(n) >= (1/2)t F(t)
          = n^{(1-h)(d-2a)+o(1)}.

Let h decrease to zero and combine with (7). This proves (4).

## Relation to classical conditional hyperscaling

The relation delta=d rho-1 and the use of annular multiplicity are
classical. C. Borgs, J. T. Chayes, H. Kesten and J. Spencer,
*Uniform Boundedness of Critical Crossing Probabilities Implies
Hyperscaling*, MSR-TR-98-26 (1998), treat conditional hyperscaling and
buffered inner/outer independence; see Section 5 and equations
(5.36)–(5.39). Their exponent convention in (2.23)–(2.28) includes a
scale-ratio condition stronger than a logarithmic limit. The proof above
is a formulation for the exact free-boundary K_n of the earlier report,
with (P) and logarithmic exponent existence. It makes no priority claim.

Source opened: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf .

In d=3 the conclusion is delta=3rho-1. Neither (1) nor (P) is established
here for critical cubic-lattice percolation. No uniform pointwise
two-point exponent, near-critical exponent, or numerical value follows.
