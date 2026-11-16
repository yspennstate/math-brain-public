---
name: embedding_publish_eval_failed_on_mac_read_cache_since_3nov_fixed_2026_11_08
description: "[VERIFIED] Did the embedding publisher's 46-check suite pass on the second machine? No since ~3 Nov: the second machine-only read cache served the mocked-unreadable file; suite fixed + chmod control (47 PASS, planted fault caught); then workstation's _only_added_between publish fix ported"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T01:23:23+04:00
  status: verified
  evidence: "8 Nov 01:23: eval_embedding_refresh PASS 47; negative control rc 1; 6 publish controls 0 failed"
---

Did the embedding publisher's regression suite (eval_embedding_refresh.py) pass on the second machine? No. From about 3 Nov to 8 Nov 01:23 it failed at its unreadable-corpus check (line 239, assert not unreadable["corpus_readable"]), and nobody ran it.

Cause: on 3 Nov the second machine's embedding_coverage.write_status gained builder.enable_read_cache(), a stat-keyed row cache that only the second machine has; origin's embedding_coverage has none. The suite calls write_status at line 174, which turns the process-wide cache on. The fixture at 239 then mocks builder.io.open to deny stable.md, but that row comes from the cache and io.open is never called. So the check failed, though production was fine. In real use a file turns unreadable through a permission change, which moves st_ctime, and the cache key holds ctime.

Fix (an agent, 8 Nov):
- The suite clears builder._READ_CACHE before the mocked denial.
- A new control covers the cached path: with stable.md's row cached, chmod 0 must read as corpus unreadable, and readable again after the mode is restored.
- Result: PASS, 47 checks (46 before).
- Negative control: with a planted cache key that drops ctime, the suite fails on the new assertion ("read cache served a file that cannot be opened").
- Backup: eval_embedding_refresh.py.pre_readcache_fixture_20261108.

The suite was then used to port the workstation's 7 Nov publish fix, [[embedding_publish_accepts_memories_added_between_its_two_reads_2026_11_07]] (_only_added_between, plus a guard for builders without a read cache). Origin's publish_memory_embeddings.py was the second machine file plus three added hunks and one changed condition, so it went live byte for byte. The suite passes 47 of 47, and the six two-read controls give the workstation's results: no change and added pass; edited, deleted, added+edited and added+sidecar all raise OSError. Backup: publish_memory_embeddings.py.pre_addedbetween_20261108.

The worker machine's own publish failures (7 Nov 03:30 dream, twice, then landed) are a different refusal: "missing 8 of 46502 (7 no newer than the newest held)", after a 746 s wait for heavy_job.lock between refresh and publish. This port does not touch that.

How to apply: when a Mac-only change goes into a shared module, run that module's workstation-written suite in the same step. A green suite elsewhere says nothing about a Mac edit it never ran against. Related: [[stat_shortcut_broke_embedding_harness_unrun_2026_11_03]], the same suite broken and unrun by a stat shortcut on 30 Oct, and [[mac_hooks_lacked_4nov_once_per_context_trims_ported_four_2026_11_08]].

