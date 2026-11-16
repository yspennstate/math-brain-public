---
name: pack_rollup_keep_pack_base_no_saving_2026_11_08
description: "Does rolling the brain clone's 327 small packs into one free Mac disk? No: repack -a --keep-pack wrote a 5.7 GB pack beside the 5.5 GB base (5.8 -> 11.0 GB); not run live"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T23:14:59+04:00
  status: verified
  evidence: "dry run on APFS clone 8 Nov: 327 packs 5827036 KB -> 3 packs 11000360 KB, fsck rc 0"
  modified: 2026-11-08T19:26:54.480Z
---

Does rolling the brain clone's small packs into one free disk on the second machine? No, measured 8 Nov ~23:1x on an APFS clone of .git (script pack_rollup_dryrun.sh).

`git -c gc.auto=0 repack -a -d --keep-pack=<5.5 GB base>` took 327 packs (5.83 GB by du, 326 promisor files) to 3 packs, but the new pack was 5,688 MB beside the 5,520 MB base it was told to keep: 11.0 GB in all. fsck --connectivity-only rc 0 and a cat-file read worked, so the result was valid, just bigger. `-a` writes every reachable object not in the kept pack, and in a partial (promisor) clone that is nearly everything again; the small packs were not mostly duplicates of the base. The scratch copy cost 5 GB of real free space until deleted (free went 20 -> 15 -> 20 GB).

So the roll-up the author OK'd (~1.9 GB estimated) was not run live. The live clone at 23:14 was 327 packs, 5.52 GiB, fsck rc 0; its largest pack (pack-4be6e965, 5,520 MB) carries a 23:07 mtime, and earlier the same evening the largest was pack-e4b52b62 at 5,079 MB, so something rewrote the base that evening. See [[a_geometric_repack_rewrote_the_5gb_brain_pack_and_nearly_filled_c_2026_11_05]] for the Windows side of the same trap. A leftover tmp_pack_KuQVvU (7.6 MB, 3 Nov) sits in the pack dir; not worth touching.

Not measured: whether a fresh blobless clone would be smaller. Context for the disk work: [[league_needs_32p3_gb_freed_9p5_to_19p9_rest_is_live_or_brain_data_2026_11_08]].


Related: [[ai_memories_clone_3352_packs_2p3gb_would_repack_to_0p4gb_2026_11_07]] - its 1.9 GB is already back. On 7 Nov 02:4x the clone was 3,353 packs, 7.09 GiB, base 4.84 GB; at 23:14 on 8 Nov it was 327 packs, 5.52 GiB, base 5.52 GB. Someone rolled the small packs into the base between the two reads (the base's 23:07 mtime fits). That is why tonight's roll-up had nothing left to win. Why the copy's repack wrote 5.7 GB instead of a small pack is not proven; the likely cause is that git's promisor-pack repack does not honour --keep-pack and rewrote the base's objects.
