# C27 v2: a persistent joint ordinary-excursion lower comparison

Status: proof (unaudited). Kind: special. Target 1.
The exact finite response operator is defined below. Its child-law order is
monotone, and its finite tree laws are lower comparisons for the ordinary
model. The recurrence criterion is only a sufficient condition. C28 now proves that
no fixed K in this ordinary family can meet it at p=1/4. No phase
classification of the full model or novelty result is asserted.

## 1. Model and hypotheses

Fix an integer K>=1 and0<p<1/2. The rooted tree is ternary. An ordinary frog
steps to its parent with probability p and to each child with probability
q=(1-p)/3. Put beta=p/(1-p). There is exactly one resident at each vertex.
A fresh recursive root receives k incoming seeds,1<=k<=K, one at a time.
The first seed awakens its resident; subsequent seeds do not add residents.
Frogs stop on reaching the parent of this recursive root.

At every parent-child edge allow at most K waking-producing downward entries.
An allowed entry explores the child's same protocol, preserving the child's
already awake residents and entry counters. Additional entries follow an
ordinary excursion but suppress every waking event during that excursion.
Suppressed steps use separate private random streams and do not consume any
awakening-enabled vertex instruction. This is an equivalent way to generate
fresh independent ordinary steps because the suppression flag is already
known before a direction is drawn. On returning to its departure vertex the
frog resumes the protocol there.
A nonreturning suppressed excursion can be discarded for all ancestor-return
counts. Waking below the finite depth cutoff is suppressed in the same way.

This is a serial exploration protocol. A child call closes all of its allowed
activity before its returned frogs are processed at the parent. The construction
does not assert agreement with a different synchronous quota rule. Projection
of infinite suppressed excursions to return/no-return outcomes is legitimate
because such excursions never affect ancestor visits or allowed waking.

## 2. The ordinary excursion probability

Starting one edge below an absorbing parent, distance from that parent has
inward probability p and outward probability1-p until it hits0. Let L>=2.
Solving the finite birth-death difference equation, with boundary values1 at0
and0 at L, gives the probability of hitting0 before L from1 as

    (beta-beta^L)/(1-beta^L).

The denominator is positive because0<beta<1. The events increase to eventual
parent hitting as L increases: any finite hitting path has a finite maximum
before its hit. Their probabilities therefore tend to beta. The strong Markov
property and independent future increments give independent Bernoulli(beta)
return indicators for successively suppressed excursions. The root reflection
rule is irrelevant before the absorbing parent is reached.

## 3. Cumulative child replies and the parent queue

Let S_K be the nondecreasing vectors r=(r_1,...,r_K) of nonnegative integers.
Given a child vector r, extend it to a nondecreasing function F:N->N by

    F(0)=0;
    F(n)=r_n                         for1<=n<=K;
    F(n)=r_K+sum_{i=1}^{n-K} B_i     for n>K,

where the B_i are the independent suppressed-excursion Bernoulli(beta)
indicators. A child vector is cumulative: after its n-th allowed input it
has returned r_n frogs in total. It is not n independent copies of a fresh
resident. Counter and resident persistence are part of this definition.

Draw three independent child vectors of law mu on S_K. Supply their independent
overflow streams, independently of an iid parent departure stack. A stack
instruction is parent with probability p and each child j with probability q.
Write U(t) and D_j(t) for their counts among the first t instructions. For k
incoming seeds plus the single resident, set

    P_k(t)=k+1+sum_j F_j(D_j(t))-t.

Define tau_k as its first zero, and set R'_k=U(tau_k).

The identity counts initial frogs, every cumulative child reply and every
parent departure. Increments of each F_j are nonnegative. Thus P_k decreases
by at most1 in a departure and cannot become negative without first hitting0.
While the queue is active its instruction is legal. The first-zero description
also matches serial seeding: adding seed k+1 raises the residual by1 throughout
the completed k-seed exploration, so its next first zero cannot precede tau_k.
Consequently R'_1<=...<=R'_K and the resident is counted exactly once.

## 4. Finite closure

Condition on finite child vectors and put C=sum_j r_(j,K). There are at most3K
allowed child entries, whose total positive reply contribution is C. Apart
from known-child return loops, at most K+1+C departure events are possible:
each consumes one pending frog, and all non-loop additions sum to C. Pending
frogs never exceed K+1+C.

If c child quotas are already exhausted, a departure followed by an immediate
return through one of those children has probability c*q*beta<=3*q*beta=p<1.
The number of successive such loops before the next other event is finite
almost surely. There are only finitely many other events as just counted.
Hence every tau_k is finite almost surely for finite child vectors. This also
establishes finite closure inductively at every finite awakening depth.

## 5. Exact finite recursive law

At awake depth0, all descendant waking is suppressed. The joint leaf law is

    R_0(k)=B_0+sum_{i=1}^k B_i,

with independent Bernoulli(beta) variables. B_0 is the single resident, and
each B_i is the ordinary parent-hit event of one incoming path.

Let T_K(mu) be the joint law of the queue responses R'. At the next depth,
child resident environments and unused excursion increments lie in disjoint
subtrees and are independent. An entering frog's future increments are fresh
even if that same frog has visited the child before. Its identity creates no
new resident. Strong Markov decomposition therefore supplies exactly one
independent persistent child response map per child. Unused coordinates are
revealed only when that input actually occurs; an entry choice does not inspect
a future response. The parent gets an independent ordinary departure stack.
Thus the finite laws satisfy exactly

    Law(R_(h+1))=T_K(Law(R_h)).

