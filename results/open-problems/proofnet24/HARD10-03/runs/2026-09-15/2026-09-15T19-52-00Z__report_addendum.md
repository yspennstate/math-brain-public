# HARD10-03 — certificate addendum for 19:31 UTC report

This append-only addendum records a checker correction and execution results. It does not change the mathematical statements NEW-L24–NEW-L27 in

`proofnet24/HARD10-03/runs/2026-09-15/2026-09-15T19-31-00Z__report.md`.

## Superseded first checker

The initially archived code artifact

`proofnet24/HARD10-03/artifacts/2026-09-15T19-41-00Z__conditional_determinant_check.py`

commit

`5a89e084ba31ebdf21fa41bded143d4b2a9a36b4`

contains an error only in its **final singleton implementation of NEW-L27**: it sets the theorem's parameter `h^2` equal to the actual Hilbert–Schmidt norm squared. The theorem instead defines

\[
h^2=|S|a,
\]

where `a` is an entrywise upper bound on the conditional local kernel. The analytic proof in the 19:31 report uses the correct definition and is unaffected. The first checker should therefore be treated as superseded, not as a valid certificate for NEW-L27.

No overwrite was performed.

## Corrected checker

The corrected append-only artifact is

`proofnet24/HARD10-03/artifacts/2026-09-15T19-46-00Z__conditional_determinant_check_corrected.py`

commit

`2df221fecadf995675f5458911524cdc8c26c6d6`.

It uses the interchange process on `C4`, freezes the edge `(3,0)` to ring once at physical time `0.37`, leaves the other three edge clocks as independent rate-one Poisson processes, and runs to `t=3`.

The conditional one-particle kernel is genuinely non-self-adjoint, so the example directly exercises the issue NEW-L27 was designed to handle.

## Executed finite-state results

The corrected calculation was executed in the research runtime. The results were:

- conditional one-particle kernel versus endpoint kernel extracted from the full conditional permutation distribution: maximum error
  `4.996003610813204e-16`;
- conditional master determinant identity for a dense deterministic test matrix: error
  `1.4432899320127035e-15`;
- localized identity `det(I-K_S) = P(no complete cycle wholly in S | frozen clocks)` for `S={0,1}`: error
  `1.1102230246251565e-15`;
- non-self-adjointness certificate `max |K-K^T| = 0.021380542155412186`;
- for the singleton NEW-L27 test, the correct entrywise parameter is
  `a = 0.24928348948917536`, hence
  `h = sqrt(a) = 0.49928297536484795 <= 1/2`;
- actual singleton local-cycle trap probability:
  `0.24928348948917536`;
- NEW-L27 bound `2 h^2`:
  `0.4985669789783507`.

Thus every asserted finite-state identity and the corrected singular-value inequality passed at floating-point precision.

These computations are sanity checks only. They are not independent verification of the analytic proof and do not prove the full Tóth conjecture.
