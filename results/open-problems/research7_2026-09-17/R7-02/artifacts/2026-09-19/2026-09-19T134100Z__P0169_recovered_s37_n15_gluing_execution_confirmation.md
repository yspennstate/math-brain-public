Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0169 recovered S=37,n=15 exact-gluing execution confirmation

A path-scoped history recheck recovered an unreported own-root HISTORY_GAP after the previous complete report: idea commit `75e7d1e63a6d35ca3c1445da3d2b810d7fe2f36a`, exact checker commit `ce9d8befc27465e71b1e808c76aecdf5bfe69120`, and archived output commit `155daa13f23a729b3c6f876663937c1f4300a388`. Those commits predate this run-start master snapshot, but no later immutable own report had integrated them.

Recovered checker:
`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_s37_n15_gluing_checker.py`

Recovered output:
`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_s37_n15_gluing_checker.out`

I independently re-executed the recovered checker in this run using Python integer arithmetic only. Captured stdout was compared byte-for-byte with the archived output: both are 1069 bytes and the equality test returned `True`. The run reaches `exact_global_multiset_survivors 0`, `S37_n15_eliminated True`, and terminates `ASSERTIONS_PASS`.

The certified finite conclusion is only the source-matching necessary-scope statement used by the checker: no symmetrized degree-five Newton/Hamming parent profile at `N=15`, signed singleton mass `37/16`, can support a globally compatible multiset of the coordinate restriction types forced by the minimal-counterexample inequalities. Hence the `S=37,n=15` branch is eliminated. This is a self-check, not an independent P26/OTHER-track audit and not source-level closure.
