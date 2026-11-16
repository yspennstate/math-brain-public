---
name: partial_clone_fetch_recopied_59mb_unmarked_pack_in_midx_2026_11_09
description: "[PROVISIONAL] Board publisher git fetch 100-400 s / every fetch writes a 59 MB promisor pack: git 2.53 index-pack --promisor re-copied 61k tip objects that the 8 Nov midx mapped to unmarked pack-e320d18f; empty .promisor beside it -> fetch 72 s to 28 s, no copy"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T05:03:31+02:00
  status: provisional
  evidence: ""
---

The board publisher's control fetch (`git fetch -q origin main` in math-brain-main, the partial blob:none clone research-repo) took 100-400 s and failed its 420 s limit on 61 of 113 runs from 7 to 9 Nov. Each fetch was re-copying the same 59 MB.

Why. git 2.53's `index-pack --promisor` copies every tree that a fetched pack points at into a new promisor pack, unless the first pack git finds it in is already a promisor pack (builtin/index-pack.c, repack_local_links, read 9 Nov). It then runs `pack-objects --exclude-promisor-objects-best-effort`, and that walk takes the tip's blobs along with the trees. A multi-pack-index written 8 Nov 18:56 maps 61,080 tip objects (44,809 blobs, 16,271 trees) to pack-e320d18f: 230 MB, dated 8 Oct, and missing its `.promisor` file. From 19:03 on, every fetch wrote the real pack (about 200 KB) plus another 58.9 MB copy of the same 61,080 objects. The copies were promisor packs, but they weren't in the multi-pack-index, so the next lookup found e320 again. That made 23+ copies, 1.83 GB.

How it was found. A GIT_TRACE of one fetch showed `index-pack --promisor` followed by `pack-objects --exclude-promisor-objects-best-effort`, so it wasn't a lazy fetch. With lazy fetch off, cat-file could see every object. Reading the .idx files directly found all 61,080 in e320 (no marker) and in 80 promisor packs.

Fix (9 Nov 04:56): an empty `pack-e320d18f1f33a8a6887fa22e37ca3974186d31f9.promisor`. To undo it, delete the file. Nothing was deleted. Result:

| fetch | time | pack-objects step | big pack written |
|---|---|---|---|
| 04:42 before | 72 s (console) | yes | 56.9 MB |
| 04:57 after | 28 s | none | no (24 KB) |

The publisher's own median was 245 s before the fix. Judge that one from PUBLISH.log/SYNC.log over the next day.

How to apply. If a partial clone's fetch suddenly writes a big promisor pack every time, list the non-promisor packs (.pack with no .promisor beside it) and check whether the copied objects live in one of them. If they do, mark that pack only when its objects are on the remote. Rewriting the multi-pack-index after a repack also fixes it. Packs e874ffc1 (455 MB) and be00b5bd (568 MB) are also unmarked; they hold 15,309 and 713 of the same objects and are left alone.

Why provisional: one fetch measured. The ~30 redundant copies are still on disk; delete them only after checking that each is a subset of e320's objects and isn't in the multi-pack-index.

Related: [[board_publish_fetch_timeouts_and_tmp_packs_2026_11_08]]. Task, an agent.


Follow-up 9 Nov 05:2x: the 24 redundant copies written after the midx (50-70 MB promisor packs, not in the midx, no .keep, every object inside e320) were deleted: 1.40 GB freed. The files are read-only on Windows, so chmod before os.remove. After the delete, the tip README reads and all 220,251 tree entries resolve with GIT_NO_LAZY_FETCH=1. Log: dup_packs_log.txt (script dup_packs.py, scratch sr_prof). The older copies (29 Oct, 31 Oct, 4 Nov) are named in the midx and stay until a repack rewrites it.

Follow-up 9 Nov 06:0x. After the marker fix the publisher still logged a 420 s refusal at 05:29 and a 348 s fetch at 05:42. NOT the main cause, as the next run showed (the publisher took 292 s at 06:07-06:11 with the orphan gone, while my console fetch took 38 s at 06:02), though it shared the disk: my own 03:35 `git repack --geometric` of this clone. Its parent had died, but its child `pack-objects --stdin-packs` (pid 49520) kept writing a roll-up into the pack folder at about 0.6 MB/s, competing for the same disk on a starved workstation. Nothing would have installed that pack, because only the parent repack renames it. I stopped it at 05:52 (it took two Stop-Process calls; taskkill said "not supported" while the process was ending) and deleted its 377 MB tmp_pack. A traced fetch at 06:02 then took 38 s: remote refs 15 s (10 s of that is git-credential-manager get/store spawning), mark_complete_local_refs 4.8 s, index-pack 5 s, consume_refs 2 s, and the post-fetch `maintenance --auto` did nothing. Lesson: a repack started by hand on a clone that a timed job fetches can outlive its shell. Before leaving, check that the parent and its pack-objects child have both exited. Also still on disk: 77,468 loose objects (3.24 GB) beside 1,185 packs. Not touched.
