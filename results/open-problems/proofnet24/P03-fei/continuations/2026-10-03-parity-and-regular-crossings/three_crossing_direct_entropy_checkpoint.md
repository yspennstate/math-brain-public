# Direct entropy routes for three nearby crossings: exact remaining gaps

Date: 2026-10-02. **Research checkpoint, not a proof of arbitrary
three-crossing FEI.** The unrestricted problem remains open in this
campaign. The successful bounded-path and parity-slab theorems are
separate statements and are not being inferred to cover this class.

## Geometry of the unresolved case

Orient weights positively and let the actual cuts be `a<b<c`, with
alternating labels. A same-label edge joining components zero and two
must jump farther than `b-a`, and a same-label edge joining components
one and three must jump farther than `c-b`. Since an edge changes the
score by at most `2w_max`, if either corresponding gap is strictly
greater than `2w_max`, one cancellation join is absent. The smaller
component-boundary budget is then exactly `I(f)` and the completed
union/slab theorem applies. Endpoint equalities require their established
tie treatment; no nonstrict assertion with arbitrary endpoint labels is
made here.

Thus the unresolved nearby regime can be confined to
`b-a<=2w_max` and `c-b<=2w_max`: all three cuts lie in a score window
of width at most `4w_max`. The function differs from a threshold only
inside that window. A band containment theorem for an entire label
does **not** apply to this threshold-plus-band perturbation: each label
also contains an unbounded-score tail.

## What the elementary tree route actually achieves

The complete
[direct tree derivation](three_crossing_lacunary_entropy_known_derivation.md)
proves `H<=16I` for three actual crossings of a superincreasing score.
It uses one-constant-child entropy splits and a bound on the number of
genuinely nonconstant branchings, with no component boundary comparison.
However, primary-source checking shows this class is already covered by
read-`k` and tree-covariance FEI theorems. It is retained as a transparent
derivation of a known class, not promoted as a new solution.

The
[full-retention obstruction](three_crossing_full_retention_obstruction.md)
demonstrates why general weights do not admit a crossing-count-only
extension: a tiny-noise block creates three actual cuts in both pivot
restrictions but preserves the old divergent largest-weight local
entropy ratio. Rare score tails must be weighted by their measure in
any stopping or regularization argument.

## A bounded signed-halfspace sum loses an unbounded factor

A different obvious reduction is
`f=h_a-h_b+h_c`, using three nested increasing thresholds. The sum of
their influences need not be comparable to the actual influence even
for three genuine crossings. Here is an exact witness.

Let `N=2d>=2`, `q=2^-N`, `A=2N+4`, and
`T(x)=sum_{i=1}^N(1+2^-i)x_i`. Use two coarse coordinates of weights
`A,2A`, so

\[
 S=A y_1+2Ay_2+T(x).
\]

The unique smallest positive coarse score `A` occurs at `c*=(-1,+1)`.
Let `v` have its first `d` fine coordinates positive and the remainder
negative, and put `t=T(v)=1-2^(1-d)+q`. The interval
`(t-q,t+q)` contains exactly that fine vertex, as proved by the binary
perturbation score spacing in the
[four-crossing predecessor](four_crossing_component_boundary_obstruction_proof.md).
Define cuts

\[
 0<a:=A+t-q<b:=A+t+q
\]

and labels `-,+,-,+`. None is attained, all four components are
nonempty, and the resulting function is exactly

\[
 f(y,x)=y_2-2\mathbf1_{\{y=c^*,x=v\}}.
\]

Writing `p=1/4`, the coarse dictator influence changes from one to
`1-2pq` in coordinate `y_2`; coordinate `y_1` and each of the `N`
fine coordinates gain `2pq`. Therefore

\[
 I(f)=1+2Npq=1+\tfrac12N2^{-N}. \tag{1}
\]

For the increasing thresholds `h_0,h_a,h_b`, exactly
`f=h_0-h_a+h_b`. The first is the dictator `y_2`. The other two split
the central fine Hamming layer inside copy `c*`. Their fine-coordinate
influence is `p M_N`, where

\[
 M_N=\mathbb E|\sum_{i=1}^N x_i|
 =N\binom N{N/2}/2^N.
\]

Their coarse-coordinate influence is exactly one. Indeed the monotone
Chow identity applied to the negative portion of the `c*` copy changes
the coarse influence sum by a multiple of `c*_1+c*_2=0`. Consequently

\[
 I(h_0)+I(h_a)+I(h_b)=3+2pM_N=3+\tfrac12M_N, \tag{2}
\]

which diverges, while (1) tends to one. This is an obstruction to
charging a signed-sum entropy inequality to the uncombined halfspaces.
It is not an obstruction to combining `h_b-h_a` first: that difference
is exactly the isolated-score slab, with tiny influence.

The witness itself is already a character modulation of a point slab:
`f=y_2(1-2·1_{(c*,v)})`. Its entropy is exactly

\[
 e((1-2r)^2)+(2^{N+2}-1)e(4r^2),\qquad r=2^{-(N+2)},
\]

so it tends to zero. The universal bound `H<=8nr` even gives
`H(f)<=2<=2I(f)` here. No FEI counterexample is present.

## Where grouped decompositions meet the same open comparison

Grouping either adjacent pair of nested thresholds gives a halfspace
plus one interval indicator. Their summed influences are exactly the
component budget for one chosen label, `B_+` or `B_-`. Choosing the
better grouping therefore leads back to the unproved three-crossing
comparison `min(B_+,B_-)<=D I(f)` or the stronger trace candidate.
The two ordinary FEI inputs alone do not close this gap: a general
entropy domination/mixture step discards the cross terms responsible
for cancellations in influence.

No bounded decomposition into arbitrary character-slabs with a proved
influence budget was obtained. The old local obstruction family is now
globally covered by the parity-slab theorem; that fact does not classify
every three-crossing truth function as a parity-slab. No such classification
is asserted.

The currently concrete open step is a **measure-sensitive** score-window
or stopping-tree estimate controlling the extra entropy by `I(f)`,
despite same-label jumps. Treating a fixed-width score band as an entire
minority support, assuming crossing counts decrease on restriction, or
charging all three halfspace boundaries independently are each invalid
shortcuts. The exact companion checker records the constructive failures,
and its finite tests are not used to infer a proof of the missing bound.
