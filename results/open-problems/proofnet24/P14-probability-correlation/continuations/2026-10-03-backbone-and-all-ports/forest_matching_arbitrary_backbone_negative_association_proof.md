# Matching negative association attached to three ports of any backbone

2 October 2026. Complete analytic derivation. The credited graphic-matroid
log-concavity theorem supplies a new three-direction Hessian bound. All other
steps, including the support-at-most-two lemma and the exact marginal law,
are given below. Independent proof and exact-check records are listed in the
completion note. Historical novelty and external review remain unverified.

## Theorem and scope

Let G be any finite graph with nonnegative edge activities and three specified
port vertices. Attach any finite even number of new vertices, with spoke
activities `a_j b_i` from new vertex j to port i, where all `a_j,b_i>=0`.
Add any matching among the new vertices with positive edge activities.
There are no other edges incident to the new vertices. The vector of marked
matching-edge indicators is negatively associated: for increasing real
functions f,g of disjoint sets of marked coordinates,

    E[f g]<=E[f] E[g].                                      (1)

The conclusion holds after conditioning any backbone-edge and/or matching-
edge indicators to values of positive conditional probability, and under
arbitrary positive fields on those edges. Rank-one changes of the spoke rows
or columns are permitted; arbitrary individual spoke fields and conditioning
spoke indicators are not asserted. Only the matching vector is claimed
negatively associated. There is no claim about all forest indicators.

## 1. Three-port transfer, including an arbitrary backbone

Record each backbone forest by the partition it induces on the three ports.
Let v be its row of total weights on the five partitions. Define operators
P,Q by adding respectively two or three spokes from one new terminal, with
the common column weights b_i. Spokes to two ports already in one component
are rejected because they form a cycle; otherwise their port blocks merge.
With `B=b_1+b_2+b_3` and `d(x)=1+Bx`, the exact terminal transfer is

    T(x)=d(x)I+x^2 P+x^3 Q,
    P^2=2BQ,  PQ=QP=Q^2=0.                           (2)

The first identity counts the six ordered ways to merge three initially
separate blocks: their summed weight is `2B b_1b_2b_3`. All the operators
commute. Equivalently, with

    alpha(x)=x^2/d(x),   gamma(x)=x^3/d(x)^2,

    T(x)=d(x) exp[alpha(x)P+gamma(x)Q].              (3)

The exponential is a finite polynomial; its `P^2/2` term gives the needed
coefficient `x^3/d(x)` on Q after normalization.

Delete all marked matching edges but keep every endpoint and spoke. This
is an actual weighted graph, called the split baseline. Its port-partition
row is

    v_0=v product_j T(a_j).

Put

    F=v_0 1>0,   M=v_0 P1>=0,   J=v_0 Q1>=0.        (4)

These quantities include all split matching endpoints and all backbone
vertices. No normalization or independence of the backbone forests is
assumed. `F` is the ordinary forest partition sum of the split graph.

## 2. The new Hessian inequality for every actual backbone

