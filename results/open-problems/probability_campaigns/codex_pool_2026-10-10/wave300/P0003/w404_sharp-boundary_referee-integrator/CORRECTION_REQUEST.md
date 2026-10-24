# C0096 math-brain card source correction

The existing `math-brain-build/export/population/nodes.jsonl:2804` C0096 card says: `Known only for n = 1 at the critical point (site percolation, Smirnov)`.

The cited [BDGS source, Section 3.4](https://arxiv.org/html/1206.2092) states that n=1 corresponds to the Ising model and that for n=1 and z=1/sqrt(3), its interface has a proved SLE(3) limit. The card's parenthetical should read `critical Ising interface, SLE(3)` at that point. The source says the other n and z cases in Conjecture 3.7 are conjectural. This correction is limited to the n=1 critical identification; it does not claim P0003 is solved.

Proposed review action: compare the card with BDGS Section 3.4 lines around Conjecture 3.7, then supersede the erroneous card statement through the integrator. The current export and live store were not edited.
