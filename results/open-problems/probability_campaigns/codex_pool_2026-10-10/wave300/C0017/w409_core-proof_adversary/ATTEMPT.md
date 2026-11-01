# C0017 adversarial work, w409

This file separates the independent obstruction from the later paired-proof audit. Current openness is UNKNOWN: the historical primary statement is verified, but a 2024 primary proof claim has not received a full proof audit here. SOURCE_STATUS.json records the evidence. No proof of conformal invariance or novelty is claimed.

## Independent obstruction, saved before paired proof

Date: 2026-10-10. No w408 proof has been read.

Take an abstract horizontal rectangle crossing function depending on aspect ratio r=width/height. For any alpha>0 put h_alpha(r)=1/(1+r^alpha).

It satisfies h_alpha(r)+h_alpha(1/r)=1, h_alpha(1)=1/2, continuity, strict decrease in r, and common-side-length scale invariance. On a compact interval [a,b] contained in (0,infinity), both h_alpha and 1-h_alpha have a positive minimum. These resemble rectangle symmetry and scalar RSW constraints. But h_1(2)=1/3 and h_2(2)=1/5, so the constraints do not determine even the value at aspect ratio 2.

The proof is elementary: substitute 1/r in the defining formula, differentiate, and use continuity on [a,b]. This is an obstruction to a particular inference, not a counterexample to conformal invariance. No probability law on planar configurations, FKG inequality, domain Markov property or compatibility between overlapping rectangles is constructed. Those must not be credited to this example.

The analytic lane's missing step is a vanishing signed sum of contour defects for the actual square-bond event observable, together with its boundary interpretation. REDUCTION.md proves the deterministic implication and leaves that probabilistic estimate open. PAIRED_AUDIT.md checks w408's separate martingale route.

## Independent cell-defect obstruction, saved before paired proof

Let f(z)=conjugate(z), sampled on the square grid of mesh delta=1/n in [0,1]^2. Define the oriented edge integral by the trapezoid rule: I([u,v])=(f(u)+f(v))(v-u)/2. Because f is affine on each segment, this is its exact integral.

For a counterclockwise mesh cell c, D_delta(c)=sum_{edges of c} I(e)=2i delta^2. Thus every cell defect tends to zero, uniformly, and f is bounded and Lipschitz with a full uniform limit. But all interior edges cancel, and the sum of the n^2 cell defects equals the fixed outer contour integral 2i. The limit f is not holomorphic. This refutes any unrestricted inference from vanishing individual cell defects to a vanishing macroscopic contour integral.

A sufficient absolute bound is sum_{c inside R}|D_delta(c)|=o(1) for every fixed interior rectangle R. A weaker sufficient hypothesis is that the signed sum tends to zero for every such R. With O(delta^-2) cells, max |D_delta(c)|=o(delta^2) suffices, whereas O(delta^2) or o(1) does not. A local defect estimate must retain the area normalization or demonstrate cancellation. This example is deterministic, and does not pretend to satisfy percolation-specific observable identities.
