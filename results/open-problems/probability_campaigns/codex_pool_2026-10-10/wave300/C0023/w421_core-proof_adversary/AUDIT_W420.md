Scoped adversary verdict, 2026-10-10: KEEP the conditional route and its explicit open gap. This is not a verdict that C0023 is solved. Referee w422 remains the named independent referee.

Read order: exact primary bond convention and independent obstructions were saved before reading the paired proof; w420's statement was read before consuming its proof output. Audited source: ~/brain_workers/w420/ATTEMPT.md, lemmas L0-L5 and gap G, as read 2026-10-10.

L0: agrees with independently saved C0023-w421-001. Boundary paths can be stopped at first exit; local finiteness identifies unboundedness and infiniteness.

L1: the residue classes modulo R+1 have pairwise separation greater than R. Strong dependence of sigma-fields for separated SETS, applied to one site versus the remaining sites, supplies mutual independence. Pairwise independence would be inadequate; it is not used here.

L2: the Peierls count is valid with the stated strong dependence. A more explicit justification of the topology is as follows. Trace the outside perimeter of the unit squares of a finite good component containing the origin. Every cell on the outside of a perimeter edge is bad. Successive outside cells coincide or meet along an edge or corner, so their centers give a closed star walk. The perimeter-to-centers deformation lies in those closed outside cells, none of which contains the origin (the origin is the center of a good square). Replacing an edge/corner transition by its straight star edge can likewise be done in the union of the two outside cells. Winding about the origin is therefore preserved. Splitting the walk at repeated vertices preserves the sum of winding numbers, so a vertex-simple bad cycle with nonzero winding remains. Its coordinate spans contain zero and are at most its length; the (2m+1)^2 8^m overcount follows. The scalar sum 9t(1+t)/(1-t)^3 and the q term are then sufficient. This is a handwritten topological check, not a formal receipt.

L3: h_w is globally the same finite anchor rule when neighboring blocks refer to it; no anchor is resampled. D_w(M) is contained in D_z(M+L). The support bond count N=d(2H)(2H+1)^(d-1) is correct. Coarse sites at separation greater than floor(2H/L) use disjoint bond sets. The event need not be increasing in p because the proof uses finite-event coupling continuity, not FKG. A strict certificate persists for some smaller p. More quantitatively, an infinite good component at coarse 0 implies an infinite-cluster vertex in S_0; the union bound gives theta_d(p)>=P(0 has an infinite good component)/(2L+1)^d, so the final countable-union step can be replaced by a finite one.

L4: M tends to infinity with L FIXED. The finitely many finite clusters from the seed eventually stop producing anchors; the first infinite-cluster seed stabilizes, and the finitely many required connecting paths eventually fit. Only then does L tend to infinity. The resulting iterated limit says nothing about M/L along a successful diagonal.

L5: the fake numerical family correctly refutes the diagonal inference, within its explicitly numerical scope. C0023-w421-004 strengthens this diagnosis with an actual stationary finite-dependent field built as a local factor of iid seeds. It does not assert that w420's particular anchor event realizes that countermodel.

The exact missing premise on this route is G: under hypothetical theta_d(p_c)>0, find finite M>=L>=1 with q_{p_c}(L,M)<800^{-(floor(2(M+L)/L)+1)^2}, or a replacement threshold that still guarantees positive coarse percolation. w420 correctly leaves G unproved. An iid/local/ergodic description of the field does not by itself close G. A fixed aspect ratio a with q_{p_c}(L,aL) tending to zero WOULD close it, but that same-scale connection estimate is not established here.

Quantitative refinement for review. The route requires positive coarse percolation, not probability greater than 9/10. The same Peierls expression gives a positive lower bound already at q<=101^{-K}: t<=8/101 and q<=1/101, so
P(0 in infinite good component)>=1-1/101-9(8/101)(109/101)/(93/101)^3
 = 378252/81240057 > 0.
Thus a strict certificate q_{p_c}(L,M)<101^{-K} also suffices in L3. This loosens the required error by a factor (800/101)^K. It does not prove that any such pair exists. Exact arithmetic and the contour argument require the referee's independent check before theorem promotion.

NEXT: w422 independently checks the countermodel and the 101^{-K} refinement; the research step remains a fixed-aspect-ratio critical anchor estimate.
