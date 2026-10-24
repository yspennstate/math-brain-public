# P0033: a stationary Galton-Watson flow that is not ergodic

Written 2026-09-06. Complete candidate counterexample; author checking and prior-literature search are in progress. No independent review or novelty claim. This file is not counted as a solved open problem merely because it exists.

Source: Lyons and Peres, *Probability on Trees and Networks*, version 19 August 2026, Question 17.18, printed page 575 (PDF page 592). The question asks whether a flow rule admitting a stationary measure equivalent to Galton-Watson measure must induce an ergodic Markov chain. Proposition 17.17 proves this under strict positivity of all child weights. Exercise 17.22 gives a nonergodic example with a merely absolutely continuous stationary measure; equivalence is the important extra requirement here.

## Construction and claim

Let GW be the law of a rooted Galton-Watson tree with independent offspring numbers D satisfying

    P(D=2)=3/5,   P(D=3)=2/5.

The tree has no leaves and mean offspring 12/5. We construct an isomorphism-invariant measurable color c(T) in {0,1}, each with probability 1/2, such that almost surely:

* at a vertex with two children, its color is the AND of its child colors;
* at a vertex with three children, its color is the OR of its child colors.

Both Boolean rules preserve unanimity. Consequently every vertex has at least one child of its own color. At every vertex, the flow chooses uniformly among those children. The resulting flow is consistent under restriction to a descendant subtree. GW itself is stationary for the Markov chain that follows this flow; nevertheless the root color is constant along the chain and has probability 1/2 for each value. Thus the chain is not ergodic, despite a stationary measure equal to GW.

## The color is a function of the uncolored tree

For a finite truncation of T at level n, give the vertices at that level independent Bernoulli(1/2) colors and propagate colors upward using AND at two-child vertices and OR at three-child vertices. Let q_n(T) be the probability, over these temporary boundary colors, that the root color is one. Thus q_0=1/2. It is a measurable, isomorphism-invariant function of the uncolored tree through level n, with values in [0,1].

The mean output probability when the children independently have probability p of color one is

    F(p)=(3/5)p^2+(2/5)[1-(1-p)^3].

Direct substitution gives F(1/2)=1/2. Let F_n denote the sigma-field of the tree through level n, meaning that the offspring numbers at depths below n have been exposed. Conditional on F_n, the offspring numbers of the level-n vertices are independent with the displayed law. The expected probability of a one at each such vertex after one additional level is 1/2. The root Boolean formula is a multilinear polynomial in the probabilities at its boundary vertices, because it is a read-once formula on a tree. Taking conditional expectations therefore gives

    E[q_(n+1) | F_n]=q_n.

Hence q_n is a bounded martingale. It converges almost surely and in L2 to a measurable q_infinity, with E q_infinity=1/2.

We must show that q_infinity is {0,1}-valued; otherwise a random boundary color would remain and would not define the required flow on uncolored trees. Put r_n=E[q_n^2]. Equivalently, use two independent boundary colorings of the same uncolored truncation: r_n is the probability that both root outputs are one. Each output has marginal probability 1/2. For a two-child AND, the probability of two one outputs is r_n^2. For a three-child OR, inclusion-exclusion gives

    1-2(1/2)^3+r_n^3=3/4+r_n^3,

since for a pair with both marginals 1/2 the probabilities of 00 and 11 agree. Different child subtrees are independent. It follows that

    r_0=1/4,
    r_(n+1)=3/10+(3/5)r_n^2+(2/5)r_n^3.

For 1/4 <= r < 1/2, the increment factors as

    3/10+(3/5)r^2+(2/5)r^3-r
      =(r-1/2)[(2/5)r^2+(4/5)r-3/5] > 0.

The quadratic factor is negative throughout [1/4,1/2], and the recursion maps this interval into itself because it is increasing and fixes 1/2. The only fixed point in this interval is 1/2: the other positive root is (sqrt(10)-2)/2 > 1/2. Thus r_n increases to 1/2. By L2 convergence,

    E[q_infinity(1-q_infinity)] = 1/2-lim r_n = 0.

