---
name: canonical_route_skips_brain_import_without_a_gate_referent_2026_11_11
description: "[VERIFIED] canonical_route hook 60+ ms every prompt? It imported all of brain.py for a 1 ms intent gate; since 11 Nov a referent pre-check (brain / ai_anchors / canonical terms from recall_policy.json) skips the import on ~60 pct of prompts, 68 -> 1.1 ms, 3255/3255 identical"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T19:54:00+02:00
  status: provisional
  evidence: ""
---

canonical_route.py (UserPromptSubmit, every Claude session) runs brain._intent_gate_strength on the prompt. The gate is about 1 ms; import brain about 60 ms (brain pulls spread_recall, 21 module regexes, a big module body). Every positive path through the gate needs, after its normalisation, 'brain', an ai_anchor or a canonical_groups term in the prompt, so _no_referent() reads those terms from the same recall_policy.json (they cannot drift) and returns 0.0 before the import when none is present; any read trouble runs the full gate. Measured 11 Nov 2026 by an agent: 34 pct of the author's last 3,003 prompts and 40 pct of recent session prompts pass the pre-check; on 3,255 prompts old and new gate strengths are identical (229 positive, 2,135 skipped); fresh process on a no-referent prompt 68.0 -> 1.1 ms; selftest 0 failures. Live md5 4915c1e7b5, record 12_cognitive_architecture/brain_improvement/canonical_route_precheck_2026_11_11 (commit a0b04b39cb). General move: when a hook imports a heavy module for a cheap test, find a necessary condition the test cannot pass without and check it first, from the same config. Related [[sqlite_hook_store_read_through_mmap_cuts_fresh_process_reads_2026_11_11]] [[directive_hooks_select_compiled_485_cues_every_prompt_lazy_prefilter_2026_11_11]] [[rank_prompt_hooks_by_wait_parallel_children_are_off_the_critical_path_2026_11_11]].
