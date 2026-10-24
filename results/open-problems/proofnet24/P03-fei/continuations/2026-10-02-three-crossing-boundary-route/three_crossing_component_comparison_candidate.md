# Three-crossing component comparison: exact stress and remaining gap

Date: 2026-10-02. **Open candidate, not a proof.**

The proposed global comparison fails for four crossings, by the
[complete construction](../2026-10-02-component-boundary-obstructions/four_crossing_component_boundary_obstruction_proof.md).
The remaining positive target is the same comparison for at most three
actual sign jumps in one weighted linear score. This note records exact
finite evidence, a counterexample to the tentative constant 2, and an
obstruction to an argument using only monotone order along cube chains.

## Exact formulation

After coordinate sign changes, all score weights are positive. Three
crossings divide the attained scores into four nonempty consecutive
components \(E_0,E_1,E_2,E_3\), with labels \(+,-,+,-\).
Let \(J_{02}\) be the total physical edge probability of jumps between
\(E_0\) and \(E_2\), and \(J_{13}\) the analogous probability for
\(E_1,E_3\). If \(B_+\) and \(B_-\) are the sums of the separate
component influences, exact edge counting gives
\[
 B_+=I(f)+2J_{02},\qquad B_-=I(f)+2J_{13}.
\]
The target is \(\min(B_+,B_-)\le D_3I(f)\), with a universal finite
\(D_3\). No such constant has been proved here. If it holds, the
proved parallel-slab FEI theorem and disjoint-union entropy inequality
give FEI for arbitrary-spacing three-crossing functions.

## Constant 2 is false

Take weights \((33,34,36,40,48)\) and crossings \((-34,0,34)\).
Use open-interval labels \(+,-,+,-\), and label each crossing by an
adjacent label. All attained scores are odd, so no endpoint convention
affects the function. Its four component sizes are \((12,4,4,12)\).
Exact cube-edge counts give
\[
 I(f)=\frac{11}{8},\qquad B_+=B_-=\frac{23}{8},\qquad
 \frac{\min(B_+,B_-)}{I(f)}=\frac{23}{11}>2.
\]
An independent [stdlib-only direct checker](verify_three_crossing_D2_witness.py)
and [exact report](three_crossing_D2_counterexample.json) reconstruct
every vertex and every component boundary. This example does not rule
out any larger dimension-independent constant.

The [integer stress checker](stress_three_crossing_component_comparison.py)
and [full report](three_crossing_component_stress_results.json) test 81
families through dimension ten: equal weights, unique near-uniform
weights, binary lacunary weights, one/two dominant weights, and random
positive integer weights. Cuts occur between adjacent attained scores;
every retained component is nonempty. The report covers 307,503 triple-cut
patterns within 677,496 total patterns for one through five crossings.
All gap patterns are exhausted when their number is below the stated
checker limit; other cases are sampled deterministically. The largest
three-crossing ratio in this finite report is \(23/11\). This is
evidence about tested cases only, not an asymptotic bound.

## Monotone order alone is insufficient

An abstract increasing four-region map on the cube need not obey the
comparison. Let \(H(x)\) be majority on an odd number \(N\ge3\)
of coordinates, taking values in \(\{0,1\}\), and let \(G(z)\)
be the independent increasing dictator bit. Set
\[
 r(x,z)=2H(x)+G(z)\in\{0,1,2,3\},
 \qquad f(x,z)=(-1)^{r(x,z)}.
\]
The region index is increasing along every upward cube edge, and all
four regions are nonempty. Yet \(f\) is a dictator, so \(I(f)=1\),
whereas both component sums equal
\[
 B_+=B_-=1+I(H)=\Theta(\sqrt N).
\]
Here \(I(H)\) means the physical influence of its sign encoding. This
follows from the product-event influence identity and the two majority
pieces, each with dictator probability \(1/2\).

These four regions cannot be the consecutive intervals of a single
positive linear score. To see this even if arbitrary positive weights
\(a_i\) are allowed on the majority coordinates, write \(N=2d+1\),
\(S=\sum_i a_i\), and let \(L\) be the sum of the largest \(d\)
weights. The score range in the majority-zero region has width \(2L\),
while the gap between its maximum and the majority-one minimum is
\(2(S-2L)\). Four consecutive ordered regions would require a dictator
weight \(w_z\) simultaneously satisfying
\[
 w_z>L\quad\text{and}\quad w_z<S-2L.
\]
But \(S\le(2d+1)L/d\), so \(S-2L\le L/d\le L\), a
contradiction. Thus a successful proof must use more than the fact that
the region index is monotone: it must use the common linear score.

## Current gap

The exact finite checks do not provide the desired uniform comparison.
The natural monotone-chain generalization fails as above. A proof must
control same-label jumps of the additive score graph by the remaining
opposite-label boundary, or directly control Fourier entropy after the
component cancellations. Full Boolean FEI and arbitrary-spacing finite-
crossing FEI are not established by this note.

A separate [trace candidate](three_crossing_trace_candidate.md) proves
the exact implication from a middle-threshold boundary trace inequality
to comparison constant 3. Its trace inequality survives the tested cases
but remains unproved.
