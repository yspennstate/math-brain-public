---
name: method_cut_a_hooks_latency_by_skipping_known_work_2026_11_12
description: "[VERIFIED] Method: to cut a per-prompt hook's latency, rank hooks by wait on the critical path (in-process rows only), then for the top ones skip work whose answer is known (a cheap referent pre-check, a per-session cache, a backward tail read) or make the cold start lazy / file-backed, and ship only with an identical-output run on thousands of real texts; eight hooks 5-100x on 11 Nov 2026"
metadata:
  node_type: memory
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T02:48:00+09:00
  status: verified
  priors: "hook latency is usually one cold-start or one repeated lookup, not spread evenly; the fix is a skip or a cache, never a rewrite"
  originSessionId: agent-2c25-4a49-9a43-6448840c2424
  modified: 2026-11-12T00:46:49.753Z
---

**The move.** Profile the chain by WAIT on the critical path (the in-process rows; a parallel child counts only when
it outlasts the chain), take the top row, and ask "what does this compute whose answer it already has?" - then skip
it: a cheap pre-check before an expensive import, a per-session cache with a short TTL and a stale-on-lock answer, a
backward read of a tail instead of the whole file, lazy compilation on first use, a sidecar or an mmap for a big
read-only store. Ship only with the old and new outputs compared on thousands of real inputs.

**Where it worked (11 Nov 2026, eight hooks, one day):** canonical_route 68 -> 1.1 ms (referent pre-check skips the
brain.py import on ~60 pct of prompts, 3,255/3,255 identical); the three Stop hooks 110 -> 4.5, 124 -> 12,
350 -> 41 ms; the checklist hook 1.7-2.2 s -> ~0 (mesh lookup cached 10 min); proof_sense 129 -> 4-5 ms (344
regexes compiled on first use, 0 diffs on 3,413 texts); the math prefilter 665 -> 40 ms (per-token sidecar stamped
with the pickle's signature); sqlite reads 24-31 -> 16 ms (mmap_size); spread_recall 29-44 -> 2.4 ms on repeats.
Story and sources: [[gist_hook_latency_pass_2026_11_11]],
[[rank_prompt_hooks_by_wait_parallel_children_are_off_the_critical_path_2026_11_11]],
[[canonical_route_skips_brain_import_without_a_gate_referent_2026_11_11]],
[[stop_hooks_three_faster_by_skipping_work_whose_answer_is_known_2026_11_11]],
[[checklist_mesh_lookup_cached_ten_minutes_1800_to_0_ms_2026_11_11]],
[[proof_sense_import_compiled_344_regexes_every_prompt_now_lazy_2026_11_11]],
[[math_prefilter_per_token_sidecar_load_665_to_40_ms_2026_11_11]],
[[sqlite_hook_store_read_through_mmap_cuts_fresh_process_reads_2026_11_11]],
[[spread_runindex_word_memo_cuts_repeat_lookups_2026_11_11]].

**Where it would NOT work.** A hook whose answer genuinely changes every prompt (a live mesh inbox, a fresh file
read the author just wrote) cannot be cached without serving a stale answer; there the fix is a timeout and a
stale-marked answer, which is a different promise. A cold start paid by a shared import (pandas, cmd /c ver on a
loaded box, [[hidden_cmd_ver_at_pandas_import_costs_seconds_on_a_loaded_box_2026_11_11]]) is not yours to skip.
And a lock convoy is a landing problem, not a cache problem
([[mesh_lock_convoy_hooks_wait_briefly_and_skip_wal_needs_one_landing_2026_11_11]]).

**The one check that breaks it.** Run the old and new hook on the same several thousand real texts and diff the
outputs. Any diff means the hook was changed, not sped up - the 11 Nov fixes all shipped at 0 diffs; a cache whose
TTL is too long shows up here as a stale line the old hook would not have printed. The 60 pct skip rate is a property
of the prompt mix and must be re-measured when the mix moves.
