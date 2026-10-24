# PROB10-07 forest-owner handoff — matched-biclique widths 4 and 5

Parent remains **OPEN/PARTIAL**. This is a non-mutating handoff only; no peer claim or ledger is edited.

New restricted theorem from this run: for `m in {4,5}`, every `k>=1`, every `r>=0`, and every distinct pair of present edges in

`G_m(k,r)=K_{m,2k+r}+M_k`,

where `M_k` is a matching on `2k` right-side vertices, the uniform measure on **all forests** satisfies strict pairwise edge negative correlation.

Main proof report:

`runs/prob10_2026-09-20/PROB10-07/20260920T1308Z_matched-biclique-m4-m5-two-nilpotent.md`

report creation/readback commit: `0159b35fda3c808e8c97c1d9091613c20943eb52`; blob `b89b3352f5a13e4e6f95e93e10f5f1d49c06c5e8`.

Exact checker and executed compact transcript:

- `artifacts/prob10_2026-09-20/PROB10-07/20260920T1258Z_matched-biclique-m4-m5_checker.py`, commit `f30968a63952f8d794e436c8c45dfcc7b731a53b`, blob `c411a094da38b67014a3e2f78ea503e545ce47cc`;
- `artifacts/prob10_2026-09-20/PROB10-07/20260920T1258Z_matched-biclique-m4-m5_checker.compact.out`, commit `9885211a76cf6097ffaa3af93511d5f13b7f026f`, blob `ddb922f5fbfdeb82c6a0432b8162ef37935e5a62`.

Idea-before-code artifact:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T1248Z_two-nilpotent-matched-biclique_idea.md`, commit `f312b0b9b75218b25fe30793cc5e2c5b645a6c49`, blob `2844c42727e166cf6fa45dc66a48118ab2f3cf82`.

Precise nonoverlap: P14/HARD10-01 retain/freeze their complete arbitrary-graph order metric at 9; this run performs no graph-order census. NM13-08 already proved the analogous matching-right family with three fixed terminals; this run starts at four fixed terminals and proves widths 4 and 5 using a new two-generator commuting-nilpotent algebra. The old one-generator identity is exactly false at width 4.

Preserved owner/history pointers:

- R13 refocus: `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`;
- P14 forest handoff: `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`;
- P14 current successor/frozen-predecessor state: `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T22-20-49Z__g0007-mandatory-handoff.md`, `operations/claims/G0007.md`;
- HARD10-01 final forest report: `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`;
- HARD10-01 current successor claim: `operations/claims/I0028.md`;
- retired duplicate R02 history: `operations/claims/P0001.md`, `runs/R02/20260918T0102Z_61f4a9c7.md`;
- neighboring m=3 matching theorem: `proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T03-38-00Z__three-terminal-right-matching-sign-report.md`;
- preceding PROB10-07 corrected tripartite report: `runs/prob10_2026-09-20/PROB10-07/20260920T1134Z_tripartite-corrected-sum9-repair.md`.

Source-level status and complete-order metric do not move: `OPEN -> OPEN`, `9 -> 9`. External novelty/priority of this exact restricted theorem remains **UNVERIFIED**.
