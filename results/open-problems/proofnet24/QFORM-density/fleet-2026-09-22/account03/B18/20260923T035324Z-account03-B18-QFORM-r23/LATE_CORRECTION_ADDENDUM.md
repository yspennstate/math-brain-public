# account03/B18 r23 — final correction refresh addendum


The following late correction events were explicitly checked after the main report was written:

1. `QFORM-ANCHOR-PACKET-ONE-LOCAL-MINOR-FALSE-v1`: aggregate Schur/Frobenius mass does not force one large physical minor. The r23 theorem does not make that inference; it retains the determinant-weighted distribution over all rank-three bases.
2. `QFORM-N3-LOCAL-COLLISION-BEFORE-AGGREGATION-FALSE-v1`: a local independent-copy/fractional collision certificate can diverge before bank aggregation. The term `disjoint-volume probability` in r23 is a different object: it is the probability that two independent **volume-sampled rank-three bases** are disjoint, after the full rank-three aggregate factor has been formed. No local independent-copy collision endpoint is used.
3. `QFORM-N3-DPRIME-D5-NONEXHAUSTIVE-v1`: fixed cross-volume D'/D5 certificates are not exhaustive. r23 does not claim exhaustiveness and does not require a fixed cross-rank-three cut.
4. `QFORM-NEARRANK1-RECOLOR-STABILITY-FALSE-v1`: perturbative transfer of an exact rank-one recoloring bound into a thin Frobenius tube is false. r23 performs no perturbative recoloring and no coefficient-continuity step; its diagonal/affine additions are kept exactly as coordinatewise unit-modulus phases.
5. `QFORM-NEARNULL-JOINT-PAIR-CAP-FALSE-v1`: bounded joint density of a dependent pair is not enough for the curved near-null chain. r23 never replaces original product provenance by a joint-density cap.
6. `QFORM-CROSS-ONLY-ANCHOR-E2-TO-FULL-PAIR-SCHUR-FALSE-v1`: cross-only Schur certificates need not survive the true full pair Schur complement. No Schur-complement surrogate is used in r23.

Accordingly, none of these corrections invalidates `QFORM-CAPPED-BASIS-SEPARABLE-PHASE-v1` or `QFORM-DISJOINT-VOLUME-PAIR-FRESNEL-v1`.

The owner target remains open. The new theorem is a supporting full-ambient branch conditional on a product-preserving rank-three packet with positive determinant-entropy/disjoint-volume certificate; it does not assert that the bare three-large-eigenvalue hypothesis forces such a packet.
