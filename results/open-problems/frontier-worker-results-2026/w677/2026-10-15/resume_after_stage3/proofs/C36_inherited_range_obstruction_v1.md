# C36 v1: full lineage-range memory still fails the T4 first-moment route

Status: proof (unaudited). Kind: route-failure. Targets: 2 and 3.
Novelty is unassessed. Neither ordinary T4 transience nor recurrence is proved.
The hardest open piece is a summable site-activation upper bound retaining
collisions between different frog families, not just a lineage's own past.

## 1. Precisely which comparison is ruled out

On the rooted 4-ary tree, start one particle at the root o with remembered
set {o}. Every particle has a finite remembered set S and current vertex x.
It takes an ordinary SRW step to y. If y is in S it has one successor with
state (S,y). Otherwise it has two successors, both with state (S union {y},y).
Successor futures are independent. One successor continues the old frog;
the other is a new resident copy. The two successors inherit the complete
visited set of their common ancestry. They never exchange later discoveries.
There is no bound on S, entry counts, time, depth, or number of particles.

Call this the inherited-range process. Stop a particle when it first returns
to o after leaving o; write Z for its total number of absorptions. We prove
E[Z]=infinity. Consequently this comparison, or any process dominating its
root counts, cannot establish ordinary T4 transience by a finite first moment.
This does NOT rule out comparisons which share discoveries between branches.

The basic branching comparison in Hoffman--Johnson--Junge, arXiv:1404.6238,
Section 3.2, Proposition 18, births on every outward step. The present process
remembers the entire lineage range and only births on a new lineage site.
The obstruction below is not a finite-type or finite-cap reset calculation.

## 2. Original-path upper coupling

Use the unstopped inherited-range process for this coupling. First-return
stopping is only an auxiliary restriction used to lower-bound its own root
counts; the stopped process is not claimed to dominate the full frog model.

Preassign an independent complete ordinary walk to each original resident.
At the first physical visit of the upper process to a nonroot vertex v,
the vertex is new to that lineage, so a resident copy is born. Assign v's
as-yet-unused original walk to this first upper birth. Later resident copies
at v use independent extra walks. The original root frog is the initial
upper particle. At each splitting step one successor retains the entire
unused future of the moving frog; the new successor receives its own fresh
walk. No motion is suppressed. Every assigned original walk is independent
of the event which first visits its origin, because that event uses only
walks of other origins. This is deferred exposure, not conditioning an
already exposed clone on a later actual activation event.

Now form the actual awake closure from those original walks. Every actually
awake original frog has its matching upper birth, possibly earlier in an
upper exploration order. Its complete physical path is represented above.
Induction along each finite actual awakening witness proves inclusion of
all actual active origins and their complete paths in the upper closure.
First-root-hit absorption loses none of the original first hits relevant to
this argument. The unstopped inherited-range process dominates all ordinary
root visits; below we already show infinite mean for its stopped version.

The order of exploring an infinite upper closure does not require a global
first time at infinity: first physical visits at finite generations suffice.
There are at most 2^n upper particles by generation n. All finite-generation
couplings can therefore be constructed consistently, followed by closure.

## 3. Exact many-to-one identity

Let X be a single ordinary SRW started at o, let tau be its first positive
return to o, and let R_n={X_0,...,X_n}. For each finite physical walk prefix,
its expected number of upper particle representatives is

    P(the SRW follows that prefix) * 2^(|R_n|-1).

Proof is induction on prefix length: a previously seen destination multiplies
the number of successors by one; a new destination multiplies it by two.
The remembered set on that prefix is exactly R_n. This is an identity of
expectations; it requires no independence between different prefixes.

Summing disjoint first-return prefixes and then times, with nonnegative terms,

    E[Z] = sum_(n>=1) E[2^(|R_n|-1) 1_{tau=n}].       (1)

Thus an infinite weighted first-return subseries suffices. Infinite
expectation is the only conclusion drawn from (1), not almost-sure recurrence.

## 4. A depth-first subseries with no repeated outward edge

At a fresh nonroot vertex, select an ordered list of k distinct children,
where 0<=k<=4. Visit each selected child by an excursion of the same form,
then take the step to the parent. In this family every used edge is traversed
once in each direction, and no other edge is used. Different choices encode
different finite walk prefixes. A vertex visited for the first time supplies
one weight factor 2. All steps before the final global root hit have
probability 1/5. The number of ordered k-child choices is (4)_k=4!/(4-k)!.

Let Y_h be the total weighted mass of these excursions starting at a fresh
nonroot vertex, including its factor 2, with at most h occupied generations
including that vertex. Set Y_0=0. Direct conditioning at this vertex gives

    Y_(h+1) = F(Y_h),
    F(y) = (2/5) * [1 + (4/5)y + (12/25)y^2
                       + (24/125)y^3 + (24/625)y^4].  (2)

For every finite h these are finite sums, with nonnegative rational terms.
No independence of frog activations has been introduced: (2) enumerates
single-walk prefixes in (1). The products are products of SRW transition
probabilities for concatenated prescribed excursions.

Starting from the global root, choose the first child (four choices, each
probability 1/4) and then perform one such excursion to o. The first-step
probabilities sum to one. Therefore (1) is at least Y_h for every h.

## 5. A uniform exact polynomial certificate

For y>=0,

    F(y)-y = P(y)/3125,
    P(y) = 48y^4+240y^3+600y^2-2125y+1250.

If 0<=y<=1, set u=1-y. The exact identity

    P(y)=13+13u+1176u^2+432u^2(1-u)+48u^4

shows P(y)>=13, since u and 1-u are nonnegative. If y>=1, set t=y-1.
The exact identity

    P(y)=48t^4+432t^3+1595t^2+13(t-1/2)^2+39/4

shows P(y)>=39/4. Hence, uniformly for all y>=0,

    F(y) >= y + 39/12500.                            (3)

Starting from Y_0=0, induction gives Y_h>=39h/12500. Since E[Z]>=Y_h
for every h, E[Z]=infinity. This proves the stated route obstruction.

## 6. Check scope and remaining route

check_c36_inherited_range.py verifies the rational polynomial identities,
the ordered-child coefficients by explicit enumeration of all 65 depth-two
excursions, and agreement with an independent integer tree-size generating
polynomial through height four. These checks support the written proof;
the global inequality follows from the nonnegative decompositions above,
not from a floating-point grid. The attached Lean source, if present, has
no formal-certification status unless a separate compiler receipt says so.

The obstruction persists with unbounded exact memory of every ancestor's
visited range. It identifies the remaining loss: discoveries made after
two lineages split are not shared. No claim is made that all upper models
with unbounded memory fail, that E[ordinary root visits] is infinite, or
that the inherited-range process is recurrent almost surely. Both ordinary
T3 and T4 remain open.
