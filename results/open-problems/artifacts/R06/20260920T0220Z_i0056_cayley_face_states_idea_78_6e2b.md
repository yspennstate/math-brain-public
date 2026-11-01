# R06 idea before code — triangle-group / face-state attack on the tetrapentagonal clause

Source remains Lyons–Peres Question 6.20 / intake I0056. The frozen regular/co-regular target is still `H_{5,5}={5,5}` with `Phi_V=sqrt(5)` and certified width zero. This note concerns only the still-open second source clause through the vertex-transitive mixed-face graph `T=r{4,5}` of face type `[4,5,4,5]`.

Previous run: exact Schreier spheres through radius 16, best certified ball bound `Phi_V(T)<=33178/38983`, plus an *unproved* order-six recurrence observed for shells 7..16.

Methods for this run (not the previous triple 12,14,19):

- **#18 SAY IT IN ANOTHER LANGUAGE.** Replace the Coxeter-matrix orbit description by the orientation-preserving triangle-group presentation. With `r=s2 s3`, `q=s1 r s1`, check whether the exact relation `(r q^{-1})^2=1` together with `r^5=q^5=1` identifies the tetrapentagonal 1-skeleton as the planar Cayley graph of `Delta(2,5,5)`. This should expose the two pentagon relators and the square relator directly.
- **#13 FIND WHAT ONLY INCREASES.** Track word distance from the identity and classify each edge by distance change `-1,0,+1`; then track which square/pentagon faces run inward or outward. The candidate monotone object is the outward frontier: a face started at a unique minimal vertex or a same-generation edge must close at the deterministic distance forced by its length.
- **#30 ONE SCALE / ONE DIRECTION AT A TIME.** Separate square and pentagon propagation. In particular split same-generation (fraternal) edges into two orientations: pentagon-in/square-out and square-in/pentagon-out. Derive exact delayed counting identities before attempting to eliminate states.

Target mathematical payoff, in decreasing order of value:

1. Prove an all-generation finite-state recurrence/growth function for `T`, not merely fit a recurrence to finitely many shells.
2. If the all-generation induction still has one unproved frontier-anatomy lemma, isolate that lemma exactly and prove every state identity conditional on it.
3. Independently of (1), use the cleaner triangle-group model to extend exact BFS only far enough to test the newly derived state identities and, if it genuinely improves the rigorous source-clause interval, archive that finite improvement.

No computed continuation will be used as proof of an all-generation recurrence. Any finite claim will be checked in exact arithmetic in `Z[sqrt(2),phi]`; theorem-sized claims must be written on the page.