# C31 v1: unequal entry budgets and the retained-path lower coupling

Status: proof (unaudited). Kind: special. Target: 1.
This is a construction theorem, not a recurrence theorem or a novelty claim.
It supplies the unequal-cap construction explicitly excluded from the C29 v1 audit.
The hardest open piece remains a positive linear exact-law mean lower bound.

## Statement and exploration protocol

Fix d>=2, 0<p<1/2, q=(1-p)/d and beta=p/(1-p). A frog at a nonabsorbing
vertex steps to its parent with probability p and to each child with probability q.
There is one original resident per vertex. Let (K_j)_(j>=0) be any deterministic
sequence of finite positive integer budgets, where j is absolute depth below a
fresh recursive root. At awakening horizon H, residents may wake only at depths
0,...,H. The parent of the recursive root is absorbing. The root receives k
incoming frogs serially, 1<=k<=K_0; only the first input wakes its resident.

An entry from depth j-1 to depth j is waking-enabled for the first K_j enabled
entries across that edge. Each allowed call uses the SAME child environment,
resident and counters as all previous calls there. Later entries perform an
ordinary excursion with all waking suppressed until that frog first returns
across this edge. During this excursion it does not consume enabled counters
or enabled departure instructions anywhere below the edge, even at an already
awake vertex. A return re-enables the frog only at the departure vertex.
Motion and its ordinary law are retained. A nonreturning suppressed excursion
can be projected to a loss for ancestor-return counting. Beyond H the same
suppression applies to all excursions. Child calls close before their returned
frogs are processed at the parent. This defines a serial protocol, not an
assertion about some different synchronous quota rule.

The claims are: (i) the finite response law has the unequal-budget recursion
specified below; (ii) its operator is monotone in cumulative child responses;
(iii) finite-horizon root responses are stochastically nondecreasing in H for
a fixed absolute-depth profile; and (iv) at ordinary p=1/(d+1), the one-input
root count is a valid original-path lower family satisfying C30's hypotheses.

## 1. Suppressed excursions and fresh randomness

Starting one edge below its absorbing target, the distance walk moves inward
with probability p and outward with probability 1-p. Its probability of hitting
0 before L, starting at 1, is (beta-beta^L)/(1-beta^L). Letting L tend to
infinity gives eventual return probability beta. Every returning excursion has
a finite hitting time; a nonreturning one produces neither allowed waking nor
ancestor returns. Thus it can be represented by an independent Bernoulli(beta)
indicator for the purposes of this exploration. This is the usual finite
gambler's-ruin calculation, also written out in C27 v2 section 2.

The suppression flag and the edge budget are known BEFORE the next direction
is sampled. It is therefore legitimate to use independent enabled departure
stacks and separate suppressed-excursion randomness: each actually sampled
ordinary direction has the required law, independent of the past. They are
different streams for generating fresh ordinary steps, not extra frogs.
The future of a frog which has returned and is sent down again is fresh by
the strong Markov property. Its identity never supplies another resident.

## 2. The operator T_(A,B)

For a positive integer B, let S_B be the nondecreasing B-tuples of finite
nonnegative integers. A point r in S_B specifies cumulative returns after
1,...,B serial inputs into one persistent child. Set r_0=0 and extend it by

    F(0)=0,   F(n)=r_n (1<=n<=B),
    F(n)=r_B+sum_(i=1)^(n-B) Z_i (n>B),

where the Z_i are independent Bernoulli(beta) variables for the suppressed
overflow excursions. They are independent of r and of all other streams.

For ANY positive A and B (there is no requirement A=B or A<=B), draw d
independent child vectors of law mu on S_B and extend each to F_j. Draw an
independent iid parent departure stack with probabilities p,q,...,q. Let U(t)
and D_j(t) count parent and child-j directions among its first t instructions.
For 1<=k<=A put

    P_k(t)=k+1+sum_(j=1)^d F_j(D_j(t))-t,
    tau_k=min{t>=0:P_k(t)=0},   R_k=U(tau_k).

The initial k+1 frogs are the k inputs and the ONE resident. Each departure
consumes one pending frog and the appropriate cumulative child increment adds
all replies from that call. Consequently this is the queue balance identity.
Every decrement is at most one. Before its first zero the residual is
positive and the next instruction is legal. Introducing the next seed after
closure gives exactly the same residual with its initial value increased by
one; hence tau_(k+1)>tau_k and R_(k+1)>=R_k. In particular the resulting joint
law is on S_A. Denote it by T_(A,B)(mu).

## 3. Finite closure does not require equal budgets

Condition on the finite child vectors and write C=sum_j r_(j,B). All enabled
child replies together contribute at most C new pending frogs. Apart from
overflow-return loops, each departure consumes one pending frog; no more than
A+1+C such non-loop departures can occur. This also bounds pending frogs.
There are at most dB enabled child calls.

When c child quotas are exhausted, a departure into an exhausted child and
its suppressed return has probability c*q*beta<=d*q*beta=p<1. The number of
such loops before another event is therefore geometric and finite almost
surely. Combining finitely many non-loop events with these finite stretches
of loops proves tau_A<infinity almost surely. All earlier closure times are
finite as well. This argument uses A for initial seeds and B for child quotas
separately. In particular no equal-budget assumption is hidden in it.

For clarity, eliminating those loops gives probabilities p/(1-c*q*beta) for
a parent exit, q/(1-c*q*beta) for each unexhausted child, and
c*q*(1-beta)/(1-c*q*beta) for a terminal overflow loss. They sum to one and
the denominator is at least 1-p. This is an exact event law; empirical child
pools and floating point simulations are only approximations to the operator.

