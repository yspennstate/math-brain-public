# BT4 handoff — account01/B05 20260922T0604Z

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Candidate: `BT4-COMPATIBLE-BYPASS-CONDENSATION-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target: `OPEN_NOT_PROVED`  
Brain: `WITHOUT_VERIFIED_BRAIN`

Canonical report: `proofnet24/collective-BT4/account01/B05/20260922T052912Z-b05-bt4-r11/report.md`, report commit `50a132fde1964a31eb1c3a4ab2f131f3d12fe0ca`, blob `9033957c23706f309a7007530fb65868d736eb61`.

Latest complete candidate consumed: account03/B06 `BT4-R4-F3-MAJORITY-CROSS-v1`, run `20260922T052316Z`, canonical blob `697fde372dee5fec64d03923523d13fc6edcab7a`. Named OTHER-account result applied: account04/B06 `BT4-SIX-DUAL-WALL-LIFT-v1`, shared blob `76bf6ed16c06e44b5a23dd5da5df2fe5fd94a69e`.

New theorem: take any compatible family of genuine same-support bypasses `P_i:a_i->...->b_i` with pairwise-disjoint R interiors and pairwise-disjoint replaced support segments. Switch all of them simultaneously. Let `B_i` be the released support block and `t_i` its terminal vertex. Put an edge `i->j` when `t_i` sends to some vertex of `B_j`. A directed circuit in this dependency graph concatenates suffixes of the released blocks and gives a directed cycle in the exchanged remainder, hence a fourth cycle alongside the three switched packed cycles.

Therefore in a counterexample the dependency graph is acyclic. A sink block has terminal `t_i` with no outneighbor in any released block. If `R_0` denotes the old remainder vertices not consumed by the bypass interiors, then `d^+_{R'}(t_i)<=|R_0|`. In particular, if the compatible bypass family consumes all old remainder vertices, `t_i` is a sink of the exchanged remainder. In the exact-seven normal form all seven of its outneighbors are packed, so some two packed cycles receive at least five; in global NO-SIX the exact fan profile is `(3,2,2)`.

Thus an accumulated strict/equality bypass family that is compatible and covers `R` cannot remain an unstructured collar obstruction: it either closes BT4 immediately or regenerates the canonical five-witness / `(3,2,2)` sink machinery. The statement does not use minimum-packing length equality, so strict collars are included.

First unpaid implication: `BT4-BYPASS-COVER-SELECTION-v1` — from the SIX/SC2/F3 accumulated CROSS/BYPASS interfaces, force either a cross-based splice or a compatible bypass family covering all old `R`; otherwise exploit the exact overlap/common-port/uncovered-core obstruction. No claim is made that the current four ladder/ray paths automatically satisfy this selection.
