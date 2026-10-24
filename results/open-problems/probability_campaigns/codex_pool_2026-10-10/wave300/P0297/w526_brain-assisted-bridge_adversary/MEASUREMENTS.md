# Measurements and proposed bounded repair

Observed generic recall command: `python -X utf8 ~/.claude/dreaming/brain.py recall "P0297 Liouville quantum gravity metric dimension KPZ mistakes"`, recorded in evidence/brain_recall.json. Runtime 24.9954479 seconds; exit code 0. The first three returned summaries contained no LQG, KPZ, or LFPP theorem. Relevant top-three hits: 0/3. The absent-token notice explicitly reported that no memory contained P0297. Unrelated private or trading memories were not opened.

Proposed bounded repair: for this mathematical query only, require a returned theorem to match a target-specific anchor (Liouville, LQG, KPZ, or LFPP) before serving it as proof evidence; when none matches, abstain and perform a read-only lookup of the mathematical store. An anchor match is only a relevance gate: the full statement, assumptions, revision, and source still require inspection. Do not infer mathematical correctness from the gate.

Replay command: `python -B -X utf8 checks/check_recall_gate.py`. Saved result evidence/gate_replay.json. The captured top three contained 3 off-target hints; the staged predicate served 0 and abstained. All six controls passed (3 target matches retained, 3 unrelated terms suppressed). Replay elapsed time 0.0017405999824404716 seconds; process wall time 8.7754942 seconds. This is a proposal until independently reviewed and deployed. Suppressing these unrelated hints is not a measured recall-accuracy improvement on a benchmark, and changing node volume is not an effectiveness claim.

Resource gate at the replay checkpoint: fresh governor status distress / throttle, reason process_critical. The run only serialized the current checkpoint and classified nine strings with the standard library. No growing path family was materialized. Large experiments were not started.

Search discipline correction: a recursive filename search for compute gates was too broad. Follow-up file access is restricted to the named compute helper, named mathematical sources, and the assigned peers' proof artifacts.

NEXT: Retrieve the mathematical cards by target title, run an offline anchor-gate replay and analytic obstruction checks under a fresh resource check, and save the exact before/after numbers.
