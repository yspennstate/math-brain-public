---
name: spread_runindex_word_memo_cuts_repeat_lookups_2026_11_11
description: "spread_recall slow on the server (~100 ms warm, CPU-bound)? The run index re-scanned the vocab blob per word (14.6k finds, ~16 ms a call); since 22:15 11 Nov each word's keys are kept until the postings change: lookups 29-44 -> 24 ms new / 2.4 ms repeat, 80/80 outputs identical. A copy reads data via DR=__file__ - point DR at live when testing"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T22:16:52+02:00
  status: verified
  evidence: "scratch area ck/runidx_test.py (0 mismatches of 543 on index lines and 63,147 names) and ck/warm_ab.py (80/80 identical through Warm().call, lookups 29-44 -> 24 / 2.4 ms); live md5 2d8588e29756"
---

The spread server (spread_server.py, which answers spread_recall on every prompt) spent its largest self-time on 11 Nov in the run index's word search: each prompt word was found again in the whole run-vocabulary blob, 14,649 `bytes.find` calls over 30 warm calls, about 16 ms of a ~100 ms call, and 140-150 ms a prompt on the 63k memory names on the loaded box. A warm served call was 78 ms of CPU out of 103 ms wall (312 calls, 20:55-21:55), so the time is compute, not waiting.

Since 22:15 `_RunIndex.hits` keeps each word's key set until the postings next change (`_add`/`_drop` bump a generation; the cache is cleared when the generation moves or when it holds over a million keys, about 40 MB). Prompts repeat words, and a loop prompt repeats verbatim every few minutes. Tested before landing: old and new indexes gave the same hits on 360 lookups and on 183 more after a resync that dropped, changed and added lines, both on the index lines and on all 63,147 names; 80 of 80 outputs through the server's own `Warm().call` were byte-identical. Lookup time per call fell from 29-44 ms to 24 ms for new prompts and 2.4 ms for repeated ones. Whole-call medians were too noisy on the loaded box to show it (sequential runs drifted 80 to 230 ms between arms). Live md5 2d8588e29756, backup `spread_recall.py.bak_wordmemo_20261111`.

Test trap worth keeping: `spread_recall.py` sets `DR` from its own `__file__`, so a copy loaded from a scratch folder reads its data files from there and gives different output (28 of 80 equal). Point `DR` at the live folder in a test-only copy before comparing outputs. The same applies to any hook that finds its data next to itself.

Remaining warm cost, same profile: `_select` about half (semantic cosine, candidate words, descriptions), `_seeds_from_prompt` a third, `_spread` and `_collapse_activations` the rest; the call also runs `_code_files()` over sys.modules on every call (3 ms).


Related: the same test trap, met earlier with another hook: [[a_hook_copy_tested_from_a_scratch_folder_reads_its_files_from_there_2026_11_11]]; how to rank which prompt hook to speed up: [[rank_prompt_hooks_by_wait_parallel_children_are_off_the_critical_path_2026_11_11]].
