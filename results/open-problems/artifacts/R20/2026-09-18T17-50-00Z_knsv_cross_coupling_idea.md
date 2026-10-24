# R20 idea before code — KNSV minimal cross-coupling attack

Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

Continuity: do not reopen retired I0100. Continue exclusive R20 claim `operations/claims/KNSV-2026-LOOPY-U.md`. Frozen metric is `N_sep>11`.

Counted Section-B moves for this run are the unused triple selected by the preceding report:

- #5 ADD A PARAMETER AND DIFFERENTIATE IN IT.
- #14 FIND THE GROUP ACTING.
- #26 HUNT THE SPORADIC CASE.

## New route

The previous exact theorem eliminated every `n=12` simpleification of the KNSV five-vertex multigraph separator in which the four excess parallel copies are replaced by internally disjoint connected two-terminal networks. The minimal missing operation is one cross-coupling edge between two internal vertices belonging to different replacement networks.

Attack exactly that first deformation parameter: cross-coupling number `c=1`, still at the first open order `n=12`. Start from the complete transfer-quotient family of 11,284 assignments per multigraph side. For each representative assignment, add every admissible edge joining internal vertices of two different replacement slots. Quotient duplicates at the graph level before comparison. The support-edge automorphism action and equal-slot permutations are used only to remove duplicates; no orbit assumption is allowed to discard a graph unless exact graph equality/isomorphism or the already-proved transfer equivalence justifies it.

Use the ordinary-U forest shadow as a rigorous first filter: `U_G=U_H` implies equality of `det(zI+L_G)` and hence all Laplacian power traces. Compare exact integer trace vectors first. Any surviving cross-side trace collision is checked by exact ordinary-U computation. Only if ordinary U agrees is the loopy polynomial (or the previously isolated hidden `(4,3)` statistic) evaluated.

## What would count as movement

- A certified simple `n=12` pair with equal U and unequal L moves `N_sep` from `>11` to `=12` and REFUTES KNSV Conjecture 8.2.
- Exhausting this one-cross-edge family with no U/L separator is PARTIAL only and leaves `N_sep>11`; it eliminates the smallest cross-coupled port of the source multigraph mechanism.

No numerical SDP or floating-point equality is admissible. Exact integer arithmetic only.