## 4. Order is on cumulative maps

Suppose two child laws admit a coordinatewise coupling r<=s. Couple d copies
independently, use common overflow streams and a common parent stack. Then
F_j(n)<=G_j(n) for every n. For fixed k the corresponding residuals are
pointwise ordered. If the larger residual's first zero were earlier than
the smaller one's, then the smaller residual would still be strictly positive
there; the larger residual could not be zero. Thus the smaller closure time
is no later, and its U-count no greater. Simultaneously for every k this proves

    T_(A,B)(mu) <= T_(A,B)(nu)

in coordinatewise stochastic order. No ordering of increments is asserted:
for example (0,1)<=(1,1) has oppositely ordered second increments. The common
finite first-zero argument of C27 therefore survives changing both dimensions.

## 5. Exact composition at absolute depths

Let L_A be the leaf law (Z_0+sum_(i=1)^k Z_i)_(k=1)^A, with independent
Bernoulli(beta) variables. The Z_0 term is the resident once; Z_i is the
ordinary parent-hit indicator of input i. All deeper waking is suppressed,
so this is the exact leaf joint law, rather than A independently restarted
two-frog systems.

Writing mu_j^H for the K_j-input law at depth j, the finite laws are exactly

    mu_H^H=L_(K_H),
    mu_j^H=T_(K_j,K_(j+1))(mu_(j+1)^H),  j=H-1,...,0.

Disjoint child resident environments and unused direction streams are
independent. Pre-sampling a child response map is equivalent to revealing
its next cumulative increment only when that input is actually made.
The parent never selects an input after inspecting its unused reply.
When a particular frog revisits a child, its unused future directions still
have the ordinary law; physical identity neither correlates unused child
randomness with a parent departure nor duplicates a sleeper. These facts
justify the independent child-map sampling and persistent counters in the RDE.

The closure bound in section 3 proves finite closure by backward induction
from the leaf. This is a finite recursion, without an assumed infinite-depth
fixed point, independent copies for successive inputs, or an unjustified
product of conditional success probabilities.

## 6. Monotonicity in the horizon

At any fixed depth, retaining only the input frogs and the first resident
gives exactly L_A. On their same ordinary future paths, permitting additional
residents changes none of these frogs' eventual parent-hit events. All these
original hits remain, even when an entry is suppressed, because suppression
retains motion. Additional residents can only supply additional hits. This
couples the cumulative responses with L_A below the one-level-deeper response,
simultaneously for all A serial inputs.

Compare horizons H and H+1 at depth H by this coupling. Their parent operators
have the SAME dimensions K_j,K_(j+1), since the profile is indexed by absolute
depth and is fixed across horizons. Apply section 4 successively for
j=H-1,...,0. It follows that mu_0^H<=mu_0^(H+1). This argument would not cover
changing the profile with H, and no such assertion is needed here.

## 7. Coupling to original frogs

One may equivalently preassign independent ordinary paths to all original
frogs and expose their increments when used. Stop each frog at its first hit
of the original root. The ordinary stopped process's awake set is the least
closure of its initial frog under visits along these assigned paths.

The lower protocol only suppresses waking; it retains each awake frog's
ordinary path. A lower awakening therefore has a witness path from an
earlier lower active frog to that resident. Induction on such witnesses puts
every lower awake resident in the ordinary stopped closure. Every counted
root hit is then the same original frog's first root hit in that closure.
There are no cloned origins and no repeated count of that frog at the root.
All finite witnesses use finitely many steps. Projecting nonreturning
suppressed excursions to losses cannot remove a necessary waking witness,
because their waking is suppressed throughout. Returning excursions have
finite length. Restoring all waking and ordinary root reflection only adds
full-model activity.

At ordinary p=1/(d+1), embed the recursive root as the first child u chosen
by the original root frog. That frog's future is the single incoming seed;
the sleeper already at u is the single resident. Only original resident
origins at depths 0,...,H below u can wake. If R_H is this one-input response
and W is full root returns, then R_H<=W on this coupling. Moreover R_H is
bounded by the sum of the all-active first-root-hit indicators of that seed
and those original resident frogs. Thus all the original-path, finite-origin
and single-count assumptions of C30 hold for this family, not just a
distributional mean comparison.

## 8. Scope and remaining gap

C29's K_j=min{K>=1:4^K>=(j+2)^2} is one such fixed absolute-depth profile.
The known-degree calibration's profile with (d+1)^K instead of 4^K is another.
At the ordinary parameter, C30 implies

    P(W=infinity)>=d limsup_(H->infinity) E[R_H]/H.

No positive value for that exact-law limsup is proved here. Finite empirical
means, population error bars, summable sterile-prefix probabilities and the
existence of this RDE supply no such bound. C29 v1's previous PASS explicitly
excluded the construction now submitted as C31. C31 has no independent audit
yet; C27 v2's PASS is supporting background, not a transferred verdict.
The full ordinary T3 and T4 problems remain OPEN. No Lean or interval-certified
evaluation of this new operator is claimed.

Sources: owner-own-work, extending C27 v2 (exact-version PASS in
AUDITS_FROM_REVIEWER.tsv); C30 v1 (exact-version PASS) for the last inequality;
Hoffman--Johnson--Junge, arXiv:1404.6238, Theorem 4 only for the ordinary
zero-one conclusion if a positive limsup is eventually established.
