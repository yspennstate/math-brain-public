# Independent analytic reconstruction of finite-phase source admission

Source: A052/runs/20261023T120425Z-fleet03-A052-critical-source-structure/ALIGNMENT_PROOF.md.
Scope: Sections1--6 analytic normalization, singleton and ORIGINAL-pair
formulas, full-bank invariance and bent corollary. Excludes numerical
census and the four-bit D_3-maximality certificate. Reviewer A005;
no repair or altered hypothesis supplied.

The degree<=d output signs form a finite multiplicative group. Affine
input conjugation preserves their degree, so the joint action is finite.
Maximizing D_K in the orbit of a positive witness retains positivity.
If that witness has least essential dimension among ALL positive
K-witnesses, any orbit image losing an essential variable would be a
smaller witness, a contradiction. Thus exact smaller-function eligibility
survives. Maximization over this SAME finite set also licenses the ratio
alternative: choose largest H/I; then every competitor has H-RI<=0.
This argument concerns the initial witness, not spent bank resets.

For the singleton split, direct inverse Walsh on the query bit gives
the rows (a_T+s b_(T+v))/2 and (a_T-s b_(T+v))/2. Their squared entropy
sum does not depend on s. The outside influence change is B_v/2.
The query edge disagreement changes by(C_0-s C_v)/2. Their sum is
the displayed physical cost. Choose s to maximize s C_v; v=0 with
opposite sign separately forces C_0>=0. Weighted averages are just
finite sums. Multiplying one full child by a character changes neither
its H nor its full affine minimum a, so the complete reserve is fixed.

For a pair, inverse Walsh on the TWO query bits gives factor1/4 and
all four signed terms; every outside label T remains. The outside cost
is B_v/4. In each queried direction, the changed branch touches ONE
of the TWO unordered square edges. That edge has root weight1/2, and
its disagreement changes by(C_(j,0)-s C_(j,v))/2. Thus the two query
costs are exactly(C_(j,0)-s C_(j,v))/4. Summing proves equation(8)
with its factor1/4, hence equation(9) by D_K extremality.
All four terminal H and a values are unchanged, so S_A* is unchanged.
The bank identity follows from the physical partition identity
I(root)=I_A+E I(child), not from a surrogate unsigned spectrum.

Pair entropy really depends on s: starting with four constant+1
branches, flipping one gives the two-bit point defect, whose four
Fourier magnitudes are1/2, hence entropy2 instead of0. Thus singleton
absolute-correlation simplification cannot be copied into the pair case.

For a bent h, its coefficient magnitudes are all equal, and each
two-term entropy sum is even in b. Character shifts only permute those
magnitudes, giving E_v=E_0. Every Inf_j(h)=1/2 by Parseval for a shift,
so B_v=0. The alignment inequality gives C_0>=|C_v| for all v;
Parseval for the ACTUAL Boolean product gh gives the claimed bound
and the equality condition. No independence of Fourier labels is used.

Verdict: the stated analytic scope HOLDS without repair. It establishes
an admissible finite normalization and necessary signed constraints,
not a paid-pair existence theorem. The new phase-gap proof in PROOF.md
shows independently why rare activated seeds already satisfy that
normalization at K>4, while failing exact smaller-child eligibility.
