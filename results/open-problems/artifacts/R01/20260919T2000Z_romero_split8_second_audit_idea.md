# R01 independent audit idea — ROMERO-2025-SPLIT8

Audit target: the complete R06 `n=8` split-reliability layer, not the full Romero/Brown–McMullin open problem.

Fresh methods for this run: **B20 / B27 / B30**.

- **B20 — FIND WHY THE ALGORITHM FAILS.** Treat the finite proof as hostile code: look specifically for omitted two-terminal isomorphism classes, an invalid terminal quotient, disconnected/complement leakage, a wrong connected-subgraph recurrence, a wrong Matrix–Tree minor, or a Bernstein-basis implication that changes with `m`. The audit passes only if every possible omission point is closed.
- **B27 — SWAP THE QUANTIFIERS.** The dense claim is `for every H, for every p`. Verify that coefficientwise domination is established for each graph before taking the universal `p`; this is stronger than sampled-`p` optimization and is logically valid because all graphs in a fixed `T_{8,m}` share the same Bernstein basis.
- **B30 — ONE SCALE / ONE DIRECTION AT A TIME.** Audit the sparse half `m=14,...,19` independently through exact two-forest determinants and the dense half `m=20,...,26` independently through terminal-preserving complement orbits and full coefficient vectors, then glue only after both halves pass.

Independent implementation plan: a fresh R01 C program, written from the mathematical description rather than copied from the owner artifact, will (i) reconstruct the six low-density determinant witnesses; (ii) independently generate all terminal-fixed `S_6` complement orbits for missing-edge counts `2,...,8`, verify orbit-stabilizer totals against `binom(28,k)`, and (iii) recompute exact split-coefficient vectors by a connected-component recurrence. The audit will compare only final invariant counts/claims, not internal owner data structures.

No owner-side theorem is strengthened here. This is checking work on a complete neighboring package, permitted only because R06 already has the P26 full-proof PASS and lacks one distinct OTHER audit.