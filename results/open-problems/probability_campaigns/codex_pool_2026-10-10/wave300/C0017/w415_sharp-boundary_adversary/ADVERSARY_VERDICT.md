# Independent adversary check of w414

2026-10-10. Reviewer w415. Reviewed w414/ATTEMPT.md, Lemmas 1-3 and the stated auxiliary bridge B, after saving my own derivations. This checks the proof itself. w416 remains the assigned referee.

Verdict: KEEP within its stated scope. I found no counterexample to Lemmas 1-3. The result refutes B, which omits marked prime-end convergence; it does not refute or prove C0017.

For Lemma 1, first condition on the corridor's edge states. If any corridor edge is closed, a cut separates the source and sink. If all are open, connectivity is equivalent to the two chamber connection events. The corridor and the two chamber edge families are disjoint and independent, so averaging gives p^k q_L q_R. External wirings that bypass a cut would invalidate this argument; the lemma explicitly excludes them. Arbitrary internal chamber dependence is harmless only under the stated independence of the three families.

For Lemma 2, the corridor's interior columns have only the row y=m. Every source-to-sink path must therefore traverse the single gate-to-gate chain. The removed vertical band has width k/n and moves to x=0. For any compact subset of (0,1)^2, its minimum x-coordinate is positive, and eventually exceeds b/n; this proves the kernel assertion without assuming crossing stability. The inward boundary stays at distance at most b/n from the left square boundary. The polygon remains connected and Jordan because each gate has a positive-height neighborhood in the interior of the union.

Lemma 3 is the key step. An exit on J_n from z_0 must first pass through the gate Sigma_n. Before that passage, Brownian motion remains in the right chamber. Ignoring the chamber's top, bottom and right absorbing walls enlarges the event to first hitting the vertical line within Sigma_n. The half-plane hitting density is at most 1/(pi s), where s=1/2-b/n. Multiplying by gate length 1/n gives 1/(pi n s). Since n>=81 implies b/n <= (2 sqrt(n)+1)/n <= 19/81 < 1/4, s>1/4. Thus the boundary arc has harmonic measure at most 4/(pi n) and disk angular length at most 8/n. Its two marked preimages have chordal distance at most that angular length. This directly establishes collapse of the marks in conformal coordinates despite their fixed Euclidean coordinates.

Minimal missing premise in B: preserve the marked boundary prime ends (or use geometric conditions strong enough to imply this). Unmarked kernel convergence and Euclidean convergence of boundary marks cannot replace it. Adding that premise removes this counterexample but is not, by itself, a proof of crossing convergence.

For the comparison with canonical critical square approximations, only a uniform positive RSW crossing bound is needed. Cardy's value on the square lattice is not assumed. The target's hardest remaining piece is still identification of the correctly marked square-bond scaling limit as Cardy's/SLE(6), not compactness or this boundary calculation.

NEXT: w416 can use this adversary verdict when checking w414, and independently check w415's separately saved two-bond and affine-metric obstructions.
