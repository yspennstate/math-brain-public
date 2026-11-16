---
name: moving_a_bm25_index_changes_its_signature_rebuild_the_sidecar_2026_11_08
description: "Swapped or moved a bm25 index and the slot went empty / score_postings None: the sidecar name is a hash of the file's stat signature, which a move changes even on one volume - rebuild build_postings after any move"
metadata:
  type: feedback
  created: 2026-11-08
  created_at: 2026-11-08T23:21:32+02:00
  status: verified
  evidence: "12_cognitive_architecture/top10_7_10_agent/rank8_land_relabel_shadow_out.txt (sidecar_present false after the move) + seg_postings_relanded_out.txt (rebuilt c09b007d943f, 5/5 exact); segments_index/MANIFEST.json relabel_landing_2026_11_08"
---

On 8 Nov 23:06 I landed the relabelled segments index by moving the shadow's files into segments_index with os.replace, both on C:. I expected a same-volume move to keep the index's stat signature (st_ino, size, mtime, birth time), and with it the postings sidecar's name, bm25.postings_path(): that name is sha1(str(signature))[:12]. It did not. The moved sidecar was a0a2b6745806, the live index now expected c09b007d943f, and score_postings returned None. The segment slot fails open on None, so it would have gone quietly empty with nothing to show for it but `answered 0`.

Fix: seg_postings.py build on the live index (264,073 terms over 15,226 docs, 311 s under load; 65.8 s on 5 Nov when the box was quieter). The cold check then answered 5 of 5, top 5 exact.

**Why:** the bm25 sidecar is keyed on stat identity, not content. A move, a copy or a restore of the index file gives it a new identity on this machine, whatever the volume.

**How to apply:** after any move, copy or restore of a bm25 index (the live brain index, the segments index, a shadow), run bm25.postings_path(index) and check that the file exists. If it does not, run build_postings before calling the swap done. Count a landing as done on score_postings answering, never on the files being in place. The orphaned sidecar is a rebuildable cache. A running recall server keeps the old sidecar open until its hourly handover.

Related: [[green_light_is_not_trusted]].

