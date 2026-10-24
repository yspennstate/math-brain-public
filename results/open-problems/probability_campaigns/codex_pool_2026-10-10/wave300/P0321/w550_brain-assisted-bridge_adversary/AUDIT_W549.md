# Audit of w549's P0321 bridge

2026-10-10. Read INDEPENDENT_DERIVATION.md first, then STATEMENT_FIRST.md and BRIDGE_PROOF.md in w549. Verdict: KEEP G1–G6 as a conditional point-process implication under their explicitly listed hypotheses. This is my independent reconstruction, not a review of another audit. No Riesz phase theorem is proved.

For G1, a central witness puts the nearest nucleus within r/8. The six angular witnesses give z dot(q-p)>=7|z|r/32 for |z|>=r. The squared-distance difference is at least (159/1024)r^2, excluding the entire exterior of B(x,r). A point outside B(x,3r) is farther than 2r from an interior cell point while the nucleus is less than 9r/8 away; it cannot alter the cell. Every shared-edge neighbor lies within 17r/8, so the complete mark and its degree are determined locally. This is a valid localization argument; checking only the nucleus's location would not have been enough.

For G2, the local shield is measurable from the local configuration. Set the approximant to zero when it fails. Its difference from the bounded mark is then at most the shield-failure indicator. The seven-disk union bound gives 7V(r/32), without independence.

For G3, layer-cake integration over [-1,1]^2 bounds a real covariance by 4alpha. Four real/imaginary terms bound a complex covariance by 16alpha. Replacing both factors in the joint expectation costs 14V; replacing their means costs another 14V. The stated bound 16alpha+28V is safe. It requires alpha for the full point-process restrictions, not only their particle-density pair function.

G4–G6 follow with the stated uniformities. In G4, r=D/12 makes the two window radii D/4 and the void argument D/384. G5's logarithmic r_D gives a void error of order D^(-p-1) and a mixing factor of order D^(-p)(log D)^(kappa/nu); all constants must be independent of window size and separation except for the displayed factor. G6's rearrangement gives c/32. Rotation invariance makes the spatial mark's mean zero, but does not set its two-point moment to zero.

The most important missing premise for applying this bridge is a uniform quantitative bound on alpha for the actual Riesz point process. A fast density pair function does not supply it. PAIR_DENSITY_COUNTEREXAMPLE.md constructs a stationary, simple, finite-intensity point process with compactly supported truncated pair density and Gaussian void tails but alpha bounded below at every distant integer translate. This is an exact counterexample to the substitution, not to the properly stated bridge.

Separately, effective-field algebraic order still needs a scale-relative comparison for the selected geometric bond observable. The spatial nearest-cell mark in G1–G6 must not silently be replaced by a two-particle Palm mark. Neither our counterexamples nor w549's upper bound supplies the microscopic algebraic lower bound on a common phase interval.

Artifact review is limited to the saved BRIDGE_PROOF.md read in this session; a later revision requires checking its changed theorem assumptions. w551 remains the designated referee for newly originated w550 claims.

NEXT: Referee checks S1.2–S1.3 and the Cox counterexample; retain the explicit block-mixing and observable hypotheses in any brain edges.
