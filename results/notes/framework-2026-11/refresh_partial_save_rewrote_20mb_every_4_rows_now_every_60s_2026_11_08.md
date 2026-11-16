---
name: refresh_partial_save_rewrote_20mb_every_4_rows_now_every_60s_2026_11_08
description: "[PROVISIONAL] Embedding refresh MemoryError in np.savez / refresh_partial_vectors.npz / refresh slow writing: the partial file carries every corpus row (9,226, 20 MB) and was rewritten after every 4 encoded rows - 545 rows = 137 saves, 2.87 GB, 78 s; now every 60 s + end (5 saves, 105 MB, 12 s, same final vectors)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T11:18:29+02:00
  status: provisional
  evidence: ""
---

8 Nov 2026, an agent (recall loop, RECALL-10X lead refresh-partial-save). The 09:31 BrainEmbeddingRefresh died at 80 of 545 rows with MemoryError inside np.savez of embedding_refresh/refresh_partial_vectors.npz (RAM 1.3 GB free, commit 95-98 pct). _encode_saving in refresh_embeddings_box.py saved after EVERY four-row chunk, and the file keeps every row whose memory is still in the corpus, so each save built about 55 MB of buffers (vstack, BytesIO, getvalue) and wrote 20 MB.

Fix landed 11:1x (ed908abe -> 159302de, backup .bak_partialsave_20261108): save when REFRESH_PARTIAL_SAVE_S (default 60) has passed and at the end; a crash loses at most that much encoding, and the resume path is unchanged. Before/after on one plan (the real 9,226-row file copied to a temp path + 545 fake rows, fake encoder, recall_xc_1d48/dev/partial_save_test.py): 137 saves / 2.87 GB written / 78 s -> 5 saves / 105 MB / 12 s at a 2 s test cadence; final rows and vectors md5 13bc8b55 identical.

How far to trust it: the bench is synthetic for the encoder; whether it stops the MemoryError is shown only by a live run (first chance the 12:20 refresh on 8 Nov). Machine memory pressure is still the cause of the failure; this only removes the biggest repeated allocation. Follow-up worth doing: the partial file never sheds rows that the published sidecar already holds, so it grows. Related: [[embedding_publish_now_accepts_edited_memories_masks_stale_rows_2026_11_08]].