The known input is Anari, Liu, Oveis Gharan and Vinzant,
*Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for
Independent Sets of Matroids*, [arXiv:1811.01600v1](https://arxiv.org/pdf/1811.01600).
Theorem 4.1 establishes complete log-concavity of the coefficient-one
homogeneous independent-set polynomial

    sum_(I independent) y^(n-|I|) product_(i in I) z_i.

There is no factorial normalization. Lemma 2.2 permits an affine map into
the nonnegative orthant. Setting y=1 and fixing edge activities therefore
gives log-concavity of the ordinary unrooted graphic-matroid forest
partition polynomial in any selected edge variables. We use only this
prior log-concavity result, not a prior off-diagonal correlation inequality.

To the split baseline, add three hypothetical edges joining the port
pairs, with activities z_12,z_13,z_23. Parallel hypothetical edges are
allowed. Let A_ij be the weight of split forests in which ports i,j are
disconnected, and let r be the weight in which all three ports are separate.
The exact partition polynomial in these three new variables is

    Z(z)=F+A_12 z_12+A_13 z_13+A_23 z_23
          +r(z_12 z_13+z_12 z_23+z_13 z_23).        (5)

The cubic term vanishes because the three hypothetical edges are a cycle.
Two of them may be added precisely when all three ports were disconnected.
The Hessian of log Z at zero is negative semidefinite, by the credited
theorem and continuity from positive activities. Writing
`A=(A_12,A_13,A_23)^T`, this is exactly

    A A^T-rF (11^T-I_3) is positive semidefinite.    (6)

Evaluate (6) on `x=(b_1b_2,b_1b_3,b_2b_3)^T`. The linear form `A^T x`
is exactly M. Also `J=r b_1b_2b_3` and
`sum_(i<j) x_i x_j=B b_1b_2b_3`. Hence

    M^2>=2BJF.                                      (7)

This is a directional logarithmic-Hessian inequality, not an assertion
that each off-diagonal Hessian entry is nonpositive. It uses the full
three-variable log-concavity, rather than scalar log-concavity in B.

A second bound is elementary and does not require (6). Every split forest
with all ports separated permits all two-spoke choices. Consequently

    M>=r(b_1b_2+b_1b_3+b_2b_3),   BM>=9J.           (8)

The last inequality is `B e_2(b)>=9b_1b_2b_3` by AMGM, with zero columns
included by continuity. Bounds (7),(8) also apply after positive-probability
backbone conditioning. Contract required-present edges and delete required-
absent edges; the resulting graphic matroid permits the same three added
edges. If two ports have become identical, a hypothetical edge is a loop,
and its coefficient vanishes. Formula (5) and the semidefinite statement
still hold, with r=J=0.

## 3. Exact whole matching marginal

First suppose B>0 and both endpoints of each marked edge have positive row
activities. For marked edge i joining rows a,b with activity w_i, define

    c_i=d(a+b)/[d(a)d(b)],
    delta_i=alpha(a+b)-alpha(a)-alpha(b),
    epsilon_i=gamma(a+b)-gamma(a)-gamma(b),
    theta_i=c_i w_i/(1+c_i w_i),   t_i=delta_i theta_i.

Contraction of a marked edge merges its endpoints and sums their row
activities; parallel spokes aggregate. By (3), its contracted-to-split
operator ratio is `c_i exp[delta_i P+epsilon_i Q]`. Since the matching
contractions are disjoint, all such ratios commute. Expanding their product
with (2) gives the exact full matching partition polynomial

    Z_mark(w)=product_i(1+c_i w_i)
        [F+sum_i h_i t_i+K sum_(i<j)t_i t_j],        (9)

where

    K=2BJ,   h_i=M+J epsilon_i/delta_i+BJ delta_i.    (10)

All matching coordinates are present in (9). In particular, no pair-only
conditioning or extrapolation to many coordinates is used.

Formula (9) has a literal probabilistic representation. Independently take
Bernoulli coordinates R_i of success probability theta_i and a forced
subset Y of size at most two with unnormalized weights

    empty: F,   {i}: h_i t_i,   {i,j}: K t_i t_j.     (11)

Then the marked vector has exactly the distribution

    X_i=R_i OR 1_(i in Y).                           (12)

For an explicit check, define `f(empty)=F`, `f({i})=h_i delta_i`,
`f({i,j})=K delta_i delta_j`. The forced subset weight is
`f(S) product_(i in S)theta_i`. Given Y=S, the probability of outcome x
in (12) is `Pr(R=x) 1_(S subset x)/product_(i in S)theta_i`.
Multiplying and summing gives `Pr(R=x) sum_(S subset x)f(S)` divided by
the bracket's normalization. Expanding (9) coefficient by coefficient
gives precisely that same matching configuration weight.

## 4. A self-contained support-at-most-two negative-association lemma

Consider (11) abstractly, with F>0, K>=0, t_i>=0 and h_i>0. It is negatively
associated if

    h_min^2>=KF,   2h_min>=h_max.                    (13)

Here is a proof including arbitrary increasing functions. For disjoint
coordinate sets E,H, let C be their complement, and set

    s_D=sum_(i in D)t_i,
    q_D=sum_({i,j} subset D)t_i t_j,
    beta_D=(sum_(i in D)h_i t_i)/s_D.

If either s_E or s_H vanishes, the joint hit probability is zero. Otherwise
the weights of the two hit events are

    W_E=s_E beta_E+Kq_E+Ks_E(s_H+s_C),
    W_H=s_H beta_H+Kq_H+Ks_H(s_E+s_C),
    W_EH=K s_E s_H.

If Z is the total weight, direct expansion gives

    W_E W_H-W_EH Z
     =s_E s_H[beta_E beta_H-KF
        +K s_C(beta_E+beta_H-beta_C)+K^2(s_C^2-q_C)]
       +Kq_E s_H(beta_H+K s_C)
       +Kq_H s_E(beta_E+K s_C)+K^2q_Eq_H.            (14)

Every term is nonnegative under (13), because all beta_D lie between the
minimum and maximum h, and `s_C^2-q_C>=0`. Arbitrary values may be assigned
to beta_C when s_C=0. Thus disjoint hit events are negatively correlated.

For two nontrivial increasing events on disjoint coordinate blocks, record
the singleton coordinates that trigger each event. Since |Y|<=2, both
events can occur simultaneously only via one triggering singleton in each
block. An event requiring two coordinates in its own block cannot co-occur
with a nontrivial event in the other block. Thus the joint event is exactly
the joint hit event for those singleton-trigger sets, whereas the marginal
probabilities are at least the respective hit probabilities. Inequality
(14) proves the event inequality. An event containing the empty coordinate
configuration is constant true and causes no difficulty. Finally express
each increasing real function on the finite cube as a constant plus a
nonnegative combination of its upper-level event indicators. This proves
negative association for all such functions, including the case K=0.

## 5. The two gates follow from the backbone Hessian and AMGM

For a,b>0, strict increase of alpha(x)/x and gamma(x)/x gives
delta_i,epsilon_i>0. Moreover

    0<delta_i<1/B^2,   0<epsilon_i/delta_i<2/B.       (15)

For the first bound, exactly

    delta_i=B^(-2)[1+1/d(a+b)-1/d(a)-1/d(b)]<B^(-2),

since `1/d(a+b)<1/d(a)`. For the second define
`H(x)=(2/B)alpha(x)-gamma(x)`; then
`H(x)/x=B^(-2)[1-d(x)^(-2)]` is strictly increasing. Its strict
superadditivity gives `(2/B)delta_i-epsilon_i>0`.

If M>0, (8),(10),(15) imply

    M<=h_i<=4M/3,

with `M<h_i<M+3J/B` when J>0, and `h_i=M` when J=0.
Consequently `h_min^2>=M^2>=KF` by (7), and
`h_max<2h_min`. Both gates (13) hold. The forced subset Y is therefore
negatively associated. If M=0, (8) forces J=0, and (9) directly gives a
product of independent Bernoullis, so there is no need to divide by h_i.

To pass to X in (12), condition on Y. For increasing f,g on disjoint
blocks, the Bernoulli variables in their two blocks are independent, so
the conditional expectation of their product is `f_bar(Y_E)g_bar(Y_H)`.
Coupling the same Bernoullis shows that both averaged functions are
increasing in their own Y coordinates. Negative association of Y proves
(1) for X.

## 6. Boundaries, conditioning and fields

If B=0, all new vertices have no spokes, so the marked matching is a union
of independent two-vertex components. If an endpoint row is zero, its
matching edge is a bridge incident to a vertex with no other edge. Its
indicator is independent of the remaining forest measure and can be
separated. These facts treat zero rows without divisions. Zero column
factors are already permitted by (2),(5)-(8),(15); when only one column is
positive, P=Q=0 and the law is directly independent. There is no strict
correlation claim at a degenerate boundary.

Conditioning marked edges present contracts their disjoint endpoints and
sums the row activities; these vertices can be absorbed into the arbitrary
backbone. Conditioning them absent removes the marked edges; those unused
endpoint stars can likewise be absorbed into the backbone. Remaining
matching endpoints still have only their proportional spokes and their
single marked matching edge. Conditioning backbone edges produces a
graphic-matroid deletion/contraction, as discussed after (8). Thus the
same theorem applies after every indicated combined conditioning.

Positive backbone and marked fields change allowed activities only. The
proof depends on the rank-one form of the spoke rows, so arbitrary fields
or conditioning on individual spokes remain outside its scope.

## 7. Verification, credit and limits

The companion `forest_matching_arbitrary_backbone_exact.py` builds the
baseline port row by literal backbone forest enumeration and computes full
matching configuration weights using direct spoke-subset connectivity
transfers. It compares them to (9),(12), checks the Hessian and AMGM gates,
and verifies increasing-event inequalities after all recorded combined
partial backbone and matching conditionings. Small examples additionally
enumerate the uncontracted graph and marked subsets directly.

The graphic-matroid log-concavity theorem is prior work. The self-contained
forced-subset lemma and rank-one transfer were developed in the earlier
restricted matching proof; the new step is applying the three-direction
Hessian inequality to an arbitrary split backbone. The new theorem
supersedes the earlier arbitrary-unmatched-terminal-H family in scope,
without changing that preserved proof. Historical priority is unverified.

The matching endpoints have no other edges, and only three common ports
are allowed. The full all-graph, all-position forest pair-correlation and
negative-association conjectures remain unresolved here. Negative
association is not asserted to imply real stability; the previously
verified non-real-stability witness lies within this family.
