# A finite-scale reduction of critical hyperscaling

Consider nearest-neighbour Bernoulli bond percolation on Z^d, d ≥ 2, at a fixed parameter p in (0,1). Write P and E for its probability and expectation. All connections without a specified domain are in the whole lattice. Put

    B_n = {x in Z^d : ||x||_infinity ≤ n},
    ∂B_n = {x : ||x||_infinity = n},
    V_n = |B_n| = (2n+1)^d,
    π(n) = P(0 ↔ ∂B_n),     π(0) = 1,
    τ(x) = P(0 ↔ x),
    X(n) = sum_{x in B_n} τ(x) = E|C(0) ∩ B_n|.

The notation X distinguishes spatial truncation at p from susceptibility as a function of p. Paths contributing to X(n) may leave B_n.

In dimension three the shell factor in (2) below is exactly 24r^2+2.

In the induced open subgraph on B_{2n}, let K_n be the number of connected components meeting both B_n and ∂B_{2n}, and put k(n) = E K_n. Distinct components here can be connected outside B_{2n}. This defines a finite-volume observable with free boundary conditions. At p in (0,1), k(n)>0, since any particular finite crossing path has positive probability of being open.

## Proposition 1: finite-scale bounds

For every integer n ≥ 1,

    X(2n) ≥ V_n π(3n)^2 / k(n).                         (1)

For every integer R ≥ 1,

    X(R) ≤ 1 + sum_{r=1}^R [(2r+1)^d − (2r−1)^d]
                              π(floor(r/3))^2.         (2)

For integers N>m≥1,

    X(N) − X(m) ≤ V_N π(floor(m/3))^2.                 (3)

These bounds require neither p=p_c nor continuity at p_c.

### Proof of (1)

List the K_n crossing components of the induced graph on B_{2n}. Let s_i be the number of vertices of component i in B_n. Set

    W = sum_{i=1}^{K_n} s_i,     Q = sum_{i=1}^{K_n} s_i^2.

Empty sums are zero. Thus W counts vertices x in B_n connected to ∂B_{2n} by paths contained in B_{2n}.

For x in B_n, a path from x to ∂(x+B_{3n}) must hit ∂B_{2n}. Indeed, any endpoint y on the translated boundary satisfies

    ||y||_infinity ≥ ||y−x||_infinity − ||x||_infinity ≥ 2n.

The nearest-neighbour path starts in B_n, so its initial segment up to the first hit of ∂B_{2n} lies in B_{2n}. Translation invariance therefore gives

    E W = sum_{x in B_n} P(x ↔ ∂B_{2n} in B_{2n})
        ≥ V_n π(3n).                                  (4)

For each configuration, Cauchy–Schwarz for the finite list (s_i) gives W^2 ≤ K_n Q. Hence a second application of Cauchy–Schwarz, this time to random variables, gives

    (E W)^2 ≤ (E sqrt(K_n Q))^2 ≤ k(n) E Q.           (5)

No independence between K_n and Q is asserted or needed.

The variable Q counts ordered pairs (x,y) in B_n lying in the same crossing component. Each such pair is connected in the whole lattice. Consequently,

    E Q ≤ sum_{x,y in B_n} P(x ↔ y)
        = sum_{x in B_n} sum_{y in B_n} τ(y−x)
        ≤ V_n X(2n),                                  (6)

because y−x belongs to B_{2n}. Combine (4), (5), and (6), and divide by the positive number V_n k(n). This proves (1).

### Proof of (2) and (3)

Take x with r=||x||_infinity≥1 and let h=floor(r/3). If h≥1, the vertex sets B_h and x+B_h are disjoint, since 2h<r. The events that 0 connects to ∂B_h inside B_h and x connects to ∂(x+B_h) inside x+B_h are therefore functions of disjoint edge sets and are independent. A connection from 0 to x implies both events: follow a connecting path from either endpoint until it first reaches the boundary of its respective box. Each event has probability π(h), since reaching a box boundary can always be witnessed before first leaving that box. Thus

    τ(x) ≤ π(floor(r/3))^2.                           (7)

If h=0, (7) follows from τ(x)≤1=π(0)^2. Summing (7) over the shell ∂B_r, which has (2r+1)^d−(2r−1)^d vertices, proves (2), with τ(0)=1 supplying the initial term.

For r>m, monotonicity of π gives π(floor(r/3))≤π(floor(m/3)). Sum (7) over B_N minus B_m and bound the number of summands by V_N. This proves (3).

## Theorem 2: existence transfers between two critical observables

Suppose

    for every ε>0, k(n) ≤ n^ε for all sufficiently large n.     (H)

Equivalently, log(1+k(n))/log n tends to zero. Then the following statements are equivalent:

1. There is a number a in (0,d/2) such that π(n)=n^{−a+o(1)}.
2. There is a number s in (0,d) such that X(n)=n^{s+o(1)}.

Whenever either statement holds, both hold and

    s = d − 2a.                                       (8)

Here all exponents denote logarithmic limits only. No regular variation or uniform comparison between π(m)/π(n) and a power of m/n is assumed.

### Proof that 1 implies 2

Fix ε>0. For all sufficiently large integers r, the first assumption gives π(r)≤r^{−a+ε}. For r≥6, floor(r/3)≥r/6. After increasing a constant to absorb the finitely many smaller r, (2) gives

    X(R) ≤ C_ε [1 + sum_{r=1}^R r^{d−1−2a+2ε}]
         ≤ C'_ε R^{d−2a+2ε}.                         (9)

For completeness, the shell bound follows from the mean value theorem:

    (2r+1)^d − (2r−1)^d ≤ 2d(2r+1)^{d−1} ≤ 2d 3^{d−1} r^{d−1}.

