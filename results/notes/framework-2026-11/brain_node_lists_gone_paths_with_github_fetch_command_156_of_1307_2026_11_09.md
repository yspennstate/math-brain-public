---
name: brain_node_lists_gone_paths_with_github_fetch_command_156_of_1307_2026_11_09
description: "A memory names a file no longer on the second machine - how do I get it back? brain.py node now ends with each gone path and its fetch.py / where.py / ghstore get command; 156 of 1,307 gone paths recoverable on 9 Nov"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T00:51:07+04:00
  status: verified
  evidence: "gone_paths.py survey; fast_push.py fetched 4891 bytes digest-checked; brain.py sha 3749f2dae47b"
---

A memory names a file that is no longer on the second machine. How do I get it back?

Read the memory with `brain.py node <slug>` (or `recall ... --read K`). Since 9 Nov 00:50 the node output ends with a block "paths named above that are no longer on this machine", one line a gone path (at most 6), each with how to get it back:
- an exact row in GHFETCH2's catalog: `python3 fetch.py <path> --to <scratch dir>`
- a folder the catalog holds files under: `where.py '<path>/*'` lists them
- a path under a ghstore stub (<folder>.GITHUB_STUB.json): `python3 ghstore.py get <folder>`
- otherwise "gone, not found in the GitHub catalog or a stub".
It reads only the local catalog and stub files, no network, and costs nothing measurable (99 vs 97 ms). BRAIN_NODE_GONE=0 turns it off.

Survey on 9 Nov (gone_paths.py over all 51,003 memories): 1,975 name at least one gone path. Of 1,307 distinct gone paths, 111 had an exact catalog row, 36 were catalogued folders, 9 sat under a stub, and 1,151 were not found. The not-found ones include deleted scratch, Windows-era paths, other machines' paths and paths that never existed. The recoverable share should rise as the author's 00:33 order moves records to GitHub; each offload must add its catalog rows or stub, or its paths join the 1,151.

Checked end to end: a compaction memory names fast_push.py (deleted earlier). The note printed the fetch.py command, and running it brought back 4,891 bytes with GitHub's whole-asset digest checked. That same file is the git fallback online_memory_pull.py runs when the contents API fails, so that fallback is dead until it is restored or repointed.

Keep CATALOG.sqlite local: it sits inside a Codex worker folder (GHFETCH2) in codex_fleet, which the offload is clearing. Offloading the catalog would leave every other offloaded file unfindable.

Related: [[ghfetch_hash_backfill_four_tars_one_range_restore_2026_11_08]] (what fetch.py can restore), [[recall_read_k_one_call_finds_and_reads_sc3b_gold_4_to_23_of_67_2026_11_09]] (--read prints nodes through the same path).

