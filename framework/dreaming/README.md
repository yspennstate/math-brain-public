# The brain's working scripts

These are the scripts the brain runs day to day: the recall path, the hooks that surface a note while an
agent works, the nightly consolidation, and the evaluations that decided which changes were kept. They are
copied as they run, with private paths replaced by placeholders. The set is partial. Some scripts import
modules that are not here (`brain.py`, the reflex engine `instinct_prime.py`), because those carry private
material and are not published. Read the scripts for the method; they will not all run as a package.

## What is here

- Recall. `bm25_append.py` and `bm25_refresh_if_stale.py` keep the lexical index current within seconds of a
  write. `fastrecall_delta.py`, `query_embed.py` and `fresh_vectors.py` serve the semantic lane.
  `graph_lane.py` and `math_walk.py` walk the association graph. `recall_protocol.py` states how an agent
  should ask.
- Hooks. `hook_dispatch.py` runs every hook under one time budget and falls back to its last known good copy
  (`hook_dispatch.lkg.py`) when an edit breaks it. `hook_dispatch_deadman.py` and `hook_reaper.py` catch a
  hook that hangs. `frontier_hook.py`, `graph_membrane_hook.py`, `proof_deny_hook.py` and
  `codex_reflex_hook.py` are the notes an agent sees mid-work. `gap_watch_hook.py` flags a silent gap in a
  log.
- Compaction. `compact_nodes.py` saves each context compaction as its own node in the graph and links it to
  the session's earlier compactions and to the memories nearest it. `compact_math.py` does the same for
  mathematical work, and `keep_working_after_compact.py` hands the open task back after a compaction.
- Proof discipline. `proof_receipt.py` ties a claim to the hash of the file that was checked. `proof_sense.py`
  and `proof_deny_hook.py` refuse a report that names a result without a receipt. `lean_check.py` and
  `lean_process.py` run Lean on a stated lemma.
- Judging the brain's own notes. `fire_judge_*.py` sample the notes the hooks surfaced, have them judged as
  on-domain or not, and feed the precision back so that a note judged wrong most of the time stops firing.
  `reflex_precision.py`, `heed_audit.py` and `shadow_deny_status.py` report it.
- Consolidation. `reconsolidate.py`, `mistake_graph.py`, `dream_mistakes.py` and `incubate.py` are parts of
  the nightly pass that merges, links and retires memories.
- Evaluations. The `eval_*.py` files are the measurements behind each change. Each one names what it compared
  and what was kept. The question banks and answer keys they read are not published.

## Credit

The lexical lane is Okapi BM25 (Robertson and coworkers). The graph walk is a personalised PageRank in the
sense of Jeh and Widom. The precision feedback on the hooks follows the signal-detection framing of Green and
Swets. Lean is the theorem prover of de Moura and coworkers.
