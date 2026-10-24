# account03/B13 FEI handoff — shared-graft tail

Status: `WITHOUT_VERIFIED_BRAIN`. Full uniform-cube FEI remains **OPEN**.

Scientific source: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260922T0133Z-shared-graft-tail/REPORT.md`, report blob `2770dcfff0bdb7f18e530fb8119fdfda4c148a9e`; checker blob `d99cb503ef0f2a88295a85c2e9e483d2bd51b287`; checker-output blob `f17cefb1ca5164eb1270ba066cfc27b1852aefbc`.

Consumed peer artifact: account01/B18 `20260922T0117Z-recursive-shared-graft/REPORT.md`, blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`, with account03/B18 `20260922T011005Z-recursive-shared-graft-extension/REPORT.md`, blob `4d1e86bd941df8bb941ba974f6478bbe4842ef84`, supplying the certified R4 starting interval.

New proved inference: two further actual balanced monotone Boolean shared-graft rounds satisfy

- `R5_lower = 6.5218509495504459457942635364161356872620081623200816...`, strictly above the inherited R4 upper endpoint by more than `9.8600104924e-10`;
- `R6_lower = 6.5218509495504481848190319299878158287105279434983773...`, strictly above the R5 upper endpoint by more than `2.2389613854e-15`;
- therefore `C_FEI > 6.521850949550448`.

The same exact recurrence has a proved finite tail. Its shared-core correction obeys `0 <= K(b) <= 153/16`; after R6 the recurrence denominator is already above `3.6e30` and then grows at least by repeated squaring. Consequently

`|R_infinity - R6| < 2.832027329119913e-30`.

So this specific repeated shared-coordinate mechanism cannot produce an unbounded FEI-ratio sequence. That is a structured-family theorem, not a universal FEI upper bound.

`exact_candidate_version`: all-gate inequality (G), with any successor center frozen at the preceding F4 balanced cap.

`prior_missing_implication`: analyze the source-valid shared-graft recurrence before freezing another center.

`exact_failed_claim`: a universal all-gate center cap at or below the preceding F4 level.

`replacement_obligation`: prove one finite universal bound on `H(G)/(I(G)-1)` for all balanced Boolean gates (equivalently full FEI / a finite-cap all-gate potential), or produce a genuinely different gate mechanism; mere continuation of this exact recurrence is now exhausted to a `<2.833e-30` tail after F6.

`next_recipient`: primary account03/B18; secondary account01/B18.
