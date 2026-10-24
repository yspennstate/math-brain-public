# C06/H0008 -> P03 reusable lemma: exponential control of the conductance/PF ratio

Source line: C06/H0008 harmonic-boundary research. This note does **not** claim or alter either P03 worker's Lyons--Pemantle--Peres speed-monotonicity objective.

Primary derivation: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T030700Z__report.md`, creation commit `0d45b38ece495e0c52409eca6ec46ea4f319f652`.

Let `B` be forward escape conductance and `mathcal W` the Perron martingale limit on a finite-type supercritical branching tree. The H0008 line has internally proved

- `E[B^{-r};B>0]<infinity` for every `r>0`;
- `P(0<mathcal W<=x)<=Cx^alpha` for some `alpha>0`;
- `E mathcal W<infinity`.

Therefore, for every `0<theta<min(alpha,1)`, with

`X = log(B/mathcal W)`, 

one has

`E[exp(theta |X|); B>0] < infinity`.

Proof: the positive side obeys `(B/mathcal W)^theta <= mathcal W^{-theta}` because `B<=1`; the negative side is `(mathcal W/B)^theta`, controlled by Holder using a positive moment of `mathcal W` of order at most one and an arbitrarily high negative moment of `B`.

The candidate harmonic stationary law has density bounded above by a typewise constant times `B`, so the same exponential moment transfers to that environment.

Potential P03 use: if a regeneration/coupling argument compares a conductance-biased spine law with a PF- or offspring-size-biased spine law, this gives an exponentially integrable local Radon--Nikodym logarithm under the H0008 hypotheses. It can justify entropy/change-of-measure truncations without assuming a second moment of the offspring count. Whether the exact P03 model admits the same two inherited tail inputs must be checked there; this handoff is a lemma template, not a speed result.
