# A boundary trace route for three crossings

Date: 2026-10-02. **Conditional route; the required trace bound is unproved.**

Let \(f=F(\sum_i w_i x_i)\), with positive weights and exactly three
retained crossings \(a<b<c\). The four nonempty score components have
labels \(+,-,+,-\). Put \(H=\operatorname{sign}(\sum_iw_i x_i-b)\),
using any tie convention consistent with the finite attained-score gaps.

For a Boolean \(H\), let
\[
 \Gamma_H(x)=\#\{i:H(x)\ne H(x^{\oplus i})\},\quad
 K=I(H)=\mathbb E\Gamma_H,
 \qquad \nu_H(x)=\frac{\Gamma_H(x)}{2^nK}.
\]
Nonempty components on both sides imply \(K>0\). Thus \(\nu_H\)
is the probability measure obtained by selecting a pivotal edge of
\(H\) uniformly and then one of its endpoints uniformly.

The positive and negative same-label joins are denoted \(J_+\) and
\(J_-\), with physical influence normalization. The pivotal edges of
the middle threshold consist of those joins and the odd-parity joins
from component 0 to 3 or component 1 to 2. Let their total physical
probability be \(D\). Exact counting gives
\[
 K=J_++J_-+D,\qquad
 \mathbb E_{\nu_H}f=\frac{J_+-J_-}{K}.
\tag{1}
\]
Indeed a same-positive edge supplies two \(+1\) endpoints, a
same-negative edge supplies two \(-1\) endpoints, and an odd edge
supplies one of each.

Consequently
\[
 K\operatorname{Var}_{\nu_H}(f)
 =\frac{4J_+J_-+2D(J_++J_-)+D^2}{J_++J_-+D}
 \ge2\min(J_+,J_-).
\tag{2}
\]
For example, if \(J_+\le J_-\), subtracting
\(2J_+(J_++J_-+D)\) from the numerator leaves
\(2J_+(J_--J_+)+2DJ_-+D^2\ge0\).

Thus the following trace inequality would imply the desired component
comparison:
\[
 \boxed{I(H)\operatorname{Var}_{\nu_H}(f)\le2I(f).}
\tag{T}
\]
Under (T), (2) and \(B_\pm=I(f)+2J_\pm\) give
\[
 \min(B_+,B_-)\le3I(f).
\tag{3}
\]
Since each label has two disjoint interval components, the completed
parallel-slab theorem and disjoint-union entropy lemma would then prove
FEI for every arbitrary-spacing three-crossing function, with a universal
constant. Equations (1)–(3) are proved here; (T) is the missing step.

## Exact finite stress

The [integer stress script](stress_three_crossing_component_comparison.py)
and [report](three_crossing_component_stress_results.json) evaluate the
trace ratio on 307,503 three-crossing configurations on 81 weight
families through dimension ten. All relevant quantities are integer
edge counts; comparisons against the proposed constant 2 are exact.
The largest tested ratio is \(3/2\), attained by weights \((9,10,12)\)
and cuts immediately before, between, and after the two central attained
scores. No tested trace ratio exceeds 2. These finite checks do not prove
(T), including any limiting or dimension-independent case.

The comparison with constant 2 in (3) would itself be false: the
[separate exact witness](three_crossing_D2_counterexample.json) gives
\(\min(B_+,B_-)/I(f)=23/11\). This does not contradict (T), which
would give comparison constant 3.

## Why common-score geometry is essential

The [companion checkpoint](three_crossing_component_comparison_candidate.md)
constructs an abstract increasing four-region map
\(r=2\operatorname{Maj}(x)+\operatorname{Dictator}(z)\).
For its alternating-label function, \(I(f)=1\), while the middle
threshold has \(I(H)=\Theta(\sqrt n)\) and
\(\operatorname{Var}_{\nu_H}(f)=1\). Therefore (T) fails without the
requirement that all four regions are consecutive intervals of one
common positive linear score. That abstract construction is not
realizable by such a score, as proved in the companion note.

A proof of (T) must exploit the additive-score structure, rather than
only monotonicity along cube chains or a generic trace Poincare bound.
No such proof is supplied here. Four-crossing component comparison fails
by a separate constructive theorem, and full Boolean FEI remains open.
