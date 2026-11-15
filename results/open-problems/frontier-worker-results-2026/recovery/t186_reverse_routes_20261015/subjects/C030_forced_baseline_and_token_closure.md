# C030 v1: a latent forced baseline and finite deduplicated change closure

Status: proof (unaudited), deterministic auxiliary result for target 3.
No finite random-graph threshold or bound on the number of multiply hit
vertices is claimed.

## Latent labels can define a comparison process

Let the message alphabet be the chain {0,...,m-1}, and the cavity update
M be coordinatewise monotone on finite input multisets. On a finite graph,
each vertex v owns outgoing baseline messages sigma_(v->u) and stored
incoming labels iota_(u->v). Assume the template equation

   sigma_(v->u)=M({iota_(w->v): w!=u})

holds at every vertex outside a specified bad set B. Every such vertex
has all its original template stubs matched. On an edge with both
endpoints outside B, assume sigma_(u->v)=iota_(u->v). No compatibility
is required across an edge incident to B.

Set x^0_(v->u)=sigma_(v->u) for v outside B and zero for v in B. Let
F_B update normal messages by M and force messages owned by B to zero.
Then F_B(x^0)<=x^0. At a normal recipient, a normal neighbor supplies
exactly its stored iota label, while a bad neighbor supplies zero,
which is no larger than that nonnegative label. Monotonicity and the
template equation prove the inequality. The bad coordinates are zero.

Consequently x^r=F_B^r(x^0) decreases and terminates at a fixed point
x^*. There are at most (m-1) times the number of directed edges strict
coordinate decreases. If y^r is ordinary unforced WP started at all
m-1, then y^r>=x^r at every r: it holds initially, and F>=F_B with both
maps monotone gives the inductive step. Thus the largest unforced fixed
point y^* dominates x^*. Any coordinatewise monotone local reconstruction
also inherits this domination. This is a deterministic comparison;
sigma, iota and B may be latent mathematical variables. Observability
by a finite-graph algorithm is not required for the inequality.

Application to the planted template construction is conditional only
on its local labels: put in B every vertex incident to an unmatched
stub and every vertex with an incident incoming or outgoing time-t
message differing from its own limiting label. Finite-history matching
then implies baseline compatibility on edges with both endpoints normal.
The stationary limiting template recursion gives the displayed equation.
This does not identify the planted graph law with G(n,c/n).

## Deduplicating marks need not miss cooperative changes

For a precise closure argument replace each B-to-normal input by a
separate external boundary coordinate with baseline iota_(u->v).
Its baseline update is the identity, and it is subsequently forced to
zero. Normal-to-normal coordinates have baseline sigma. The full baseline
is now a fixed point of this augmented monotone network; its forced
trajectory is exactly the normal part of the comparison process above.
External coordinates are a proof device, not additional random vertices.

Here is a finite conservative change exploration for any such monotone
network with a fixed baseline s. A token for coordinate e has the form
(e,s_e,b), 0<=b<s_e. Each token is enqueued and processed at most once.
Initialize with (e,s_e,0) at each forced boundary coordinate having s_e>0.
At each normal update site keep the set of distinct incoming tokens seen.

* On its first token, evaluate every outgoing coordinate using this one
  incoming reduction and all other inputs at baseline. Enqueue its
  strict outgoing reduction, if any.
* On its second distinct incoming token, enqueue every possible strict
  baseline-to-lower token for every output of the site. Flag it once;
  subsequent incoming tokens produce no further output tokens.

The second token can concern either a second incoming coordinate or
a different lower value on the same coordinate. A duplicate of exactly
the same token adds no new information. Sites with no incoming token
need no action. Forced boundary coordinates simply keep their zero value.

This closure contains every strict coordinate reduction occurring in
every synchronous round of the forced trajectory, not merely final
reductions. Induct on the round. Boundary reductions are initial tokens.
At a normal site, all currently reduced incoming coordinates have their
baseline-to-current-value tokens in the closure by induction. With no
such token the output remains baseline. With exactly one distinct token
ever available, the site's actual output is precisely the first-token
single-input response. With at least two distinct tokens ever available,
the flagged output list includes every possible lower actual value.
This proves the inductive claim. Using the eventual closed set avoids
any assumption about the order in which the queue processes its tokens.

There are at most sum_e s_e <=(m-1)*number_of_coordinates tokens, so
the queue terminates. For four-state WP there are at most three tokens
per coordinate at a fixed baseline. Even if one instead allows every
ordered strict pair, there are at most six pair keys per directed edge.
Assigning one fixed nonnegative cost to each token bounds its total
charged cost by the sum of these costs over the marked token set;
duplicates need no additional multiplicity factor. A site is flagged
only once, so all its spurious output pairs can be charged once each.
C024 already budgets all six pairs in both orientations for a supplied
exceptional half-edge set.

Boundary of the conclusion. Deduplication controls multiplicity, not
how many sites receive a second distinct token. The token closure may
be much larger than the true forced cascade because a flagged site
broadcasts every possible lower output. No probability estimate for its
size has been proved. C028-C029 conditional means apply only to genuine
first-token responses with their specified fixed-template sampler and
depletion hypotheses. Relative class depletion, the number/weight of
newly flagged sites, and transfer of the planted model remain open.
No c_1 or finite strong-core threshold is improved by this lemma alone.

Sources: deterministic monotonicity and closure derivations above; own
C005 defines the four-state monotone update, C024 its initial inventory,
C028-C029 the conditional first-response estimates.
