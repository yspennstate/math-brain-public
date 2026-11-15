# Coordinate-coalesced closure: deterministic proposed repair

15 October2026, codex-term-362ebe34. Auxiliary proposal, independent review
pending. This replaces C030's second-distinct-TOKEN flag by a
second-distinct-INPUT-COORDINATE flag. The original C030 remains valid as
a conservative closure; its constant-update-chain diagnostic shows that
its flagged set can be unnecessarily large. No stochastic sparsity or
finite strong-core threshold is claimed here.

Consider a finite monotone coordinate network F on the product of chains
{0,...,m-1}, with fixed baseline s=F(s). Force a specified boundary set
of coordinates to zero. Normal update sites can own several outgoing
coordinates; for each output its dependency list is specified. It is
safe to use the union of those lists as the site's incoming coordinates.
Write F_B for the forced map, and x^r=F_B^r(s), with forced boundary
coordinates zeroed initially if desired. The initial boundary reset
cannot change the eventual decreasing fixed point.

Maintain one lower proposal l_e per coordinate, initially s_e except
the boundary proposals0. A site counts distinct incoming coordinate
indices with l_e<s_e, not the number of different lower values ever
received on one coordinate. The rules are:

* With no changed input, do nothing.
* With exactly one changed input e, recompute every output's exact
  baseline response with input e at its CURRENT lowest proposal l_e
  and all other inputs at baseline. Lower that output's proposal to
  the minimum of its old proposal and the response. Recompute whenever
  l_e strictly decreases again. An output excluding e has its unchanged
  baseline response.
* As soon as two distinct input coordinates have changed, flag the site
  permanently and lower all its output proposals to0. Later tokens
  on the same coordinate do not create another changed-input index.

Any fair queue order terminates: proposals only decrease, so there are
at most sum_e s_e strict coordinate decreases; each triggers finitely
many site updates, and each site is flagged at most once. Duplicate
tokens have no effect. Several lower values on one chain coordinate
coalesce to their minimum, which is one of those values, rather than
creating a new cooperative input.

Let l be the completed closure. On an unflagged site all its final
inputs except possibly one are baseline. Its last one-input response
was evaluated after that input's final decrease. Hence every normal
output there equals its value under F(l): earlier responses were
larger by monotonicity and taking minima did not introduce a smaller
value. At a flagged site its output0 is at most F(l). Forced coordinates
are0. Therefore l<=F_B(l) and l<=s. Monotonicity gives x^r>=l for all r,
and the true forced fixed point x^*>=l. This is a lower domination
certificate. It does NOT claim that every intermediate actual output
value appears as an exact token in the queue.

There is also a static response-graph containment. Use potential tokens
(e,s_e,b), b<s_e. A token points to each strict output reduction given
by its one-input baseline response. Every strict proposal generated
without a flag is reachable in this fixed graph from a boundary token
or a flag-generated0 token. Coalescing cannot invent a new value because
the minimum of a finite set on a chain is one of its elements. Thus the
algorithm is single-response reachability with new0 seeds at sites
receiving changes on two distinct input coordinates.

The constant-update-chain obstruction is removed: two seed coordinates
can flag their first common site, but that site's outputs affect each
next site on only one coordinate. A constant site has no strict
single-input response, so propagation stops there. Two different lower
values on that one edge cannot flag its recipient. This observation
does not exclude a genuine cooperative two-input cascade elsewhere.

For four-state messages there are at most three lower proposals per
fixed-baseline coordinate. A site may reevaluate the same incoming
coordinate at most three times before receiving a distinct changed
coordinate. These are dependent evaluations and cannot be billed as
fresh independent offspring draws. A finite random-graph proof still
needs the conditional first-response law, a sparse two-coordinate-hit
budget, weighted class depletion and planted-to-ER transfer. The reverse
ancestry route supplies proposed ideal-tree occupation estimates, not
these finite-graph conclusions.