Geometric elimination of known-child return loops gives first-event probabilities

    parent:       p/(1-c*q*beta);
    fresh child:  q/(1-c*q*beta) for each of the3-c children;
    terminal loss:c*q*(1-beta)/(1-c*q*beta).

They sum to1. The denominator is at least1-p>0. Batched multinomial/binomial
draws apply these independent first-event laws to current pending frogs.
Allowed child entries consume the next increments of the SAME child vector;
excess entries use the same child's independent overflow stream. Processing
returned frogs in a later batch is a serial scheduling choice and changes no
cumulative input/output identity. These are the transitions implemented in
simulate_joint_ordinary_excursions.py. Empirical child pools approximate mu;
they are not exact evaluations of this distributional equation.

## 6. Child-law order

Use stochastic coordinate order in its coupling definition: mu<=nu when a pair
X~mu,Y~nu exists with X_i<=Y_i almost surely for every i. Take three independent
copies of this coupling, common overflow Bernoulli streams and a common parent
stack. Then F_j(n)<=G_j(n) for every child and every n, including n>K.

For each k the smaller pending function is pointwise at most the larger one.
If the larger first zero sigma_k were before the smaller first zero tau_k,
then the smaller residual there would be strictly positive, and the larger
residual at least as large. That contradicts its being0. Thus tau_k<=sigma_k.
U is nondecreasing, so every smaller root response is at most the corresponding
larger response. This proves T_K(mu)<=T_K(nu).

It is essential to compare cumulative replies, not individual increments.
For example (0,1)<=(1,1), but their second increments are1 and0. The order
argument still applies. Exact finite controls include this case. The abstract
finite first-zero implication is the step submitted to Lean; it does not
formalize the probabilistic model or its ordinary comparison.

The depth0 law is below the depth1 law: retain the same incoming and resident
ordinary paths while permitting additional residents to wake. Suppression
changes no trajectory of those original frogs, so their parent-hit indicators
are retained for every serial input. Child-law monotonicity then gives stochastic
height monotonicity of the finite laws by induction. A globally coupled infinite
joint response or an infinite fixed-point equation is not needed below.

## 7. Comparison with the ordinary model

Preassign independent ordinary paths to all original frogs. Stop each path at
its first arrival at the original root for this comparison. The ordinary
stopped-path awake set is the least closure of the initial frog under visiting
resident vertices along those assigned paths.

The quota exploration suppresses selected waking events and suppresses waking
beyond its finite cutoff; it changes no path segment of an already awake frog.
Every return/no-return projection above is the projection of its actual ordinary
excursion. Induction over lower awakening witnesses puts every lower awake
resident in the stopped ordinary closure. Its root-return path is therefore
also present there. Each finite witness uses finitely many ordinary steps;
conditional returning excursions have finite return times. Nonreturning
suppressed excursions create no required witness. Restoring root reflection
and all suppressed waking can only add full-model activity.

Embed the fresh recursive root as the child chosen by the original root frog
on its first step. The ordinary future of that frog is the first incoming
path, and the existing child resident is the single resident in the construction.
There is no extra root resident or copied sleeper. Therefore the number W of
full ordinary root visits dominates R_h(1) at every finite depth h.

## 8. What would imply recurrence

Suppose epsilon>0 satisfies: for every integer M>=1 there is a finite height
h(M) with P(R_h(M)(1)>=M)>=epsilon. The height is allowed to depend on M.
The comparison gives P(W>=M)>=epsilon for every M. The events {W>=M} decrease
to {W=infinity}, so continuity from above gives P(W=infinity)>=epsilon.
At the ordinary value p=1/4, HJJ1404.6238 Theorem4 for the full one-frog
rooted-tree simple-random-walk model makes this probability1. At another p,
the argument above proves positive probability of infinite full-model returns;
a probability-one conclusion needs a separately justified zero-one law. The
cited theorem is used here only at p=1/4. This is a sufficient criterion, not
a verified hypothesis here; C28 rules it out for every fixed K at p=1/4.

An optional bootstrap has the same precise gap. If laws mu_a on S_K satisfy
T_K(mu_a)>=mu_(a+delta) for all a>=A and a fixed delta>0, if a finite law
Law(R_N)>=mu_A, and if for every M the tail probabilities
mu_(A+n*delta){r_1>=M} have liminf at least epsilon>0, monotonicity gives the
required uniform tail criterion. None of these quantitative initializer/tail
inequalities follows from Monte Carlo estimates.

## 9. Verification and scope

Local verification: C27_QUEUE_CONTROLS.json reports 1,990,656 exact finite
queue cases with no failure, including ordered cumulative replies with
nonordered increments. C25 supplies independent direct finite-tree numerical
controls and zero-drift/support/resident controls. The first Mathlib attempt
was RUNTIME_UNVERIFIED. The separate named core-Lean natural-number
first-zero statement compiled with compiler exit 0 and no axioms, but the
wrapper reports COMPILED_SOURCE_UNREVIEWED, formal_target_verified=false.
Thus no formal-verification PASS is claimed. The natural-number statement
is an isolated first-zero comparison, not the integer queue or this coupling. The probabilistic stack representation and lower coupling still require
independent exact-version review. The p=0 boundary is the trivial zero-return
law; the proof above uses0<p<1/2 and does not extend to beta>=1.

The absorbing finite atom in C26 prevents zero-PGF screening. Positive probability
of infinite lower returns, rather than probability-one lower recurrence, is the
appropriate target. The main T127 problem is unclassified. Rung after local
completion: proof (unaudited). C28 closes this fixed-cap recurrence route
subject to its independent audit; the construction remains useful as a model
definition and control. No Lean-checked probability claim is made.
