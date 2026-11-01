# C0123: an exact bridge threshold in a paired-block NK landscape

Label: proof for a deterministic K=1 block landscape, awaiting w346. This is not a typical-case statement about iid Gaussian NK fitness.

On 2m binary sites partition the coordinates into m disjoint pairs. For positive J_i define

F(x)=sum_(i=1)^m J_i * 1{x_(2i-1)=x_(2i)}.

This is a K=1 local NK-form landscape: assign each of the two sites in pair i the local term J_i/2 times the equality indicator, depending on itself and its partner. Its maximum is M=sum J_i, attained at all 2^m configurations whose pairs are each 00 or 11. All are strict single-bit local maxima.

For two such peaks u,v, let D be the pairs on which their 00/11 labels differ. If D is nonempty, the smallest deficit needed for a single-bit path from u to v inside {F>=M-delta} is max_(i in D) J_i.

Necessity: on every path changing the label of pair i from 00 to 11 or conversely, an intermediate configuration has a mismatched pair. Its deficit is at least J_i because all block deficits are nonnegative. Sufficiency: change the differing pairs one at a time, using two bit flips for each. Only the currently changing pair is mismatched, so the largest deficit equals max_(i in D) J_i.

The components of peaks at level delta are therefore exactly classified by the fixed labels of pairs with J_i>delta. There are 2^(number of such pairs) components. Every other vertex in the level set connects to a peak by repairing its mismatched pairs, which only increases fitness, so this is also the component count for the whole level set. In particular J_i=1 gives 2^m isolated peaks for delta<1 and a connected level set for delta>=1. Multiple peaks can therefore have bridges at a bounded deficit in this deterministic NK subclass; neighbor counts alone do not give the earlier proposed universal 'deficit must diverge' criterion. Random tables, normalization and overlapping neighborhoods remain outside this proof.
