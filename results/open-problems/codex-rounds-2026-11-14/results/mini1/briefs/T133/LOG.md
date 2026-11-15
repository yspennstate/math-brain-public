# T133 work log

Task received 2026-11-14, approximately 22:01 Asia/Tbilisi (18:01 UTC): "push this problem forward by one checkable piece."

## 18:01–18:03 UTC: orientation and literature screening

All writes are confined to this folder. The task's explicit restriction rules out the global mesh, checklist and brain commands that write elsewhere. No git or subagents are used. Startup memory and the compute governor were read directly. Governor: `warn`, `owner_away_open`, CPU saturated; only small read operations are being run.

Shell operations use `env OMP_NUM_THREADS=1 nice -n 15 ...`. macOS printed `nice: setpriority: Operation not permitted`; startup memory records this can happen when the inherited process already has nice 20. This will be checked before numerical work.

Web search queries:

- `six vertex domain wall arctic curve proof general weights 2025 2026 Aggarwal`
- `arctic curve six vertex disordered antiferroelectric rigorous proof 2024 2025`
- `"Boundary statistics" "six-vertex" Gorin Liechty arxiv`
- `"arctic" "six-vertex" "proved" "2026"`
- `"arctic" "six-vertex" "2025" "proof"`

Opened arXiv pages for 0907.1264, 1812.03847, 2509.25442. Screening found no general DWBC arctic-curve proof. It found Gorin–Liechty, arXiv:2310.12735 (2023, published 2025), claiming GUE-corners boundary statistics for all positive symmetric weights with Delta < 1, including the antiferroelectric regime. Need inspect the theorem and its scope before deciding whether the instruction to stop for a substantial advance applies. This predates the brief's November 2026 check, so its chronology must be stated plainly.

## 18:03 UTC: substantial advance found; stop branch selected

Additional web query `six vertex arctic curve rigorous general weights 2026 domain wall limit shape` found:

Alexey Bufetov, *Limit shape for domain-wall six-vertex model*, arXiv:2609.20576v1, submitted 17 September 2026.

Opened both https://arxiv.org/abs/2609.20576 and https://arxiv.org/html/2609.20576v1. The abstract calls this an announcement. Theorem 3.1 states the height-function limit shape for all Delta < -1 and all a/b > 0. Theorem 3.2 states it for -1 < Delta <= 1/2 and all a/b > 0. Section 4.2 identifies the outer boundaries as the Colomo–Pronko and Colomo–Pronko–Zinn-Justin curves. This is a substantial advance beyond the brief's mathematical status, although it was posted before the claimed November 2026 check. The remaining disordered interval 1/2 < Delta < 1 is not covered.

Per instruction 1, select the literature-update branch and do not start an independent computation or proof. Inspect the rest of the note to distinguish announced results from proofs actually supplied.

Resource check command: `env OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c 'ps -o pid=,ppid=,ni=,comm= -p $$ -p $PPID'`. Output: `nice: setpriority: Operation not permitted`; `zsh:1: operation not permitted: ps`. No numerical workload launched.

## 18:04 UTC: source audit and deliverables

Opened https://arxiv.org/pdf/2609.20576 and compared its extracted text with the HTML. Requested PDF pages 4–5 through the web screenshot tool as a supplementary check. Main audit uses the explicit theorem text, not search snippets.

Read Section 5 and searched the full text for `proof` and `future`. The note supplies a short strategy discussion, not full theorem proofs; it does not explicitly promise a date or venue for a complete proof, so none is asserted here. Remark 3.3 confirms the omitted interval 1/2 < Delta < 1 and the omitted point Delta = -1. Section 4.2 identifies the predicted outer curves. Abstract, theorem ranges and PDF agree. This is independent checking of transcriptions, not independent verification of the mathematics.

Follow-up queries: `"Alexey Bufetov" "domain-wall" "proof" 2026`; `"2609.20576" proof limit shape`. No complete proof located in this bounded search. Did not pursue unrelated edge-fluctuation results surfaced by the search.

Created SOLVED_ELSEWHERE.md and REPORT.md using apply_patch. No PROOF.md, script or numerical data is appropriate for the mandated literature-update stopping branch. Total screening time remains below ten minutes. No files outside this folder were modified by task commands.

Final file audit command: `env OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c 'head -1 REPORT.md; wc -c LOG.md REPORT.md SOLVED_ELSEWHERE.md; rg -n "2609.20576|announcement|1/2 < Delta < 1|VERDICT" REPORT.md SOLVED_ELSEWHERE.md'`. Exit 0 (with the same nice warning). Confirmed the required first-line verdict and consistent announcement caveats and omitted parameter range in both deliverables. REPORT.md: 1902 bytes; SOLVED_ELSEWHERE.md: 2206 bytes.
