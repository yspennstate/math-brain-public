# P0019: Half-space case via reversal and logarithmic-time Gaussian recurrence

Label: sketch; author checked only. Independent audit: PENDING w347.

PROOF SKETCH, pending independent verification: Brownian motion started inside a half-space in dimension d>=2 should have the whole closed outward hemisphere as its cluster set of normalized approach directions at its first boundary hit. The proposed route uses the conditional reversed normal path as a three-dimensional Bessel bridge, the reversed tangential paths as Brownian bridges, and dense Gaussian directions in logarithmic time.

Assumptions: Half-space domain; Brownian motion starting at positive normal height; The conditional reversal and bridge absolute-continuity identities still need a full check

Condition on exit time T=t>0 and tangential exit location. Reversing the terminal path is expected to give an independent product of (d-1) Brownian bridges and a BES(3) bridge, started at zero, on the reversed interval. On any [0,epsilon] with epsilon<t, bridge laws are absolutely continuous with respect to unconditioned Brownian motion and BES(3); the density is the remaining-time transition density divided by its starting value. Represent BES(3) as the radius of three independent Brownian coordinates, independently of the d-1 tangential coordinates. For a Brownian vector W of dimension d+2, V_u=exp(u/2)*W_(exp(-u)) has stationary centered Gaussian covariance exp(-|u-v|/2), and hence its Gaussian stationary process is ergodic. Every open cone of positive Gaussian mass is visited infinitely often. The map v -> (v_1,...,v_(d-1), sqrt(v_d^2+v_(d+1)^2+v_(d+2)^2))/|v| has support the closed outward hemisphere. A countable base of cones gives all directions as subsequential limits. Absolute continuity would pass this almost sure property to the reversed bridges. The unresolved proof-check obligation is to derive the stated conditional reversal and bridge density from killed one-dimensional Brownian transition and first-hitting densities, including the zero starting boundary. This obligation is not replaced by a simulation.

Limits: Only a sketch is claimed; it is a concept card, not an accepted theorem. It does not cover arbitrary domains in d>2.

Existing card: math:probability.core:open-problem-p0019-brownian-exit-approach-directions-in-higher-dimensions
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:5773
