# A four-lineage criterion and the exclusion of disjoint merger bursts

The results here are auxiliary criteria for the N-BBM genealogy conjecture.
No asymptotic estimate for N-BBM is proved.

## 1. Setting and notation

Let Pi_n be an exchangeable, right-continuous coarsening partition process
on {1,2,3,4}, starting from four singletons. Assume every jump merges exactly
two current blocks and eventual absorption occurs at a finite time. Write

    S_n = inf{t: #Pi_n(t) <= 3},
    U_n = inf{t: #Pi_n(t) <= 2},
    V_n = inf{t: #Pi_n(t) = 1},
    H_n = U_n-S_n,       G_n = V_n-U_n.

Thus S_n<U_n<V_n, with positive H_n,G_n. Let D_n be one if the partition
between U_n and V_n consists of two pairs, and zero if it has sizes 3+1.
Exchangeability means invariance under permutations of the sample labels.
It does not mean invariance of particles ranked by spatial position.

Let B_4 be the four-label Bolthausen–Sznitman coalescent with specified
k-block merger rate, when b blocks remain,

    lambda_(b,k) = integral_0^1 x^(k-2)(1-x)^(b-k) dx.

The pair merger rate for b=2 is one. This is the normalization in Section 1.3
of [Julien Berestycki, Nathanaël Berestycki and Jason Schweinsberg,
The genealogy of branching Brownian motion with absorption,
arXiv:1001.2337v3](https://arxiv.org/html/1001.2337v3).
All formulas below follow directly from this definition.

For B_4 use the same threshold times S,U,V and H=U-S, G=V-U.
These holding times may be zero. Define D=1 if G>0 and the two-block
partition has sizes 2+2; otherwise set D=0.

## 2. The criterion

For nonnegative s,r,q put

    F_n(s,r,q) = E exp(-s S_n-r H_n-q G_n),
    M_n(s,r,q) = E[D_n exp(-s S_n-r H_n)(1-exp(-q G_n))].

**Theorem.** Pi_n converges in finite-dimensional distributions to B_4 if
and only if, for every s,r,q>=0, both limits below hold:

    F_n(s,r,q) -> F(s,r,q)
      = 1/(s+3) [1/3 + 2/(3(q+1))
                         + (1+3/(q+1))/(r+2)],              (1)

    M_n(s,r,q) -> M(s,r,q)
      = q/[(q+1)(s+3)(r+2)].                                (2)

No Markov property is assumed for Pi_n. The factor 1-exp(-qG_n) in (2)
removes information about a two-block state that disappears in the limit.
The unweighted mark D_n need not converge on {G=0}.

For N-BBM, take a uniform ordered sample of four distinct particles and
measure backward time in units a_N=kappa(log N)^3. Branching times are
distinct almost surely, each ancestral identification is binary, and sample
relabelling gives exchangeability. Spatial crossings do not identify
ancestors. If only a history of length L_N is given, require L_N/a_N to
tend to infinity and complete the genealogy after that history with
exchangeable binary mergers. This changes no fixed bounded time window.
Neither kappa nor the required limits (1)–(2) are calculated here.

## 3. Calculation of the target law

At four blocks, the specified pair, triple and quadruple rates are

    lambda_(4,2) = integral_0^1 (1-x)^2 dx = 1/3,
    lambda_(4,3) = integral_0^1 x(1-x) dx = 1/6,
    lambda_(4,4) = integral_0^1 x^2 dx = 1/3.

The total rate is 6/3+4/6+1/3=3. Hence S is Exp(3), independently of the
first jump type. The total rates for first jumps of size two, three and
four are 2, 2/3 and 1/3. After a pair jump, the three remaining blocks have
total rate 2: the triple rate is 1/2 and the three pair rates total 3/2.
At two blocks the holding time is Exp(1).

There are four possible block-count routes. Their probabilities and holding
times after S are:

| Route | Probability | H | G |
|---|---:|---|---|
| 4 to 1 | 1/9 | 0 | 0 |
| 4 to 2 to 1 | 2/9 | 0 | Exp(1) |
| 4 to 3 to 1 | 1/6 | Exp(2) | 0 |
| 4 to 3 to 2 to 1 | 1/2 | Exp(2) | Exp(1) |

Conditional on each route, displayed positive holding times are independent
of one another and of S. Multiplying their transforms gives

    F = [3/(s+3)] [1/9 + 2/(9(q+1))
                     + (1/6)2/(r+2)
                     + (1/2)2/((r+2)(q+1))],

which simplifies to (1). The route probabilities sum to one.

Only the last route can visit a 2+2 state. After the first pair, say {1,2},
the three blocks are {1,2},{3},{4}. Their pair rates are all 1/2. Of these
three choices only merging {3} with {4} produces 2+2. Its conditional
probability among pair jumps is 1/3. Therefore

    P(D=1) = (1/2)(1/3) = 1/6.

More precisely, summing over the six possible first pairs gives

    P(S in du,H in dv,G in dw,D=1)
        = exp(-3u-2v-w) du dv dw,   u,v,w>0.                 (3)

Indeed the summed first-pair density is 2exp(-3u), the density for merging
the two singleton blocks next is (1/2)exp(-2v), and the final holding density
is exp(-w). Integration against exp(-su-rv)(1-exp(-qw)) proves (2).

## 4. A finite-sample reconstruction lemma

For a coarsening process on k labels with finite absorption time, let

    T_ij = inf{t: i and j belong to the same block},  i<j.

Suppose a proposed limiting coarsening process has finite pair times with
continuous marginal distributions. Then finite-dimensional convergence of
the partition processes is equivalent to joint weak convergence of the
vector (T_ij).

To prove the forward implication, for arbitrary nonnegative t_ij use

    {T_ij<=t_ij for all i<j}
       = intersection_(i<j) {i and j share a block at t_ij}.

Finite-dimensional convergence gives convergence of these probabilities.
The target joint CDF is continuous: a change of thresholds can affect it
only when some coordinate lies between its old and new thresholds, whose
probability tends to zero by marginal continuity. The vectors are tight,
since the probability some T_ij exceeds R is bounded by the sum of the
coordinate tail probabilities. Each such probability converges at fixed R
and the limiting sum tends to zero as R tends to infinity. The joint CDF
criterion now gives joint weak convergence.

Conversely, i and j share a block at time t exactly when T_ij<=t.
Thresholding the vector at finitely many deterministic times is continuous
except where a coordinate equals one of those times. The limiting probability
of that exceptional set is zero. The continuous mapping theorem gives the
reverse implication.

For B_4 these assumptions hold. Each restricted pair has constant merger
rate one: while its two blocks are distinct among b current blocks, their
total identification rate is

    sum_(k=2)^b choose(b-2,k-2) lambda_(b,k)
      = integral_0^1 [x+(1-x)]^(b-2) dx = 1.

Consequently each T_ij is Exp(1).

For four labels S is the smallest of the six pair times, U the second
smallest counting multiplicity, and V the largest. Indeed four blocks have
zero identified pairs, three blocks have exactly one, and at most two blocks
have at least two. Order statistics are continuous functions of the vector.

## 5. Necessity of (1)–(2)

Suppose Pi_n converges in finite-dimensional distributions to B_4. The lemma
and the order-statistic observation give

    (S_n,H_n,G_n) -> (S,H,G).

Bounded continuous test functions give (1). To obtain (2), regard its
integrand as a function of the pair-time vector. When G>0, the partition at
the midpoint (U+V)/2 has exactly two blocks. Its shape is stable under small
perturbations of a valid pair-time vector: the midpoint is separated from
every pair time. Thus D is locally constant there. When G=0, the factor
1-exp(-qG) is zero, and its absolute value tends to zero under perturbation,
irrespective of D. Hence the whole integrand is bounded and continuous on
the set of finite pair-time vectors of coarsening partitions. Weak convergence
and (3) give (2).

## 6. Sufficiency of (1)–(2)

First (1) implies weak convergence of the time vector. For clarity, set
Y_n=(exp(-S_n),exp(-H_n),exp(-G_n)). Integer s,r,q in (1) determine all its
monomial moments. Polynomial approximation on [0,1]^3 gives weak convergence
of Y_n to the target exponential time vector. The target coordinates are
strictly positive almost surely; taking negative logarithms gives

    (S_n,H_n,G_n) -> (S,H,G).                                (4)

The quadruples (S_n,H_n,G_n,D_n) are tight. Take any weakly convergent
subsequence, with limit (S,H,G,D*). Its time marginal is fixed by (4).
Equation (2) holds for this limit because its integrands are bounded and
continuous in the time coordinates and in the discrete coordinate D.

Define the finite measure

    nu*(A) = E[D*(1-exp(-G)) 1_{(S,H,G) in A}].

Its Laplace transform at (s,r,q) equals

    M(s,r,q+1)-M(s,r,q)
       = 1/[(s+3)(r+2)(q+1)(q+2)].                          (5)

The identity follows by subtracting 1-exp(-qG) from
1-exp(-(q+1)G). Laplace transforms uniquely determine these finite measures:
push forward by coordinatewise exponentiation to the compact cube and use
the polynomial approximation argument again. Total mass is included by
the zero exponents. The target measure obtained from (3) has transform (5).
Therefore nu* equals that target measure. Since 1-exp(-G)>0 on {G>0},
division by this factor shows that the joint submeasure with D*=1 on
{G>0} is exactly (3). Together with the time marginal this determines the
whole marked law on {G>0}. The law of D* on {G=0} is left free.

It remains to check that these are all the data needed to reconstruct the
partitions. A complete binary four-label chain has one of two forms:

- D_n=1: first merge a pair J, then its complementary pair, then all blocks;
- D_n=0: first merge J, then merge that block with one of the two remaining
  singletons, then all blocks.

For D_n=1 the six possible chains form one orbit under label permutations;
for D_n=0 the twelve possible chains form one orbit. Exchangeability makes
each chain equally likely conditional on the time vector and its shape.
Formally, the probability of a time Borel set and a specified chain is the
same for every chain in that orbit, by applying a label permutation.

Thus reconstruct the law using a pair J uniform among six possibilities,
and an independent fair choice R between its remaining singletons, both
independent of the times and D_n. For D_n=1 ignore R and merge the
complementary pair at U_n; for D_n=0 use R to choose the singleton merged
with J. Use S_n,U_n,V_n for the three merger times.

The same reconstruction realizes B_4 with its target marked time law.
On a route with H,G>0 the six balanced chains or twelve nested chains are
uniform by its rates. If H=0<G, the uniform nested chain produces a uniform
triple: each of the four triples arises from three choices of its first pair.
If G=0, only a uniform first pair can be visible before absorption; if H=G=0
no proper intermediate partition is visible.

At finitely many deterministic observation times this reconstruction is
continuous whenever none equals S,U,V, including when H=0 or G=0. On {G=0}
the intermediate two-block state is invisible and the reconstructed law
depends only on J and the times, so the free value of D* has no effect.
The marginal laws of S,U,V have no atoms: conditional on a route in Section 3
each is S plus a sum of independent holding times, and S has a density.

Consequently every convergent subsequence of marked time laws reconstructs
the B_4 finite-dimensional law: on {G>0} its marked law is fixed, and on
{G=0} the remaining freedom is irrelevant. Tightness and this uniqueness of
the reconstructed limit prove convergence for the full sequence. This
completes the proof of the theorem.

## 7. The disjoint-pair burst diagnostic

For any fixed T,h,epsilon>0, the equivalent assertions imply

    P(S_n<=T, H_n<=h, G_n>=epsilon, D_n=1)
       -> [(1-exp(-3T))(1-exp(-2h))/6] exp(-epsilon).         (6)

This follows by integrating (3). There is no boundary mass at the specified
positive thresholds, and the shape is identified away from G=0. In
particular,

    lim_(h down to 0) lim_(n to infinity)
      P(S_n<=T,H_n<=h,G_n>=epsilon,D_n=1) = 0,               (7)

and the right side of (6), divided by h, tends to
(1-exp(-3T))exp(-epsilon)/3.

The condition G_n>=epsilon is essential. Without it, a rapid sequence ending
in a quadruple merger could temporarily visit a 2+2 partition and still have
the correct finite-dimensional limit. Its binary refinement is not observable
at deterministic times. Formula (7) excludes two disjoint mergers followed
by a macroscopic two-block interval, rather than excluding valid quadruple
bursts. Like the earlier three-label diagnostic, this is an iterated limit;
it gives no prescribed shrinking sequence h_n.

## 8. Correct three-label laws do not exclude these bursts

Consider the following exchangeable coalescent, defined on every finite label
set. Superpose three independent mechanisms on its current blocks:

1. Every specified block pair merges at rate 1/3.
2. At rate 1/3 all current blocks merge into one.
3. At rate 2/3 assign each current block an independent fair coin; merge
   all heads blocks together and all tails blocks together. Ignore groups
   of size zero or one and ignore events that cause no change.

The construction is consistent under restriction. In the first mechanism,
mergers with a block carrying no retained label make no projected change;
each pair of retained ancestral blocks still has merger rate 1/3. In the
second mechanism the retained blocks all merge. In the third mechanism the
coins of retained ancestral blocks are independent fair coins, irrespective
of the blocks without retained labels. Thus each mechanism induces exactly
the same mechanism on the retained blocks. Their sum does too.

For three blocks a specified pair alone is merged by the third mechanism
with probability 1/4: its two coins agree and the third is opposite.
All three coins agree with probability 1/4. Hence its three-label rates are

    specified pair: 1/3+(2/3)(1/4) = 1/2,
    triple:          1/3+(2/3)(1/4) = 1/2.

With two blocks their merger rate is 1/3+1/3+(2/3)(1/2)=1.
Every three-label restriction is exactly the normalized B_3, including its
full time dependence and the earlier joint transform.

For four blocks the rate table is instead

| Specified transition | B_4 rate | Counterexample rate |
|---|---:|---:|
| One specified pair, other blocks separate | 1/3 | 1/3 |
| One specified triple, singleton separate | 1/6 | 1/12 |
| Quadruple | 1/3 | 5/12 |
| One specified pairing into two pairs | 0 | 1/12 |

For the coin mechanism each specified triple/singleton split, each specified
two-pair split, and the all-equal outcome has probability 2/16=1/8. This
gives the table. Both total first-event rates are 3:

    6(1/3)+4(1/12)+5/12+3(1/12) = 3.

Nevertheless the counterexample has direct disjoint-pair bursts. Their
total rate is 3/12=1/4. Their first-event density is (1/4)exp(-3u), and the
following two-block holding time is Exp(1). Therefore its analogue of (7) is

    (1-exp(-3T))exp(-epsilon)/12 > 0.                        (8)

A single-time test also separates the two laws. Their probabilities of
three blocks at time t are both 2(exp(-2t)-exp(-3t)), since their rates from
four to three blocks are both 2. Entry into 2+2 from three blocks has rate
1/2 in both processes. The counterexample also enters 2+2 directly from four
blocks at rate 1/4. The survival rate in 2+2 is one in both. Thus the excess
probability of a 2+2 partition at time t is

    (1/4) integral_0^t exp(-3u)exp(-(t-u))du
       = (exp(-t)-exp(-3t))/8.

At t=log 2 this difference is exactly 3/64.

This example can also be approximated by strictly binary exchangeable
genealogies, so the binary finite-n hypothesis does not cure the problem.
On each path enumerate its finitely many state-changing events at times
tau_1<tau_2<... . Resolve each event into r_j binary mergers leading to its
post-event partition. For a triple or quadruple choose a label-invariant
random binary resolution inside that merged group; for two disjoint pairs
choose their order by a fair coin. Place the kth binary merger of event j at

    tau_j + (sum_(i<j) r_i + k)/n,  k=1,...,r_j.

The times are strictly ordered even across different events; total delay
is at most (k_labels-1)/n for a fixed sample. Each resolution is exchangeable.
At every deterministic time the resolved path converges to the unresolved
one unless that time is an event time, an event of probability zero.
Thus the binary approximations have all three-label restrictions converging
to B_3 while their four-label limit violates (7). They also have first
four-label merger time converging to Exp(3). They are abstract genealogies,
not N-BBM particle systems.

## 9. The time transform alone is insufficient

Take (S,H,G) with the target law of Section 3. Set S_n=S,
H_n=H+1/n, G_n=G+1/n. At each n choose a uniformly relabelled binary chain
whose two-block state always has sizes 3+1. These processes are exchangeable
and strictly binary. Their F_n converge exactly to (1), but M_n=0 identically.
They never visit 2+2, whereas B_4 visits that shape with positive probability.
Hence the shape condition (2) cannot be dropped, even after all three
block-count holding times have their correct joint limit.
