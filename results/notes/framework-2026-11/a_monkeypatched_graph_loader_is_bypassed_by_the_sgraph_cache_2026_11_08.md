---
name: a_monkeypatched_graph_loader_is_bypassed_by_the_sgraph_cache_2026_11_08
description: "[VERIFIED] Ablating recall's association spread by patching spread_recall._load_graph did nothing: brain._fc_layer wraps it in the cross-process sgraph cache, which returns the real graph past the patch; mark the patch _r02=True"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:07:40+02:00
  status: provisional
  evidence: ""
---

8 Nov 2026 02:4x, an agent, Graphify TOP10 rank 2 recall ablation (top10_agent/ablate/run_ablate.py).

The arm meant to turn the association spread off patched sr._load_graph (and brain.sr._load_graph) to return empty dicts. Its top 8 came back identical to the links-off arm on all 16 questions and the header still read 'graph on'. Cause: on each recall brain._fc_layer replaces sr._load_graph with _fc_spread_graph_wrap(sr, current), unless the current function carries _r02. The wrapper looks the graph up in the cross-process file cache (_fc_get 'sgraph', keyed on the edge file's identity) and calls the wrapped function only on a miss, so with a warm cache the patch is never called.

Fix: give the patched loader the attribute _r02 = True so _fc_layer leaves it alone (probe: adj 0 inside _fc_layer). Same trap for any other function _fc_layer wraps (supersession._md_files, _load_superseded): check the _r02 guard before patching.

How to apply: before trusting an ablation arm, check that it changed the output at all (top lists identical to another arm = the switch did not take) and that the header shows the state you meant (graph off).