The exponent u=d−2a+2ε is positive. The bound sum_{r≤R} r^{u−1}≤C_u R^u follows by splitting into dyadic ranges R/2^{j+1}<r≤R/2^j, bounding each range by a constant times (R/2^j)^u, and summing the resulting geometric series. This justifies the last step of (9).

Using (1), the lower bound π(3n)≥(3n)^{−a−ε}, and (H), for all sufficiently large n,

    X(2n) ≥ (2n+1)^d (3n)^{−2a−2ε} n^{−ε}
           ≥ c_ε n^{d−2a−3ε}.                        (10)

For any large R take n=floor(R/2). Then 2n≤R and n is comparable to R, so monotonicity of X extends (10) to every large R. Equations (9) and (10), followed by ε decreasing to zero, yield log X(R)/log R → d−2a. This is in (0,d), as required.

### Proof that 2 implies 1

From (1), (H), and X(2n)=n^{s+o(1)},

    π(3n)^2 ≤ k(n) X(2n)/V_n ≤ n^{s−d+o(1)}.         (11)

For an arbitrary large integer r use n=floor(r/3). Since r≥3n and π is decreasing, (11) gives

    liminf_{r→∞} [−log π(r)]/log r ≥ (d−s)/2.         (12)

For the opposite inequality fix t in (0,1). For each integer n let

    m=3n,     N=ceil((3n)^{1/t}).

Then log m/log N→t. The assumed exponent of X gives

    log[X(m)/X(N)]/log N → ts−s = −s(1−t)<0.

In particular X(m)≤X(N)/2 for all sufficiently large n. Applying (3), with floor(m/3)=n, gives

    π(n)^2 ≥ [X(N)−X(m)]/V_N ≥ X(N)/(2V_N)
            = N^{s−d+o(1)}.

Since log N/log n→1/t, this implies

    limsup_{n→∞} [−log π(n)]/log n ≤ (d−s)/(2t).       (13)

The inequality is valid for each t<1. Let t increase to one and combine (12) and (13). The limit exists and equals a=(d−s)/2, which lies in (0,d/2). This proves the theorem.

## Corollary 3: a quantitative obstruction to hyperscaling

Suppose π(n)=n^{−a+o(1)} and X(n)=n^{s+o(1)}, with 0<a<d/2. Do not assume (H). Then

    s ≤ d−2a,
    k(n) ≥ n^{d−2a−s+o(1)}.                          (14)

The first assertion follows from the proof of (9), which did not use (H). The second follows by rearranging (1):

    k(n) ≥ V_n π(3n)^2 / X(2n).

In particular, if a uniform pointwise logarithmic exponent exists,

    τ(x)=||x||_infinity^{−b+o(1)} as ||x||_infinity→∞,
    with 0<b<d,

then X(n)=n^{d−b+o(1)}. The upper bound follows by summing the uniform estimate τ(x)≤||x||^{−b+ε}; the lower bound follows by summing τ(x)≥||x||^{−b−ε} over B_n minus B_{floor(n/2)}, which has at least c_d n^d vertices. Taking ε to zero proves the asserted exponent. Therefore (14) becomes

    b ≥ 2a,
    k(n) ≥ n^{b−2a+o(1)}.                            (15)

In the usual critical notation a=1/ρ and b=d−2+η. Under (H), Theorem 2 and the preceding shell argument give

    d−2+η = 2/ρ,                                    (16)

provided the pointwise exponent exists with 0<d−2+η<d. Theorem 2 itself only supplies a spatially averaged exponent; it does not supply pointwise asymptotics.

In dimension three, (16) reads 1+η=2/ρ. If, in addition, one independently proves near-critical matching β=ν/ρ and γ=ν(2−η), then

    γ+2β = ν(2−η+2/ρ) = 3ν.

The near-critical matching relations and the hypotheses of Theorem 2 are not proved here for Z^3.

## Corollary 4: the supremum two-point exponent also exists

Define the envelope

    M(n) = sup{τ(x) : ||x||_infinity ≥ n}.

Under (H) and either equivalent hypothesis of Theorem 2,

    M(n) = n^{−2a+o(1)}.                             (17)

Indeed, (7) and monotonicity imply

    M(n) ≤ π(floor(n/3))^2 = n^{−2a+o(1)}.

For the reverse bound, fix t in (0,1), let N=ceil(n^{1/t}), and recall X(r)=r^{s+o(1)} with s=d−2a>0. Then X(n−1)/X(N)→0, so

    V_N M(n) ≥ X(N)−X(n−1) ≥ X(N)/2

for all sufficiently large n. It follows that

    limsup_{n→∞} [−log M(n)]/log n ≤ (d−s)/t = 2a/t.

Let t increase to one and use the upper bound on M for the opposite logarithmic inequality. This proves (17). It proves an exponent for a supremum over positions, not a uniform pointwise exponent. No lower bound for τ(x) at every prescribed x follows from this argument.

## Relation to earlier work

The geometric connection between multiplicity of macroscopic clusters and hyperscaling is classical. Michael Aizenman, *On the Number of Incipient Spanning Clusters*, arXiv:cond-mat/9609240v4, discusses subpolynomial multiplicity and hyperscaling: https://arxiv.org/html/cond-mat/9609240v4 . C. Borgs, J. T. Chayes, H. Kesten and J. Spencer, *Uniform Boundedness of Critical Crossing Probabilities Implies Hyperscaling*, MSR-TR-98-26, prove more extensive conditional hyperscaling results: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf .

The result above is a self-contained finite-scale formulation and a transfer of logarithmic exponent existence in both directions for π and X, with a further consequence for M. It establishes no new numerical exponent and makes no claim of priority over these works. Its unresolved geometric input in dimension three is (H).
