# account03/B11 r26 scope addendum

The structural family in the main r26 handoff correctly disproves a universal **fixed-cardinality packet extraction** step, but the first handoff overstated the repair as necessarily high-cardinality bank aggregation.

Two existing receivers apply directly:

1. Predecessor account03/B11 r24 (`math-open-problems@c157c4b54b2b34fee3a7cc05d337c2fd654a77e7`) detects the r26 family through its balanced defect STAR theorem. Here `F=J-A` and every row has exact defect energy

`sum_{j!=i} F_ij^2=(6n-4)delta^2`.

At `delta=n^(-1/2)` this equals `6-4/n`, so the collective STAR certificate is fixed-scale even though all bounded-cardinality blocks tend to rank one.

2. The spectral-window ridge theorem (`math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`) pays the large-n family itself. For `n>16384`, the residual eigenvalue `2/sqrt(n)` is below `1/64`; the high spectral projection is exactly onto `span{1,u,v}` and has diagonal leverage `3/n<1/32`. Hence the full output has a continuous density with

`||p_Q||inf <=288 sqrt(3e)/13 <64`.

Thus this family is a diagnostic witness against a local-packet structural lemma, not an unpaid QFORM chamber. The correct next B11 debt, after combining r24 with the ridge theorem, is the **high-spectral-leverage balanced defect receiver**: pay STAR/CROSS-2VOL when the high spectral projection is not diffuse, especially high augmented-leverage stars and collective second-volume endpoints, while preserving original-coordinate product provenance.

The designated account04/B11 splice from the main handoff remains valid: if the same near-rank-one magnitudes carry one frustrated triangle, `eta=4delta` gives

`||p_Q||inf <=6 sqrt(pi)/(1-8delta)<11.344`

for `delta<=1/128`.

Full QFORM remains open. Global continuity remains open. Canonical scope addendum: `yspennstate/math-open-problems@8bf8e11ea552e8d807709a041b277629b048d3f7`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T093835Z-account03-B11-QFORM-r26/SCOPE_ADDENDUM.md`; verifier later committed in the same run folder and terminates `QFORM_B11_R26_BALANCED_FIXED_PACKET_CHECK_PASS`.
