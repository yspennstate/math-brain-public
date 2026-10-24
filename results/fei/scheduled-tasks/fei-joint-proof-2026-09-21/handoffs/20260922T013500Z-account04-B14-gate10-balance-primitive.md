# account04/B14 handoff — arity-10 gate falsifier is balance-primitive under physical restriction

Source scientific report: `proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260922T012003Z-gate-witness-balance-primitive/REPORT.md`, initial report commit `28c8292b76b11c904476f1529a31b3f924a77b48`, read back after checker/output at `85684b456b3780d6821815f2064b01f538c494ac`, report blob `c8618d08a3bb7cbfebcb40ecb645defd8f3fa1a4`.

Consumed exact peer results:
- account01/B14 `20260922T0044Z-balanced-gate-margin-refutation`, blob `776ade5c2e2017844785b09ab7af50c7eaf54c03`: balanced-uniform identity `c_G=4(H/(I-1)-6.4548)`.
- account03/B12 `20260922T004418Z-arity10-gate-refutation`, blob `d12fe592f4fa6db16cb571557f6cc41392dd5860`: genuine balanced monotone arity-10 gate with `c_G>0.018289126551422926`, rigorously above the globally certified AND-family margin `0.01`.

New exact calculation: exhaust all `3^10-1=59048` proper coordinate restrictions of that arity-10 gate. Exactly `9514` are balanced. None has 8 or 9 free coordinates. Of the balanced restrictions, exactly `460` have `I>1`; after deleting zero-influence free coordinates, every such restriction has effective arity 4 or 6. Their exact Walsh/influence data fall into seven types and

`max H/(I-1) = 46/5-(9/5)log2(3) = 6.347067498701918873... < 6.4`.

Hence every proper balanced restriction has gate margin strictly below `-0.2192`, whereas the parent arity-10 gate has margin above `+0.0182891`. The known obstruction therefore cannot be reduced to a smaller balanced gate by ordinary physical coordinate restriction; its positive gate defect is collective across all ten active coordinates in this precise sense.

Checker SHA-256 `23b5a94ebe16cf486281cb64b66db83d17e6560d5d273c245c19428c0f09f2d7`; output SHA-256 `ca4dd0de21c9993dd2c567512db825ac690ad252ad783bbdf60acfd69e69a1`.

Full FEI remains OPEN. The current read-once-potential AND/decomposable extremality candidate is REFUTED, not merely unproved. A smaller falsifier, if one exists, must be a different gate or exploit nonuniform biases; simply restricting the certified arity-10 balanced witness cannot supply it. No prescribed-coordinate payment or weakening of the addressing/erasure obstruction is claimed.
