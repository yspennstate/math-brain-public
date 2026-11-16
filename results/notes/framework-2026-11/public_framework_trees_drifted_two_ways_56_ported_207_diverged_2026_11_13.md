---
name: public_framework_trees_drifted_two_ways_56_ported_207_diverged_2026_11_13
description: "[VERIFIED] brain-framework vs math-brain-public framework/dreaming out of sync? 13 Nov: 263 shared files differed, 56 one-way (ported, 4192cd5), 207 diverged both ways, 63 mbp-only"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T07:40:14+02:00
  status: provisional
  evidence: ""
---

13 Nov 2026 07:3x, an agent. Found because brain-framework's test_marshal_memo failed 4/4 on Windows Python 3.14 while math-brain-public had carried the fix since 7 Nov (d49fed6b; scar windows_stat_and_fstat_disagree_on_ctime_memo_never_hit_2026_11_07). Same fix put into brain-framework as f1643c9.

How to tell which side is ahead without a common base: build each repo's blob history for the path (git log --raw --no-abbrev --format= -- <dir>); if repo A's CURRENT blob for a file appears in repo B's history, B is strictly ahead and the file can be copied B -> A byte for byte. Last-commit time is useless here: a sweep commit (the help-flag guard) touched files on both sides.

Result on dreaming/ (bfp 657 files, mbp framework/dreaming 708): 263 differ; 56 had mbp strictly ahead and were copied into brain-framework (4192cd5; label check clean, 12 ported tests pass, help ratchet OK); 0 had bfp strictly ahead (bfp history only starts 5 Nov); 207 diverged both ways and were NOT merged - each needs a per-file 3-way read, and a set difference of lines is not a diff (brain_py_drift_was_one_way_not_two_2026_08_17). 63 files exist only in mbp, 12 only in bfp.

How to apply: before syncing anything between the two public framework repos, run this blob-history test first; port only the one-way files mechanically; merge diverged files one at a time with both versions read. A thin clone (--depth 1 --filter=blob:none, then fetch --shallow-since) gives the history at about 8 MB instead of the 2.2 GB checkout. Status: verified for dreaming/ only; other framework dirs not scanned.

**Update 13 Nov 08:5x (same session).** The 207 "diverged" count was mostly false. Checking only whether one side's current blob appears in the other side's history misses a copy that is an older mbp version plus small local edits. Sorting each file by its closest mbp version (any blob in mbp history) showed 72 within 4 changed lines and 93 more within 20. The local edits were help-flag guards and comment wording, often comments that mbp had already cleaned. A three-way merge (base = closest mbp blob, ours = bfp, theirs = mbp HEAD) merged 157 files cleanly; only 41 of them changed. Landed as brain-framework db99717 with the suite at 159 of 165 passing, up from 156.
How to apply: (1) Never resolve conflicts toward mbp wholesale. fastrecall.py's hash pins must match the tree's own retrieval.py and query_embed.py, and mbp's pins would have silently turned fast recall off (scar public_fastrecall_pins_drift_silently_test_guards_them_2026_11_07). (2) The reference is the live ~/.claude/dreaming copy, not mbp HEAD. math_sense.py in bfp is 874 lines from live against mbp's 3677: mbp is a separate lineage there, and five other files move 25-153 lines AWAY from live when mbp's side is taken (recall_server, build_keyword_nodes, github_push_cost_guard, memory_pull, instinct_prime). (3) A file mbp moved to a new path shows a huge false distance unless the history scan follows the old path.

Update 13 Nov 09:1x: second batch landed as 892dd41 (39 conflict files taken from the other tree). Five files stayed on brain-framework's copy because the other tree's version moves them away from the live ~/.claude/dreaming copy (recall_server, build_keyword_nodes, github_push_cost_guard, memory_pull, instinct_prime); a test the other tree edited alongside a kept file must stay too (test_memory_pull wanted blob_id). Suite 156 -> 161 of 165 across both batches. The secret scanner's --range refuses a shallow clone; scan the changed file list instead.

Update 13 Nov 11:0x: brain-framework d753240 closes the drift outside dreaming/ from that side - the 150 diverged files merged (mbp HEAD for import-only lines, real brain-framework edits kept, 5 clean three-way merges, 5 --ours), 72 newer and 22 added landed earlier (9b03c6f, ddb4271). Tests on the merged tree: 1184 mathbrain pytest pass, same as before; note the mathbrain tests are pytest files, so running them as scripts only checks imports, and against the installed package at that. math-brain-public has not taken brain-framework's own edits back yet.

Correction 13 Nov 11:1x: the "keep brain-framework's genuine edits" rule was wrong for 10 files. Their later-commit lines were agent ids, private memory slugs and hard ~/the private repository paths that math-brain-public had stripped (env vars instead), so the merge put them back into brain-framework (d753240). Fixed in 1587559: math-brain-public text for those files, plus one real fix kept (claim_files.sh Mac POSIX branch). Lesson: when one tree is the sanitized one, a line that exists only in the other tree is a private line until shown otherwise; diff the two and read the extra lines before keeping them. brain-framework still has about 159 agent-id mentions elsewhere (dreaming/bm25.py and others) - check each against the math-brain-public text.

Update 13 Nov 12:2x: agent ids gone from both public trees. brain-framework 20694ac (comments in 34 files, code AST-identical) and 5629e64 (test docstrings; the label check now has an "agent session id" shape rule that lets obvious fixture ids through, with a both-ways test); math-brain-public 9eb386d carries the same rule and was already clean over all 1534 framework files. From now on check_no_private_labels.py fails a push that brings an agent id back.
