# FEI handoff: quadratic symmetry payments

20 September 2026. Full FEI remains unproved in this continuation.

Read `REPORT.md` for the complete proof and exact scope; `WORKLOG.md` preserves the attempted routes and their outcomes. Run `python3 verify_quadratic_symmetry.py --output verification.json` to reproduce the exact checks. The other exploration script requires NumPy and is explicitly floating-point exploratory work.

## Reusable positive result

For an arbitrary d-part-symmetric Boolean core h and an arbitrary quadratic phase Q on the same coordinates,

    H((-1)^Q h) <= (12.04 + log_2 d) J((-1)^Q h).

More generally, for a product of independently supported cores h_t, each with at most d_* symmetry parts, the same bound holds with d_*, independently of the number of cores. Quadratic interactions may couple every core to every other core. For any number of fully symmetric cores the constant is 12.04.

The physical influence budget is folded: J=sum_i min(Inf_i,1-Inf_i), so J<=I. This is NOT a claim for minimum influence under arbitrary linear changes of input coordinates.

The key coordinate payment is j_i>=1/4 whenever a quadratic neighbor row mixes a symmetry part; a coordinate with a quadratic edge outside its independently supported core has j_i=1/2. Removing these coordinates leaves a character times a product of part-symmetric functions. Physical deletion costs at most two entropy bits per coordinate and average remaining folded influence cannot increase. This proves the bound and the sharper defect margins in the report.

The only non-elementary external input is the published O'Donnell–Wright–Zhou part-symmetric FEI theorem. The constants are theirs. Publication priority for the quadratic-twist extension has not been cleared.

## Additional universal identity

For any Boolean h, without symmetry, and any nonzero quadratic row,

    j_i(h) + j_i((-1)^Q h) >= 1/2.

The report gives a low-folded-influence transfer corollary with explicit leaf-certificate assumptions. Do not omit those assumptions.

## Remaining full problem

Do not replace quadratic phases by arbitrary high-degree phases without a different payment. A rare monomial perturbation breaks the original full symmetry while all relevant influences tend to zero. The universal weighted-erasure / hereditary allocation estimate is still missing; the new class supplies certified stopping leaves rather than proving that missing estimate.

Do not revive the refuted absolute-overlap selector, pointwise erasure converse, full-resolvent targets, or fixed-coefficient affine drift payments. Existing positive constant-four affine-clause results retain their stronger constants and their own independent-clause hypotheses.

Exact output: 67,732 symmetric-core / graph cases, 29,896 partition / core / graph / linear cases, 840 sampled general product cases, 108,506 graph-structure checks, 171,150 physical leaf tables, and 4,640 universal pair coordinate checks. All reported checks passed; families overlap and do not constitute unrestricted all-function coverage. No independent review or formal verification is claimed.
