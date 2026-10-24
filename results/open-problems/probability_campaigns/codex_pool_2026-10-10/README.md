# Codex pool, 10 October 2026: work on open problems in probability

These folders hold what two groups of Codex workers wrote on 10 October 2026 while working on major open problems in
probability. The snapshot was taken at 10 Oct 2026 10:28 (UTC+3) while the workers were still running.

`wave300/` is the 300-worker wave: 25 candidate targets from the 7 September ranking, twelve workers on each, in four
approaches of three roles (prover, adversary, referee). By the snapshot 228 workers had written, on 20 of the
25 targets. Each worker has its own folder, named by worker, approach and role, under its target.

`team_O/` is team O (workers w330 to w347): sixteen solvers with about ten problems each, ranked biggest first, and two
auditors on other models (w346, w347). `LEDGER.md` lists every worker's problems and the proof files it wrote.

No target problem is solved here. Every claim row in these folders states a remaining gap. The status words in
`CLAIMS.jsonl` (for example "independently checked proof", "proved special case", "sketch") are the workers' own labels:
"independently checked" means another worker of the same pool read the argument, not that a referee of another model
family has accepted it. The wave's 1193 claim rows break down as 419 proved special case, 333 independently checked proof, 268 sketch, 94 conjecture, 33 numerical evidence.

A worker folder usually holds `STATUS.md` (state and next step), `ATTEMPT.md` (the proof attempt), `CLAIMS.jsonl` (one
row per claimed statement, with its assumptions, proof or counterexample, reviewer and remaining gap), `REPORT.md`,
`REVIEW_PACKET.md`, `checks/` and `tests/` (the computations and their receipts), `drafts/` (math-brain draft bundles) and
`patches/` (proposed changes to the brain's code, not applied by this commit).

Left out: compiled Python caches, downloaded paper PDFs, files over 1 MB, binary receipts, copies of other workers'
files, the few files that mention the evaluation material of the brain's tests (which stays off GitHub), and 33
math-brain draft bundles and patch drafts whose source ids (a date, a colon and a long slug) the secret scanner reads as
credentials; their content repeats the attempts and claims beside them.
`MANIFEST.tsv` lists every file with its size and git blob id. `PROBLEM_LEDGER.json` is the machine-readable ledger.
