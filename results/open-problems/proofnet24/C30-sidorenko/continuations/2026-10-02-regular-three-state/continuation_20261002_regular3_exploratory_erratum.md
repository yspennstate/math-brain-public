# Exploratory three-state calculation: discarded root fixing

2 October 2026. The files
`continuation_20261002_regular3_cone_I_exploratory.json`,
`continuation_20261002_regular3_cone_T_exploratory.json`, and
`continuation_20261002_regular3_I_order*_exploratory.json` are INVALID as
homomorphism-density certificates. No theorem was claimed from them.

The scratch calculation fixed one source vertex to host state0 and
multiplied by3. That step is valid in the vertex-transitive Klein-group
host family, but is not valid in the arbitrary regular symmetric
three-state family being tested. Regularity alone does not make the
conditional homomorphism weight independent of the root's host label.
All three root labels must be enumerated.

An analytic cross-check exposed the mistake: on the identity cone the
two centered eigenvalues are alpha plus/minus sqrt(beta^2+gamma^2+delta^2
-beta*gamma-beta*delta-gamma*delta). The leading fourth-cycle coefficient
must therefore be5s^11 times their fourth-power sum. The invalid
root-fixed polynomial contradicted that exact coefficient. The
corrected enumeration is being saved in a new standalone script and
separate JSON, preserving this history rather than silently replacing it.

This mistake does not apply to the four-state Klein-group theorem: there
simultaneous translation acts transitively on the host and preserves all
edge weights. Moreover its entire density polynomial has three
independent generators (vertex, transfer, Fourier flow) and separate
audits.
