---
name: bm25_lazy_imports_save_30_ms_per_scoring_hook_2026_11_11
description: "bm25 import slow inside a hook? Since 11 Nov bm25.py loads brain_node_documents and tempfile lazily: import 124 -> 95 ms, recognize_on_read's bm25 import 57-78 -> 32-36 ms, rankings and read_doc unchanged"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T08:45:31+02:00
  status: verified
  evidence: "scratch area eq.py: 12 rankings, 41 attachment digests, 80 read_doc, _stage_pickle bytes identical"
---

Since 11 Nov 2026 08:21 local, ~/.claude/dreaming/bm25.py imports brain_node_documents and tempfile only when they are first used. brain_node_documents pulls in dataclasses, inspect and linecache, about 30 ms of a cold import, yet a scoring hook never touches it: only read_doc and the attachment helpers need it, and only the index writers need tempfile.

How: `node_docs` is a small stand-in object whose `__getattr__` imports the real module, swaps it into the module globals and answers the call, so later calls go straight to the module. `import tempfile` moved inside `_stage_pickle` and `_publish_payload`.

Measured: bm25 import from source 124 -> 95 ms; inside recognize_on_read (which imports bm25 on every Read/Bash) 57-78 -> 32-36 ms. Every hook or script that imports bm25 and only scores gains about 30 ms.

Checked before the swap, old and new loaded side by side with `__file__` set to the live path: 12 rankings identical, attachment_mtimes and attachment_manifest_digests identical (41 entries), read_doc identical on 80 slugs (40 with documents), _stage_pickle bytes identical. `brain.py recall` answered after the swap. Backup bm25.py.bak_lazyimports_20261111; repo mirror 12_cognitive_architecture/dreaming/bm25.py.

How to apply: a module that a per-call hook imports should keep heavy imports that only writers or rare paths need inside those functions. Profile a hook's imports with `python -X importtime` before tuning its logic; in this case the import cost more than the hook's own work. Next lead on the same path: a covering index p_df on the postings sidecar for the df prefetch (32-41 -> 2-4 ms in a scratch copy), see [[hook_budget_agent_loop]] and [[read_time_recognition_hook_live_lesson_on_read_2026_11_11]].