Nonnegativity forces q_infinity in {0,1} almost surely. Define c(T)=q_infinity(T) on this probability-one set. The recursion for q_n at the root is a continuous polynomial in the q_(n-1) values of its child subtrees, so passage to the limit proves the AND/OR color recursion. Apply this simultaneously to all vertices, a countable set. For a global Borel definition on leafless locally finite rooted trees, set c(T)=0 outside the Borel set where the displayed limit exists and is binary (and outside the offspring-2-or-3 tree space). At each vertex apply the same local same-color rule; if there are no same-color children, use equal weights on all children. Defining ray probabilities by products of these local weights gives consistency everywhere, including the null exceptional set, and leaves all GW claims unchanged.

## Stationarity with no density change

Write A_c={T:c(T)=c} and GW_c=GW(. | A_c), for c=0,1. Both events have probability 1/2. Conditional on the root offspring number D=d and the vector of its child colors (c_1,...,c_d), the child subtrees are independent, and child i has law GW_(c_i). This follows directly from independent Galton-Watson child subtrees and the fact that each color is a measurable function of its own subtree.

The color of the parent is a deterministic function of d and this vector. Let I_c={i:c_i=c} when the parent color is c. This set is nonempty by the AND/OR rules. Choosing uniformly from I_c uses no further information about the internal shape of the chosen subtree. For every bounded measurable function h,

    E[ sum_(i in I_c) h(T_i)/|I_c| | D=d, (c_i) ]
       = integral h dGW_c.

Averaging conditional on the parent color c proves GW_c K=GW_c for the child-selection kernel K. Finally,

    GW K = (1/2) GW_0 K + (1/2) GW_1 K
         = (1/2) GW_0 + (1/2) GW_1 = GW.

Thus the stationary measure is exactly GW, not merely an absolutely continuous measure supported on a smaller set of trees.

## Consistency and failure of ergodicity

The local rule assigns probability 1/|I_c| to each same-color child and zero to the other children. Products of these transition weights assign mass to all finite initial ray segments. Their consistency defines a Borel probability measure on the infinite boundary by the usual cylinder extension. At a descendant receiving positive mass, the conditional continuation is the identical rule applied to that descendant subtree. This is a flow rule in the sense of the source.

The event A_1 has GW measure 1/2, and K(T,A_1)=1_(A_1)(T) almost surely. Therefore it is a nontrivial invariant event for the stationary Markov chain. Equivalently, in its stationary path space the root-color event is invariant under the time shift and has probability 1/2. The chain is not ergodic.

## Adversarial checks and remaining status work

1. A recursive distributional fixed point alone is insufficient: it might require extra randomness after the full tree is known. The second-moment calculation above proves this does not happen here.
2. The two boundary trials are independent conditional on the tree, so their joint probability really is E q_n^2. Their unconditional correlation is retained in r_n; treating them as independent would destroy the proof.
3. Merely conditioning GW on the existence of an n-ray does not give equivalence to GW, as the source's Exercise 17.22 illustrates. Here the two invariant classes partition a GW-full set and GW itself is stationary.
4. The selected child may depend on all child colors, but these are exactly the conditions used in the disintegration argument. No unconditional independence after selection is asserted.
5. Rooted isomorphisms permute children; both Boolean rules, q_n, its limit, and uniform selection of eligible children are invariant under those permutations. No hidden labels are used.
6. Strict positivity of every child weight fails on some configurations, as it must in view of Proposition 17.17. At a two-child vertex with colors 0,1 only the zero child is chosen; at a three-child vertex with both colors only the one children are chosen.
7. All arithmetic is exact rational algebra. Independent symbolic or finite-depth checks are diagnostics only; the argument proves all depths and the infinite-tree limit.
8. Search prior work on endogeny and interpretable tree automata before calling this a new resolution. Johnson, Podder, and Skerman, *Random tree recursions: which fixed points correspond to tangible sets of trees?*, arXiv:1808.03019, is a relevant primary source. Its general endogeny criteria are not assumed in this self-contained argument.

Exact scope check: the definition in Section 17.5, printed pages 573-574, explicitly permits nonnegative child probabilities and imposes conditional-flow consistency only at children with positive mass. Equivariance is required and was checked above. Thus zeros in this construction are permitted by the source definition; they are not a silent relaxation of it.
