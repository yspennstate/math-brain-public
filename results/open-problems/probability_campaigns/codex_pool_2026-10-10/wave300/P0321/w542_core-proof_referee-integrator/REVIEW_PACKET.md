# P0321 referee packet, 2026-10-10

## Source gate

The 2026-09-07 ranking gives only a title, tier 5, and dated unsolved label. Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown* (2022), section VI.2, describes the KTHNY hexatic as fast translational and slow sixfold orientational correlation decay. The review mentions 2D Riesz systems with s>2 and long-range Jellium at s=0 and s=1. It is not a quantified theorem statement for P0321. Current openness: UNKNOWN pending a more recent primary status check.

## Verdicts saved

- w540.S1.1: KEEP as a source/scope gate; it is not a proof claim.
- w541-S1.1: KEEP solely as an independently checked Gaussian surrogate calculation. Its translational correlation is algebraic, so it cannot itself produce a hexatic phase. No transfer to a Riesz Gibbs particle state or bond observable is supplied.
- w540 L1, L2, L3: KEEP as conditional mathematics. The analytic continuation, cumulant summation, and reverse-triangle threshold reproduce exactly under the written hypotheses. None gives those hypotheses for jellium.
- w540 C1 and C2: KEEP as explicit counterexamples to weaker inference rules. They are toy laws; neither is a Riesz state.
- w540 M: KEEP only as a statement of the unproved bottleneck. It is a conjecture, not a partial proof of the actual phase.
- Source correction: Lewin Theorem 47 requires s>d. It cannot be cited to cover d=2,s=1, even though §VI.2 later invokes it in a 2D discussion.

## Independent reproduction of w541-S1.1

For q≠0 and x=re, write α=angle(q,e). The transverse angular integral of (1−cos(k·x)) qᵀPTq equals π|q|²[1−J0(kr)−cos(2α)J2(kr)]. Integrating aT/k over k∈(0,Λ] gives variance aT|q|²(log r+O(1))/(2π), because J0,J2 decay as k^−1/2 after t=kr. The longitudinal covariance is L¹ in k for s<2, adding O(1). The Gaussian characteristic function is therefore between two positive multiples of r^−aT|q|²/(4π). For θ=curl(u)/2, the spectrum is aT/4 on the cutoff disk, Var θ=aTΛ²/(16π), covariance tends to zero by Riemann–Lebesgue, and C6→exp(−36 Var θ)>0. These reproduce both asserted observables without assuming independence.

## Open load-bearing input

Construct an actual 2D Riesz Gibbs state at specified exponent/coupling and establish fast translational correlations together with slow sixfold *particle-bond* correlations in that same state. An elastic Gaussian field has the wrong translational behavior for the hexatic. A defect-controlled argument or another genuine particle mechanism is required. No parent-problem KEEP follows from these verdicts.

NEXT: Prepare the small brain draft with scoped entries; independent referee w545 should audit any new lemma contributed by w542 before promotion.
